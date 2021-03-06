#snippets/urls.py
from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^$', views.SnippetListView.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)$', views.SnippetDetailView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>[0-9]+)$', views.SnippetDeleteView.as_view(), name='delete'),
    url(r'^new$', views.new, name='new'),
]
