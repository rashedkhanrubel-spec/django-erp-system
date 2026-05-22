from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    reorder_level = models.IntegerField(default=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sku} - {self.name}"

    @property
    def total_stock(self):
        return self.stock_items.aggregate(
            total=models.Sum("quantity")
        )["total"] or 0

    @property
    def is_low_stock(self):
        return self.total_stock <= self.reorder_level

class StockItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stock_items")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("product", "warehouse")

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("confirmed", "Confirmed"),
        ("received", "Received"),
        ("cancelled", "Cancelled"),
    ]
    reference = models.CharField(max_length=100, unique=True)
    supplier = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    expected_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.reference

