from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, min_length=4, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }), min_length=6)


class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, min_length=4, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }), min_length=6)


class PostForm(forms.Form):
    post_title = forms.CharField(label='Post Title', max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    post_content = forms.CharField(label='Post Content', widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))