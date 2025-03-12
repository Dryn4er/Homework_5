from django import forms
from django.core.exceptions import ValidationError
from .models import Product
from catalog import constanta


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price', 'category', 'publication_status']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продукта'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продукта'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'type': 'image'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'type': 'integer'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control'
        })

    def clean_name(self):
        block_list = constanta.BLOCK_LIST
        name = self.cleaned_data.get('name')
        if name.lower() in block_list:
            raise ValidationError('Имя имеет запрещенное слово')
        return name

    def clean_description(self):
        block_list = constanta.BLOCK_LIST
        description = self.cleaned_data.get('description')
        if description.lower() in block_list:
            raise ValidationError('Описание имеет запрещенное слово')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена введена неправильно')
        return price


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['publication_status']