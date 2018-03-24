from django.contrib import admin

# Register your models here.

from .models import Question, QuestionCategory, QuestionTag, Answer, AnswerComment

admin.site.register([QuestionTag, AnswerComment])


class AnswerInstanceInline(admin.TabularInline):
    model = Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = ['title', 'nb_views', 'anonymously', 'asker', 'created_at', 'last_edited_at', 'category']
    list_filter = ['category', 'anonymously', 'tags', 'asker']

@admin.register(QuestionCategory)
class QuestionCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
