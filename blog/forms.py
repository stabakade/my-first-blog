from django import forms

from .models import Post

class PostForm(forms.ModelForm):   #Django will understand that it is a ModelForm

    class Meta:
        model = Post
        fields = ('title', 'text',)