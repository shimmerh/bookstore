#coding:utf8
# Create your views here.

#just echo once
import csv

from django.http import *
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import View, ListView 
from django.views.generic.detail import DetailView
from django.utils import timezone

from models import *
from myapp.forms import AuthorForm

class MyView(View):
	def get(self, request , *args, **kwargs):
		return HttpResponse("Hello,World")


class AuthorList(ListView):
	model = Author


class AuthorCreate(CreateView):
	model = Author
	fields = ['name']


class AuthorUpdate(UpdateView):
	model = Author
	
	fields = '__all__'
	template_name_suffix='_update_form'
	success_url = reverse_lazy('author-list')


class AuthorDelete(DeleteView):
	model = Author
	success_url = reverse_lazy('author-list')


class AuthorDetail(DetailView):
	model = Author
	def get_context_data(self, **kwargs):
		context = super(AuthorDetail, self).get_context_data(**kwargs)
		return context


class AuthorForm(FormView):
	template_name = 'myapp/author_form.html'
	success_url = '/authors/'
	form_class = AuthorForm

	def form_vaild(self, form):
		return super(AuthorForm, self).form_valid(form)


class BookList(ListView):
	queryset = Book.objects.order_by('-publication_date')
	context_object_name = 'book_list'






def test(request):
	return HttpResponse(reverse('authors-list'))
