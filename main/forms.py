from django.forms import ModelForm
from main.models import Product

class ShopForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "quantity", "brand", "description", "thumbnail", "category", "is_featured"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)