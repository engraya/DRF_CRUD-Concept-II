from django.shortcuts import render
from django.http import HttpResponse
from .models import ProgrammingLanguage
from rest_framework import serializers
from rest_framework import generics
from base.serializers import ProgrammingLanguageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class ProgrammingLanguageList(APIView):

    def get(self, request, format=None):
        programmingLanguages = ProgrammingLanguage.objects.all()
        serializer = ProgrammingLanguageSerializer(programmingLanguages, many=True)
        return Response(serializer.data)


class ProgrammingLanguageCreate(APIView):

    def post(self, request, format=None):
        serializer = ProgrammingLanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProgrammingLanguageDetail(APIView):

    def get_object(self, pk):
        try:
            return ProgrammingLanguage.objects.get(pk=pk)
        except ProgrammingLanguage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        programmmingLanguage =self.get_object(pk)
        serializer = ProgrammingLanguageSerializer(programmmingLanguage)
        return Response(serializer.data)


class ProgrammingLanguageUpdate(APIView):

    def get_object(self, pk):
        try:
            return ProgrammingLanguage.objects.get(pk=pk)
        except ProgrammingLanguage.DoesNotExist:
            raise Http404


    def put(self, request, pk, format=None):
        progarmmingLanguage = self.get_object(pk)
        serializer = ProgrammingLanguageSerializer(progarmmingLanguage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProgrammingLanguageDelete(APIView):

    def get_object(self, pk):
        try:
            return ProgrammingLanguage.objects.get(pk=pk)
        except ProgrammingLanguage.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        programmingLanguage = self.get_object(pk)
        programmingLanguage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




