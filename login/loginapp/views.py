from django.shortcuts import render,redirect
from loginapp.models import logindb
from loginapp.loginform import logform
from django.http import HttpResponse
from django import forms 


# Create your views here.
def log(request):
    lg = logform()
    if request.method == 'POST':
        lgf = logform(request.POST)
        print(lgf)
        if lgf.is_valid():
            lgf.save()
            return redirect('/ss')
            
    return render(request,'newlog.html',{'lgs':lg})

def fmview(request):
    lgdb = logindb.objects.all()
    
    return render(request,'view.html',{'lgdb':lgdb})

def success(request):
    return render(request,'success.html')

def update(request,id):
    lgd = logindb.objects.get(id=id)
    if request.method == 'POST':
        lgu = logform(request.POST,instance=lgd)
        if lgu.is_valid():
            lgu.save()
            return redirect('/show')
        
    return render(request,'update.html',{'lgd':lgd})

def delete(request,id):
    lgd = logindb.objects.get(id=id)
    lgd.delete()
    return redirect('/show')

def check(request):
    lg = logform()
    lfdb = logindb.objects.all()
    if request.method == 'POST':
        lgf = logform(request.POST)
        print(lgf)
        if lgf.is_valid():
            usn = lgf.cleaned_data['username']
            psf = lgf.cleaned_data['password']
            for i in lfdb:
                if i.username == usn and i.password==psf:
                    return redirect('/ss')
                
    return render(request, 'newlog.html', {'lgs': lg})
    
    
    

# def verify(request):
    