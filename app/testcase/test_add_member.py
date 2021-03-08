from app.page.app import App


class TestAddMember:

    def setup_class(self):
        self.app = App().start()
        self.main_page = self.app.goto_main_page()

    def teardown_class(self):
        self.app.stop()

    def test_add_member(self):
        self.main_page.goto_contacts_page().goto_add_member_page().goto_add_member_info_page(). \
            input_and_save_member_completely("112233", "123", "554", "男", "15677892235", "021021112", "123@test.com",
                                             "XXX路45号", "产品经理", "产品部", "普通成员")
