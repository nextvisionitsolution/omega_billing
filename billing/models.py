from django.db import models
from django.utils import timezone


# CATEGORY
class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ITEM
class Item(models.Model):

    name = models.CharField(max_length=100)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    price1 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    price2 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    price3 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.name


# BILL
class Bill(models.Model):

    customer_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    shift = models.CharField(
        max_length=10
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # NEW
    is_edited = models.BooleanField(
        default=False
    )

    edited_at = models.DateTimeField(
        null=True,
        blank=True
    )


# BILL ITEMS
class BillItem(models.Model):

    bill = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    qty = models.IntegerField()

    def total(self):
        return self.qty * self.price
    
# SHIFT STATUS
class Shift(models.Model):

    SHIFT_CHOICES = (
        ('1', 'Shift 1'),
        ('2', 'Shift 2'),
    )

    active_shift = models.CharField(
        max_length=1,
        choices=SHIFT_CHOICES,
        default='1'
    )

    opened_at = models.DateTimeField(
        auto_now_add=True
    )

    closed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"Shift {self.active_shift}"
    
class EditedBillHistory(models.Model):

    bill = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )

    old_qty = models.IntegerField()

    new_qty = models.IntegerField()

    old_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    new_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    edited_at = models.DateTimeField(
        auto_now_add=True
    )