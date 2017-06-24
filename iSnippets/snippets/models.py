from django.db import models

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    language = models.CharField(max_length=256, blank=False, null=False)
    snippet = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return "Title: %s\nLanguage:%s\nSnippet:%s\nDescription:%s\n" %(self.title, self.language, self.snippet, self.description)
    
