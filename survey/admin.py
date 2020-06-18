from django.contrib import admin

from .models import Survey,Question,TextAnswer,SingleChoiceAnswer,MultipleChoiceAnswer,Option

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(TextAnswer)
admin.site.register(SingleChoiceAnswer)
admin.site.register(MultipleChoiceAnswer)
admin.site.register(Option)