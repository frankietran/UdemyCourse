import json
from utility import merge_dict

class StorefrontConfig:
    def __init__(self, data):
        self.data = data

    def update(self, modify_data):
        merge_dict(self.data, modify_data)


class FileController:
    @staticmethod
    def read_file(file_name):
        with open(file_name) as infile:
            d = json.load(infile)
        return StorefrontConfig(d)

    @staticmethod
    def write_file(config, file_name):
        with open(file_name, "w") as outfile:
            json.dump(config.data, outfile, indent=2)
