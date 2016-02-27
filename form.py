from django import forms

class ContactForm(form.Form):
	name = forms.CharField()
	message = forms.CharField(widget=forms.Textarea)

	def send_mail(self):
		pass
