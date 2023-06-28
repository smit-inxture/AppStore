from django.urls import path

from play_store.views import AppPackageListCreate, AppDetailsListView

urlpatterns = [
    path('package/', AppPackageListCreate.as_view(),name="list_create_app_package"),
    path('app_details/', AppDetailsListView.as_view(),name="list_create_app_details"),
]
