from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Category, Cart, CartItem, Order, OrderItem
from .forms import CheckoutForm

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop/products.html', {
        'products': products,
        'categories': categories
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    print(f"Product found: {product.name}")
    print(f"Template: shop/product_detail.html")
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f'{product.name} added to cart!')
    
    referer = request.META.get('HTTP_REFERER', '/shop/')
    return redirect(referer)

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    total = cart.get_total()
    
    print(f"Cart: {cart}")
    print(f"Cart Items: {cart_items}")
    print(f"Total: {total}")
    
    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('view_cart')

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('view_cart')

@login_required
def checkout(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = cart.items.all()
        
        if not cart_items:
            messages.warning(request, 'Your cart is empty!')
            return redirect('product_list')
        
    except Cart.DoesNotExist:
        messages.warning(request, 'Your cart is empty!')
        return redirect('product_list')
    
    if request.method == 'POST':
        try:
            from decimal import Decimal
            
            # Build full address
            house = request.POST.get('house_number', '')
            road = request.POST.get('road_number', '')
            block = request.POST.get('block', '')
            city = request.POST.get('city', '')
            additional = request.POST.get('additional_info', '')
            
            full_address = f"House: {house}, Road: {road}, Block: {block}, {city}"
            if additional:
                full_address += f"\n{additional}"
            
            # Calculate total and convert to Decimal
            cart_total = cart.get_total()
            total_amount = Decimal(str(cart_total))
            
            # Create the order
            order = Order.objects.create(
                user=request.user,
                total_amount=total_amount,
                phone_number=request.POST.get('phone_number', ''),
                house_number=house,
                road_number=road,
                block=block,
                city=city,
                additional_info=additional,
                shipping_address=full_address,
                status='pending'
            )
            
            # Create order items
            for cart_item in cart_items:
                # Convert price to Decimal
                item_price_str = str(cart_item.product.price)
                item_price = Decimal(item_price_str)
                
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=item_price
                )
            
            # Clear the cart
            cart_items.delete()
            
            messages.success(request, f'Order placed successfully! Order ID: {order.id}')
            return redirect('order_confirmation', order_id=order.id)
            
        except Exception as e:
            messages.error(request, f'Error placing order: {str(e)}')
            return redirect('checkout')
    
    total = cart.get_total()
    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'shop/my_orders.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'shop/order_detail.html', {'order': order})

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'shop/order_confirmation.html', {'order': order})