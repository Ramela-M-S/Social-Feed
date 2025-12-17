from django import forms 
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ["title","post_image","desc"]
        widgets = {
            "title":forms.TextInput(
                attrs = {"class":"form-control",
                         "placeholder": "Post Title"}
            ),
            "desc" : forms.Textarea(
                attrs = {"class":"from-control",
                         "placeholder": "Post Description",
                         "rows":3}
            ),
            
        }