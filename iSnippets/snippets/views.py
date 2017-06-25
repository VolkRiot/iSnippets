from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import SnippetForm
from .models import Snippet

# Create your views here.
class SnippetListView(ListView):
    model = Snippet
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(SnippetListView, self).get_context_data(**kwargs)
        return context


def new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            Snippet(
            title= form.cleaned_data['title'],
            language= form.cleaned_data['language'],
            snippet= form.cleaned_data['snippet'],
            description= form.cleaned_data['description']).save()
            return redirect('home')
    else:
        context = { 'header': 'GET', 'form': SnippetForm() }
        return render(request, 'new.html', context)
