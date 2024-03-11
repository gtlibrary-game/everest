from django.db import models

from django.db import models

class AIRequest(models.Model):
    query = models.TextField()
    response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
