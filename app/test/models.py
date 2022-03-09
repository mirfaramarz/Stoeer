from django.test import TestCase
from app.models import BankData

class TestBankData(TestCase):

    def test_model_str(self):
        first_name = BankData.objects.create(first_name='Doe')
        self.assertEqual(first_name,  'Doe')
        