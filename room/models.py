from django.db import models

class RoomCategory(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Room(models.Model):
    label = models.PositiveIntegerField()
    category = models.ForeignKey(RoomCategory, on_delete=models.PROTECT)

    def __str__(self):
        return f"Room #{self.label} of category - {self.category}"


class Seats(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    seat = models.PositiveIntegerField()

    def __str__(self):
        return f"Seat # {self.seat} in Room - {self.room}"
