# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

import datetime
import os
import sys


base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + \
           'mercadopago' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

import mercadopago

module = GetParams("module")

global items, sdk, testkey, payments_id
items = []

if module == "login":
    try:
        testkey = GetParams("testkey")
        sdk = mercadopago.SDK(testkey)

    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "add_recipient":

    email = GetParams("email")
    name = GetParams("name")
    phone = GetParams("phone")

    try:
        customer_data = {
            "email": email,
            "phone": phone,
            "description": name
        }
        customer_response = sdk.customer().create(customer_data)
        customer = customer_response["response"]

    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "add_item":

    amount = GetParams("amount")
    quantity = GetParams("quantity")
    item = GetParams("item")
    amount = int(amount)

    try:
        temp = {"title": item, "quantity": quantity, "unit_price": amount}
        items.append(temp)
        print(items)
    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "create_invoice":

    total = GetParams("total")
    payment_name = GetParams("payment_name")
    payment_method = GetParams("payment_method")
    email = GetParams("email")
    total = int(total)
    try:
        preference_data = {
            "items": items
        }

        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]

        payment_data = {
            "transaction_amount": total,
            "description": payment_name,
            "payment_method_id": payment_method,
            "payer": {
                "email": email
            }
        }

        payment_response = sdk.payment().create(payment_data)
        payment = payment_response["response"]
        print(payment)
    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "get_invoice":
    id = GetParams("id")
    var = GetParams("var")
    try:
        auth = 'Bearer ' + testkey
        headers = {
            'Authorization': auth,
        }
        url = 'https://api.mercadopago.com/v1/payments/' + id
        response = requests.get(url, headers=headers)
        resp = response.json()
        SetVar(var, resp)

    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "search_payments":
    id = GetParams("id")
    criteria = GetParams("criteria")
    sort = GetParams("sort")
    var = GetParams("var")

    try:
        if id is None:
            id = ""
        if not criteria:
            criteria = "desc"
        if not sort:
            sort = "date_created"

        auth = 'Bearer ' + testkey
        headers = {
            'Authorization': auth,
        }
        url = "https://api.mercadopago.com/v1/payments/search?sort=" + sort + "&criteria=" + criteria + "&external_reference=" + id
        response = requests.get(url, headers=headers)
        res = response.json()

        payments_id = [result["id"] for result in res["results"]]
        SetVar(var, payments_id)
    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e
































"""{
      "en": {
        "title": "Create Invoice",
        "description": "Create an invoice for the customer",
        "title_options": null,
        "options": null
      },
      "es": {
        "title": "Crear factura",
        "description": "Crea una factura para el cliente",
        "title_options": null,
        "options": null
      },
      "form": {
        "css": "modal-lg",
        "inputs": [
          {
            "type": "input",
            "placeholder": {
              "es": " ",
              "en": " "
            },
            "title": {
              "es": "Total:",
              "en": "Total:"
            },
            "help": {
              "es": " ",
              "en": " "
            },
            "id": "total",
            "css": "col-lg-6"
          },
          {
            "type": "input",
            "placeholder": {
              "es": " ",
              "en": " "
            },
            "title": {
              "es": "Nombre de pago",
              "en": "Payment Name:"
            },
            "help": {
              "es": " ",
              "en": " "
            },
            "id": "payment_name",
            "css": "col-lg-6"
          },
          {
            "type": "select",
            "placeholder": {
              "es": " ",
              "en": " "
            },
            "title": {
              "es": "Método de pago",
              "en": "Payment Method:"
            },
            "options": [
              {
                "title": "credit card",
                "value": "credit_card"
              },
              {
                "title": "debit card",
                "value": "debit_card"
              }
            ],
            "help": {
              "es": " ",
              "en": " "
            },
            "id": "payment_method",
            "css": "col-lg-6"
          },
          {
            "type": "input",
            "placeholder": {
              "es": " ",
              "en": " "
            },
            "title": {
              "es": "Correo electrónico:",
              "en": "Email:"
            },
            "help": {
              "es": " ",
              "en": " "
            },
            "id": "email",
            "css": "col-lg-6"
          }
        ]
      },
      "video_youtube": "",
      "icon": "data:image/png;base64,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",
      "module": "create_invoice",
      "module_name": "MercadoPago",
      "visible": true,
      "options": false,
      "father": "module",
      "group": "scripts",
      "linux": true,
      "windows": true,
      "mac": true,
      "docker": true
    },
    {
      "en": {
        "title": "Add Item",
        "description": "Add an item to the invoice",
        "title_options": null,
        "options": null
      },
      "es": {
        "title": "Añadir artículo",
        "description": "Agregar un artículo a la factura\n",
        "title_options": null,
        "options": null
      },
      "form": {
        "css": "modal-lg",
        "inputs": [
          {
            "type": "input",
            "placeholder": {
              "es": " ",
              "en": " "
            },
            "title": {
              "es": "Nombre del árticulo",
              "en": "Item Name:"
            },
            "help": {
              "es": " ",
              "en": " "
            },
            "id": "item",
            "css": "col-lg-6"
          },
          {
            "type": "input",
            "placeholder": {
              "es": " ",
              "en": " "
            },
            "title": {
              "es": "Precio:",
              "en": "Price:"
            },
            "help": {
              "es": " ",
              "en": " "
            },
            "id": "amount",
            "css": "col-lg-6"
          },
          {
            "type": "input",
            "placeholder": {
              "es": " ",
              "en": " "
            },
            "title": {
              "es": "Cantidad:",
              "en": "Quantity:"
            },
            "help": {
              "es": " ",
              "en": " "
            },
            "id": "quantity",
            "css": "col-lg-6"
          }
        ]
      },
      "video_youtube": "",
      "icon": "data:image/png;base64,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",
      "module": "add_item",
      "module_name": "MercadoPago",
      "visible": true,
      "options": false,
      "father": "module",
      "group": "scripts",
      "linux": true,
      "windows": true,
      "mac": true,
      "docker": true
    },
        {
      "en": {
        "title": "Add Customer",
        "description": "Add a recipient to the invoice",
        "title_options": null,
        "options": null
      },
      "es": {
        "title": " ",
        "description": " ",
        "title_options": null,
        "options": null
      },
      "form": {
        "css": "modal-lg",
        "inputs": [
          {
            "type": "input",
            "placeholder": {
              "es": " ",
              "en": " "
            },
            "title": {
              "es": "Nombre del cliente",
              "en": "Customer Name:"
            },
            "help": {
              "es": " ",
              "en": " "
            },
            "id": "name",
            "css": "col-lg-6"
          },
          {
            "type": "input",
            "placeholder": {
              "es": " ",
              "en": " "
            },
            "title": {
              "es": "Correo electrónico:",
              "en": "Email:"
            },
            "help": {
              "es": " ",
              "en": " "
            },
            "id": "email",
            "css": "col-lg-6"
          },
          {
            "type": "input",
            "placeholder": {
              "es": " ",
              "en": " "
            },
            "title": {
              "es": "Teléfono:",
              "en": "Phone:"
            },
            "help": {
              "es": " ",
              "en": " "
            },
            "id": "phone",
            "css": "col-lg-6"
          }
        ]
      },
      "video_youtube": "",
      "icon": "data:image/png;base64,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",
      "module": "add_recipient",
      "module_name": "MercadoPago",
      "visible": true,
      "options": false,
      "father": "module",
      "group": "scripts",
      "linux": true,
      "windows": true,
      "mac": true,
      "docker": true
    }"""