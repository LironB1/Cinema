from django.contrib import admin
from .models import Hall,Screening,Movie

admin.site.register(Movie)
admin.site.register(Screening)
admin.site.register(Hall)