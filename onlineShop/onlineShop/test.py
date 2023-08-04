from django.shortcuts import render

# 初期画面
def init(request):
    return render(request, 'index.html')

# 明細追加画面
def add(request):
    return render(request, 'detail.html')

# 売上登録画面
def register(request):
    return render(request, 'register.html')