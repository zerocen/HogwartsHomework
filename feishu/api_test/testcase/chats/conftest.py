import pytest
from feishu.api_test.feishu_api.chats.chat_group import ChatGroup
from feishu.api_test.feishu_api.chats.chat_group_member import ChatGroupMember
from feishu.api_test.feishu_api.chats.chat_group_message import ChatGroupMessage
from feishu.api_test.utils.logger import init_logger


@pytest.fixture(scope="session", autouse=True)
def configure_logger():
    init_logger()


@pytest.fixture(scope="module")
def chat_group():
    chat_group = ChatGroup()
    yield chat_group


@pytest.fixture(scope="module")
def chat_group_member():
    chat_group_member = ChatGroupMember()
    yield chat_group_member


@pytest.fixture(scope="module")
def chat_group_message():
    chat_group_message = ChatGroupMessage()
    yield chat_group_message
