from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    context = {
        'name': 'John Doe',
        'age': 30,    
        'skills': ['Python', 'Django', 'JavaScript'],
        'user' : User('kumar', 23),
        'blog': {
            'title': 'My First Blog Post',
            'content': 'This is the content of my first blog post.',
            'author': 'John Doe',
            'date_posted': datetime.now(),
        },
        'empty_value': None,
    }
    return render(request, 'blog/home.html', context=context)
        

# Create your views here.
