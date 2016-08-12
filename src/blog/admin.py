from django.contrib import admin

from .models import Post, Vehicle, Location, Rating, Date

from .forms import PostForm

class PostAdmin(admin.ModelAdmin):
    form=PostForm

class DateAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'user',
        'start',
        'end'
    ]


admin.site.register(Post, PostAdmin)

admin.site.register(Vehicle)

admin.site.register(Location)

admin.site.register(Rating)

admin.site.register(Date, DateAdmin)

