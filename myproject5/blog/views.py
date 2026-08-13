from django.shortcuts import render
from datetime import datetime


def blog_details(request):

    post = {
        "title": "My First Blog Post",
        "content": "This is the content of my first blog post.",
        "author": "yes",
        'comment_count': 4,
        "date_posted": datetime.now(),
        "price": 19.99,
        "number": 10,
        'tags': ['django', 'python', 'web development'],
    }
    return render(request, 'blog/blog_details.html',{"post":post})
# Create your views here.
