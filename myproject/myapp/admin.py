from django.contrib import admin
from myapp.models import User,Room,Booking

# Register your models here.
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Booking)