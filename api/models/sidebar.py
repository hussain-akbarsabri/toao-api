from django.db import models
from . import Company, Role, SidebarItem

class Sidebar(models.Model):
    sidebar_item = models.ForeignKey(SidebarItem, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return f"{{'id': '{self.id}', 'sidebar_item': '{self.sidebar_item}', 'role': '{self.role}', 'company': '{self.company}', 'created_at': '{self.created_at}', 'updated_at': '{self.updated_at}'}}"

    class Meta:
        unique_together = ("sidebar_item","role","company")
