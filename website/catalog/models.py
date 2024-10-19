from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .utils import product_images_directory_path, seller_image_directory_path


class Category(models.Model):
    """
    Модель категории товара
    name: название категории
    icon: иконка категории
    archived: статус архива категории
    parent_category: ссылка на родительскую категорию (если значение не NULL, то это подкатегория категории)
    """

    class Meta:
        verbose_name_plural = "categories"
        ordering = ("name",)

    name = models.CharField(max_length=100, verbose_name=_("Name"))
    icon = models.FileField(
        upload_to="assets/img/icons/departments", verbose_name=_("Icon")
    )
    archived = models.BooleanField(default=False, verbose_name=_("Archived status"))
    parent_category = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sub_categories",
        verbose_name=_("PK category"),
    )


class Product(models.Model):
    """
    Модель товара
    name: имя товара
    description: описание товара
    manufacture: производитель товара
    created_at: когда создан товар
    category: категория товара (Category)
    archived: статус архива товара
    limited_edition: статус ограниченности предложения товара
    view: статус просмотра товара
    """

    name = models.CharField(max_length=100, db_index=True, verbose_name=_("Name"))
    description = models.TextField(
        null=True, blank=True, db_index=True, verbose_name=_("Description")
    )

    manufacture = models.CharField(
        max_length=100, db_index=True, verbose_name=_("Manufacture")
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("'Created at"))
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_("PK category"),
        related_name="products",
    )
    archived = models.BooleanField(default=False, verbose_name=_("Archived status"))
    limited_edition = models.BooleanField(
        default=False, verbose_name=_("Limited edition")
    )
    view = models.BooleanField(default=False, verbose_name=_("View"))

    def __str__(self) -> str:
        return f"Product(id={self.pk}, name={self.name!r})"


class ProductImage(models.Model):
    """
    Модель изображения товара
    product: ссылка на товар к которому относится фотография (Product)
    image: изображение товара
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_("PK product")
    )
    image = models.ImageField(
        upload_to=product_images_directory_path, verbose_name=_("Image product")
    )


class Seller(models.Model):
    """
    Модель продавца
    name: название продавца
    description: описание продавца
    image: изображение (если есть) продавца
    phone: телефон продавца
    address: адрес продавца
    email: адрес электронной почты продавца
    created_at: когда создан продавец
    archived: статус архива продавца

    """

    name = models.CharField(max_length=100, db_index=True, verbose_name=_("Name"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    image = models.ImageField(upload_to=seller_image_directory_path, null=True, blank=True, verbose_name=_("Image"))
    phone = models.CharField(max_length=15, null=False, verbose_name=_("Phone"))
    address = models.TextField(null=True, blank=True, verbose_name=_("Address"))
    email = models.EmailField(max_length=100, verbose_name=_("Email"))
    products = models.ManyToManyField(
        "Product",
        blank=True,
        through="Storage",
        related_name="sellers",
        verbose_name=_("Products")
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    archived = models.BooleanField(default=False, verbose_name=_("Archived status"))

    def __str__(self) -> str:
        return f"Seller(id={self.pk}, name={self.name!r})"


class Storage(models.Model):
    """
        Модель склада
        seller: название продавца
        product: название продукта
        quantity: доступное количество
        price: цена
        created_at: дата создания записи

        """
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="storage", verbose_name=_("Seller"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="storage", verbose_name=_("Product"))
    quantity = models.PositiveIntegerField(default=0, verbose_name=_("Quantity"))
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name=_("Price"))
    created_at = models.DateField(auto_now_add=True, verbose_name=_("Created at"), null=True)

    def __str__(self):
        return f"Storage(product={self.product}, seller={self.seller})"


class Review(models.Model):
    """
    Модель отзыва
    product: товар к которому относится данный отзыв
    user: пользователь, который оставил отзыв #TODO после создания модели CustomUser заменить связанную
    text: текст отзыва
    created_at: время создания отзыва (создается автоматически)
    """

    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, verbose_name=_("Product")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    text = models.TextField(verbose_name=_("Text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))


class NameSpecification(models.Model):
    """
    Модель названия характеристики
    name: название характеристики
    """

    name = models.CharField(
        max_length=100, db_index=True, verbose_name=_("Name specification")
    )


class Specification(models.Model):
    """
    Модуль характеристики
    value: значение характеристики
    specification: название характеристики
    product: товар к которому относится данная характеристика
    """

    value = models.DecimalField(
        default=0,
        max_digits=2,
        decimal_places=2,
        verbose_name=_("Value specification"),
    )
    name = models.ForeignKey(
        NameSpecification,
        on_delete=models.CASCADE,
        verbose_name=_("Name specification"),
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name=_("PK Product")
    )

