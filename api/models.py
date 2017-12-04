from django.db import models


class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150, blank=True, default='')
    content = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ('created',)
