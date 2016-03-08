#coding:utf8
# Create your views here.

#just echo once
import csv

from django.http import *
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import View, CreateView, UpdateView, DeleteView, FormView, ListView, DetailView
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
	fields = '__all__'
	success_url = reverse_lazy('author-list')


class AuthorUpdate(UpdateView):
	fields = '__all__'
	model = Author
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
	form_class = AuthorModelForm


def test(request):
	return HttpResponse(reverse('authors-list'))
