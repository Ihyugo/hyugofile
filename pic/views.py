# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import UploadFile
from .forms import UploadFileForm

# Create your views here.

def index(request):
    c = {}
    hello = "Hello Django!"
    file = UploadFileForm
    c = {'hello': hello, 'file': file}
    return render(request, 'pic/index.html', c)


