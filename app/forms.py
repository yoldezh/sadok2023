from django import forms
from .models import Post, Media

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['image']  

 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False