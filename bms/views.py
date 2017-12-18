from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Author
from .models import Publisher
from .models import Book

class HomeView(TemplateView):
	template_name = 'bms/index.html'

class AuthorsView(ListView):
	model = Author
	context_object_name = 'authors'

class AuthorView(DetailView):
	model = Author

class PublishersView(ListView):
	model = Publisher

class PublisherView(DetailView):
	model = Publisher

class BooksView(ListView):
	model = Book

class BookView(DetailView):
	model = Book
