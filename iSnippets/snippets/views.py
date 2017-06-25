from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SnippetForm
from .models import Snippet

# Create your views here.
class SnippetHomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)

def new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            Snippet(
            title= form.cleaned_data['title'],
            language= form.cleaned_data['language'],
            snippet= form.cleaned_data['snippet'],
            description= form.cleaned_data['description']).save()
            return redirect('snippets:home')
    else:
        context = { 'header': 'GET', 'form': SnippetForm() }
        return render(request, 'new.html', context)
