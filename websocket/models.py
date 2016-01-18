from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse
# Create your models here.


TITLE_CHOICES = (
	('MR', 'Mr.'),
	('MRS', 'Mrs'),
	('MR', 'Ms.')
)

class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	class Meta:
		ordering = ["-name"]
	
	def __unicode__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=3, choices=TITLE_CHOICES)
	birth_date = models.DateField(blank=True, null=True)
	email = models.EmailField()
	headshot = models.ImageField(upload_to='author_headshot')

	def get_absolute_url(self):
		return reverse('author-detail', kwargs={'pk':self.pk})

	def __unicode__(self):
		return self.name


class Book(models.Model):
	name = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	publication_date = models.DateField()


class AuthorForm(ModelForm):
	class Meta:
		model = Author
		fields = ['name', 'title', 'birth_date']


class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ['name','authors']


