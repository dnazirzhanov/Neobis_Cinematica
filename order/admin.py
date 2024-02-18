from django.contrib import admin
from .models import Booking, Ticket, TicketCategory, Order

admin.site.register(Booking)
admin.site.register(Ticket)
admin.site.register(TicketCategory)
admin.site.register(Order)
