from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.


class LocationTestClass(TestCase):
    # Set up method that helps to create an instance of a class
    def setUp(self):
        self.keke= Location(name='kakiru')


    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.keke,Location))

 



class CategoryTestClass(TestCase):
    # Set up method that helps to create an instance of a class
    def setUp(self):
        self.lili= Category(name='remembrance')


    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.lili,Category))

    def test_save_method(self):
        self.lili.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)
 
class ImageTestClass(TestCase):

   def setUp(self):
        # Creating a new location and saving it
        self.keke= Location(name = 'kakiru')
        self.keke.save_location()

        # Creating a new category and saving it
        self.lili = Category(name = 'remembrance')
        self.lili.save()

        self.image= Image(img_name = 'passport',img_description = 'This is a random test Photo',location = self.keke)
        self.image.save()

        self.image.category.add(self.category)
