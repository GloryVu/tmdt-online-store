
from distutils.command.upload import upload
from django.db import models
from django.forms import DateField

# Create your models here.

class Publisher(models.Model):
    ID=models.IntegerField(primary_key=True)
    name=models.TextField()
    address=models.TextField()
    def __str__(self):
        return self.name
class Category(models.Model):
    ID=models.IntegerField(primary_key=True)
    name=models.TextField()
    createAt=DateField()
    def __str__(self):
        return self.name
class Author(models.Model):
    ID=models.IntegerField(primary_key=True)
    name=models.TextField()
    biography=models.TextField()
    def __str__(self):
        return self.name
class Book(models.Model):
    ISBN=models.CharField(max_length=255)
    title=models.TextField()
    numberOfPage=models.IntegerField()
    language=models.TextField()
    img=models.ImageField(upload_to = 'pictures', null=True, blank=True)
    publisher=models.ForeignKey(Publisher ,on_delete=models.CASCADE)
    category=models.ForeignKey(Category ,on_delete=models.CASCADE)
    author=models.ForeignKey(Author ,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class BookItem(models.Model):
    ID=models.IntegerField(primary_key=True)
    barcode=models.TextField()
    price=models.FloatField()
    discount=models.FloatField()
    # book=models.ForeignKey(Book, unique=True,on_delete=models.CASCADE)
    book=models.OneToOneField(Book,on_delete=models.CASCADE)
    def __str__(self):
        return self.barcode
class BookStats(models.Model):
    ID=models.IntegerField(primary_key=True)
    quantity=models.IntegerField()
    importPrice=models.FloatField()
    quantityLeft=models.IntegerField()
    createAt=models.DateField()
    book=models.ForeignKey(Book ,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.ID)
