from django.db import models


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


