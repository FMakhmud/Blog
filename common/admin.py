from django.contrib import admin
from .models import *

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Skill)
