from django.shortcuts import render
from .serializers import Postserializer, RegisterSerializer
from .models import Post, User
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Postserializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
    
    def update(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != self.request.user:
            return Response({'detail': 'you are not author of this post'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != self.request.user:
            return Response({'detail':'you are not author of this post'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def like(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response({'detail':'post not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.user in post.like.all():
        post.like.remove(request.user)
        return Response({'detail': 'post unliked'}, status=status.HTTP_200_OK)
    else:
        post.like.add(request.user)
        return Response({'detail':'post liked'})


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'detail':'registration successfully'}, status=status.HTTP_201_CREATED)
    return Response({'detail':'registration failed'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request):
    
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'detail': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

  
    user = authenticate(username=username, password=password)
    if user:
       
        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
    
 
    return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)














