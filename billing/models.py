from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES = [('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), 
                ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), 
                ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), 
                ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), 
                ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'), 
                ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), 
                ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), 
                ('WY', 'WY'), ('', '')]


class Company(models.Model):
    name = models.CharField(primary_key=True, max_length = 100)
    street_address = models.CharField(max_length = 100, default = "123 Internet Street")
    city = models.CharField(max_length = 100, default = "Downtown")
    state = models.CharField(max_length = 2, default = "CA", choices = STATE_CHOICES)
    phone = models.CharField(max_length = 10, default = "7601234567")
    email = models.EmailField(max_length = 100, default = "billing@company.com")


class BillHeader(models.Model):
    # users create the bill invoice
    # https://stackoverflow.com/questions/583327/django-model-with-2-foreign-keys-from-the-same-table
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user")
    date_created = models.DateTimeField(auto_now_add = True)
    date_submitted = models.DateTimeField(auto_now_add = False, null=True)
    #company = models.ForeignKey(Company, related_name = "company")
    company_name = models.CharField(primary_key=True, max_length = 100)
    street_address = models.CharField(max_length = 100, default = "123 Internet Street")
    city = models.CharField(max_length = 100, default = "Downtown")
    state = models.CharField(max_length = 2, default = "CA", choices = STATE_CHOICES)
    phone = models.CharField(max_length = 10, default = "7601234567")
    email = models.EmailField(max_length = 100, default = "billing@company.com")


class BillLines(models.Model):
    header = models.ForeignKey(BillHeader)
    description = models.TextField(default = "labor at $75/hour")
    quantity = models.IntegerField()
    unit_price = models.DecimalField(decimal_places = 2)
