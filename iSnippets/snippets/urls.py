#snippets/urls.py
from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^$', views.SnippetListView.as_view()),
    url(r'^new$', views.new, name='new'),
]
