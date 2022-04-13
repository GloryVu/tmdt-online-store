from django import forms  
from book.models import Book 
class BookForm(forms.ModelForm):  
    class Meta:  
        model = Book  
        fields = "__all__" 



from book.models import BookItem
class BookItemForm(forms.ModelForm):  
    class Meta:  
        model = BookItem 
        fields = "__all__" 


from book.models import BookStats
class BookStatsForm(forms.ModelForm):  
    class Meta:  
        model = BookStats
        fields = "__all__" 