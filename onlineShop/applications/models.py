# モデル読み込
from django.db import models

# 商品マスタ
class Product(models.Model):
    # 商品ID
    id = models.CharField(max_length=16)
    # 商品名
    name = models.TextField()
    # 単価
    price = models.IntegerField()