
from test_app.page.app import App
from test_app.page.profile import Profile


class TestProfile:
    def setup(self):
        self.profile = App().start.main().goto_profile()

    def test_profile(self):
        assert '错误' in self.profile.login("15611112222","123456")
