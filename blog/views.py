from django.shortcuts import render,get_object_or_404
from .models import Article
from .form import ArticleForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def article_list(request):

    articles = Article.objects.filter(published_date__isnull=False).order_by('-published_date')
    #.filter(published_date__isnull=False)
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request,pk):
    article=get_object_or_404(Article,pk=pk)
    return render(request,'blog/article_detail.html',{'article':article})

@login_required
def article_new(request):
    if request.method=='POST':
        form=ArticleForm(request.POST)
        if form.is_valid():
            article=form.save(commit=False)
            article.author=request.user
            article.save()
            return redirect('blog.views.article_detail',pk=article.pk)
    else:
        form=ArticleForm()
    return render(request,'blog/article_edit.html',{'form':form})


@login_required
def article_edit(request,pk):
    article = get_object_or_404(Article,pk=pk)
    if request.method=='POST':
        form=ArticleForm(request.POST,  instance=article)
        if form.is_valid():
            article=form.save(commit=False)
            article.author=request.user
            article.save()

            return redirect('blog.views.article_detail',pk=article.pk)

    else:
        form = ArticleForm(instance=article)
    return render(request,'blog/article_edit.html',{'form':form})


def article_draft_list(request):
    articles = Article.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'blog/article_draft_list.html', {'articles': articles})
@login_required
def article_publish(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.publish()
    return redirect('blog.views.article_detail', pk=pk)

@login_required
def article_remove(request, pk):
    article  = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('blog.views.article_list')

#    form=ArticleForm()
#    return render(request,'blog/article_edit.html',{'form':form})