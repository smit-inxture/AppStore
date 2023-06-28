from django.shortcuts import render
from rest_framework import generics, status, filters
from rest_framework.response import Response

from play_store.models import AppPackage, AppDetails
from play_store.serializers import AppPackageListSerializer, AppDetailsSerializer
from play_store.soup import package_name_scrapper
from play_store.tasks import app_details_task
from play_store.utils import StandardResultsSetPagination


# Create your views here.


class AppPackageListCreate(generics.ListCreateAPIView):
    """
    it is list and create view
    in listing providing pagination,search and ordering
    default pagination is 10
    to increase page size use page_size in query params and page for page number
    """

    queryset = AppPackage.objects.all()
    serializer_class = AppPackageListSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['package_name']
    ordering_fields = ['id', 'package_name', '-id', '-package_name']

    def post(self, request, *args, **kwargs):
        package_name_scrapper()
        return Response({"message": "Packages Scrapped Successfully"}, status=status.HTTP_200_OK)


class AppDetailsListView(generics.ListCreateAPIView):
    """
    it is list and create view
    in listing providing pagination,search and ordering
    default pagination is 10
    to increase page size use page_size in query params and page for page number
    """

    # Here For query optimization I have used  prefetch_related
    queryset = AppDetails.objects.all().prefetch_related('app_details')
    serializer_class = AppDetailsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['id', 'title', '-id', '-title']


    def post(self, request, *args, **kwargs):
        app_details_task.delay()
        return Response({"message":"App Details Scrapping Started Successfully"})