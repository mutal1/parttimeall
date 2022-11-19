from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.

class Signup(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        print('회원가입화면입니다')
        return render(request, "user/signup.html")

class Login(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        print('로그인화면입니다')
        return render(request, "user/LogIn.html")