import pytest

from test_app.page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start.main()

    @pytest.mark.parametrize("expect_address,key", [
        ("FC75511249", "75511249")
    ])
    def test_search(self, expect_address, key):
        assert expect_address in self.main.goto_search().search(key).get_address()

    @pytest.mark.parametrize("key", [
        ("75511249")
    ])
    def test_box_select(self, key):
        step1 = self.main.goto_search().search(key).add_select()
        assert "已收藏" in step1.get_msg()
        step2 = step1.un_select()
        assert "收藏" in step2.get_msg()

