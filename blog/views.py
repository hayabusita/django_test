from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
class ArticleListView(ListView):
    context_object_name = 'art_list'
    queryset = Article.objects.all()
    template_name = 'articles/article_list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

    def get_object(self):
        _id = self.kwargs.get('id')
        return get_object_or_404(Article, id=_id)

class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'articles/article_create.html'

class ArticleUpdateView(UpdateView):
    form_class = ArticleForm
    template_name = 'articles/article_create.html'

    def get_object(self):
        _id = self.kwargs.get('id')
        return get_object_or_404(Article, id=_id)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        _id = self.kwargs.get('id')
        return get_object_or_404(Article, id=_id)
    
    def get_success_url(self):
        return reverse('blog:article-list')