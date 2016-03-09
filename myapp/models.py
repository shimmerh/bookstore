#coding:utf8

from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Create your models here.


TITLE_CHOICES = (
	('MR', 'Mr.'),
	('MRS', 'Mrs'),
	('MR', 'Ms.')
)

class Publisher(models.Model):
	name = models.CharField(max_length=30, verbose_name='姓名')
	address = models.CharField(max_length=50, verbose_name="地址")
	city = models.CharField(max_length=60, verbose_name='市')
	state_province = models.CharField(max_length=30, verbose_name='邮政编码')
	country = models.CharField(max_length=50, verbose_name='国家')
	website = models.URLField(verbose_name='主页')

	class Meta:
		ordering = ["-name"]
	
	def __unicode__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=100, verbose_name='姓名')
	title = models.CharField(max_length=3, choices=TITLE_CHOICES, verbose_name='称呼')
	birth_date = models.DateField(blank=True, null=True, verbose_name='生日')
	email = models.EmailField(verbose_name='电子邮箱')
	headshot = models.ImageField(blank=True, upload_to='author_headshot', verbose_name='头像')
	create_by = models.ForeignKey(User, verbose_name='操作人')

	def get_absolute_url(self):
		return reverse('author-detail', kwargs={'pk': self.pk})	
	
	def get_image_url(self):
		return "/media/%s" % self.headshot

	def __unicode__(self):
		return self.name


class Book(models.Model):
	name = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	publication_date = models.DateField()




