# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.test import APITestCase
from pooopers.models import Poooper
from django.core.urlresolvers import reverse



class PoooperApiTest(APITestCase):
    """
    Tests for user management
    """


    def setUp(self):  
        self.poooper = Poooper.objects.create_user(username="Bob",password='xxx',email="empleado@sisi.ya")
        self.client.force_authenticate(user=self.poooper)

    def test_jwt_success(self):
        url = reverse('obtain_jwt_token')
        data= {'username': self.poooper.username,'password':'xxx'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_jwt_failed(self):
        url = reverse('obtain_jwt_token')
        data= {'username': self.poooper.username,'password':'xxxa'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    
