
# Create your views here.

#just echo once
import csv

from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import ListView
from django.http import HttpResponse, JsonResponse
from django.forms import modelformset_factory
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from models import Author


class AuthorList(ListView):
	model = Author


class AuthorCreate(CreateView):
	model = Author
	fields = ['name']

class AuthorUpdate(UpdateView):
	model = Author
	fields = ['name']

class AuthorDelete(DeleteView):
	model = Author
	success_url = reverse_lazy('author-list')

def some_view(request):
	return JsonResponse({'errcode':0})

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

def get_balls(request):
	return Jsonresponse(['a',b])

def mail_notify(subject, message, from_mail, to_mail):
	send_mail(subject, message, from_mail, to_mail)
