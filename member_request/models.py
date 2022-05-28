from django.db import models
from account.models import User
from book.models import BookItem
from datetime import datetime
from django.db.models.signals import post_save, post_delete
from  django.dispatch import receiver

class BookLending(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    book_item = models.ForeignKey(BookItem, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField()
    is_return = models.BooleanField(default=False)

@receiver(post_save, sender=BookLending)
def update_status_rack(sender, instance, created, **kwargs):
    if created:
        book_lending = instance
        book_id = book_lending.book_item.id
        book = BookItem.objects.get(pk=book_id)
        book.is_rent = True   
        book.save()

class BookReservation(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    book_item = models.ForeignKey(BookItem, on_delete=models.CASCADE)
    reservation_date = models.DateField()   
    status = models.BooleanField(default=False) 

@receiver(post_save, sender=BookReservation)
def update_status_rack(sender, instance, created, **kwargs):
    if created:
        book_reservation = instance
        book_id = book_reservation.book_item.id
        book = BookItem.objects.get(pk=book_id)
        book.is_reserve = True   
        book.save()

