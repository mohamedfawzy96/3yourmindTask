from django.conf.urls import url
from .views import *

app_name = 'materials'
urlpatterns = [
    #url(r'^generate/$', generate_data_for_materials , name='generate_data_materials'),
    url(r'^home/$', return_all_materials , name='materials_home'),
    url(r'^supplier/(?P<id>[0-9]+)$', return_materials_supplier, name='supplier'),

]


