from django.shortcuts import render
from . import forms,models

# Create your views here.
def index(request):
	return render(request,'edufox/index.html')

def page2(request):
	return render(request,'edufox/page2.html')

def feedback(request):
	f = forms.feedback()
	return render(request,'edufox/form.html',{"form":f})

def save(request):
	if(request.method=='POST'):
		form=forms.feedback(request.POST)
		if(form.is_valid()):
			models.data.objects.create(comment=form.cleaned_data['comment'], 
				YourName=form.cleaned_data['YourName'],
				email=form.cleaned_data['email']
				)
	return render(request,'edufox/index.html')

def register(request):
	d = forms.register()
	return render(request,'edufox/form2.html',{"form":d})

def save2(request):
	if(request.method=='POST'):
		form2=forms.register(request.POST)
		if(form2.is_valid()):
			models.data2.objects.create(ContactNumber=form2.cleaned_data['ContactNumber'], 
				YourName=form2.cleaned_data['YourName'],
				email=form2.cleaned_data['email'],
				CourseName=form2.cleaned_data['CourseName'],
				)
	return render(request,'edufox/index.html')
