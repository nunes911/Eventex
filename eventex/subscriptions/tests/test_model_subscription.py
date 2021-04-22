from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(name='Marcus Nunes', cpf='12345678901', 
                            email='marcus@nunes.net', phone='21-987654321')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())
    
    def test_created_at(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)
    
    def test_str(self):
        self.assertEqual('Marcus Nunes', str(self.obj))