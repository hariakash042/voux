from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def product_list(request):
    return Response({
        "message": "Welcome to the VOUX Products API"
    })