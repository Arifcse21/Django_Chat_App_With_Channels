from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(usermessages)
class usermessagesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "sender",
        "reciever",
        "timestamp"
    ]
    list_display_links = ["id", "sender"]
