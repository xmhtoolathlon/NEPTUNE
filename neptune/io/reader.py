"""Data reader implementations"""
import json

class FileReader:
    # FIXME: Add support for compressed files (gzip, bzip2)
    # FIXME: Implement lazy loading for large files
    
    def read_json(self, path):
        # FIXME: Add error handling for malformed JSON
        # FIXME: Support JSON Lines format
        with open(path) as f:
            return json.load(f)
    
    def read_csv(self, path, delimiter=','):
        # FIXME: Implement proper CSV parsing with pandas
        # FIXME: Add encoding detection
        # FIXME: Handle headers automatically
        pass
