from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from .models import JobPost
from .serializers import JobPostSerializer
# Create your views here.
class JobPostCreateList (generics.ListCreateAPIView):
  permission_classes = [AllowAny]
  queryset= JobPost.objects.all().order_by('-created_at')
  serializer_class = JobPostSerializer
  def delete(self, request, *args, **kwargs):
    JobPost.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class JobPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    lookup_field = "pk"


