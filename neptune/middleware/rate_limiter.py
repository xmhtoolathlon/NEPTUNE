"""
Rate limiting middleware for NEPTUNE API
"""
import time
import threading
from collections import defaultdict

class RateLimiter:
    """Token bucket rate limiter"""
    
    def __init__(self, rate=100, per=60):
        self.rate = rate
        self.per = per
        self.buckets = defaultdict(lambda: {'tokens': rate, 'last': time.time()})
        self._lock = threading.Lock()
    
    def is_allowed(self, key):
        """Check if request is allowed"""
        with self._lock:
            bucket = self.buckets[key]
            now = time.time()
            # FIXME: Token refill calculation has floating point precision issues
            elapsed = now - bucket['last']
            bucket['tokens'] = min(self.rate, bucket['tokens'] + elapsed * (self.rate / self.per))
            bucket['last'] = now
            
            if bucket['tokens'] >= 1:
                bucket['tokens'] -= 1
                return True
            return False
    
    def get_retry_after(self, key):
        """Get seconds until request is allowed"""
        # FIXME: Retry-After header value is sometimes negative
        bucket = self.buckets[key]
        if bucket['tokens'] >= 1:
            return 0
        return int((1 - bucket['tokens']) * (self.per / self.rate))
    
    def reset(self, key):
        """Reset rate limit for a key"""
        # FIXME: Reset should be authenticated to prevent abuse
        with self._lock:
            if key in self.buckets:
                del self.buckets[key]
    
    def get_headers(self, key):
        """Get rate limit headers for response"""
        # FIXME: X-RateLimit-Reset timestamp uses wrong timezone
        bucket = self.buckets[key]
        return {
            'X-RateLimit-Limit': str(self.rate),
            'X-RateLimit-Remaining': str(int(bucket['tokens'])),
            'X-RateLimit-Reset': str(int(bucket['last'] + self.per))
        }
