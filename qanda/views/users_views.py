from django.shortcuts import render
from django.views import generic
from ..models import Question, View360Question, QuestionCategory, Answer, QuestionTag, AnswerComment, View360Answer
from ..models import View360QuestionCategory
from ..forms import QuestionForm, UserForm, ProfileForm
from dal import autocomplete
from django.http import HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

@login_required
@transaction.atomic
def profile_view(request):
    user = request.user
    print(user.username)
    #l'utilisateur à qui appartient le profile qu'on visite
    profile_user = user
    user_form = UserForm(instance = profile_user)
    profile_form = ProfileForm(instance= profile_user.profile)

    return render(
        request,
        'users/profile.html',
        context={'profile_user': profile_user, 'user_form': user_form, 'profile_form': profile_form}
    )

def update_profile_view(request):
    
    if request.method == 'POST':  
        
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Votre profile a été mis à jour avec succès!')
            
        else:
            print(user_form.errors.as_data())
            print(profile_form.errors.as_data())
            messages.error(request, 'Erreur lors de la mise à jour de votre profile')

    return redirect('profile_view')