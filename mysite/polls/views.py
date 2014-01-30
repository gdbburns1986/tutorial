from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the polls index page")

def detail(request, poll_id):
    return HttpResponse("This is poll number %s" % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
