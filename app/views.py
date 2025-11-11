from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # If user is authenticated, log them in and return a token
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            # Authentication failed
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        # Handle other HTTP methods (GET, etc.) as needed
        return JsonResponse({'error': 'Method not allowed'}, status=405)

class ReactView(APIView):
    serializer_class = ReactSerializer

    def get(self, request):
        output = [{"username":output.username,"password":output.password,"email":output.email}
                  for output in React.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostingView(APIView):
    serializer_class = PostingSerializer

    def get(self, request):
     output = [{"name": output.name, "email": output.email, "problem": output.problem,"age":output.age,"amount":output.amount,  "image":output.image.url if output.image else None,"upi":output.upi}
                  for output in Posting.objects.all()]
     return Response(output)

    def post(self, request):
        serializer = PostingSerializer(data=request.data)
        if serializer.is_valid():
            image_file = request.FILES.get('image')
            if image_file:
                filename = default_storage.save(image_file,ContentFile(image_file.read()))
                image_url = default_storage.url(filename)
                serializer.validated_data['image'] = image_url

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
