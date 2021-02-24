from django import forms
from .models import Product

# El formulario intermedio
# class ProductForm(forms.Form):
#     title= forms.CharField(max_length=100)

class ProductForm(forms.ModelForm):

    class Meta:
        model= Product
        fields = ['title', 'description']

        # VAMOS A VALIDAR LA DATA ANTES DE MANDARLA A VIEW.
        # ESTA VALIDACIÓN SE HACE CUANDO DESDE LA VIEW HACEmos::
        # if form.is_valid():
    def clean_title(self):
        data = self.cleaned_data.get('title')
#        return data        CON ESTO YA ESTARÍA VALIDADA
        if len(data) < 4:   #validamos q el nombre sea mas largo q 4
            raise forms.ValidationError("This is not long enought")
        return data 
 
