# MercadoPago
  
Module to work with MercadoPago  

*Read this in other languages: [English](Manual_MercadoPago.md), [Español](Manual_MercadoPago.es.md).*
  
![banner](imgs/Banner_MercadoPago.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Login
  
Input the access token
|Parameters|Description|example|
| --- | --- | --- |
|Access Token|MercadoPago access token|token|

### Search Payments
  
Get the ids of all payments
|Parameters|Description|example|
| --- | --- | --- |
|External Reference ID|External Reference ID of the payment|id|
|Criteria|Search criteria|criteria|
|Sort|Sort by|sort|
|Variable|Variable to store all payment ids|result|

### Get Payment
  
Get the details of a payment
|Parameters|Description|example|
| --- | --- | --- |
|Payment Id|Payment ID to search|id|
|Variable|Variable to store the payment details|result|
