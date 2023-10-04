from django.test import TestCase
from .models import Record
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from .views import *

# Create your tests here.
# Test our model
class RecordTest(TestCase):

    # Create our model instance
    def create_record(self):
        return Record.objects.create(first_name="David", last_name="Muyesi", 
                                     email="dav@gm.com", phone="078327452", 
                                     address="3211-Caryford", city="Caryford",
                                     state="New Oaklands", zipcode="02002",
                                     created_at=timezone.now())
    

    # Test the model instance creation
    def test_record_creation(self):
        record = self.create_record()
        self.assertTrue(isinstance(record, Record))
        self.assertEqual(record.__str__(), 
                         record.first_name + " " + record.last_name)


# Test views
class RecordViewTest(TestCase):
    # Test List View
    def test_get_record_list(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')



    # Test Production Creation View
    def test_create_record_logged_in(self):
        self.client.login(username="Ronny", password="testing321")
        response = self.client.post('/add_record/', {
            "first_name": "David",
            "last_name": "Muyesi",
            "email": "dav@gm.com",
            "phone": "078327452",
            "address": "3211-Caryford",
            "city": "Caryford",
            "state": "New Oaklands",
            "zipcode": "02002",
            "created_at": timezone.now(),
        })

        # Assert that the response is a 302 redirect code
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, "add_record.html")
        self.assertRedirects(response, '/')

    
    # Test single record view
    def test_get_single_record_when_logged_in(self):
        # Create a logged-in user
        user = User.objects.create(username="testuser", password="password")
        self.client.login(username="testuser", password="password")

        # Create a record instance
        record = Record.objects.create(first_name="David", last_name="Muyesi", 
                                     email="dav@gm.com", phone="078327452", 
                                     address="3211-Caryford", city="Caryford",
                                     state="New Oaklands", zipcode="02002",
                                     created_at=timezone.now())

        # Get the response from the view
        response = self.client.get(f'/records/{record.pk}/')

        # Assert that the response is a 200 OK status code
        self.assertEqual(response.status_code, 200)

        # Asser that it redirects you to the home page
        self.assertRedirects('/')

        # Assert that it renders to the right template
        self.assertTemplateUsed(response, "single_record.html")

    