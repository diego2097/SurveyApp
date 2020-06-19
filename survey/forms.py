from django import forms 

class CreateNewSurvey(forms.Form): 
    name = forms.CharField(label="Nombre de la encuesta", max_length=200)

class CreateQuestion(forms.Form):
    question = forms.CharField(label="Texto de la pregunta", max_length=200)

class CreateOption(forms.Form): 
    option = forms.CharField(label="Texto de la opcion", max_length=200)