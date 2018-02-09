# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.core.files import File
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .forms import UploadFileForm,SubmitForm,MakeForm
from django.template.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_protect ,csrf_exempt
from .models import UploadFile
from mysite.settings import MEDIA_ROOT
from django.core.files.storage import get_storage_class
import os
import glob
import shutil
import pdb
from mysite import settings
# Create your views here.


def file(request):
    return render_to_response('app/dropzone.html')


@csrf_protect
def index(request):
    c = {}
    makepath = MakeForm(request.POST or None)
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
         if 'upload-all' in request.POST:
             return HttpResponseRedirect('/app/shape/')
         if form.is_valid():
             new_file = UploadFile(file = request.FILES['file'])
             new_file.save()

             return HttpResponseRedirect(reverse('app:index'))
         if 'search' in request.POST:
             if makepath.is_valid():
                  pathname = request.POST['directory_name']
                  if os.path.exists(pathname):
                      newfiles = glob.glob(pathname+'/*')
                      for newfile in newfiles:
                            makefile = os.path.basename(newfile)
                            shutil.copy(newfile,MEDIA_ROOT)
                            obj = UploadFile.objects.get_or_create(file=makefile)
    c = {'form': form, 'makepath': makepath, }
    return render(request,'app/index.html', c)


@csrf_exempt
def shape(request):
    c = {}
    if request.method == 'POST':
        if 'addim' in request.POST:
            return HttpResponseRedirect('/app/app/')
        if 'deleteim' in request.POST:
            obj = UploadFile.objects.all()
            obj.delete()
        else:
            postroot = request.POST['test_path']
            postfile = request.POST['test_text']
            passname = MEDIA_ROOT +'/'+ postfile
            if os.path.exists(postroot) == False:
                os.mkdir(postroot)
            if os.path.exists( postroot +'/' +postfile )== False:
                shutil.move(passname,postroot)
            storage = get_storage_class()
            obj = UploadFile.objects.get(file=postfile)
            obj.delete()
      
    items = []
    for item in UploadFile.objects.all():
        items.append({'file':item.file })

    filepass = SubmitForm()
    c = {'items':items , 'filepass':filepass}
    return render(request, 'app/shape.html',c)
