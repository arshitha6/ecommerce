from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product
from .forms import CustomerRegistrationForm
from django.contrib import messages
from django.db.models import Q

class ProductView(View):
    def get(self, request):
        topwear = Product.objects.filter(category='TW')
        bottomwear = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        return render(request, 'app/home.html', {'topwear': topwear, 'bottomwear': bottomwear, 'mobiles': mobiles})

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Successfully Registered!')
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})
