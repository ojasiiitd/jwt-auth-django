from django.contrib.auth.models import User, Group
from django.http.response import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

def index(response):
    return HttpResponse('<h1>NEW PAGE</h1>')

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)