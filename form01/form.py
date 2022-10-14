from django import forms

class Userform(forms.Form):
    fio = forms.CharField(max_length=100,widget=forms.TextInput(
        attrs={'class':'form-control shadow','id':'validationCustom01','name':'fio'}
    ))
    data_rojdeniya = forms.CharField(max_length=10,widget=forms.TextInput(
        attrs={'class':'form-control shadow','type':'number','id':'validationCustomUsername','name':'data_roj','aria-describedby':'inputGroupPrepend'}
    ))