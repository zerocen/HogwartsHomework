from api.wecom.contacts import Contacts


class TestWecomContacts:

    def setup_class(self):
        self.contacts = Contacts()

    def test_get_member_info(self):
        r = self.contacts.get_member_info()
        print(r)
