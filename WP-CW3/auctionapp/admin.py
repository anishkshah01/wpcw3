from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account,Userr,Item,Bid,Question,Answer

# Register your models here.
admin.site.register(Account, UserAdmin)
admin.site.register(Userr)
admin.site.register(Item)
admin.site.register(Question)
admin.site.register(Bid)
admin.site.register(Answer)





