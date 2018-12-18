from django import forms

class feedback(forms.Form):
	comment=forms.CharField(max_length=30)
	YourName=forms.CharField(max_length=30)
	email=forms.EmailField(max_length=30)

class register(forms.Form):
	ContactNumber=forms.IntegerField(max_length=14)
	YourName=forms.CharField(max_length=30)
	email=forms.EmailField(max_length=30)
	CourseName=forms.CharField(max_length=20)