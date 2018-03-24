from django.shortcuts import render
from django.views import generic
from ..models import Question, View360Question, QuestionCategory, Answer, QuestionTag, AnswerComment, View360Answer
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



class View360QuestionListView(generic.ListView):
    
    slug = None
    model = View360Question
    template_name = 'questions/questions_list.html'

    def get_queryset(self):
        self.slug = self.kwargs.get('slug')
        #self.slugs = dict({'hots': False, 'interesting': False, 'week': False, 'month': False, 'all': True})
        self.hots_slug = False
        self.interesting_slug = False
        self.week_slug = False
        self.month_slug = False   
        self.all_slug = False

        if self.slug == 'hots':
            self.hots_slug = True
        elif self.slug == 'interesting':
            self.interesting_slug = True
        elif self.slug == 'week':
            self.week_slug = True
        elif self.slug == 'month':
            self.month_slug = True    
        else:
            self.all_slug = True   
        
        queryset = super(View360QuestionListView, self).get_queryset()
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super(View360QuestionListView, self).get_context_data(**kwargs)
        context['current_slug'] = self.slug
        context['hots_slug'] = self.hots_slug
        context['interesting_slug'] = self.interesting_slug
        context['week_slug'] = self.week_slug
        context['month_slug'] = self.month_slug
        context['all_slug'] = self.all_slug

        return context
    paginate_by = 5