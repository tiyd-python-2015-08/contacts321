from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Contact
from .serializers import ContactSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
