# CurrencyMicroservice
Currency Conversion Microservice

**How to Programmatically REQUEST data:**

Data can be requested using the function "send_conversion_request" in the test program 'currencyRequest.py".
This function can either be imported, or copied over to your main program. A request involves writing to a JSON file that is being monitored by the currencyConversionService.

An example function call could be:
send_conversion_request('CAD', 'USD', 20, False, 'currency_request.json')
The five parameters are:
Detect Currency (str)
Taret Currency (str)
Value (float) / (The amount being converted)
Override (float or Null) / (Optionally specify a conversion rate to be used, otherwise use the service's lookup conversion rate)
file_path (str) / (The file path where the request will be written)

The written JSON data looks like this:

currency_request = {"Detect": detect_currency,
                        "Target" : target_currency,
                        "Value" : value,
                        "Override": override}


**How to Programmatically RECEIVE data:**

The currencyConversionService reads data from currency_request.json and then writes its response to currency_response.json.
As this service is running constantly, no function call is required, simply read data from the output at currency_response.json.

An example response would look like this:

{"Value": 14.43, "Conversion_rate": 0.72, "Error": false}

The data is in this format:

Value (float) / (The value of money in the Target Currency)

Conversion Rate (float) / (The conversion rate that was used by the service)

Error (boolean) / (Returns true if an error occured. Either the detect or target currency could not be found)





