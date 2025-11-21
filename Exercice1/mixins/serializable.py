
import json

class Serializable:
    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False, indent=2)
