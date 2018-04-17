from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, Http404
from django.template.loader import render_to_string


# Create your views here.
all_products = Product.objects


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# Страница с товарами
def product_list(request):
    products = Product.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        'products': products,
        'cart_product_form': cart_product_form,
    }
    return HttpResponse(render_to_string('home.html', context))