import configuration
import data
import requests

def post_new_order():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                             json=data.order_body)
    return response

def get_order_info(track_number):
    response = requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION,
                            params={"t": track_number})
    return response
