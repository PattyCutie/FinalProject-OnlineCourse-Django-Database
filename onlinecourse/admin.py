from django.contrib import admin
# from django.db import models
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Add inline class below>>
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['course', 'title']

# Add class model admin below>>
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'lesson']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'lesson']

# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
