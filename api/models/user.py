from django.db import models
from django.contrib.auth.models import User

class User(User):
    device_id = models.CharField(max_length=50)
    device_type = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return f"{{'id': '{self.id}', 'email': '{self.email}', 'username': '{self.username}', 'first_name': '{self.first_name}', 'last_name': '{self.last_name}', 'device_id': '{self.device_id}', 'device_type': '{self.device_type}', 'time_zone': '{self.time_zone}', 'created_at': '{self.created_at}', 'updated_at': '{self.updated_at}'}}"
