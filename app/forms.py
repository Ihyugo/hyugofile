from django import forms
from .models import UploadFile

class UploadFileForm(forms.ModelForm):
	class Meta:
		model = UploadFile
		fields = '__all__'

class SubmitForm(forms.Form):
	file_name=forms.CharField(max_length=30)
	pass_name=forms.CharField(max_length=60)

class MakeForm(forms.Form):
	directory_name=forms.CharField(max_length=200)
