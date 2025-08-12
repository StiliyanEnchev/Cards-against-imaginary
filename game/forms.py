from django import forms

class NickNameForm(forms.ModelForm):
    nickname = forms.CharField(label='Nickname', max_length=20, required=True)
    roomname = forms.CharField(label='Room Name', max_length=15, required=True)