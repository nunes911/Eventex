from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Marcus Nunes', cpf='12345678901',
                    email='marcus@nunes.net', phone='21-98655-5315')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]
            
    def test_subscription_email_subject(self):
        expect = 'Confirmacao de inscricao'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)
    
    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'marcus@nunes.net']
        self.assertEqual(expect, self.email.to)
    
    def test_subscription_email_body(self):
        contents = ['Marcus Nunes', '12345678901', 
                    'marcus@nunes.net', '21-98655-5315']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
        