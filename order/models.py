from django.db import models
from users.models import User, BonusCard
from movies.models import Cinemas, Movie, ShowTimes, MovieFormat
from room.models import Room, RoomCategory, Seats


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seats, on_delete=models.CASCADE)
    showtime = models.ForeignKey(ShowTimes, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} has booked {self.seat} in {self.room} in {self.showtime}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} -- {self.total_price}"


class TicketCategory(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Ticket(models.Model):
    price = models.IntegerField()
    ticket_category = models.ForeignKey(TicketCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats = models.ForeignKey(Seats, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    showtime = models.ForeignKey(ShowTimes, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        price = (
                    self.ticket_category.price + self.showtime.rooms.category.price + self.showtime.movie.movie_format.price)
        bonus_card = BonusCard.objects.filter(user=self.user).first()

        if bonus_card is None:
            self.price = price
        else:
            discount = bonus_card.discount
            if discount == 0:
                self.price = price
            else:
                price_with_discount = (price / 100 * discount)
                self.price = (price - price_with_discount)

        super().save(*args, **kwargs)


