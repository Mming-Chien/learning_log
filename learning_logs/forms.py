from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
	"""Class for form for add new topic"""
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}

class EntryForm(forms.ModelForm):
	"""Class for adding new entries"""
	class Meta:
		model = Entry
		fields = ["text"]
		labels = {"text": ''}
		widgets = {"text": forms.Textarea(attrs={"cols": 80})}