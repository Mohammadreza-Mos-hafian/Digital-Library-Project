from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def home_page(request):
    return Response(
        {
            'message': 'Hi, Welcome to Digital Library App.'
        },
        status=status.HTTP_200_OK
    )
