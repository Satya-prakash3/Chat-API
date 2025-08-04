from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class Root(APIView):
    def get(self, request):
        context = {
            "Message": "Hello Welcome to my application.",
        }
        return Response(context, status=status.HTTP_200_OK)