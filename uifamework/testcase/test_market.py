from uifamework.page.app import App


class TestContacts:

    def setup(self):
        self.app = App().start()
        self.main_page = self.app.goto_main_page()

    def teardown(self):
        self.app.stop()

    def test_market(self):
        self.main_page.goto_market_page().goto_search_page().search("apple")

    def test_market_2(self):
        self.main_page.goto_market_page_2().goto_search_page().search("apple")

