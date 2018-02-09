from django.shortcuts import render
from django.views import generic
from ..models import Question, View360Question, QuestionCategory, Answer, QuestionTag, AnswerComment, View360Answer
from ..models import View360QuestionCategory
from ..forms import QuestionForm
from dal import autocomplete
from django.http import HttpResponseRedirect,Http404

# Create your views here.

def index(request):
    
    #on récupère le nombre de questions
    num_questions = Question.objects.all().count()
    
    #nombre de questions anonymes
    num_anonym_questions = Question.objects.filter(anonymously= True).count()

    #nombre de réponses
    num_answers = Answer.objects.all().count()

    #nombre de Catégories
    num_categories = QuestionCategory.objects.all().count() 

    return render(
        request,
        'index.html',
        context={'num_questions': num_questions, 'num_anonym_questions': num_anonym_questions,
        'num_answers': num_answers, 'num_categories': num_categories}
    )



def qaIndex(request):

    return render(request, 'qa.html')


def categoriesIndex(request):
    
     #on récupère le nombre de questions
    categories = View360QuestionCategory.objects.all()    
    
    return render(
        request,
        'categories_index.html',
        context={'categories': categories}
    )

