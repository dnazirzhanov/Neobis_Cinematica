from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Booking, TicketCategory, Ticket, Order

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    def validate(self, data):
        seat = data.get('seat')
        room = data.get('room')
        showtime = data.get('showtime')
        if Booking.objects.filter(seat=seat, room=room, showtime=showtime).exists():
            raise ValidationError('This seat is already booked')
        return data

class OrderSerializer(ModelSerializer):
    total_price = SerializerMethodField('get_total_price')

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price']

    def get_total_price(self, obj):
        tickets = Ticket.objects.filter(order=obj.id)
        total_price = 0
        for ticket in tickets:
            total_price += ticket.price
        return total_price


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"

    def validate(self, data):
        seat = data.get('seats')
        showtime = data.get('showtime')
        if Booking.objects.filter(seats=seat, showtime=showtime).exists():
            raise ValidationError('This seat is already booked')
        return data