from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.HomeView.as_view(), name='index'),
	url(r'^author/$', views.AuthorsView.as_view(), name='authors'),
	url(r'^author/(?P<pk>\d+)/$', views.AuthorView.as_view(), name='author'),
	url(r'^publisher/$', views.PublishersView.as_view(), name='publishers'),
	url(r'^publisher/(?P<pk>\d+)/$', views.PublisherView.as_view(), name='publisher'),
	url(r'^book/$', views.BooksView.as_view(), name='books'),
	url(r'^book/(?P<pk>\d+)/$', views.BookView.as_view(), name='book'),
]
