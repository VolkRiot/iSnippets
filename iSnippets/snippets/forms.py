from django import forms
from snippets.models import Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SnippetForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
