#coding:utf8
# Create your views here.

#just echo once
import csv

from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import ListView
from django.http import *
from django.forms import modelformset_factory
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import View, ListView 
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.utils import timezone

from models import *
from myapp.forms import AuthorForm


class MyView(View):
	def get(self, request , *args, **kwargs):
		return HttpResponse("Hello,World")


class PublisherList(ListView):
	model = Publisher
	# 用于手动设置context对象名
	context_object_name = 'publisher_list'


class PublisherDetail(DetailView):
	
	model = Publisher

	def get_context_data(self, **kwargs):
		context = super(PublisherDetail, self).get_context_data(**kwargs)
		context['book_list'] = Book.objects.all()
		return context

	context_object_name = "publisher_list"
	queryset = Publisher.objects.all()


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


# for output a cvs
def output_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

	writer = csv.writer(response)
	writer.writerow(('First row', 'Foo', 'Bar', 'Baz'))
	writer.writerow(('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"))
	writer.writerow(('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"))
	writer.writerow(('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"))

	return response


def send_mail(request):
	subject = request.GET.get('s')
	message = request.GET.get('m')
	from_mail = '12243211@qq.com'
	to_mail = ['shimmerh@qq.com']
	mail_notify(subject, message, from_mail, to_mail)

	return Jsonresponse({'errcode':0}, safe=True)


def mail_notify(subject, message, from_mail, to_mail):
	send_mail(subject, message, from_mail, to_mail)


def test(request):
	return HttpResponse(reverse('authors-list'))
