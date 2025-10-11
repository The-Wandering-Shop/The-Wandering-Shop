from django.db import models

from django.utils.text import slugify

class Category(models.Model):
    """Lets you create categories for products, like Toys or Clothes."""

    # Input for the category name, maximum length 255 characters
    name = models.CharField(max_length=255)

    slug = models.SlugField(unique=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('name',) # Orders the catergories alphabetically
        verbose_name_plural = 'Categories'  #Displays plural name correctly in Django admin site

    def __str__(self):
        return self.name # Fixes string representataion problem and shows the catergory name in Django admin site instead of Catergory object(1)


class Product(models.Model):
    """Lets you create and manage products."""
    # Lets you choose which catergory the product belongs in 
    # related_name='products' : makes it easy to get all of the products belonging to a catergory
    # on_delete=models.CASCADE: if a category is deleted, all the products belonging to a catergory is also deleted
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)

    # Input for product name
    name = models.CharField(max_length=255)

    slug = models.SlugField(unique=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('name', 'category')

    # Input for product description 
    description = models.TextField(blank=True, null=True)

    # Input for product price
    price = models.FloatField()

    # Input for image (Lets you add an image)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    # This allwos admin to put in stock quantity
    quantity = models.PositiveIntegerField(default=1)
    
    # Checkbox this is for new items of stock
    is_new = models.BooleanField(default=False)

    # Automatically records date and time when the product was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name # Fixes string representataion problem and shows the product name in Django admin site instead of product object(1)


class ProductDetail(models.Model):
    """This allows unlimited detail per product"""
    product = models.ForeignKey(Product, related_name='details', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.label}: {self.value}"



RATING_CHOICES = [
    (1, "⭐"),
    (2, "⭐⭐"),
    (3, "⭐⭐⭐"),
    (4, "⭐⭐⭐⭐"),
    (5, "⭐⭐⭐⭐⭐"),
]


class Reviews(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(Product,related_name='reviews',on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)

    class Meta:
        verbose_name_plural = 'Product Reviews'  #Displays plural name correctly in Django admin site

    def __str__(self):
        return self.name
