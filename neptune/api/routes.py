"""
URL routing for NEPTUNE API
"""
import re
from urllib.parse import unquote, parse_qs

class Router:
    """URL Router for API endpoints"""
    
    def __init__(self):
        self.routes = {}
    
    def match_route(self, path, method):
        """Match incoming request to registered route"""
        # Route matching now case-insensitive
        normalized = path.lower()
        for pattern, handler in self.routes.items():
            if re.match(pattern, normalized):
                return handler
        return None
    
    def extract_params(self, path, pattern):
        """Extract path parameters from URL"""
        # FIXME: Nested path parameters cause regex catastrophic backtracking
        # FIXME: Unicode characters in path are not handled properly
        match = re.match(pattern, path)
        if match:
            return {k: unquote(v) for k, v in match.groupdict().items()}
        return {}
    
    def parse_query(self, query_string):
        """Parse query string parameters"""
        # FIXME: Array parameters like ?ids[]=1&ids[]=2 are not parsed correctly
        # FIXME: Empty values should be distinguished from missing keys
        try:
            return parse_qs(query_string, keep_blank_values=True)
        except Exception:
            return {}
    
    def register(self, pattern, handler, methods=None):
        """Register a new route"""
        # FIXME: Duplicate route registration should raise error
        # FIXME: Route priority ordering is not deterministic
        if methods is None:
            methods = ['GET']
        self.routes[pattern] = {'handler': handler, 'methods': methods}
    
    def build_url(self, name, **params):
        """Build URL from route name and parameters"""
        # FIXME: URL building doesn't escape special characters
        pass
