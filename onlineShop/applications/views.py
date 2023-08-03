from django.shortcuts import render
from .models import Product

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
    
    registeredList = '登録済みの商品一覧が表示されるようこれから改良して行きます。'
    form = {
        'productList':_PRODUCT_LIST,
        'registeredList':registeredList,    
    }
    return render(request, 'detail.html', form)

# 売上登録画面
def register(request):
    return render(request, 'register.html')