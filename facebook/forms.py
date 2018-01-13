from django import forms
from .models import FacebookPage

class FacebookPageForm(forms.ModelForm):
	class Meta:
		model = FacebookPage
		fields = [
			#'page_id',
			#'name',
			'url',
            #'created_at',
		]

		labels = {
			#'page_id': 'Page',
			#'name': 'Name',
			'url': 'Name/URL',
			#'created_at': 'Created at',
		}

		widgets = {
			'page_id': forms.TextInput(attrs={'class':'form-control'}),
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'url': forms.TextInput(attrs={'class':'form-control col-md-9','placeholder':'Name/URL'}),
			'created_at': forms.SelectDateWidget(attrs={'class':'form-control'}),
		}