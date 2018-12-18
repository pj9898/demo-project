from django.db import models

# Create your models here.
class data(models.Model):
	comment=models.CharField(max_length=30)
	YourName=models.CharField(max_length=30)
	email=models.EmailField(max_length=30)

class data2(models.Model):
	ContactNumber=models.IntegerField(max_length=14)
	YourName=models.CharField(max_length=30)
	email=models.EmailField(max_length=30)
	CourseName=models.CharField(max_length=20)

