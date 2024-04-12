from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.


def custom_logout_view(request):
    logout(request)
    return redirect('custom_logout_page')


def custom_logout_page(request):
    return render(request, 'logout.html')
