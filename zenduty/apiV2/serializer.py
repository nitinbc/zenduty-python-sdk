import json
from datetime import datetime
from uuid import UUID


class JsonSerializable:
    def to_json(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)

    def __repr__(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)

    def __str__(self):
        return json.dumps(self, default=serialize, sort_keys=True, indent=4)


def serialize(o):
    if type(o) is datetime:
        return o.isoformat()
    elif type(o) is UUID:
        return str(o)
    else:
        return o.__dict__
