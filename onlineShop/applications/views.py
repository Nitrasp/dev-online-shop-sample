from django.shortcuts import render
from django.db import connection
from django.db.models import Sum
from django.views.generic import TemplateView
from .models import Product,Cart

# 商品マスタの全商品
_PRODUCT_LIST = Product.objects.all()

# 初期画面
def init(request):
    form = {
        'productList':_PRODUCT_LIST,
    }
    
    return render(request, 'index.html', form)

# 明細追加画面
def add(request):
    
    productId = request.POST['product']
    quantity = request.POST['quantity']
    
    Cart.objects.update_or_create(product_id=productId, defaults={'quantity':quantity})
    
    results = Cart.objects.all()
        
    form = {
        'productList':_PRODUCT_LIST,
        'registeredList':list(results),
    }
    return render(request, 'detail.html', form)

# 売上登録画面
def register(request):
    return render(request, 'register.html')