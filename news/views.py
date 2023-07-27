from django.shortcuts import render
from rest_framework import generics, permissions
from .models import TextNewsModel, AudioNewsModel
from .serializers import TextNewsSerializer, AudioNewsSerializer
from .permissions import IsOwnerOrReadOnly

class TextNewsList(generics.ListAPIView):
    queryset = TextNewsModel.objects.all()
    serializer_class = TextNewsSerializer
    permission_classes = (permissions.IsAuthenticated, )


class TextNewsCreate(generics.CreateAPIView):
    queryset = TextNewsModel.objects.all()
    serializer_class = TextNewsSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)
    
class TextNewsRetrieve(generics.RetrieveAPIView):
    queryset = TextNewsModel.objects.all()
    serializer_class = TextNewsSerializer
    permission_classes = (permissions.IsAuthenticated, )


class TextNewsUpdate(generics.UpdateAPIView):
    queryset = TextNewsModel.objects.all()
    serializer_class = TextNewsSerializer
    permission_clases = (
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly
    )


class TextNewsDestroy(generics.DestroyAPIView):
    queryset = TextNewsModel.objects.all()
    serializer_class = TextNewsSerializer
    permission_clases = (
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly
    )


class NewsByCategory(generics.ListAPIView):
    serializer_class = TextNewsSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        category = self.kwargs['category']
        return TextNewsModel.objects.filter(category=category)


class NewsByRegion(generics.ListAPIView):
    serializer_class = TextNewsSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        region = self.kwargs['region']
        return TextNewsModel.objects.filter(region=region)


class AudioNewsList(generics.ListAPIView):
    queryset = AudioNewsModel.objects.all()
    serializer_class = AudioNewsSerializer
    permission_classes = (permissions.IsAuthenticated, )


class AudioNewsCreate(generics.CreateAPIView):
    queryset = AudioNewsModel.objects.all()
    serializer_class = AudioNewsSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)
    

class AudioNewsRetrieve(generics.RetrieveAPIView):
    queryset = AudioNewsModel.objects.all()
    serializer_class = AudioNewsSerializer
    permission_classes = (permissions.IsAuthenticated, )


class AudioNewsUpdate(generics.UpdateAPIView):
    queryset = AudioNewsModel.objects.all()
    serializer_class = AudioNewsSerializer
    permission_clases = (
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly
    )


class AudioNewsDestroy(generics.DestroyAPIView):
    queryset = AudioNewsModel.objects.all()
    serializer_class = AudioNewsSerializer
    permission_clases = (
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly
    )