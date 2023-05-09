from rest_framework import serializers
from api.models import Sidebar

class SidebarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sidebar
        fields = '__all__'
