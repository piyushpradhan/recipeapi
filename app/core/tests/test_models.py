from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = 'example@gmail.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalizer(self):
        """test the email for a new used is normalized"""
        email = "example@GMAIL.com"
        user = get_user_model().objects.create_user(email, 'testpassword')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpassword')

    def test_create_new_super_user(self):
        """test creating a new super user"""
        user = get_user_model().objects.create_super_user(
            'example@gmail.com',
            'testpassword'
        )

        self.assertTrue(user.is_superuser) #included as a part of PermissionsMixin
        self.assertTrue(user.is_staff)
