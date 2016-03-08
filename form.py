from django import forms

class AuthorForm(form.Form):
	name = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)

	def send_mail(self):
		pass
