from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from kafka_app.consumer import consumer1
from kafka_app.producer import producer1
from kafka_app.categories import categories
from rest_framework.views import APIView


class ProducerAPI(APIView):

    def get(self, request, **kwargs):
        result = producer1()
        return Response(result)


class ConsumerAPI(APIView):

    def get(self, request, **kwargs):
        result = consumer1()
        return Response(result)


class CategoriesAPI(APIView):

    def get(self, request, **kwargs):
        result = categories()
        return Response(result)
