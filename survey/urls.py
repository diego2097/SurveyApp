from django.urls import path

from . import views

app_name = 'survey'
urlpatterns = [
    path('', views.index, name='index'),
    path('surveys/<int:user_id>', views.SurveysView.as_view(), name='surveys'),
    path('my_surveys/<int:user_id>', views.MySurveysView.as_view(), name='my_surveys'),
    path('create_survey/',views.CreateSurveyView, name="create_survey"),

    path('create_survey/<int:survey_id>',views.CreateSurveyQuestions, name="create_survey_questions"),
    path('create_questions/<int:survey_id>', views.CreateQuestions, name="create_questions"),

    path('create_survey/<int:survey_id>/create_options/<int:question_id>',views.CreateQuestionsOptions, name="create_question_options"),
    path('add_options/<int:survey_id>/<int:question_id>', views.CreateOptions, name="add_options"),

    path('delete_option/<int:option_id>/<int:survey_id>/<int:question_id>', views.DeleteOptions, name="delete_option"),

    path('view_options/<int:survey_id>/<int:question_id>', views.ViewOptions, name="view_options"),
    
    path('<int:pk>/response', views.ResponseView.as_view(), name='response'),
    path('<int:pk>/results', views.ResultsView.as_view(), name='results'),
]


