import pytest
from feishu.api_test.feishu_api.message.chat_group import ChatGroup
from feishu.api_test.utils.logger import init_logger


class TestFeishuChats:

    def setup_class(self):
        # configure logger
        init_logger()
        self.chats = ChatGroup()

    @pytest.mark.parametrize("chat_group_name, chat_group_description", [
        ("Test Chat Group", "This is a test chat group")
    ])
    def test_get_chat_group_info(self, chat_group_name, chat_group_description):
        # create a chat group before get the information
        chat_id = self.chats.create_chat_group(chat_group_name, chat_group_description)["data"]["chat_id"]

        r = self.chats.get_chat_group_info(chat_id)
        assert r["data"]["name"] == chat_group_name

    @pytest.mark.parametrize("chat_group_name, chat_group_description", [
        ("Test Chat Group", "This is a test chat group")
    ])
    def test_create_chat_group(self, chat_group_name, chat_group_description):
        r = self.chats.create_chat_group(chat_group_name, chat_group_description)
        chat_id = r["data"]["chat_id"]
        assert r["data"]["name"] == chat_group_name

        r = self.chats.get_chat_group_info(chat_id)
        assert r["data"]["name"] == chat_group_name

    @pytest.mark.parametrize("old_name, old_description, new_name, new_description", [
        ("Test Chat Group", "This is a test chat group", "Updated name", "Updated Description")
    ])
    def test_update_chat_group_info(self, old_name, old_description, new_name, new_description):
        chat_id = self.chats.create_chat_group(old_name, old_description)["data"]["chat_id"]
        r = self.chats.update_chat_group_info(chat_id, new_name, new_description)
        assert r["code"] == 0

        r = self.chats.get_chat_group_info(chat_id)
        assert r["code"] == 0 and r["data"]["name"] == new_name
        assert r["code"] == 0 and r["data"]["description"] == new_description

    @pytest.mark.parametrize("chat_group_name, chat_group_description", [
        ("Test Chat Group", "This is a test chat group")
    ])
    def test_dissolve_chat_group(self, chat_group_name, chat_group_description):
        chat_id = self.chats.create_chat_group(chat_group_name, chat_group_description)["data"]["chat_id"]
        r = self.chats.dissolve_chat_group(chat_id)
        assert r["code"] == 0

        r = self.chats.dissolve_chat_group(chat_id)
        assert r["code"] == 232009
