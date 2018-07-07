import json

from django.http import Http404, JsonResponse, HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

class EstudianteLogin(APIView):
    def post(self, request, format=None):
        students = json.load(open('students.json'))

        passwords = json.load(open('passwords.json'))

        codigo = request.POST['code']
        documento = request.POST['doc']
        password = request.POST['pass']

        estudiante = students.get(codigo)

        print(codigo)

        if estudiante is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            if estudiante["codigo"] == codigo and estudiante["documento"] == documento and passwords.get(codigo) == password:
                return JsonResponse(estudiante)

        return Response(status=status.HTTP_401_UNAUTHORIZED)

class DocenteLogin(APIView):
    def post(self, request, format=None):
        teachers = json.load(open('teachers.json'))

        passwords = json.load(open('passwords.json'))

        codigo = request.POST['code']
        documento = request.POST['doc']
        password = request.POST['pass']

        docente = teachers.get(codigo)

        if docente is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            if docente["codigo"] == codigo and docente["documento"] == documento and passwords.get(codigo) == password:
                return JsonResponse(docente)

        return Response(status=status.HTTP_401_UNAUTHORIZED)
