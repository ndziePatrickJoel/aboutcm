from django.shortcuts import render
from django.views import generic
from ..models import Question, View360Question, QuestionCategory, Answer, QuestionTag, AnswerComment, View360Answer
from ..models import View360QuestionCategory
from ..forms import QuestionForm, UserForm, ProfileForm
from dal import autocomplete
from django.http import HttpResponseRedirect,Http404

# Create your views here.

def profile_view(request):
    
    if request.method == 'POST':  
        pass  
        
    else:
        user = request.user
        #l'utilisateur à qui appartient le profile qu'on visite
        profile_user = user
        user_form = UserForm(instance = profile_user)
        profile_form = ProfileForm(instance= profile_user.profile)

    return render(
        request,
        'users/profile.html',
        context={'profile_user': profile_user, 'user_form': user_form, 'profile_form': profile_form}
    )

