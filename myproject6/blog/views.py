from django.shortcuts import render
from datetime import datetime

def blog_list(request):
    now = datetime.now()

    blogs = [
        {"title":"Django Basics","is_featured":True, "author":"Mohit Kumar"},
        {"title":"Django Advanced","is_featured":False, "author":""},
        {"title":"Django REST Framework","is_featured":False, "author":"Anu Choudhary"},
    ]

    context = {
        "blogs":blogs,
        'today': datetime.now().date(),
        'html_code': '<h1>Welcome to Django</h1>',
    }
    return render(request, 'blog/blog_list.html', context)
# Create your views here.
