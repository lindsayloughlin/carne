from django.conf.urls import url
from django.conf.urls.static import static

from meat import views
from meat.data_api import DataApi

app_name = 'meat'
urlpatterns = [
    url(r'^$', views.meat_land_page, name='landing'),
    url(r'^suburbs/$', DataApi.suburbs, name='data_suburb'),
    # /*\w+$
    url(r'^supplier/(?P<supplier_name>\w+)/$', views.supplier_detail_page, name='supplier_detail')
    #url(r'^animal/*?P<animal_name>[a-zA-Z0-9]+/$', views.)
]
