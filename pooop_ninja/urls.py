from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from pooop_ninja.pooopers.views import PoooperViewSet
from pooop_ninja.time_management.views import PooopViewSet

router = routers.DefaultRouter()
router.register(r'pooopers', PoooperViewSet)
router.register(r'pooops', PooopViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token',name='obtain_jwt_token'),
]
