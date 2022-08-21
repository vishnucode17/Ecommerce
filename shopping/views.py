from django.shortcuts import render
from .forms import UserLoginForm,ProductForm
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request,'index.html')


def signup(request):
    if request.method=='POST':
        form =UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'registration/signup.html', {'form': form})

def sellerinfo(request):
    if request.method =='POST':
        form=ProductForm()
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=ProductForm()
    return render(request, 'product_update.html',{'form':form})