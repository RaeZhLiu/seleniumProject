from page.main_wework import MainWework
from time import sleep
import pytest


class TestAddMember(object):
    def setup(self):
        self.main = MainWework()

    def teardown(self):
        pass

    @pytest.mark.skip
    def test_add_more_members(self):
        # 实现批量添加成员
        self.main.goto_contact()
        for i in range(20, 100):
            add_member = self.main.goto_add_member()
            add_member.add_member("admin"+str(i), "admin"+str(i), "111111111"+str(i))
            sleep(3)
        # assert "aaaaa" in add_member.get_member()

    def test_add_member(self):
        self.main.goto_contact()
        add_member = self.main.goto_add_member()
        add_member.add_member("hhhhaaaaabb", "hhhhaaaaaabb", "12111234539")
        assert add_member.get_member("hhhhaaaaabb")