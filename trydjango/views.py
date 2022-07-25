"""
To render html web pages.
"""
from django.http import HttpResponse

from django.template.loader import render_to_string

from articles.models import Article

def home_view(request):
    name = "Chris"
    article = Article.objects.get(id=1)
    
    context = {
        'title': article.title,
        'id': article.id,
        'content': article.content
    }
    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """
    # <h1>{title} (id: {id})</h1>
    # <p>{content}!</p>
    # """.format(**context)
    return HttpResponse(HTML_STRING)