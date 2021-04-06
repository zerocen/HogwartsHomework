import pytest
from api.utils.logger import init_logger
from api.wecom.contacts import Contacts


class TestWecomContacts:
    userid = "wecomtest"
    name = "Wecom Test"

    def setup_class(self):
        # configure logger
        init_logger()
        self.contacts = Contacts()
        self.mobile = "17166553321"
        self.department = [1]

    def setup(self):
        # self.userid += "_tmp"
        self.contacts.delete_member(self.userid)

    def teardown(self):
        self.contacts.delete_member(self.userid)

    def test_get_member_info(self):
        # create a member before get the information
        self.contacts.create_member(self.userid, self.name, self.mobile, self.department)

        r = self.contacts.get_member_info(self.userid)
        assert r["name"] == self.name

    def test_create_member(self):
        r = self.contacts.create_member(self.userid, self.name, self.mobile, self.department)
        assert r["errmsg"] == "created"

        r = self.contacts.get_member_info(self.userid)
        assert r["name"] == self.name

    @pytest.mark.parametrize("new_name", [name + "_tmp"]*10)
    def test_update_member_name(self, new_name):
        self.contacts.create_member(self.userid, self.name, self.mobile, self.department)
        r = self.contacts.update_member_name(self.userid, new_name)
        assert r["errmsg"] == "updated"

        r = self.contacts.get_member_info(self.userid)
        assert r["name"] == new_name

    def test_delete_member(self):
        self.contacts.create_member(self.userid, self.name, self.mobile, self.department)
        r = self.contacts.delete_member(self.userid)
        assert r["errmsg"] == "deleted"

        r = self.contacts.get_member_info(self.userid)
        assert r["errcode"] == 60111
