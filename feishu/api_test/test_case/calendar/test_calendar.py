import pytest

from feishu.api_test.test_case.calendar.base_calendar_test_case import BaseCalendarTestCase
from feishu.api_test.utils import Utils


class TestCalendar(BaseCalendarTestCase):
    def setup(self):
        pass

    # 1. 参数化+数据驱动
    # 2. 纯数据驱动，把用例步骤也数据化
    @pytest.mark.parametrize("test_param", Utils.load_yaml("data/calendar/create.yml"))
    def test_creat(self, test_param):
        item = self.calendar.creat("xxxx")
        item_list = self.calendar.list()
        assert item in item_list
