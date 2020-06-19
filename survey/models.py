from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Survey(models.Model): 
    name = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_questions(self):
        return self.question_set.all()

    def __str__(self): 
        return "id: "+str(self.id)+", name: "+str(self.name)+", created_by: "+str(self.created_by.id) 

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    class QuestionType(models.TextChoices):   
        TEXT = 'TE', _('Text')
        SINGC = 'SC', _('Single Choice')
        MULTIC = 'MC', _('Multiple Choice')
    
    QType = models.CharField(
            max_length=2,
            choices=QuestionType.choices,
            default=QuestionType.TEXT,
        )
    def __str__(self): 
        return "id: "+str(self.id)+", survey: "+str(self.survey.id)+", text: "+str(self.text)+", Qtype: "+str(self.QType)

class Option(models.Model):
    order = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self): 
        return "id: "+str(self.id)+", order: "+str(self.order.id)+", text: "+str(self.text)     

class Answer(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    answered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_date = models.DateTimeField('response date')

    def __str__(self): 
       return "id: "+str(self.id)+", survey: "+str(self.survey.id)+", answered_by: "+str(self.answered_by.id)+", question: "+str(self.question.id)+", response_date: "+str(self.response_date)

class TextAnswer(Answer):
    text = models.TextField(default="")

    def __str__(self):
        return str(super().__str__())+", text: "+str(self.text)

class SingleChoiceAnswer(Answer): 
    option = models.ForeignKey(Option,on_delete=models.CASCADE)

    def __str__(self):
        return str(super().__str__())+", option: "+str(self.option.id)

class MultipleChoiceAnswer(Answer):
    options = models.ManyToManyField(Option, db_table="survey_choices")
    def __str__(self):
        return str(super().__str__()) 
