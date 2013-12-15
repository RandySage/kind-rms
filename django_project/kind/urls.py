from django.conf.urls import patterns, url

from kind import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<specification_id>\d+)/form/$', views.form_view, name='form_view'),
    url(r'^(?P<specification_id>\d+)/vote/$', views.vote, name='vote'),
)
