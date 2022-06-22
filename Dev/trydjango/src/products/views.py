from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(*args, **kwargs): # llok into those commands
    return ("<h1>Hello World</h1>") # string of HTML code
