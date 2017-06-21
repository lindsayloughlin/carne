from django.conf.urls import url
from django.conf.urls.static import static

from mysite import settings
from polls import data_access
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/hints/$', views.hints, name='hints'),
    url(r'^(?P<question_id>[0-9]+)/model/$', data_access.question_json ,name='question_model')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
