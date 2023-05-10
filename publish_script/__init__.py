import json
import os

import logging
logging.basicConfig(level=logging.DEBUG)

class Publisher():
    def __init__(self):
        pass

    def generate(self):
        agent_files = self.collect_files("agents")
        biz_files   = self.collect_files("businesses")

    def collect_files(self, root_path: str):
        files = list()
        for root, dirs, files in os.walk(root_path):
            new_files = [
                fname
                for fname in files
                if fname.endswith(".json")
            ]
            logging.info(f"found {len(new_files)} in {root}")
            files += new_files

        return files
