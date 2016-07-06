from django.db import models
import math, random

# Create your models here

def getRandomColor():
    letters = '0 1 2 3 4 5 6 7 8 9 A B C D E F'.split(' ');
    color = '#';
    for i in range( 0, 6):
        color += letters[int(math.floor(random.random() * 16))]
    return color

class Article(models.Model):
    title = models.TextField(null=False, blank=False)
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    @classmethod
    def create(cls, title, paragraphs):
        article = cls(title=title)
        article.save()
        for para in paragraphs:
            Paragraph.create(article, para)

class Paragraph(models.Model):
    article = models.ForeignKey(Article)
    text = models.TextField(null=False, blank=False)
    color = models.CharField(max_length=8, default='#000')
    created_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_time = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    @classmethod
    def create(cls, article, txt):
        para = cls(article=article, text=txt, color=getRandomColor())
        para.save()

class Comment(models.Model):
    article = models.ForeignKey(Article)
    paragraph = models.ForeignKey(Paragraph)
    text = models.TextField(blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
