from seleniumpractice.pom.basepos.base_po import BasePO


class BasePage(BasePO):
    page_url = None

    def is_present(self):
        return self.dc.does_curr_url_contain(self.page_url)
