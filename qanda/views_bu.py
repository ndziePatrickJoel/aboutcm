from django.shortcuts import render
from django.views import generic
from .models import Question, View360Question, QuestionCategory, Answer, QuestionTag, AnswerComment, View360Answer
from .forms import QuestionForm
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

    return render(request, 'categories_index.html')


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



def questionDetailView(request, pk):
    
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    #à ce niveau on récupère les réponses de la question

    answers = View360Answer.objects.filter(question_id = pk)

    #book_id=get_object_or_404(Book, pk=pk)
    
    return render(
        request,
        'questions/question_details.html',
        context={'question':question, 'answers': answers}
    )


def treatRawString(rawString):
    """Cette méthode prend en paramètre une chaine brute
    et retourne celle-ci après avoir ait les traitements suivants
    - Rendre l'image responsive
    - Retirer le paramètre width"""

    result = rawString.replace("img", "img class='img img-fluid'")
    
    return result

def newQuestionView(request):

    if request.method == 'POST':

        form = QuestionForm(request.POST)

        if form.is_valid():
            
            newQuestion = Question()

            newQuestion.title = form.cleaned_data['title']
            #Les détails tels que reçu de l'interface graphique
            rawDetails = form.cleaned_data['details']
            details = treatRawString(rawDetails)
            newQuestion.details = details
            newQuestion.anonymously = form.cleaned_data['anonymously']
            newQuestion.category = form.cleaned_data['category']
            newQuestion.asker = request.user
            newQuestion.save()

            newQuestion.tags = form.cleaned_data['tags']           
            newQuestion.save()
            
            return HttpResponseRedirect("qa_index")
    #s'il ne s'agit pas d'une requête POST
    else:
        form = QuestionForm()

    
    return render(request, 'questions/new_question.html', {'form': form})


class QuestionCategoryAutocomplete(autocomplete.Select2QuerySetView):
        
    def get_queryset(self):
        #if not self.request.user.is_authenticated():
        #    return QuestionCategory.objects.none()

       
        qs = QuestionCategory.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        
        return qs

class QuestionTagsAutocomplete(autocomplete.Select2QuerySetView):
        
    def get_queryset(self):
        #if not self.request.user.is_authenticated():
        #    return QuestionCategory.objects.none()

        qs = QuestionTag.objects.all()

        if self.q:
            qs = qs.filter(title__istartswith=self.q)
        else:
            qs = QuestionTag.objects.none()

        return qs
        