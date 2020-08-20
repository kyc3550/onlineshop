from django.shortcuts import render, get_object_or_404
from .models import *
from cart.cart import Cart
from .forms import *

# Create your views here.

def order_create(request):
    #한 페이지에서 POST와 GET 방식 모두 처리
    cart = Cart(request)
    if request.method =='POST':
        # 입력받은 정보를 후처리
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.amount
                order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            return render(reauest, 'order/created.html',{'order':order})
    else:
        #주문자 정보를 입력받는 페이지
        form = OrderCreateForm()
    return render(request, 'order/create.html',{'cart':cart,'form':form})

# JS가 동작하지 않는 환경에서도 주문은 가능해야 한다.

def order_complete(request):
    order_id = request.GET.get('order_id')
    order = Order.objects.get(id=order_id)
    return render(request,'order/created.html',{'order':order})