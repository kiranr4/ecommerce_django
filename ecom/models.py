from django.db import models

# Create your models here.

from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField


class Brand(models.Model):

    id = models.AutoField(verbose_name="Brand ID", primary_key=True)
    bid = ShortUUIDField(unique=True, length=7, max_length=10, alphabet="123456789", prefix="brd")
    name = models.CharField(verbose_name="Brand Name", max_length=50, unique=True)
    created_at = models.DateTimeField(verbose_name="Brand - Created Date", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Brand - Last Updated Date", auto_now=True)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Brand_detail", kwargs={"pk": self.pk})


class Category(models.Model):

    id = models.AutoField(verbose_name="Category ID", primary_key=True)
    cid = ShortUUIDField(unique=True, length=7, max_length=10, alphabet="123456789", prefix="cat")
    name = models.CharField(verbose_name="Category Name", max_length=50, unique=True)
    image = models.ImageField(verbose_name="Category Image", upload_to="img_category/", height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(verbose_name="Category - Created Date", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Category - Last Updated Date", auto_now=True)


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s%" width="50" height="50" />' %(self.image.url))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Product(models.Model):

    id = models.AutoField(verbose_name="Product ID", primary_key=True)
    pid = ShortUUIDField(unique=True, length=7, max_length=10, alphabet="123456789", prefix="pdt")
    category = models.ForeignKey(Category, verbose_name="Product Category", on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, verbose_name="Product Brand", on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(verbose_name="Product Name", max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, editable=False)
    image = models.ImageField(verbose_name="Product Image", upload_to="img_product/", height_field=None, width_field=None, max_length=None)
    description = models.TextField(verbose_name="Product Description", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="Product - Created Date", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Product - Last Updated Date", auto_now=True)
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    is_featured = models.BooleanField(verbose_name="Fetured Product", default=False)
    is_popular = models.BooleanField(verbose_name="Popular Product", default=False)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def product_image(self):
        return mark_safe('<img src="%s%" width="50" height="50" />' %(self.image.url))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})


class ProductImage(models.Model):

    images = models.ImageField(verbose_name="Product Images", upload_to="img_product/")
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Product Images - Created Date", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Product Imageas- Last Updated Date", auto_now=True)


    class Meta:
        verbose_name = "ProductImage"
        verbose_name_plural = "ProductImages"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ProductImage_detail", kwargs={"pk": self.pk})
