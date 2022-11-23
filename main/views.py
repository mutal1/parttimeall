from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from .models import Todo, Upload
# from .forms import Uploadform
""" title_box = request.POST['titlebox']
           content_box = request.POST['contentbox']

       print(title_box, content_box)
       Upload.objects.create(
                               title_box=title_box,
                               content_box=content_box,
                               email=email_upload
                           )"""
""" title_box = request.data.get('title_box')
       content_box = request.data.get('content_box')

       Upload.objects.create(
                             title_box=title_box,
                             content_box=content_box,
                             email=email_upload
                             )

       return Response(status=200)"""
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

        match_main = Todo.objects.filter(email=email, year=year, month=month, day=day)

        return Response(status=200)

class Uploadviews(APIView):

    def get(self, request):

        email = request.session.get('email', None)
        print(email)

        if email is None:
            return render(request, "user/LogIn.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/LogIn.html")

        return render(request, "main/jobopening.html")

    def post(self, request):
        email_upload = request.session.get('email')
        if request.method == 'POST':

            print(request.POST)
            title_box = request.POST["titlebox"]
            print(title_box)
            content_box = request.POST["contentbox"]
            print(content_box)

            Upload.objects.create(title_box=title_box, content_box=content_box, email=email_upload)

            return render(request, "main/Calendar.html")










