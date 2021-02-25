import string, random
from urllib.parse import urlparse
import os
from .models import Mainurl

#function to generate a unique character to shorten the url
def generate_encode():
    text = [''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range(6)])]
    random.shuffle(text)
    sub_url = ''.join(text)
    return sub_url


def shorten_url(host, url_):
    original_url = str(url_)

    if urlparse(original_url).scheme == '':
        original_url = "http://"+original_url

    else:
        original_url = original_url


    encoded_path = ''

    exist = True

    while exist:

        url_path = generate_encode()

        try:
            response = Mainurl.objects.get(encoded=str(url_path))

            print(response)

            if response:
                exist = True

        except:
            encoded_path = url_path
            print(url_path)
            exist = False

    url_data = {
        "encoded": encoded_path,
        "original_url": original_url
    }


    return url_data