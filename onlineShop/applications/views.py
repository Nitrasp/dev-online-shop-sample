from django.shortcuts import render, redirect
from django.db import connection
from django.db.models import Sum,ExpressionWrapper,F,DecimalField
from django.views.generic import TemplateView
from .models import Product,Cart

# 商品マスタの全商品
_PRODUCT_LIST = Product.objects.all()

# 初期画面
def init(request):
    
    # カートTBLのレコードをすべて削除する
    Cart.objects.all().delete()
    
    form = {
        'productList':_PRODUCT_LIST,
    }
    
    return render(request, 'index.html', form)

# 明細追加画面
def add(request):
    
    # POSTメソッドの場合、カートTBLの更新を行う
    if request.method == 'POST':    
        # 商品IDと数量の取得
        productId = request.POST['product']
        quantity = request.POST['quantity']
        
        # quantityが0以下の場合
        if int(quantity) <= 0:
            
            # 前画面に戻る
            previous_url = request.META.get('HTTP_REFERER')
            return redirect(previous_url)
        
        # カートTBLの更新
        Cart.objects.update_or_create(product_id=productId, defaults={'quantity':quantity})
    
    # カートTBLの取得（小計の計算）
    results = Cart.objects.all().annotate(
        subtotal=(ExpressionWrapper(F('product__price') * F('quantity'), output_field=DecimalField(null=False, blank=False)))
    )
    
    form = {
        'productList':_PRODUCT_LIST,
        'registeredList':results,
    }
    
    return render(request, 'detail.html', form)

# 売上登録画面
def register(request):
    
    # 更新後のカートTBLの取得（小計の計算）
    results = Cart.objects.all().annotate(
            subtotal=(ExpressionWrapper(F('product__price') * F('quantity'), output_field=DecimalField(null=False, blank=False)))
        )
    
    total = results.aggregate(total=Sum('subtotal'))['total']
    
    form = {
        'productList':_PRODUCT_LIST,
        'registeredList':results,
        'total':total,
    }
    
    return render(request, 'register.html', form)