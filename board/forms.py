# from collections.abc import Mapping
# from typing import Any
# from django.core.files.base import File
# from django.db.models.base import Model
# from django.forms.utils import ErrorList
from django import forms
from .models import Board, Comment


class BoardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._widget_update()
    
    class Meta:
        model = Board
        fields = ["title", "content"]
        widgets = {
            'title':forms.TextInput(
                attrs={
                    'placeholder':"제목을 입력하세요."
                }
            )
        }

    def _widget_update(self):
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._widget_update()
    
    class Meta:
        model = Comment
        fields = ["content"]


    def _widget_update(self):
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'