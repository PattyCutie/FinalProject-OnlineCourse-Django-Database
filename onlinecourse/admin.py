from django.contrib import admin
from django.db import models
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 2
# Add inline class below>>
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title']

# Add class model admin below>>
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionInline)
admin.site.register(Choice)
admin.site.register(Submission)
