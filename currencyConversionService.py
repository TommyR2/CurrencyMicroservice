import json
import time
import requests

API_KEY = ''

class CurrencyConverter:

    def __init__(self, monitor_path, response_path):
        self.monitor_path = monitor_path
        self.response_path = response_path

    def monitor_server(self):
        """Monitor the request file for changes."""

        while True:
            time.sleep(0.1)
            # Accept the current command
            with open(self.monitor_path, 'r') as request_file:
                    data = json.load(request_file)
                    if data != {}:
                        self.convert_currency(data)
                        self.cleanup_request()

    def cleanup_request(self):
        # Clean up the request JSON
        with open(self.monitor_path, 'w') as cleanup_file:
            data = {}
            json.dump(data, cleanup_file)
            

    def convert_currency(self, request_data):
        """Convert a detect value to a target value."""

        detect_currency = request_data['Detect']
        target_currency = request_data['Target']
        value = request_data['Value']

        try:
            # If the user has specified an exchange rate, use this rate
            if request_data['Override']:
                exchange_rate = request_data['Override']

            # If the exchange rate needs to be calculated, send a request
            else:
                url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{detect_currency}'
                response = requests.get(url)
                data = response.json()
                exchange_rate = data['conversion_rates'][target_currency]

                # If the target rate cannot be found, send an error response
                if not exchange_rate:
                    self.send_response(None, None, True)
                    return

            value = value * exchange_rate
            self.send_response(round(value,2), round(exchange_rate,2), False)
        except:
            # If the detect rate cannot be found, send an error response
            self.send_response(None, None, True)
            

    def send_response(self, value, conversion_rate, error):
        """Write a generated response to the currency response file."""

        response_data = {"Value": value,
                        "Conversion_rate" : conversion_rate,
                        "Error" : error}
        
        with open(self.response_path, 'w') as response_file:
            json.dump(response_data, response_file)


if __name__ == '__main__':
    currency_service = CurrencyConverter('currency_request.json', 'currency_response.json')
    currency_service.monitor_server()
