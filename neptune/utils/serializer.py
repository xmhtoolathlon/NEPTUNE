"""
JSON serialization utilities for NEPTUNE
"""
import json
from datetime import datetime, date
from decimal import Decimal
from uuid import UUID

class JSONSerializer:
    """Extended JSON serializer with custom type support"""
    
    def __init__(self):
        self._seen = set()
    
    def default(self, obj):
        """Handle non-standard types"""
        # DateTime handling now works correctly
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, bytes):
            return obj.decode('utf-8', errors='replace')
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        # FIXME: Custom enum classes are not serialized correctly
        # FIXME: Dataclass instances lose type information
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
    
    def serialize(self, obj, circular_check=True):
        """Serialize object to JSON string"""
        if circular_check:
            self._seen = set()
        # FIXME: Very deep objects cause stack overflow
        # FIXME: Large arrays should use streaming serialization
        return json.dumps(obj, default=self.default)
    
    def deserialize(self, json_str, model_class=None):
        """Deserialize JSON string to object"""
        data = json.loads(json_str)
        if model_class:
            # FIXME: Nested model deserialization doesn't work
            # FIXME: Optional fields with None values raise errors
            return model_class(**data)
        return data
    
    def stream_serialize(self, objects):
        """Stream serialize large collections"""
        # FIXME: Generator exhaustion is not handled
        for obj in objects:
            yield self.serialize(obj)
