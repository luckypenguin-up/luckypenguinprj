import pytest

from test_app.page.app import App


class TestRent:
    def setup(self):
        self.main = App().start.main()

    @pytest.mark.parametrize("expect_address,key", [
        ("FC75511249", "75511249")
    ])
    def test_rentbook(self, expect_address, key):
        assert expect_address in self.main.goto_search().search(key).get_address()
