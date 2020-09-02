import json
import time


class StorefrontConfig:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def merge(ori, new):
        """
        Function used to merge two dictionary
        Reference source: https://stackoverflow.com/questions/7204805/how-to-merge-dictionaries-of-dictionaries
        :param ori: the data dictionary
        :param new: the modify_data dictionary
        :return: none
        """
        for key in new:
            if key not in ori:
                ori[key] = new[key]
            else:
                if type(ori[key]) == type(new[key]):
                    if ori[key] == new[key]:
                        pass
                    elif isinstance(ori[key], dict):
                        StorefrontConfig.merge(ori[key], new[key])
                    else:
                        ori[key] = new[key]
                else:
                    print("Type Err")

    def update(self, modify_data):
        StorefrontConfig.merge(self.data, modify_data)


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


modify_data = {
  "expiration_time": 200,
  "product": "qchat",
  "utm_campaign": str(time.time()),
  "storefront": {
    "banner_enabled": False,
    "purchase_options": [
          {
              "button_text": "Dynamic offer 1 - button_text",
              "description": "Dynamic offer 1 - description",
              "id": "",
              "price": "99.99",
              "price_text": "price_text",
              "session_count": "0",
              "subtitle": "Dynamic offer - subtitle",
              "title": "Dynamic offer - title",
              "suffix": "Dynamic offer - suffix",
              "trial_duration": 0,
              "min_member_count": 1,
              "max_member_count": 1,
              "action": "purchase",
              "frequency_view": "monthly",
              "free_learning_subscription": False,
              "team_type": "personal",
              "frequency": None,
          }
      ]
  }
}

file_controller = FileController()
config = file_controller.read_file("data.json")
config.update(modify_data)
file_controller.write_file(config, "result.json")
