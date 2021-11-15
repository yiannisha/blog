from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'class' : 'form-group',
            'placeholder' : 'Your name',
        })
    )

    body = forms.CharField(
        widget=forms.Textarea(attrs={
            'class' : 'form-group',
            'placeholder' : 'Leave a comment',
        })
    )
