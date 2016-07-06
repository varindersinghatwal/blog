from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json, math

from web.forms import ArticleForm, CreateCommentForm
from web.models import Article, Comment, Paragraph


# Create your views here.

def home(request):
    current_page = request.GET['cp'] if 'cp' in request.GET else 1
    limit = 5
    start = ((int(current_page) - 1)*limit)
    end = start + limit
    articles = Article.objects.all().order_by('-id')
    total = len(articles)
    total = int(math.ceil(total/float(limit))) + 1
    return render(request, 'index.html', {'articles': articles[start:end], 'total':range(1,total)})

@csrf_exempt
def add_article(request):
    if request.method == 'POST':
        title = request.POST['title'] if 'title' in request.POST else ''
        text = request.POST['text'] if 'text' in request.POST else ''
        if title == '':
            return HttpResponse(json.dumps({'status':0, 'error': 'title required'}))
        elif text == '':
            return HttpResponse(json.dumps({'status':0,'error': 'paragraphs not found'}))
        else:
            paragraphs = text.split("\n\n")
            print paragraphs 
            article = Article.create(title, paragraphs)
            return HttpResponse(json.dumps({'status':1,'error': ''}))
    else:
        context = {}
        return render(request, 'article_form.html', context)

def view_article(request, article_id):
    article = Article.objects.get(id=article_id)
    paragraphs = Paragraph.objects.filter(article=article_id).order_by('id')
    comments = Comment.objects.filter(article=article_id).order_by('id')
    context = {
        'article':article,
        'paragraphs': paragraphs,
        'comments': comments,
        'form': CreateCommentForm()
    }
    return render(request, 'view_article.html', context)

def comments(request):
    if request.method == 'GET':
        comments = serializers.serialize("json", Comment.objects.all())
        return HttpResponse(json.dumps({'comments': comments}))
    elif request.method == 'POST':
        text = request.POST['text']
        paragraph = Paragraph.objects.get(id=request.POST['para'])
        article = Article.objects.get(id=request.POST['article'])
        comment = Comment.objects.create(text=text, article=article, paragraph=paragraph)
        return HttpResponseRedirect("/article/%s/"%article.id)
