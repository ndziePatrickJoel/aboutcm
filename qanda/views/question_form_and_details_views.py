from django.shortcuts import render
from django.views import generic
from ..models import Question, View360Question, QuestionCategory, Answer, QuestionTag, AnswerComment, View360Answer
from ..forms import QuestionForm, AnswerForm
from dal import autocomplete
from django.http import HttpResponseRedirect,Http404
from django.shortcuts import redirect

# Create your views here.


def treatRawString(rawString):
    """Cette méthode prend en paramètre une chaine brute
    et retourne celle-ci après avoir ait les traitements suivants
    - Rendre l'image responsive
    - Retirer le paramètre width"""

    result = rawString.replace("img", "img class='img img-responsive'")
    
    return result

def newAnswerView(request):

    if request.method == 'POST':

        form = AnswerForm(request.POST)

        if form.is_valid():
            answer = Answer()
            answer.details = request.POST.get('details', None)
            answer.question = Question.objects.get(pk = request.POST.get('questionId'))
        
            if request.POST.get('anonymously') is not None:
                answer.anonymously = True
        
            answer.author = request.user
            answer.save()
            
            return redirect("question_details", pk=request.POST.get('questionId'))

        
        

        return Json

        

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



def questionDetailView(request, pk):
    
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    #à ce niveau on récupère les réponses de la question

    answers = View360Answer.objects.filter(question_id = pk)    

    #book_id=get_object_or_404(Book, pk=pk)

    form = AnswerForm(initial = {'questionId': pk})

    
    return render(
        request,
        'questions/question_details.html',
        context={'question':question, 'answers': answers, 'form': form}
    )

        