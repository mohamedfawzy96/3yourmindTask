from django.conf.urls import url
from .views import *

app_name = 'materials'
urlpatterns = [
    url(r'^generate/$', generate_data_for_materials , name='generate_data_materials'),
]


