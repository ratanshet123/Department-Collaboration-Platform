from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Document
from .forms import DocumentForm

def knowledge_base_view(request):
    query = request.GET.get('q')
    if query:
        documents = Document.objects.filter(title__icontains=query)
    else:
        documents = Document.objects.all()
    return render(request, 'knowledge_base/knowledge_base.html', {'documents': documents})

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.uploaded_by = request.user
            document.save()
            return redirect('knowledge_base')
    else:
        form = DocumentForm()
    return render(request, 'knowledge_base/upload_document.html', {'form': form})

def view_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    document.views_count += 1
    document.save()
    response = HttpResponse(document.file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{document.file.name}"'
    return response

def download_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    document.downloads_count += 1
    document.save()
    response = HttpResponse(document.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response
