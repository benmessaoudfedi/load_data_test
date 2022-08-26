
from django.contrib import admin
from django.urls import path
from load_csv import views

urlpatterns = [
    path('', views.index),
    path('load_csv/', views.import_csv_view, name='import_csv_view'),
    path('upload-csv',views.import_csv_view, name='csv_upload'),
    path('document-support/<numdos>', views.document_support, name='document-support'),

]
