from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework import status
from django.contrib.auth import logout
from .models import Book



def index(request):
    return render(request, 'index.html')  # Or any valid template
# views.py
def product_details(request):
    # Optional: Fetch a specific book/product by ID if you want
    return render(request, 'productDetails.html')


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        login(request, user)  # automatically log in the user
        messages.success(request, 'Registration successful. Welcome!')
        return redirect('index')  # send to index page after signup

    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    
    return render(request, 'login.html')


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('index')  # Assuming your index.html is mapped to the name 'index' in urls.py

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_book_detail(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['POST'])
def api_register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    if User.objects.filter(username= username).exists():
        return Response({'error': 'Username already exist'},status=status.HTTP_400_BAD_REQUEST)
                        
    user = User.objects.create_user(username=username, password=password, email=email)
    return Response({'message': 'user registered successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def api_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def api_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'User not Logged in'}, status=status.HTTP_400_BAD_REQUEST)
  



    
    

