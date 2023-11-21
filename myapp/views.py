from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MyData
from .serializers import MyDataSerializer
from django.http import Http404

class MyDataAPIView(APIView):
    def post(self, request):
        name = request.data.get('name')
        if not name:
            return Response("Name is required.", status=status.HTTP_400_BAD_REQUEST)

        serializer = MyDataSerializer(data={'name': name})
        if serializer.is_valid():
            serializer.save()
            return Response(f"Welcome, {name}! Data saved.", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        data = MyData.objects.all()
        serializer = MyDataSerializer(data, many=True)
        return Response(serializer.data)
# ... (Previous imports and MyDataAPIView definition)

class MyDataDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return MyData.objects.get(pk=pk)
        except MyData.DoesNotExist:
            return Response("Data not found.", status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        data = self.get_object(pk)
        serializer = MyDataSerializer(data)
        return Response(serializer.data)

    def put(self, request, pk):
        data = self.get_object(pk)
        serializer = MyDataSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data updated successfully.", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        data = self.get_object(pk)
        data.delete()
        return Response("Data deleted successfully.", status=status.HTTP_204_NO_CONTENT)
