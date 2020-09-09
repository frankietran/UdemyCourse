from selenium.webdriver.common.by import By

from seleniumpractice.POM.BasePOs.base_modal import BaseModal

modal_id = "modal-choose-package"


class ChoosePackageModal(BaseModal):
    def __init__(self, driver_controller):
        BaseModal.__init__(self, driver_controller)
        assert self.is_present(modal_id), "Choose package modal does not exist"
