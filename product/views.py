from django.shortcuts import render , redirect
from . models import Product, Product2 , Product3 

from django.conf import settings
import stripe
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem , Order
from django.contrib.auth.decorators import login_required



def product_list(request):
    products = Product.objects.all()
    products2 = Product2.objects.all()
    products3 = Product3.objects.all()  

    context = {
        'products': products,
        'products2': products2,  
        'products3': products3, 
    }
    return render(request, 'product.html', context)



def product_detail(request, category_slug, product_id):
    product = Product.objects.get(category__slug=category_slug , id = product_id)
    


    context={
        'product': product,
        
        
    }
    return render(request, 'products.html', context)



def product_detail2(request, category_slug, product2_id):
    product2 = Product2.objects.get(category__slug=category_slug , id = product2_id)
    
    context = {
        'product2': product2,
    }
    
    return render(request, 'products2.html', context)




def product_detail3(request, category_slug, product3_id):
    product3 = Product3.objects.get(category__slug=category_slug , id = product3_id)
    
    context = {
        'product3': product3,
    }
    
    return render(request, 'products3.html', context)





stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart_detail')


@login_required
def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'cart_detail.html', {'cart': cart})


@login_required
def payment_view(request):
    cart = Cart.objects.get(user=request.user)
    total_amount = sum(item.product.price * item.quantity for item in cart.items.all())
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            charge = stripe.Charge.create(
                amount=int(total_amount * 100),  # amount in cents
                currency='usd',
                description='Payment for cart',
                source=token,
            )
            # Ödeme başarılı, sipariş oluştur ve sepeti temizle
            Order.objects.create(user=request.user, total=total_amount)
            cart.items.all().delete()
            return redirect('success')
        except stripe.error.CardError as e:
            return redirect('error')

    context = {
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        'total_amount': total_amount,
    }
    return render(request, 'payment.html', context)

@login_required
def success_view(request):
    return render(request, 'success.html')

@login_required
def error_view(request):
    return render(request, 'error.html')