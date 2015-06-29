# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from pooopers.models import Poooper
from time_management.models import Pooop
from datetime import datetime,timedelta


class PoooperApiTest(APITestCase):
    """
    Tests for user management
    """
    start = datetime(2015,1,1,12,0)
    end   = datetime(2015,1,1,12,10)


    def setUp(self):  
        self.poooper = Poooper.objects.create_user(username="Bob",password='xxx',email="empleado@sisi.ya")
        self.client.force_authenticate(user=self.poooper)


    def test_total_poooped(self):
        p = Pooop(poooper=self.poooper,start=self.start,end=self.end)
        p.save()
        url = reverse('poooper-detail',kwargs={'pk': self.poooper})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['total_poooped'],str(self.end - self.start))

    
