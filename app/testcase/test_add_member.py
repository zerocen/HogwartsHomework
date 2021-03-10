import pytest
from app.page.app import App


class TestContacts:

    def setup(self):
        self.app = App().start()
        self.contacts_page = self.app.goto_main_page().goto_contacts_page()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name, account, alias, gender, mobile_phone, telephone, email, address, position,"
                             "department, role",
                             [("张三", "ZhangSan", "zs", "男", "12345678900", "021456789", "zhangsan@test.com",
                               "XXX路XX号", "总经理", "市场部", "上级"),
                              ("Keely", "keely", "k", "女", "18545654585", "021001155", "keely@test.com",
                               "XXX路1号", "工程师", "技术部", "普通成员"),
                              ("Erwin", "erwin", "e", "男", "15677895422", "021021554", "erwin@test.com",
                               "XXX路2号", "产品经理", "产品部", "普通成员")
                              ])
    def test_add_member_completely(self, name, account, alias, gender, mobile_phone,
                                   telephone, email, address, position, department, role):
        add_member_info_page = self.contacts_page.goto_add_member_page().goto_add_member_info_page()
        add_member_info_page.add_member_completely(name, account, alias, gender, mobile_phone, telephone,
                                                   email, address, position, department, role)

    @pytest.mark.parametrize("name, mobile_phone", [("张三2", "11111111111"),
                                                    ("Keely2", "15875658845"),
                                                    ("Erwin2", "16845628841"),
                                                    ])
    def test_add_member_simplify(self, name, mobile_phone):
        add_member_info_page = self.contacts_page.goto_add_member_page().goto_add_member_info_page()
        add_member_info_page.add_member_simplify(name, mobile_phone)

    @pytest.mark.parametrize("name", [("张三2",), ("Keely2",), ("Erwin2",)])
    def test_delete_member(self, name):
        self.contacts_page.goto_member_info_page_by_search(name)
            # .goto_member_info_settings_page()\
            # .goto_edit_member_info_page().delete_member()
