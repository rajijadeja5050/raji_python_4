from django.db import models

# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	gender=models.CharField(max_length=10)
	subject=models.CharField(max_length=300)
	city=models.CharField(max_length=30)
	address=models.TextField()

	def __str__(self):
		return self.name
