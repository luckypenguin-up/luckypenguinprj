
#import sys
#sys.path.append('selenium/page/contact')
from ..page.contact import Contact

class TestContact:
    def test_add_member(self):

        contact=Contact()
        contact.add_member("xxx")