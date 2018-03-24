from django import forms
from .models import Question, User, Profile
from .models import QuestionCategory, QuestionTag
#from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from dal import autocomplete


class QuestionForm(forms.Form):
    
    title = forms.CharField(label="Titre de la question", max_length=1024,
                            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))

    category = forms.ModelChoiceField(queryset = QuestionCategory.objects.all(), 
                             widget=autocomplete.ModelSelect2(url='question_category_autocomplete', 
                             attrs={'class':'form-control', 'style': 'width: 100%;'}),
                            label="Dans quelle catégorie situerez-vous votre question?")

    tags = forms.ModelMultipleChoiceField(queryset = QuestionTag.objects.all(), 
            widget= autocomplete.ModelSelect2Multiple(url='question_tags_autocomplete', 
            attrs={'class':'form-control', 'style': 'width: 100%;'}), label="Mots clés")

    details = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control','style': 'width: 80%;'}), label="Détails")

    anonymously = forms.BooleanField(required=False, label="Poser la question de façon anonyme")


class AnswerForm(forms.Form):
    
    anonymously = forms.BooleanField(required=False, label="Répondre de façon anonyme")
    details = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control','style': 'width: 80%;'}))
    questionId = forms.IntegerField(required = True, widget=forms.NumberInput(attrs={'style':'display:none'}))


class UserForm(forms.ModelForm):

    username = forms.CharField(label="Pseudo/Identifiant",
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label="Prénom",
                            widget=forms.TextInput(attrs={'class':'form-control'}))

    last_name = forms.CharField(label="Nom",
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label="Adresse mail",
                            widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

        labels = {
            'username': 'Pseudo/Identifiant',
            'first_name': 'Prénom(s)',
            'last_name': 'Nom(s)'}


class ProfileForm(forms.ModelForm):
    
    bio = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), label="Détails")
    location = forms.CharField(label="Où vivez-vous?",
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    user_picture = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required = False, label="Uploadez une photo")

    title = forms.CharField(label="Qui êtes-vous en une phrase?",
                            widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = Profile
        fields = ('title', 'bio', 'location', 'user_picture')

        labels = {'title': 'Titre', 
                  'location': 'Où vivez-vous?', 
                  'user_picture': 'Photo de profile'}
        
        