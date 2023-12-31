# モデル読み込
from django.db import models

# 商品マスタ
class Product(models.Model):
    # 商品ID
    id = models.CharField(max_length=16, primary_key=True, auto_created=True)
    # 商品名
    name = models.TextField()
    # 単価
    price = models.IntegerField()
    
# 登録済み商品
class Cart(models.Model):
    # 数量
    quantity = models.PositiveIntegerField(blank=False)
    # 商品
    product = models.ForeignKey(Product, on_delete=models.CASCADE)