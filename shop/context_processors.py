def cart_count(request):
    if request.user.is_authenticated:
        try:
            from .models import Cart
            cart = Cart.objects.get(user=request.user)
            count = cart.items.count()
        except:
            count = 0
    else:
        count = 0
    
    return {'cart_count': count}