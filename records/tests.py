from django.test import TestCase
from .models import Record
from django.utils import timezone
from django.urls import reverse

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
class ProductViewTest(TestCase):
    # Test List View
    def test_get_product_list(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    