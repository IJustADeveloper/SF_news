from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    txt = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'title',
            'txt',
            'author_id'
        ]

    def clean(self):
        cleaned_data = super().clean()
        txt = cleaned_data.get("txt")
        title = cleaned_data.get("title")

        if txt == title:
            raise ValidationError(
                "Текст не должно быть идентичен названию."
            )
        elif title[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )

        return cleaned_data

