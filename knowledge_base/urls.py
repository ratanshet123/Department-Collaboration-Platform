from django.urls import path
from .views import download_document, knowledge_base_view, upload_document, view_document

urlpatterns = [
    path('', knowledge_base_view, name='knowledge_base'),
    path('upload/', upload_document, name='upload_document'),
     path('view/<int:document_id>/', view_document, name='view_document'),
    path('download/<int:document_id>/', download_document, name='download_document'),
]
