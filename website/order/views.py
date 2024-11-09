from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from order.forms import OrderForm
from order import utils

products_list = {
    'product1': {
        "quantity": 2,
        "product_id": 1,
        "price": 1200,
        "seller_id": 2,
        "to_order": True
    },
    'product2': {
        "quantity": 1,
        "product_id": 2,
        "price": 1300,
        "seller_id": 1,
        "to_order": True
    },
    'product3': {
        "quantity": 1,
        "product_id": 3,
        "price": 1500,
        "seller_id": 1,
        "to_order": True
    }
}


class OrderCreateView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {}
        if request.user.is_authenticated:
            user = utils.get_user_data(request)
            context.update(user)

            prices = utils.get_correct_queryset(products_list)

            context['order_data'] = prices

        return render(request, "order/order.html", context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        data = request.POST
        validate_data = OrderForm(data)
        if validate_data.is_valid():
            correct_data = validate_data.cleaned_data
            utils.check_data_into_db(correct_data, products_list, request.user.pk)
        else:
            data_errors = validate_data.errors.items()
        return redirect(reverse('order:order_create'))


def order_detail_view(request: HttpRequest):
    return render(request, "order/order-detail.html")


def pay_view(request: HttpRequest):
    return render(request, 'order/payment.html')

def pay_view2(request: HttpRequest):
    return render(request, 'order/paymentsomeone.html')
