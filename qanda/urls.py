from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^qa_index$', views.qaIndex, name='qa_index'),
    url(r'^new_question$', views.newQuestionView, name="new_question"),
    url(r'^categories$', views.categoriesIndex, name='categories_index'),
    url(r'^questions/(?P<slug>\w*)$', views.View360QuestionListView.as_view(),name="questions"),
    url(r'^questions/(?P<slug>\w+)/(?P<query>\w+)$', views.View360QuestionListView.as_view(),name="questions"),
    url(r'^question/(?P<pk>\d+)$', views.questionDetailView, name="question_details"),
    url(r'^new_answer$', views.newAnswerView, name="new_answer"),
    url(r'^question_category_autocomplete/$', views.QuestionCategoryAutocomplete.as_view(),  name="question_category_autocomplete"),
    url(r'^question_tags_autocomplete/$',views.QuestionTagsAutocomplete.as_view(create_field='title'), name="question_tags_autocomplete"),
    url(r'^profile/$', views.profile_view, name='profile_view'),
    url(r'^update_profile/$', views.update_profile_view, name='update_profile_view')
]