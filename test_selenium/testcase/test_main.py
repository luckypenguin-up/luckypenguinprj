from ..page.main import Main


class TestMain:
    def setup(self):
        self.main = Main(reuse=True)

    def test_add_member(self):
        self.main.add_member().add_member("xxx")
        assert "aaa" in self.main.import_user().get_message()

    def test_import_user(self):
        self.main.import_user("/Users/liqian/PycharmProjects/luckypenguinprj/test_selenium/通讯录批量导入模板.xlsx")
        #assert "success" in self.main.get_message()

    def test_import_photo(self):
        self.main.import_photo("/Users/liqian/PycharmProjects/luckypenguinprj/test_selenium/jiafeicat.jpg")

'''
    def test_send_message(self):
        main.send_message()
        assert  "" in main.get_message()

'''