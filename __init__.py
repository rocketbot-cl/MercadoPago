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
        auth = 'Bearer' + testkey
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

    try:
        auth = 'Bearer' + testkey
        headers = {
            'Authorization': auth,
        }
        url = "https://api.mercadopago.com/v1/payments/search?sort=" + sort + "&criteria=" + criteria + "&external_reference=" + id
        response = requests.get(url, headers=headers)
        res = response.json()
        payments_id = [result["id"] for result in res["results"]
    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "get_payment":
    id = GetParams("id")

    try:
        auth = 'Bearer' + testkey
        headers = {
            'Authorization': auth,
        }
        url = "https://api.mercadopago.com/v1/payments/" + id
        reponse = requests.get(url, headers=headers)
    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e