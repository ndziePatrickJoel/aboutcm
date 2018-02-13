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

    #othersTags = forms.CharField(max_length=1024,
    #                       widget=forms.TextInput(attrs={'class':'form-control'}), label="Saisissez les mots clés séparés d'un espace")

    details = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control','style': 'width: 80%;'}), label="Détails")

    anonymously = forms.BooleanField(required=False, label="Poser la question de façon anonyme")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

        labels = {
            'username': 'Pseudo/Identifiant',
            'first_name': 'Prénom'}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('title', 'bio', 'location', 'user_picture')

        labels = {'title': 'Titre', 'bio': 'A propos de vous', 
                  'location': 'Où vivez-vous?', 
                  'user_picture': 'Photo de profile'}
        widgets = {'bio':  forms.CharField(widget=CKEditorWidget())
        }