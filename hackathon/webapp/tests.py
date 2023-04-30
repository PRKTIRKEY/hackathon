from django.test import TestCase

# Create your tests here.

class Tests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_women_page_status_code(self):
        response = self.client.get('/women/')
        self.assertEqual(response.status_code, 200)

    def test_admin_register_page_status_code(self):
        response = self.client.get('/admin_register/')
        self.assertEqual(response.status_code, 200)
    
    def test_admin_page_status_code(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)

    def test_book_page_status_code(self):
        response = self.client.get('/book/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_status_code(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_pre_book_page_status_code(self):
        response = self.client.get('/pre_book/')
        self.assertEqual(response.status_code, 200)

    def test_register_page_status_code(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_stand_women_page_status_code(self):
        response = self.client.get('/stand_women/')
        self.assertEqual(response.status_code, 200)

    def test_stand_page_status_code(self):
        response = self.client.get('/stand/')
        self.assertEqual(response.status_code, 200)

    def test_w_pre_book_page_status_code(self):
        response = self.client.get('/w_pre_book/')
        self.assertEqual(response.status_code, 200)

    def test_women_book_page_status_code(self):
        response = self.client.get('/women_book/')
        self.assertEqual(response.status_code, 200)