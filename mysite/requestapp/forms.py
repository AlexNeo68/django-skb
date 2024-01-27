from django import forms


class UserBioForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ваше имя")
    age = forms.IntegerField(label="Ваш возраст")
    bio = forms.CharField(label="Немного о себе", widget=forms.Textarea())