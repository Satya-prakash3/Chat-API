from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class root(APIView):
    def get(self, request):
        data = {
            "Hello welcome"
        }
        return Response(data, status=200)
