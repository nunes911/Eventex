from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Marcus Nunes',
            slug='marcus-nunes',
            photo='http://hbn.link/hb-pic'
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='marcus@nunes.net'
        )

        self.assertTrue(Contact.objects.exists())
    
    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='21-987654321'
        )

        self.assertTrue(Contact.objects.exists())
    
    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')

        self.assertRaises(ValidationError, contact.full_clean)
    
    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='marcus@nunes.net'
        )

        self.assertEqual('marcus@nunes.net', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Marcus Nunes',
            slug='marcus-nunes',
            photo='http://hbn.link/hb-pic'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='marcus@nunes.net')
        s.contact_set.create(kind=Contact.PHONE, value='21-987654321')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['marcus@nunes.net']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
    
    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['21-987654321']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)