from django import forms
from django.contrib.auth.models import User
from .models import Product,Store
class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =('username','first_name','last_name','email','password')
    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =('product_name','Category','product_info','price','product_img')

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields ='__all__'