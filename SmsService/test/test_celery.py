from pytest import mark, fixture
from SmsService.tasks import send_email

class TestCelery:
    def test_celery(self):
        elem = send_email.delay('qqq@aaa.asd', 'trial email')
        assert True
