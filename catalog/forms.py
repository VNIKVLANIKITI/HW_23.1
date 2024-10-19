from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

class ProductForm(FormStyleMixin, forms.ModelForm):
    banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'category', 'price')  # базовые поля

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Извлекаем пользователя из аргументов
        super(ProductForm, self).__init__(*args, **kwargs)

        # Проверяем наличие полномочия у пользователя
        if user.has_perm('yourapp.can_cancel_publish'):
            self.fields['publish'] = forms.BooleanField(required=False)  # Добавляем поле publish

        # Если у пользователя нет полномочий, можно выбросить исключение (по желанию)
        # else:
        #     raise PermissionDenied("У вас нет полномочий для отмены публикации.")

    def clean_title(self):
        list_words = []
        cleaned_data = self.cleaned_data['title']
        for word in self.banned_words:
            if word in cleaned_data:
                list_words.append(word)
        result_banned_words = ", ".join(list_words)
        if len(result_banned_words) != 0:
            raise forms.ValidationError(f'Запрещено использовать в названии слова: {result_banned_words}')
        return cleaned_data

    def clean_description(self):
        list_words = []
        cleaned_data = self.cleaned_data['description']
        for word in self.banned_words:
            if word in cleaned_data:
                list_words.append(word)
        result_banned_words = ", ".join(list_words)
        if len(result_banned_words) != 0:
            raise forms.ValidationError(f'Запрещено использовать в описании слова: {result_banned_words}')
        return cleaned_data


class VersionForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('title', 'counter', 'currented')
