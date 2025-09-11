from django.forms import ModelForm
from main.models import Product

class ShopForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "quantity", "brand", "description", "thumbnail", "category", "is_featured"]