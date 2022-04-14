from django import forms  
from clothes.models import Clothes, ClothesItem, ClothesBrand, ClothesStats
class ClothesForm(forms.ModelForm):  
    class Meta:  
        model = Clothes
        fields = "__all__" 

class ClothesItemForm(forms.ModelForm):  
    class Meta:  
        model = ClothesItem 
        fields = "__all__" 

class ClothesBrandForm(forms.ModelForm):  
    class Meta:  
        model = ClothesBrand
        fields = "__all__" 
class ClothesStatsForm(forms.ModelForm):  
    class Meta:  
        model = ClothesStats
        fields = "__all__" 
        