import json

def send_conversion_request(detect_currency, target_currency, value, override, file_path):
    """
    Send a currency conversion request.
    Params: Detect Currency (str)
            Target Currency (str)
            Value (float)
            Override (float) or (Null) Float will override the conversion service to use a specified conversion rate
    """

    currency_request = {"Detect": detect_currency,
                        "Target" : target_currency,
                        "Value" : value,
                        "Override": override}
    
    with open(file_path, 'w') as file:
        json.dump(currency_request, file)


send_conversion_request('CAD', 'USD', 20, False, 'currency_request.json')

