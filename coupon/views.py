from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Coupon
from .forms import AddCouponForm

@require_POST
def add_coupon(request):
    now = timezone.now()
    form = AddCouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']

        try:
            coupon = Coupon.objects.get(code__iexact=code, use_from__lte=now, use_to__gte=now, active=True)
            #code__iexact 대소문자 가리지않고 일치, (use_from__lte) (use_to__gte)사이에 현재시간이 있으면 된다. 
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon.id'] = None

    return redirect("cart:detail")
