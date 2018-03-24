import datetime
from haystack import indexes
from qanda.models import Question




class QuestionIndex(indexes.SearchIndex, indexes.Indexable):
    text= indexes.CharField(document = True, use_template = True)
    created_at = indexes.DateTimeField()

    def get_model(self):
        return Question

    
    def index_queryset(self, using = None):

        return self.get_model().objects.filter(created_at__lte=datetime.datetime.now())
    