from django.forms import ModelForm
from myapp.models import Author

# Create the form from class
class AuthorForm(ModelForm):
	class Meta:
		model = Author
		fields = '__all__'

	

