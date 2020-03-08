import pytest

from test_app.page.app import App


class TestSearch:
    def setup(self):
        self.main = App().start.main()


    def test_search(self):
        #print(self.main)
        assert self.main.goto_search().search("alibaba").get_price("BABA") > 200

    def test_market_select(self):
        step1 = self.main.goto_market().market_search("jd").add_select()
        assert "已添加" in step1.get_msg()
        step1.un_select()
        step1.market_search_back()



    @pytest.mark.parametrize("key,stock_type,price", [
        ("alibaba", "BABA", 200),
        ("JD", "JD", 20)
    ])
    def test_search_data(self, key, stock_type, price):
        assert self.main.goto_search().search(key).get_price(stock_type) > price
