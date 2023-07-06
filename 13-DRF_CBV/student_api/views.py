from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Student
from .serializers import StudentSerializer

class StudentListCreate(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailUpdateDelete(APIView):

    def get(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student)
        return Response(serializer.data)
    
    def put(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)


# Generic APIView

from rest_framework.generics import GenericAPIView
from rest_framework import mixins


class StudentGenericListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
  
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# ListCreateAPIView
# RetrieveUpdateDestroyAPIView
# https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes
# ----------------------------------------------------------------

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Kayıt Listeleme ve Yeni Kayıt Ekleme:
class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Tek kayıt görüntüle/güncelle/sil:
class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # lookup_field = "id" # Default: "pk"


# ModelViewSet:
# https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
# ----------------------------------------------------------------

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

# Tüm İşlemler:
class StudentMVS(ModelViewSet):
    queryset = Student.objecta.all()
    serializer_class = StudentSerializer

    @action(methods=["GET"], detail=False)
    def count(self, request):
        return Response({
            "count": Student.objects.count()
        })