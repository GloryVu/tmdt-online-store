import http
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from clothes.models import Clothes
from clothes.forms import ClothesForm

def view_clothes(request):
    ctx={}
    clotheses=Clothes.objects.all()
    print(clotheses)
    ctx["clotheses"]=clotheses
    return render(request,"clothes/view_clothes.html",ctx)

def create_clothes_form(request):
    ctx={}
    ctx["form"]=ClothesForm(request.POST or None)
    return render(request,"clothes/create_clothes_form.html",ctx)

def save_clothes(request):
    if(request.method=="POST"):
        form=ClothesForm(request.POST,request.FILES)
        if(form.is_valid):
            form.save()
            return view_clothes(request)
    return HttpResponse("That bai")    
def update_clothes_form(request,ID):
    ctx = {}
    obj=get_object_or_404(Clothes,ID =ID)
    form = ClothesForm(instance=obj)
    ctx["form"] = form
    return render(request,"update_clothes_form.html", ctx) 

def update_clothes(request):
    ctx = {}
    
    form = ClothesForm(request.POST,request.FILES)
    obj=get_object_or_404(Clothes,ID =form["ID"].value())
    form.instance = obj
    if(form.is_valid):
        form.save()
        return view_clothes(request)
    ctx["form"] = form
    return render(request,"update_clothes_form.html", ctx) 

def delete_clothes(request,ID):
    obj=get_object_or_404(Clothes,ID=ID)
    if(request.method =="POST"):
        obj.delete()
        return render(request,"clothes/view_clothes.html")
    return HttpResponse("That bai")

















from clothes.models import ClothesItem
from clothes.forms import ClothesItemForm
def view_clothesItem(request):
    ctx={}
    clothesItems=ClothesItem.objects.all()
    ctx["clothesItems"]=clothesItems
    return render(request,"clothes/view_clothesItem.html",ctx)
def create_clothesItem_form(request):
    ctx={}
    ctx["form"]=ClothesItemForm(request.POST or None)
    return render(request,"clothes/create_clothesItem_form.html",ctx)
def save_clothesItem(request):
    if(request.method=="POST"):
        form=ClothesItemForm(request.POST,request.FILES)
        if(form.is_valid):
            form.save()
            return render(request,"clothes/view_clothesItem.html")
    return HttpResponse("That bai")    
def update_clothesItem_form(request,ID):
    obj=get_object_or_404(Clothes,ID=ID)
    ctx={}
    ctx["form"]=ClothesItemForm(request.POST or None,instance=obj)
    return render(request,"clothes/update_clothesItem_form.html",ctx)     
def delete_clothes(request,ID):
    obj=get_object_or_404(Clothes,ID=ID)
    if(request.method =="POST"):
        obj.delete()
        return render(request,"clothes/view_clothes.html")
    return HttpResponse("That bai")