import json
import os

import logging
logging.basicConfig(level=logging.DEBUG)

class Publisher():
    def __init__(self):
        pass

    def generate(self, constructor_cls):
        directory_entries = self.collect_files(
            constructor_cls.from_dir(),
            constructor_cls
        )
        for de in directory_entries:
            de.validate()

        document_ids = [
            de.document["id"]
            for de in directory_entries
        ]
        duplicate_ids = [
            document_id
            for document_id in document_ids
            if document_ids.count(document_id) > 1
        ]
        unique_duplicate_ids = list(set(duplicate_ids))
        if len(unique_duplicate_ids) > 0:
            raise Exception(f"Duplicate IDs: {unique_duplicate_ids}")

        directory = [
            de.document
            for de in directory_entries
        ]

        logging.info(f"{len(directory)} entities to export to {constructor_cls.export_loc()} (and individual references)")
        assert(len(directory) == len(directory_entries))

        for entry in directory_entries:
            path = entry.to_file()
            logging.debug(f"exporting {entry.document['id']} to {path}")
            with open(path, "w") as f:
                json.dump(entry.document, f, indent=4)

        with open(constructor_cls.export_loc(), "w") as f:
            json.dump(directory, f, indent=4)

    def collect_files(self, root_path: str, constructor_cls):
        logging.info(f"processing files for {constructor_cls}")

        retfiles = list()
        for root, dirs, files in os.walk(root_path):
            new_files = [
                constructor_cls(os.path.join(root, fname))
                for fname in files
                if fname.endswith(".json")
            ]
            logging.info(f"found {len(new_files)} in {root}")
            retfiles += new_files

        return retfiles
