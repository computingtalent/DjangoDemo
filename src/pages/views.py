from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.


def home_view(*args, **kwargs):
    now = datetime.datetime.now()
    html = f"<h1>Welcome to the fit store,<br> It's currently{now},</h1>"
    html += '<img src="drip.jpg" width="500" height="600">'
    return HttpResponse(html)