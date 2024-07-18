

from django.shortcuts import render,redirect
from .models import Profile
# # Create your views here.

def add(req):
    if req.method=='POST':
        name=req.POST.get('name','')
        phone=req.POST.get('phone','')
        email=req.POST.get('email','')
        alter=req.POST.get('alter','')
        image = req.FILES['image']  # Use get to avoid KeyError
        if image:  # Check if an image is uploaded
            contacts= Profile(name=name, phone=phone, email=email, alter=alter, image=image)
        else:
            contacts= Profile(name=name, phone=phone, email=email, alter=alter)
        contacts.save()
        return redirect('home')
    return render(req,'add.html')
def home(req):
    contacts=Profile.objects.all()
    return render(req,'index.html',{"contacts":contacts})
def update(req,id):
    update=Profile.objects.get(id=id)
    if req.method=='POST':
        newname=req.POST.get('newname','')
        newphone=req.POST.get('newphone','')
        newemail=req.POST.get('newemail','')
        newimage=req.FILES.get('newimage')
        update.name=newname
        update.phone=newphone 
        update.email=newemail  
        if newimage:
            update.image=newimage
        update.save() 
        return redirect('home') 
    return render(req,'update.html',{"update":update}) 
def delete(req,id):
      delete=Profile.objects.get(id=id)
      delete.delete()
      return redirect('home')
      return render(req,'delete.html',{"delete":delete})


def details(req,id):
    details=Profile.objects.get(id=id)
    return render(req,'details.html',{"details":details})
def call(req,id):
    call=Profile.objects.get(id=id)
    return render(req,'call.html',{"call":call})  
                     
