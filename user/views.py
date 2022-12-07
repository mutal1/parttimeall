from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User

from django.contrib.auth.hashers import make_password
class Signup(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        print('회원가입화면입니다')
        return render(request, "user/signup.html")

        # noinspection PyMethodMayBeStatic

    def post(self, request):
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        password = request.data.get('password', None)
        name = request.data.get('name', None)
        area = request.data.get('area', None)
        year = request.data.get('year', None)
        master = request.data.get('master', None)

        if master == "1":
            master = True
        else:
            master = False

        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            area=area,
                            year=year,
                            master=master
                            )

        return Response(status=200)

class Login(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        return render(request, "user/login.html")

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=400, data=dict(messege="회원정보가 잘못되었습니다."))
        if user.check_password(password):
            request.session['email'] = email
            return Response(status=200)
        else:
            return Response(status=400, data=dict(messege="회원정보가 잘못되었습니다."))

class Logout(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, "user/LogIn.html")