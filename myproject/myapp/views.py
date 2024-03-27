from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import User,Room,Booking
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == "POST":

        user = User.objects(username=username, password=password)
        username = request.POST["username"]
        password = request.POST["password"]

        if user is not None:
            login(request, user,password)
            return redirect("userclassroom")
        
    else:
        return render(request,"login.html")

def userclassroom(request):
    all_room  = Room.objects.all()
    return render(request,"user-classroom.html",{"all_room":all_room })

def reservationlist(request):
    all_booking  = Booking.objects.all()
    return render(request,"reservation-list.html",{"all_booking":all_booking })

def booking(request):
    if request.method == "POST":

        classroom = request.POST["classroom"]
        namebooker = request.POST["namebooker"]
        seatsuse = request.POST["seatsuse"]
        datetime = request.POST["datetime"]
        note = request.POST["note"]
        print(classroom,namebooker,seatsuse,datetime)

        booking = Booking.objects.create (
            classroom = classroom,
            namebooker = namebooker,
            seatsuse = seatsuse,
            datetime = datetime,
            note = note
        )

        return redirect("/reservationlist")
    else:
        return render(request,"booking.html")


def bookingform(request):
    if request.method == "POST":

        classroom = request.POST["classroom"]
        namebooker = request.POST["namebooker"]
        seatsuse = request.POST["seatsuse"]
        detetime = request.POST["detetime"]
        note = request.POST["note"]
        print(classroom,namebooker,seatsuse,detetime,note)

        booking = Booking.objects.create (
            classroom = classroom,
            namebooker = namebooker,
            seatsuse = seatsuse,
            detetime = detetime,
            note = note
        )
        booking.save()

        return redirect("/")
    else:
        return render(request,"form.html")

def deletebooking(request,booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.delete()
    return redirect("/reservationlist")