
"""
Generate lots of kinds data with Faker
* User information
"""

from faker import Faker, Factory
import logging


class FakerGenerator(object):
    """Generate different data by this class."""
    fake = None

    def __init__(self, language=None):
        if language:
            self.fake = Factory.create(language)
        else:
            self.fake = Faker()

    def gen_user_info(self):
        user = User()
        user.name = self.fake.name()
        user.address = self.fake.address()
        return user

    def get_full_values(self):
        full_values = FullValues()
        full_values.address = self.fake.address()
        # full_values.barcode = self.fake.barcode()
        full_values.color = self.fake.safe_hex_color()
        full_values.company = self.fake.company()
        full_values.credit_card = self.fake.credit_card_number()
        full_values.currency = self.fake.currency_code()
        full_values.date_time = self.fake.date_time()
        full_values.file = self.fake.file_name()
        full_values.internet = self.fake.company_email()
        full_values.job = self.fake.job()
        full_values.lorem = self.fake.text(max_nb_chars=200)
        full_values.misc = self.fake.password()
        full_values.person = self.fake.name_female()
        full_values.phone_number = self.fake.phone_number()
        full_values.profile = self.fake.profile()
        # full_values.python = self.fake.python()
        full_values.ssn = self.fake.ssn()
        full_values.user_agent = self.fake.user_agent()
        return full_values


class FullValues(object):
    address = None
    barcode = None
    color = None
    company = None
    credit_card = None
    currency = None
    date_time = None
    file = None
    internet = None
    job = None
    lorem = None
    misc = None
    person = None
    phone_number = None
    profile = None
    python = None
    ssn = None
    user_agent = None

    def __str__(self):
        """Get this object instance string values."""
        return 'FullValues = [%s]' % ', '.join(['%s: %s' % item for item in self.__dict__.items()])


class User(object):
    name = ''
    address = ''

    def __str__(self):
        """Get this object instance string values."""
        return 'User = [%s]' % ', '.join(['%s: %s' % item for item in self.__dict__.items()])

gen = FakerGenerator(language='zh_CN')
print gen.gen_user_info().__str__()
logging.info(gen.gen_user_info().__str__())

full = gen.get_full_values()
print full.__str__()
