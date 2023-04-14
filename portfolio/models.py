from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	phone_number = models.CharField(max_length=10)
	description = models.TextField()
    
	def __str__(self):
		return self.name