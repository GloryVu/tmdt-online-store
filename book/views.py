import http
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from book.models import Book
from book.forms import BookForm

def view_book(request):
    ctx={}
    books=Book.objects.all()
    print(books)
    ctx["books"]=books
    return render(request,"book/view_book.html",ctx)
def create_book_form(request):
    ctx={}
    ctx["form"]=BookForm(request.POST or None)
    return render(request,"book/create_book_form.html",ctx)
def save_book(request):
    if(request.method=="POST"):
        form=BookForm(request.POST,request.FILES)
        if(form.is_valid):
            form.save()
            return render(request,"book/view_book.html")
    return HttpResponse("That bai")    
def update_book_form(request,ISBN):
    print(ISBN)
    obj=get_object_or_404(Book,ISBN=ISBN)
    ctx={}
    ctx["form"]=BookForm(request.POST or None,instance=obj)
    return render(request,"book/update_book_form.html",ctx)   
def update_book(request):
    form=BookForm(request.POST,request.FILES)
    obj=get_object_or_404(Book,ISBN=form["ISBN"].value())
    form.instance=obj
    if(form.is_valid):
        form.save();
        return view_book(request)
    return render(request,"book/view_book.html")      
def delete_book(request,ISBN):
    obj=get_object_or_404(Book,ISBN=ISBN)
    if(request.method =="POST"):
        obj.delete()
        return view_book(request)
    return HttpResponse("That bai")

















from book.models import BookItem
from book.forms import BookItemForm
def view_bookItem(request):
    ctx={}
    bookItems=BookItem.objects.all()
    ctx["bookItems"]=bookItems
    return render(request,"book/view_bookItem.html",ctx)
def create_bookItem_form(request):
    ctx={}
    ctx["form"]=BookItemForm(request.POST or None)
    return render(request,"book/create_bookItem_form.html",ctx)
def save_bookItem(request):
    if(request.method=="POST"):
        form=BookItemForm(request.POST,request.FILES)
        if(form.is_valid):
            form.save();
            return view_bookItem(request)
    return HttpResponse("That bai")    
def update_bookItem_form(request,ID):
    obj=get_object_or_404(BookItem,ID=ID)
    ctx={}
    ctx["form"]=BookItemForm(request.POST or None,instance=obj)
    return render(request,"book/update_bookItem_form.html",ctx) 
def update_bookItem(request):
    form=BookItemForm(request.POST,request.FILES)
    obj=get_object_or_404(BookItem,ID=form["ID"].value())
    form.instance=obj
    if(form.is_valid):
        form.save();
        return view_bookItem(request)
    return render(request,"book/view_bookItem.html")    
def delete_bookItem(request,ID):
    obj=get_object_or_404(BookItem,ID=ID)
    if(request.method =="POST"):
        obj.delete()
        return view_bookItem(request)
    return HttpResponse("That bai")





























from book.models import BookStats
from book.forms import BookStatsForm
def view_bookStats(request):
    ctx={}
    bookStatss=BookStats.objects.all()
    ctx["bookStatss"]=bookStatss
    return render(request,"book/view_bookStats.html",ctx)
def create_bookStats_form(request):
    ctx={}
    ctx["form"]=BookStatsForm(request.POST or None)
    return render(request,"book/create_bookStats_form.html",ctx)
def save_bookStats(request):
    if(request.method=="POST"):
        form=BookStatsForm(request.POST,request.FILES)
        if(form.is_valid):
            form.save();
            return view_bookStats(request)
    return HttpResponse("That bai")    
def update_bookStats_form(request,ID):
    obj=get_object_or_404(BookStats,ID=ID)
    ctx={}
    ctx["form"]=BookStatsForm(request.POST or None,instance=obj)
    return render(request,"book/update_bookStats_form.html",ctx) 
def update_bookStats(request):
    form=BookStatsForm(request.POST,request.FILES)
    obj=get_object_or_404(BookStats,ID=form["ID"].value())
    form.instance=obj
    if(form.is_valid):
        form.save();
        return view_bookStats(request)
    return render(request,"book/view_bookStats.html")    
def delete_bookStats(request,ID):
    obj=get_object_or_404(BookStats,ID=ID)
    if(request.method =="POST"):
        obj.delete()
        return view_bookStats(request)
    return HttpResponse("That bai")