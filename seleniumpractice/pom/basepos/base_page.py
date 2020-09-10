from seleniumpractice.pom.basepos.base_po import BasePO


class BasePage(BasePO):
    page_url = None

    def is_present(self):
        return self.dc.wait_for_url_that_contains(self.page_url)
