from django.contrib import admin
from .models import Location, Tur, Gallery, Event

admin.site.register(Tur)
admin.site.register(Location)
admin.site.register(Event)
admin.site.register(Gallery)