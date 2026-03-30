# Importing libraries
import time
import hashlib
import ssl
from urllib.request import urlopen, Request

# setting the URL you want to monitor
url = Request('https://en.wikipedia.org/wiki/Main_Page', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url, context=ctx).read()

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("running")
time.sleep(10)

while True:
    try:
        # perform the get request and store it in a var
        response = urlopen(url, context=ctx).read()
        # create a hash
        currentHash = hashlib.sha224(response).hexdigest()
        # wait for 30 seconds
        time.sleep(30)
        # perform the get request
        response = urlopen(url, context=ctx).read()
        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()
        # check if new hash is same as the previous hash
        if newHash == currentHash:
            continue
        # if something changed in the hashes
        else:
            # notify
            print("something changed")
            # again read the website
            response = urlopen(url, context=ctx).read()
            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()
            # wait for 30 seconds
            time.sleep(30)
            continue
    # To handle exceptions
    except Exception as e:
        print("error")