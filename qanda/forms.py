from django import forms
from .models import Question
from .models import QuestionCategory, QuestionTag
#from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
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