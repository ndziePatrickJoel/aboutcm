from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=300, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(blank = True, max_length=1024)
    user_picture = models.FileField(blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    


class QuestionCategory(models.Model):
    """
    Cette classe représente une catégorie
    """

    name = models.CharField(max_length = 255, help_text="Entrez une catégorie de question")
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='static/uploads/question_category/', null = True)


    def __str__(self):

        return self.name

class View360QuestionCategory(models.Model):
    """
    Cette classe représente une catégorie
    """

    name = models.CharField(max_length = 255, help_text="Entrez une catégorie de question")
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='static/uploads/question_category/', null = True)
    nb_questions = models.IntegerField()
    
    def __str__(self):

        return self.name

    class Meta:
        managed = False
        db_table = "view_360_question_category"


class QuestionTag(models.Model):
    """
    Un tag est un label qui permet de dire de façon plus subtile
    de quoi il est question dans la question
    """
    title = models.CharField(max_length=255, primary_key=True)
    description = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)    
    created_by = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
        
    def __str__(self):
        return self.title


class Question(models.Model):

    title = models.CharField(max_length=1024)
    nb_views = models.IntegerField(default=0)
    anonymously = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)
    details = RichTextUploadingField(null = True)
    #une question appartient à une seule catégorie
    category = models.ForeignKey('QuestionCategory', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(QuestionTag, help_text="Selectionnez un tag pour cette question")
    asker = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        """
        Retourne l'url pour accéder à une question particulière
        """

        return reverse('question-detail', args=[str(self.id)])

class Answer(models.Model):
    """
    Cette classe représente une réponse
    """
    nb_upvotes = models.IntegerField(default=0)
    nb_downvotes = models.IntegerField(default=0)
    nb_views = models.IntegerField(default = 0)
    details = RichTextUploadingField()
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)
    anonymously = models.BooleanField(default = True)

    def __str__(self):
        return "Answer " + str(self.id) 

class View360Answer(models.Model):
    """
    Cette classe représente une réponse
    """
    nb_upvotes = models.IntegerField(default=0)
    nb_downvotes = models.IntegerField(default=0)
    nb_views = models.IntegerField(default = 0)
    details = RichTextUploadingField()
    username = models.TextField()
    anonymously = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)
    question_id = models.IntegerField()
    positives_votes = models.IntegerField()

    def __str__(self):
        return "Answer " + str(self.id) 

    class Meta:
        managed = False
        db_table = "view_360_answer"





class AnswerComment(models.Model):
    """
    Cette classe représente les commentaires qui
    sont faits sur les réponses
    """

    nb_upvotes = models.IntegerField(default=0)
    nb_downvotes = models.IntegerField(default =0)
    details = models.TextField()
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True)

    

class View360Question(models.Model):
    """ Cette classe est une classe maitresse de l'application
    elle représente la vue qui permet d'avoir toutes les informations
    nécéssaires à l'affichage d'un élément de la liste des questions 
    avec le plus de détails possibles"""

    id = models.BigIntegerField(primary_key=True)
    title = models.TextField(max_length=1024)
    nb_views = models.IntegerField()
    created_at = models.DateTimeField()
    last_edited_at = models.DateTimeField()
    nb_answers = models.IntegerField()
    tags = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    username = models.TextField()
    user_picture = models.FileField()
    user_title = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = "view_360_question"