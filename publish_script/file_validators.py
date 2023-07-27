import json
import os
from typing import List

from jsonschema import validate
from jsonschema.exceptions import ValidationError

class AgentFile():
    def __init__(self, filename):
        self.filename = filename
        self.document = None
        with open("publish_script/agent.schema.json", "r") as f:
            self.schema = json.load(f)

    def validate(self):
        with open(self.filename, 'r') as f:
            self.document = json.load(f)
            # re-raise with the filename in the message
            try:
                validate(instance=self.document, schema=self.schema)
            except ValidationError as e:
                raise Exception(f"failed to validate {self.filename}:" + e.message)
            return True

    @classmethod
    def from_dir(cls):
        return os.path.join(os.getcwd(), "agents")

    @classmethod
    def export_loc(cls):
        return os.path.join(os.getcwd(), "docs/agents.json")

    def to_file(self):
        return os.path.join(
            os.getcwd(),
            "docs",
            "agents",
            f"{self.document['id']}.json"
        )

class BusinessFile():
    def __init__(self, filename):
        self.filename = filename
        self.document = None
        with open("publish_script/business.schema.json", "r") as f:
            self.schema = json.load(f)

    def validate(self):
        with open(self.filename, 'r') as f:
            self.document = json.load(f)
            # re-raise with the filename in the message
            try:
                validate(instance=self.document, schema=self.schema)
            except ValidationError as e:
                raise Exception(f"failed to validate {self.filename}:" + e.message)
            return True

    @classmethod
    def from_dir(cls):
        return os.path.join(os.getcwd(), "businesses")

    @classmethod
    def export_loc(cls):
        return os.path.join(os.getcwd(), "docs/businesses.json")

    def to_file(self):
        return os.path.join(
            os.getcwd(),
            "docs",
            "businesses",
            f"{self.document['id']}.json"
        )
