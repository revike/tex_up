from django import forms

from main_app.models import Client


class ClientForm(forms.ModelForm):
    """Форма клиента"""

    class Meta:
        model = Client
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
        self.fields['first_name'].widget.attrs[
            'placeholder'] = 'Введите ваше имя'
        self.fields['phone'].widget.attrs[
            'placeholder'] = 'Введите ваш номер'
        self.fields['phone'].widget.attrs[
            'pattern'] = r'^\+1?\d{11,11}$'
        self.fields['phone'].widget.attrs[
            'oninvalid'] = "this.setCustomValidity('Неверный номер " \
                           "телефона...')"
        self.fields['phone'].widget.attrs[
            'oninput'] = "setCustomValidity('')"
