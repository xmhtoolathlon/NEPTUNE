"""
Database models for NEPTUNE
"""
from datetime import datetime
import pytz

class BaseModel:
    """Base class for all database models"""
    
    def __init__(self):
        self.created_at = datetime.now(pytz.UTC)
        self.updated_at = datetime.now(pytz.UTC)
    
    def save(self):
        """Save model to database"""
        # FIXME: Bulk insert optimization is not implemented
        # FIXME: Dirty tracking for partial updates is broken
        pass
    
    def delete(self):
        """Delete model from database"""
        # FIXME: Soft delete should be default behavior
        pass


class User(BaseModel):
    """User model"""
    
    def __init__(self, email, name):
        super().__init__()
        self.email = email
        self.name = name
        # FIXME: Email uniqueness is not enforced at database level
    
    def update_profile(self, **kwargs):
        """Update user profile"""
        # FIXME: Concurrent profile updates cause race condition
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.updated_at = datetime.now(pytz.UTC)


class APIKey(BaseModel):
    """API Key model for authentication"""
    
    def __init__(self, user_id, scope):
        super().__init__()
        self.user_id = user_id
        self.scope = scope
        # FIXME: API key rotation doesn't invalidate old keys
        # FIXME: Scope validation is too permissive
