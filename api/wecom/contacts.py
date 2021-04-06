from api.utils.logger import logger
from api.wecom.base import Base


class Contacts(Base):

    def get_member_info(self, userid):
        logger.info("Getting member information...")
        path = "/cgi-bin/user/get"
        params = {
            "userid": userid
        }
        r = self.send_request("GET", f"{self.base_url}{path}", params=params)
        return r.json()

    def create_member(self, userid, name, mobile, department):
        logger.info("Creating member response...")
        path = "/cgi-bin/user/create"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = self.send_request("POST", f"{self.base_url}{path}", json=data)
        return r.json()

    def update_member_name(self, userid, name):
        logger.info("Updating member name response...")
        path = "/cgi-bin/user/update"
        data = {
            "userid": userid,
            "name": name
        }
        r = self.send_request("POST", f"{self.base_url}{path}", json=data)
        return r.json()

    def delete_member(self, userid):
        logger.info("Deleting member response...")
        path = "/cgi-bin/user/delete"
        params = {
            "userid": userid
        }
        r = self.send_request("GET", f"{self.base_url}{path}", params=params)
        return r.json()
