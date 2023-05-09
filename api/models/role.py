from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return f"{{'id': '{self.id}', 'name': '{self.name}', 'created_at': '{self.created_at}', 'updated_at': '{self.updated_at}'}}"

    class Meta:
        unique_together = ("name",)
