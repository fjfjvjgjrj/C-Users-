from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    category =models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(default=1)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ordered by {self.customer}: {self.product} = {self.quantity}"

class Cart(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.product} ({self.quantity})"

class AdminUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username



if __name__ == "__main__":
    def crate_starter_products():
        if Product.objects.count() == 0:
            Product.objects.create(name='apple', price=50.0)
            Product.objects.create(name='orange', price=90.0)
            Product.objects.create(name='nuts', price=150.0)
            Product.objects.create(name='lemon', price=110.0)

        if Category.objects.count() == 0:
            Category.objects.create(name='fruits')
            Category.objects.create(name='vegatebles')

        if Customer.objects.count() == 0:
            Customer.objects.get_or_create(first_name='bob', last_name='smith', email='bob@mail.com')
            Customer.objects.get_or_create(first_name='ron', last_name='taylor', email='ron@mail.com')

        if Order.objects.count() == 0 and Product.objects.count() > 0 and Customer.objects.count() > 0:
            product1 = Product.objects.get(name='apple')
            customer1 = Customer.objects.get(first_name='bob')
            Order.objects.get_or_create(customer=customer1, product=product1)

        print("Created")

    crate_starter_products()