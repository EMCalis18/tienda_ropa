from django import forms

from .models import Product , SubCategoria


class FormProduct(forms.ModelForm):
    """FormProduct definition."""
    class Meta:
        model = Product
    
        fields=(
            'name',
            'description',
            'marca',
            'unit',
            'size',
            'sizeNumber',
            'gender',
            'stock',
            'purchase_price',
            'sale_price',
            'main_image',
            'image1',
            'image2',
            'image3',
            'image4',
            'color',
            'category', 
            'offer',
            'discount',
        )
       
    # validations
    def clean_sale_price(self):
        sale_price = self.cleaned_data['sale_price']
        purchase_price = self.cleaned_data['purchase_price']
        if not sale_price >= purchase_price:
            raise forms.ValidationError('el precio de venta debe ser mayor al de compra')
        
        return sale_price

    """def clean_sizeNumber(self):
        sizeNumber = self.cleaned_data['sizeNumber']
        if not sizeNumber > 35 :
            raise forms.ValidationError('Ingrese un talle entre 35 y 45 ')
        
        return sizeNumber
        

    def clean_purchase_price(self):
        purchase_price = self.cleaned_data['purchase_price']
        if not purchase_price > 0:
            raise forms.ValidationError('el precio de venta no puede ser cero')

        return purchase_price


    def clean_sale_price(self):
        sale_price = self.cleaned_data['sale_price']
        purchase_price = self.cleaned_data['purchase_price']
        if not sale_price >= purchase_price:
            raise forms.ValidationError('el precio de venta debe ser mayor al de compra')
        
        return sale_price


        
"""