from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

@api_view()
def hello_world_view(request:Request)->Response:
    return Response({'message': 'Hello World!'})