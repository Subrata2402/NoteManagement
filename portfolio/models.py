from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	phone_number = models.CharField(max_length=10)
	description = models.TextField()
    
	def __str__(self):
		return self.name
	
class Blog(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	auther = models.CharField(max_length=100)
	image = models.ImageField(upload_to='media/', blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title