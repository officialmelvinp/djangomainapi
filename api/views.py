from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class StudentListEndpoint(APIView):
    def get(self, request):
        students=Student.objects.all()
        serializer=StudentSerializers(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"post added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id):
        try:
            student = Student.objects.get(pk=id)
        except Student.DoesNotExist:
            raise Response({"error":"student does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"data successfully updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    def delete(self, request, id):
        try:
            student = Student.objects.get(pk=id)
        except Student.DoesNotExist:
            raise Response({"error": "Student does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        student.delete()
        return Response({"message":"student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        