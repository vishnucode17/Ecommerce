from django.shortcuts import render
from shopping.models import Product
from django.contrib.auth.models import User
# Create your views here.
def search(request):
    product=request.GET['product']
    result =Product.objects.all().filter(product_name__icontains=product)
    search_string_length=len(result)>0
    product_details=[]
    if search_string_length:
        for i in range(len(result)):
            a=result[i].product_img
            product_details.append(a)
    return render(request,'search.html',{'result':result,'search_string_length':search_string_length,'product_details':product_details})