from django.urls import path

from .views import (
    create_order,
    user_orders,
)

urlpatterns = [
    path('', user_orders),

    path('create/', create_order),
]