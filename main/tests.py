from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    #ini adalah test yang digunakan untuk cek apakah 'name' dan 'class'ada
    #ada di context di bagian views#
    
    def test_main_context_variables(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('appName', response.context)
        self.assertIn('name', response.context)
        self.assertIn('class', response.context)
        context = response.context
        self.assertEqual(context['appName'], 'Pacil-Storage')
        self.assertEqual(context['name'], 'Fatih Raditya Pratama')
        self.assertEqual(context['class'], 'PBP A')