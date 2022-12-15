from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import *
from django.http import JsonResponse
from rest_framework import generics


api_view(['GET'])
def allProduct(request):
    products = Product.objects.all()
    serialization = ProductSerializer(products,many=True)
    return JsonResponse(serialization.data, safe=False)



api_view(['GET'])
def getProduct(request,id):
    products = Product.objects.get(id=id)
    serialization = ProductSerializer(products)
    return JsonResponse(serialization.data, safe=False)



api_view(['POST'])
class CreateProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        serializer.save()


api_view(['PUT'])

class UpdateProductView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
        serializer.save()


class DeleteProductView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

