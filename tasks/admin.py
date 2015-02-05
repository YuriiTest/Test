from django.contrib import admin
from tasks.models import Information, ImageUpload, Middleware, SignalLogEntry

admin.site.register(Information)
admin.site.register(ImageUpload)
admin.site.register(Middleware)
admin.site.register(SignalLogEntry)