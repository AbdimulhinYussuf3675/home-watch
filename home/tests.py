from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile,Business,Post,Neighborhood,EmergencyContacts
# Create your tests here.

class UserProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='user-password')
        self.new_profile = UserProfile(id=1,first_name='Firstname',last_name='Lastname',user=self.new_user,location='Test Location')
        self.new_neighborhood = Neighborhood(id=1,neighborhood_name='Test Neighborhood')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,UserProfile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = UserProfile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = UserProfile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_assign_neighborhood(self):

        self.new_profile.save_profile()
        profile = UserProfile.objects.filter(id=1).first()
        self.new_neighborhood.save()
        neighborhood = Neighborhood.objects.filter(id=1).first()
        profile.assign_neighborhood(neighborhood)

        self.assertEqual(profile.neighborhood.id,1)

class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.new_neighborhood = Neighborhood(id=1,neighborhood_name='Test Neighborhood')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighborhood,Neighborhood))

    def test_create_neighborhood(self):
        self.new_neighborhood.create_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) > 0)

    def test_delete_neighborhood(self):
        self.new_neighborhood.delete_neighborhood()
        neighborhoods = Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) == 0)

    def test_find_neighborhood(self):
        self.new_neighborhood.create_neighborhood()
        neighborhood = Neighborhood.find_neighborhood(1)
        self.assertEqual(neighborhood.neighborhood_name,'Test Neighborhood')

    def test_update_neighborhood(self):
        self.new_neighborhood.create_neighborhood()
        neighborhood = Neighborhood.find_neighborhood(1)
        neighborhood.neighborhood_name = 'Another Neighborhood'
        self.assertEqual(neighborhood.neighborhood_name,'Another Neighborhood')



