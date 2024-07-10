from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='knowledge_base/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='knowledge_base_documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    document_type = models.CharField(max_length=50)
    views_count = models.PositiveIntegerField(default=0)
    downloads_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
