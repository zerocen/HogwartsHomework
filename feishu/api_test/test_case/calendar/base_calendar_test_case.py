from feishu.api_test.api.calendar.calendar_api import CalendarApi
from feishu.api_test.test_case.base_feishu_test_case import BaseFeishuTestCase


class BaseCalendarTestCase(BaseFeishuTestCase):
    def setup_class(self):
        self.calendar = CalendarApi()
