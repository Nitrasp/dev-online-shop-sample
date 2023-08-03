from django.shortcuts import render
from .models import Product

# 初期画面
def init(request):
    
    # 商品マスタから全商品のリストを取得する
    productList = {'productList' : Product.objects.all()}
    print(productList)
    return render(request, 'index.html', productList)

# 明細追加画面
def add(request):
    return render(request, 'detail.html')

# 売上登録画面
def register(request):
    return render(request, 'register.html')