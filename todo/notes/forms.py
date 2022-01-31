from django import forms


class AddNoteForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(max_length=1000)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
