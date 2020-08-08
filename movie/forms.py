from django import forms
from django.forms import ModelForm
from .models import Review
class ReviewForm(ModelForm):
	class Meta:
		model=Review
		fields=['Name','Review']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['Name'].widget.attrs.update({'class': 'form-control','placeholder':'Type your name','label':None})
		self.fields['Review'].widget.attrs.update({'class':'form-control','placeholder':'Write your review'})