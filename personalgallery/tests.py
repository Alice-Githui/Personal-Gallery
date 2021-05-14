from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.

class ImageTestClass(TestCase):
    #setup method

    def setUp(self):

        #creating new location and saving it
        self.park=Location(name="park")
        self.park.save_location()

        #creating new category and saving it 
        self.outside = Category(name="outside")
        self.outside.save_category()
        
        #creating new image instance and saving it 
        self.image1 = Image(image="https://unsplash.com/photos/8ZfTxdPvNos", image_name='Elephant Portrait', description='Gorgeous close up image of an elephant', location=self.park, category=self.outside)
        self.image1.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image1, Image))

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


# class LocationTestClass(TestCase):
#     #setUpmethod
#     def setUp(self):
#         self.park=Park(name="park")
#         self.park.save_location()

# class CategoryTestClass(TestCase):
#     #setUpmethod

#     def setUp(self):
#         self.outside = Category(name="outside")
#         self.outside.save_category()
