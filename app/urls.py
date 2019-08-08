from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from .import views

router = routers.DefaultRouter()
router.register(r'StudentViews', views.StudentViews)
app_name = 'app'


urlpatterns = [
    path('', views.StudentCreateView.as_view(), name='student_registeration'),
    path('api/', include(router.urls))
]
