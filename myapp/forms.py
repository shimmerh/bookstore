from django.forms import ModelForm
from myapp.models import * 

# Create the form from class
class AuthorModelForm(ModelForm):
	class Meta:
		model = Author
		fields = '__all__'

	
class AuthorForm(ModelForm):
	class Meta:
		model = Author
		fields = ['name','title', 'birth_date']


class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ['name','authors']
