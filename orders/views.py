#orders/views.py
from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from django.core.exceptions import ObjectDoesNotExist

def checkout(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

def order_complete(request):
    return render(request, 'order_complete.html')

def create_order(request):
    # Get the total price from the session
    total = request.session.get('total', 0)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Create a new Order object
            order = Order(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                order_phone=form.cleaned_data['order_phone'],
                order_email=form.cleaned_data['order_email'],
                order_address=form.cleaned_data['order_address'],
                order_total_prices=total,
            )

            # Save the Order object to the database
            order.save()

            # Redirect the user to a confirmation page
            return redirect('order_complete')
    else:
        form = OrderForm(initial={'order_total_prices': total})

    return render(request, 'orders.html', {'form': form, 'total': total})