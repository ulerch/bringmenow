from django.db import models
from bringmenow import utils


class Supplier (models.Model):
    class RecieveOrders(utils.ChoiceEnum):
        SMS = 'SMS'
        MAIL = 'Email'
        WEB = 'Web'

    user_name = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    business_name = models.CharField(max_length=40, null=False, blank=False)
    contact_name = models.CharField(max_length=40, null=False, blank=False)
    street = models.CharField(max_length=40, null=False, blank=False)
    plz = models.CharField(max_length=5)
    location = models.CharField(max_length=20, null=False, blank=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    email = models.EmailField(max_length=100, null=False, blank=False)
    contact_phone = models.PositiveIntegerField(null=False, blank=False)
    contact_mobile = models.PositiveIntegerField(null=False, blank=False)
    recieve_orders = models.CharField(max_length=10, choices=RecieveOrders.choices(), default=RecieveOrders.SMS.name)
    bank_account = models.CharField(max_length=20, null=False, blank=False)
    logo = models.ImageField(upload_to='logos/', null=False, blank=False)


    class Meta(object):
        ordering = ['business_name']
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return "{}, {}".format(self.business_name, self.location)


class Product (models.Model):
    class Category(utils.ChoiceEnum):
        FRUITS = 'Fruits'
        VEGETABLES = 'Vegetables'
        MILK = 'Milch'
        MEAT = 'Meat'
        FISH = 'Fish'
        BAKED = 'Baked Goods'
        BEVERAGES = 'Beverages'
        ALCOHOL = 'Alcohol'
        OTHERS = 'Others'

    supplier = models.ForeignKey(Supplier, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=False, blank=False)
    category = models.CharField(max_length=20, choices=Category.choices(), default=Category.OTHERS.name)
    image = models.ImageField(upload_to='products/', null=False, blank=False)
    vegan = models.BooleanField(default=False)
    glutenfree = models.BooleanField(default=False)
    nutfree = models.BooleanField(default=False)
    unit = models.PositiveIntegerField(null=False, blank=False)
    price = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    stock = models.PositiveIntegerField(null=False, blank=False)
    reduction = models.PositiveIntegerField(null=False, blank=False)

    class Meta(object):
        ordering = ['category', 'name']
        verbose_name = 'Products'
        verbose_name_plural = 'Products'

    def __str__(self):
        return "{}, {}".format(self.category, self.name)


class Customer (models.Model):
    user_name = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=40, null=False, blank=False)
    street = models.CharField(max_length=40, null=False, blank=False)
    plz = models.CharField(max_length=5)
    location = models.CharField(max_length=20, null=False, blank=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    email = models.EmailField(max_length=100, null=False, blank=False)
    contact_phone = models.PositiveIntegerField(null=False, blank=False)
    contact_mobile = models.PositiveIntegerField(null=False, blank=False)

    class Meta(object):
        ordering = ['name']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return "{}, {}".format(self.name, self.location)


class Deliverer (models.Model):
    user_name = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=40, null=False, blank=False)
    street = models.CharField(max_length=40, null=False, blank=False)
    plz = models.CharField(max_length=5)
    location = models.CharField(max_length=20, null=False, blank=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    email = models.EmailField(max_length=100, null=False, blank=False)
    contact_phone = models.PositiveIntegerField(null=False, blank=False)
    contact_mobile = models.PositiveIntegerField(null=False, blank=False)

    class Meta(object):
        ordering = ['name']
        verbose_name = 'Deliverer'
        verbose_name_plural = 'Deliverers'

    def __str__(self):
        return "{}, {}".format(self.name, self.location)


class Order (models.Model):
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, null=False, on_delete=models.CASCADE)
    deliverer = models.ForeignKey(Deliverer, null=True, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True, editable=False, null=False, blank=False)
    delivery_date_planned = models.DateTimeField(null=False, blank=False)
    delivery_date_executed = models.DateTimeField(null=True, blank=True)
    total = models.DecimalField(blank=False, null=False, max_digits=6, decimal_places=2)

    class Meta(object):
        ordering = ['customer', 'order_date']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return "{}, {}".format(self.customer.name, self.order_date)


class OrderItem (models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    units_planned = models.PositiveIntegerField(null=False, blank=False)
    units_executed = models.PositiveIntegerField(null=False, blank=False)
    price_unit = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    price_total = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)

    class Meta(object):
        ordering = ['order', 'product']
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return "{}, {}".format(self.oder.pk, self.product_name)
