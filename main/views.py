from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from .models import Todo, Upload, Hots
from uuid import uuid4
import os
from parttime.settings import MEDIA_ROOT
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

        if user.master == True:
            return render(request, "main/Calendar.html")
        else:
            return render(request, "main/jobopening.html")

    def post(self, request):
        if request.method == 'POST':
            modal = request.POST['Start']
            Hot_list = Hots.objects.filter(start=modal)
            upload_list = Upload.objects.filter(start=modal)
            return render(request, "main/list.html", context=dict(uploads=upload_list, Hottimes=Hot_list))

        email = request.session.get('email', None)
        todo_list = request.data.get('todo_list')
        day = request.data.get('day')
        month_year = request.data.get('month_year')

        Todo.objects.create(
                            Todo_list=todo_list,
                            email=email,
                            day=day,
                            month_year=month_year
                            )

        match_main = Todo.objects.filter(email=email, month_year=month_year, day=day)

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
            money = request.POST["money"]
            print(money)
            gender = request.POST["userGender"]
            print(gender)
            start = request.POST["workStart"]
            print(start)
            end = request.POST["workEnd"]
            print(end)
            #area = request.POST["address"]
            area = "서울"
            print(area)

            Upload.objects.create(title_box=title_box,
                                  content_box=content_box,
                                  email=email_upload,
                                  money=money,
                                  gender=gender,
                                  start=start,
                                  end=end,
                                  area=area
                                  )

            return render(request, "main/Calendar.html")

class List(APIView):
    def get(self, request):

        upload_list = Upload.objects.all().order_by('-id')
        hots_list = Hots.objects.all().order_by('-id')

        email = request.session.get('email', None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")

        return render(request, "main/list.html", context=dict(uploads=upload_list, Hottimes=hots_list))

class Hot(APIView):

    def get(self, request):

        email = request.session.get('email', None)
        print(email)

        if email is None:
            return render(request, "user/LogIn.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/LogIn.html")

        return render(request, "main/hottime_opening.html")

    def post(self, request):
        email_Hot = request.session.get('email')

        if request.method == 'POST':

            print(request.POST)
            title_box = request.POST["titlebox"]
            print(title_box)
            content_box = request.POST["contentbox"]
            print(content_box)
            start_money = request.POST["startmoney"]
            print(start_money)
            end_money = request.POST["endmoney"]
            print(end_money)
            gender = request.POST["userGender"]
            print(gender)
            start = request.POST["workStart"]
            print(start)
            end = request.POST["workEnd"]
            print(end)
            area = request.POST["address"]
            print(area)

            file = request.FILES['file']

            uuid_name = uuid4().hex
            save_path = os.path.join(MEDIA_ROOT, uuid_name)

            with open(save_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            image = uuid_name
            print(file)
            print(image)
            Hots.objects.create(title_box=title_box,
                                  content_box=content_box,
                                  email=email_Hot,
                                  start_money=start_money,
                                  end_money=end_money,
                                  gender=gender,
                                  start=start,
                                  end=end,
                                  area=area,
                                  image=image
                                )

            return render(request, "main/Calendar.html")












