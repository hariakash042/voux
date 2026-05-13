from django.urls import path

from .views import (
    view_cart,
    add_to_cart,
)

urlpatterns = [
    path('', view_cart),

    path('add/', add_to_cart),
]