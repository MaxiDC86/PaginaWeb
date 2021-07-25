from django.shortcuts import render
import mercadopago
sdk = mercadopago.SDK("TEST-1682191286570055-072420-081eaf21dbcddd9e349e4e05abdcad98-97637851")

# Create your views here.
def process_payment(request):

    if request.method =="POST":
        # Create a preference item
        preference_data = {
        "items": [
        {
            "title": "My Item",
            "quantity": 1,
            "unit_price": 75.76
            }
        ]
        }

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]


    return render(preference)