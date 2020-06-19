from django.shortcuts import render,redirect
from django.views import generic
from .models import Survey,Question
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q 
from .forms import CreateNewSurvey, CreateQuestion,CreateOption
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
def index(request):
    return render(request, "survey/index.html")

class SurveysView(LoginRequiredMixin,generic.ListView):
    login_url = '/accounts/login'
    template_name = 'survey/surveys.html'
    context_object_name = 'available_surveys_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Survey.objects.filter(~Q(created_by_id=self.kwargs['user_id']))

class MySurveysView(LoginRequiredMixin,generic.ListView):
    login_url = '/accounts/login'
    template_name = 'survey/my_surveys.html'
    context_object_name = 'my_surveys_list'

    def get_queryset(self):   
        """Retorna la lista de encuestas creadas por el usuario"""
        return User.objects.get(pk=self.kwargs['user_id']).survey_set.all()
    
@login_required
def CreateSurveyView(request):
    if request.method == "POST": 
        form = CreateNewSurvey(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            s = request.user.survey_set.create(name=name)
        return HttpResponseRedirect("create_survey/%i" %s.id)
    else: 
        form = CreateNewSurvey()
    return render(request, "survey/create_survey.html", {"form":form}) 

@login_required
def CreateSurveyQuestions(request,survey_id):
    s = Survey.objects.get(pk=survey_id) 
    questions = s.question_set.all()
    form = CreateQuestion()
    return render(request,"survey/create_survey_questions.html", {"s":s,"questions":questions,"form":form})


@login_required
def CreateQuestions(request,survey_id):
    s = Survey.objects.get(pk=survey_id) 
    if request.POST.get("add_question"):
        form = CreateQuestion(request.POST)
        if form.is_valid():
            text = form.cleaned_data["question"]
            s.question_set.create(text=text, QType= Question.QuestionType.TEXT.label)
    elif request.POST.get("add_options"):   
        form = CreateQuestion(request.POST)
        if form.is_valid():
            text = form.cleaned_data["question"]
            q = s.question_set.create(text=text, QType= Question.QuestionType.SINGC.label)
            return HttpResponseRedirect(reverse('survey:create_question_options', args=(s.id,q.id,)))

    return HttpResponseRedirect(reverse('survey:create_survey_questions', args=(s.id,)))

@login_required
def CreateQuestionsOptions(request,survey_id,question_id):
    s = Survey.objects.get(pk=survey_id)
    q = Question.objects.get(pk=question_id) 
    options = q.option_set.all()
    form = CreateOption()
    return render(request,"survey/create_question_options.html", {"s": s, "q":q,"options":options,"form":form})


@login_required
def CreateOptions(request,survey_id,question_id):
    s = Survey.objects.get(pk=survey_id)
    q = Question.objects.get(pk=question_id)
    if request.method == "POST": 
        form = CreateOption(request.POST)
        if form.is_valid():
            text = form.cleaned_data["option"]
            q.option_set.create(text=text)
    return HttpResponseRedirect(reverse('survey:create_question_options', args=(s.id,q.id,)))




class ResponseView(LoginRequiredMixin,generic.DetailView):
    login_url = '/accounts/login'
    model = Survey
    template_name = 'polls/detail.html'

class ResultsView(LoginRequiredMixin,generic.DetailView):
    login_url = '/accounts/login'
    model = Survey
    template_name = 'polls/detail.html'
