from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from .models import Todo
# Create your views here.
class Main(APIView):

    def get(self, request):

        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/LogIn.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/LogIn.html")

        return render(request, "main/Calendar.html")

    def post(self, request):

        email = request.session.get('email', None)
        todo_list = request.data.get('todo_list')
        day = request.data.get('day')
        year = request.data.get('year')
        month = request.data.get('month')

        Todo.objects.create(
                            Todo_list=todo_list,
                            email=email,
                            day=day,
                            year=year,
                            month=month
                            )

        match = Todo.objects.filter(email=email, year=year, month=month, day=day)

        return Response(status=200)

