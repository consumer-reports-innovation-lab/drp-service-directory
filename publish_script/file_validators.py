import json
import os
from typing import List

class AgentFile():
    def __init__(self, filename):
        self.filename = filename
        self.document = None

    def validate(self):
        with open(self.filename, 'r') as f:
            self.document = json.load(f)

            self.document["id"] is not None 
            self.document["verify_key"] is not None 
            self.document["web_url"] is not None 
            self.document["technical_contact"] is not None 
            self.document["business_contact"] is not None 
            self.document["identity_assurance_url"] is not None 

            return True

    @classmethod
    def from_dir(cls):
        return os.path.join(os.getcwd(), "agents")

    @classmethod
    def to_file(cls):
        return os.path.join(os.getcwd(), "docs/agents.json")

class BusinessFile():
    def __init__(self, filename):
        self.filename = filename
        self.document = None

    def validate(self):
        with open(self.filename, 'r') as f:
            self.document = json.load(f)

            self.document["id"] is not None 
            self.document["name"] is not None 
            self.document["logo"] is not None 
            self.document["api_base"] is not None 
            if not isinstance(self.document["supported_actions"], list):
                raise Exception("supported_actions must be list")
            self.document["web_url"] is not None 
            self.document["technical_contact"] is not None 
            self.document["business_contact"] is not None 

            return True

    @classmethod
    def from_dir(cls):
        return os.path.join(os.getcwd(), "businesses")

    @classmethod
    def to_file(cls):
        return os.path.join(os.getcwd(), "docs/businesses.json")
