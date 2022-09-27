from django import forms


# Tie the information here with the models class we've made
class TaskUpload(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', max_length=255)
    
