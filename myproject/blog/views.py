from django.shortcuts import render
from django.http import HttpResponse


def post_details(request,post_id):
    return HttpResponse(f"<h2> show blog post {post_id}</h2>")

def user_profile(request,username):
    return HttpResponse(f"<p> show the details of {username}</p>")

def article_by_year(request,year):
    return HttpResponse(f"the article{year}")

def article_details(request,**kwargs):
    return HttpResponse(f"<p>this is the details of article{kwargs}")


# Create your views here.
