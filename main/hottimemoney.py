from apscheduler.schedulers.background import BackgroundScheduler
from .models import Hots

def Hottime_func():

    hotlist = Hots.objects.all()
    for money in hotlist:
        if money.start_money < money.end_money:
            money.start_money += 100
            print(money.start_money)
            money.save()


def Hottime_main():
    sched = BackgroundScheduler()
    sched.add_job(Hottime_func, 'interval', seconds=3)
    sched.start()