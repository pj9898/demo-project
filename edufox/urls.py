from django.urls import path
from . import views
urlpatterns=[
	path('',views.index,name='index'),
	path('page2/',views.page2, name='page2'),
	path('feedback/',views.feedback,name='feedback'),
	path('save/',views.save,name='save'),
	path('register/',views.register,name='register'),
	path('save2/',views.save2,name='save2'),
	]