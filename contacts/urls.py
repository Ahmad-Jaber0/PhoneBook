from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('export/', export_contacts, name='export_contacts'),
    path('show_export/', show_export_page, name='show_export_page'),


]
