<<<<<<< HEAD
from django.test import TestCase

# Create your tests here.
from .models import Movies
from .forms import UserForm
class MovieTestCase(TestCase):
    def setUp(self):
        Movies.objects.create(Director="Raju Hirani",Cast_I="Amir Khan",Cast_II="Karina Kapoor",Name="3 idiots",ReleaseYear=2009,ImdbRating="8.3",Genre="comedy",Language="hindi",Like=3,Dislike=1,Availbility="Youtube")
    def test_return_string(self):
        test_obj=Movies.objects.get(Director="Raju Hirani")
        self.assertTrue(isinstance(test_obj,Movies))
        self.assertEqual(test_obj.__str__(), f'{test_obj.Name} {test_obj.ReleaseYear}')
    def test_show_name(self):
        test_obj=Movies.objects.get(Director="Raju Hirani")
        self.assertEqual(test_obj.show_name(),'3 idiots')
    def test_release_year(self):
        test_obj=Movies.objects.get(Director="Raju Hirani")
        self.assertEqual(test_obj.ReleaseYear,2009)
class UserFormTest(TestCase):
    def test_valid_user_form(self):
        data={'username':'test','email':'test@gmail.com','first_name':'test','last_name':'test','password1':'pass12345','password2':'pass12345'}
        form = UserForm(data=data)
        self.assertTrue(form.is_valid())
    def test_invalid_user_form(self):
        data={'username':'test','email':'test@gmail.com','first_name':'test','last_name':'test','password1':'pass12345','password2':'pass'}
        form = UserForm(data=data)
=======
from django.test import TestCase

# Create your tests here.
from .models import Movies
from .forms import UserForm
class MovieTestCase(TestCase):
    def setUp(self):
        Movies.objects.create(Director="Raju Hirani",Cast_I="Amir Khan",Cast_II="Karina Kapoor",Name="3 idiots",ReleaseYear=2009,ImdbRating="8.3",Genre="comedy",Language="hindi",Like=3,Dislike=1,avail="Youtube")
    def test_return_string(self):
        test_obj=Movies.objects.get(Director="Raju Hirani")
        self.assertTrue(isinstance(test_obj,Movies))
        self.assertEqual(test_obj.__str__(), f'{test_obj.Name} {test_obj.ReleaseYear}')
    def test_show_name(self):
        test_obj=Movies.objects.get(Director="Raju Hirani")
        self.assertEqual(test_obj.show_name(),'3 idiots')
    def test_release_year(self):
        test_obj=Movies.objects.get(Director="Raju Hirani")
        self.assertEqual(test_obj.ReleaseYear,2009)
class UserFormTest(TestCase):
    def test_valid_user_form(self):
        data={'username':'test','email':'test@gmail.com','first_name':'test','last_name':'test','password1':'pass12345','password2':'pass12345'}
        form = UserForm(data=data)
        self.assertTrue(form.is_valid())
    def test_invalid_user_form(self):
        data={'username':'test','email':'test@gmail.com','first_name':'test','last_name':'test','password1':'pass12345','password2':'pass'}
        form = UserForm(data=data)
>>>>>>> 4e9142ffc6ed65bd7d01cf4c30fd7c063a11f45f
        self.assertFalse(form.is_valid())