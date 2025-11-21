import json
from datetime import datetime

class Serializable:
    def to_json(self):
        def serializer(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return str(obj)
        
        d = {k: v for k, v in self.__dict__.items() if k != 'historique'}
        return json.dumps(d, default=serializer)
