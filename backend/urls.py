from django.urls import *

from .views import *


urlpatterns = [
    path('product/', allProduct),

    path('product/<int:id>/', getProduct),

    path('add/',CreateProductView.as_view()),

    path('update/<int:pk>', UpdateProductView.as_view()),

    path('delete/<int:pk>', DeleteProductView.as_view()),
]





