from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import Group

from .serializers import GroupSerializer

@api_view()
def hello_world_view(request:Request)->Response:
    return Response({'message': 'Hello World!'})

class GroupView(APIView):
    def get(self, request: Request)->Response:
        groups = Group.objects.all()
        return Response({"groups": GroupSerializer(groups, many=True).data})
