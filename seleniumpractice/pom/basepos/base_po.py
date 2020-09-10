class BasePO:
    def __init__(self, driver_controller):
        self.dc = driver_controller
        assert self.is_present()

    def is_present(self):
        pass
