from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Sidebar
from api.serializers import SidebarSerializer

class SidebarList(APIView):

    def get(self, request, company, role):
        sidebars = Sidebar.objects.filter(company=company, role=role)
        serializer = SidebarSerializer(sidebars, many=True)
        return Response(serializer.data)

    def post(self, request, company, role):
        serializer = SidebarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SidebarDetail(APIView):
    def get_object(self, pk):
        try:
            return Sidebar.objects.get(pk=pk)
        except Sidebar.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        sidebar = self.get_object(pk)
        serializer = SidebarSerializer(sidebar)
        return Response(serializer.data)

    def put(self, request, company, role, pk):
        sidebar = self.get_object(pk)
        serializer = SidebarSerializer(sidebar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sidebar = self.get_object(pk)
        sidebar.delete()
        return Response({'message': 'Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
