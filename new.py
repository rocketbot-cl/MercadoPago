import mercadopago
import requests

sdk = mercadopago.SDK("TEST-7480524387124622-071417-8975c181b9dcaba1fd2a3999b8ecb4ff-386738209")


customer_data = {
  "email": "test@test.com"
}
customer_response = sdk.customer().create(customer_data)
customer = customer_response["response"]
print(customer)

card_data = {
  "token": "9b2d63e00d66a8c721607214cedaecda",
  "issuer_id": "3245612",
  "payment_method_id": "debit_card"
}
card_response = sdk.card().create(customer["id"], card_data)
card = card_response["response"]

preference_data = {
    "items": [
        {
            "title": "My Item",
            "quantity": 1,
            "unit_price": 75
        }
    ]
}

preference_response = sdk.preference().create(preference_data)
preference = preference_response["response"]
print(preference)
collector_id = preference["collector_id"]
client_id = preference["client_id"]
id = preference["id"]


payment_data = {
    "transaction_amount": 100,
    "description": "Product Title",
    "payment_method_id": "credit_card",
    "payer": {
        "email": "test_user_15748052@testuser.com"
    }
}

payment_response = sdk.payment().create(payment_data)
payment = payment_response["response"]
print(payment)