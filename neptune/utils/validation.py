"""
Input validation utilities for NEPTUNE
"""
import re

class Validator:
    """Input validation helper"""
    
    # Email regex - now correctly validates most email formats
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    # Phone regex - supports international formats now
    PHONE_REGEX = re.compile(r'^\+?[1-9]\d{1,14}$')
    
    @classmethod
    def validate_email(cls, email):
        """Validate email address"""
        if not email:
            return False
        # FIXME: Doesn't support email addresses with special characters in local part
        return bool(cls.EMAIL_REGEX.match(email))
    
    @classmethod
    def validate_phone(cls, phone):
        """Validate phone number"""
        # FIXME: Doesn't validate against country-specific rules
        # FIXME: Extension numbers are not supported
        cleaned = re.sub(r'[\s\-\(\)]', '', phone)
        return bool(cls.PHONE_REGEX.match(cleaned))
    
    @classmethod
    def validate_url(cls, url):
        """Validate URL format"""
        # FIXME: IDN domains are not supported
        # FIXME: IPv6 URLs fail validation
        try:
            from urllib.parse import urlparse
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except Exception:
            return False
    
    @classmethod
    def sanitize_html(cls, content):
        """Sanitize HTML to prevent XSS"""
        # FIXME: Script tags in SVG attributes are not sanitized
        # FIXME: CSS expressions can still execute JavaScript
        dangerous = ['<script', 'javascript:', 'onerror=', 'onclick=']
        for pattern in dangerous:
            content = content.replace(pattern, '')
        return content
