#coding:utf8
# Create your views here.

#just echo once
import csv

from django.http import *
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import (
	View, CreateView, UpdateView, DeleteView, 
	FormView, ListView, DetailView
	)
from django.utils import timezone

from models import *
from myapp.forms import AuthorModelForm

class MyView(View):
	def get(self, request , *args, **kwargs):
		return HttpResponse("Hello,World")


class AuthorList(ListView):
	model = Author


class AuthorCreate(CreateView):
	model = Author
	template_name = "myapp/author_add.html"
	fields = '__all__'


class AuthorUpdate(UpdateView):
	queryset = Author.objects.all()
	template_name = "myapp/author_update_form.html"
	# for instance to add extra validation
	# if you specify the form_class,you dont set fields
	# in here, both the fields and form_class are same.
	form_class = AuthorModelForm


class AuthorDelete(DeleteView):
	model = Author
	success_url = reverse_lazy('author-list')


class AuthorDetail(DetailView):
	model = Author


class AuthorForm(FormView):
	template_name = 'myapp/author_form.html'
	success_url = reverse_lazy('author-list')
	form_class = AuthorModelForm


def test(request):
	return HttpResponse(reverse('authors-list'))
