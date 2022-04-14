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




























































# from book.models import Publisher
# from book.forms import PublisherForm
# def view_publisher(request):
#     ctx={}
#     publishers=Publisher.objects.all()
#     ctx["publishers"]=publishers
#     return render(request,"book/view_publisher.html",ctx)
# def create_publisher_form(request):
#     ctx={}
#     ctx["form"]=PublisherForm(request.POST or None)
#     return render(request,"book/create_publisher_form.html",ctx)
# def save_publisher(request):
#     if(request.method=="POST"):
#         form=PublisherForm(request.POST,request.FILES)
#         if(form.is_valid):
#             form.save();
#             return view_publisher(request)
#     return HttpResponse("That bai")    
# def update_publisher_form(request,ID):
#     obj=get_object_or_404(Publisher,ID=ID)
#     ctx={}
#     ctx["form"]=PublisherForm(request.POST or None,instance=obj)
#     return render(request,"book/update_publisher_form.html",ctx) 
# def update_publisher(request):
#     form=PublisherForm(request.POST,request.FILES)
#     obj=get_object_or_404(Publisher,ID=form["ID"].value())
#     form.instance=obj
#     if(form.is_valid):
#         form.save();
#         return view_publisher(request)
#     return render(request,"book/view_publisher.html")    
# def delete_publisher(request,ID):
#     obj=get_object_or_404(Publisher,ID=ID)
#     if(request.method =="POST"):
#         obj.delete()
#         return view_publisher(request)
#     return HttpResponse("That bai")




























# from book.models import Category
# from book.forms import CategoryForm
# def view_category(request):
#     ctx={}
#     categorys=Category.objects.all()
#     ctx["categorys"]=categorys
#     return render(request,"book/view_category.html",ctx)
# def create_category_form(request):
#     ctx={}
#     ctx["form"]=CategoryForm(request.POST or None)
#     return render(request,"book/create_category_form.html",ctx)
# def save_category(request):
#     if(request.method=="POST"):
#         form=CategoryForm(request.POST,request.FILES)
#         if(form.is_valid):
#             form.save();
#             return view_category(request)
#     return HttpResponse("That bai")    
# def update_category_form(request,ID):
#     obj=get_object_or_404(Category,ID=ID)
#     ctx={}
#     ctx["form"]=CategoryForm(request.POST or None,instance=obj)
#     return render(request,"book/update_category_form.html",ctx) 
# def update_category(request):
#     form=CategoryForm(request.POST,request.FILES)
#     obj=get_object_or_404(Category,ID=form["ID"].value())
#     form.instance=obj
#     if(form.is_valid):
#         form.save();
#         return view_category(request)
#     return render(request,"book/view_category.html")    
# def delete_category(request,ID):
#     obj=get_object_or_404(Category,ID=ID)
#     if(request.method =="POST"):
#         obj.delete()
#         return view_category(request)
#     return HttpResponse("That bai")






























# from book.models import Author
# from book.forms import AuthorForm
# def view_author(request):
#     ctx={}
#     authors=Author.objects.all()
#     ctx["authors"]=authors
#     return render(request,"book/view_author.html",ctx)
# def create_author_form(request):
#     ctx={}
#     ctx["form"]=AuthorForm(request.POST or None)
#     return render(request,"book/create_author_form.html",ctx)
# def save_author(request):
#     if(request.method=="POST"):
#         form=AuthorForm(request.POST,request.FILES)
#         if(form.is_valid):
#             form.save();
#             return view_author(request)
#     return HttpResponse("That bai")    
# def update_author_form(request,ID):
#     obj=get_object_or_404(Author,ID=ID)
#     ctx={}
#     ctx["form"]=AuthorForm(request.POST or None,instance=obj)
#     return render(request,"book/update_author_form.html",ctx) 
# def update_author(request):
#     form=AuthorForm(request.POST,request.FILES)
#     obj=get_object_or_404(Author,ID=form["ID"].value())
#     form.instance=obj
#     if(form.is_valid):
#         form.save();
#         return view_author(request)
#     return render(request,"book/view_author.html")    
# def delete_author(request,ID):
#     obj=get_object_or_404(Author,ID=ID)
#     if(request.method =="POST"):
#         obj.delete()
#         return view_author(request)
#     return HttpResponse("That bai")