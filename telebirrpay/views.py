from django.shortcuts import render, redirect

import base64
import time
import json
import math
import requests
import rsa
import six
import random
import string
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from hashlib import sha256
from urllib3.exceptions import *
from datetime import datetime


from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import logging
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.http import HttpResponseRedirect
from .models import PaymentNotification
from decouple import config
from orders.models import Order
from django.contrib.auth import get_user_model
from users.models import CustomUser
from rewardpay.models import RewardRate

# Define a logger
logger = logging.getLogger(__name__)

# from carts.views import clear_cart

def payment_page(request):
    return render(request, 'payment_page.html')
@csrf_exempt
def payment_notification(request):
    if request.method == 'POST':
        # print(request.POST) 
        # Extract the encrypted data from the request
        encrypted_data = request.body.decode('utf-8')
        print("encrypted data",encrypted_data)
        if not encrypted_data:
            return JsonResponse({"error": "Invalid request"}, status=400)

        # Initialize TelebirrWeb with your details
        telebirr = TelebirrWeb(
            appId=config('TELEBIRR_APP_ID'), 
            appKey=config('TELEBIRR_APP_KEY'), 
            shortCode=config('TELEBIRR_SHORT_CODE'),
            publicKey=config('TELEBIRR_PUBLIC_KEY'), 
            receiveName=config('TELEBIRR_RECEIVE_NAME')
        )

        # Decrypt the data using the TelebirrWeb instance
        try:
            decrypted_data = telebirr.get_decrypt_data(encrypted_data)
            print("decrypted data",decrypted_data)

            msisdn = decrypted_data.get('msisdn')
            out_trade_no = decrypted_data.get('outTradeNo')
            total_amount = float(decrypted_data.get('totalAmount'))
            trade_date = datetime.fromtimestamp(int(decrypted_data.get('tradeDate')) / 1000)
            trade_no = decrypted_data.get('tradeNo')
            trade_status = decrypted_data.get('tradeStatus')
            transaction_no = decrypted_data.get('transactionNo')
         
            # Create a new instance of the PaymentNotification model
            payment_notification = PaymentNotification.objects.create(
                msisdn=msisdn,
                out_trade_no=out_trade_no,
                total_amount=total_amount,
                trade_date=trade_date,
                trade_no=trade_no,
                trade_status=trade_status,
                transaction_no=transaction_no
            )
            # Save the instance to the database
            payment_notification.save()

            try:
                order = Order.objects.get(outTradeNo=out_trade_no)
            except Order.DoesNotExist:
                return JsonResponse({"error": "Order does not exist"}, status=404)
            # Update the phone number
            order.order_phone = msisdn
            order.transaction_no = transaction_no
            if  trade_status == 2:
                order.payment_status = True
            if order.referral_code:
                try:
                    user = CustomUser.objects.get(referral_code=order.referral_code)
                    reward_rate = RewardRate.objects.first()
                    get_point = total_amount * reward_rate.referral_rate
                    user.point_reward += get_point
                    user.save()

                    user = CustomUser.objects.get(email=order.user.email)
                    get_point = total_amount * reward_rate.user_referral_rate
                    user.point_reward += get_point
                    user.save()
                except CustomUser.DoesNotExist:
                    pass

            order.save()

            # Update the user point reward
            try:
                user = CustomUser.objects.get(email=order.user.email)
                get_point = total_amount * reward_rate.user_rate
                user.point_reward += get_point
                user.save()
            except CustomUser.DoesNotExist: 
                pass
            
            
              # Clear the cart
            # clear_cart(request)


            return JsonResponse({"message": "Payment notification processed successfully"}, status=200)
        except Exception as e:
            return JsonResponse({"error": "Failed to decrypt data"}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)

class MakePaymentView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'cart.html')

    def post(self, request, *args, **kwargs):
        print("payment view recived POST request")  
        print("Received form data:", request.POST)
     
        try:
            order = Order.objects.filter(user=request.user, payment_status=False).latest('order_date')
            # Use the totalAmount and outTradeNo from the order
            totalAmount = float(order.order_total_prices)
            print("order outTradeNoooooooooooo",order.outTradeNo)
            outTradeNo = order.outTradeNo

            subject = config('SUBJECT')
            print('totalAmount',totalAmount)
            nonce = str(int(time.time() * 1000)) + ''.join(random.choices(string.ascii_lowercase, k=3))
            # outTradeNo = str(int(time.time() * 1000)) + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            notifyUrl = config('NOTIFY_URL')
            returnUrl = config('RETURN_URL')
            print('notifyUrl',notifyUrl)
            print('returnUrl',returnUrl)
            print('outTradeNo',outTradeNo)
            print('nonce',nonce)
         
            telebirr = TelebirrWeb(
                appId=config('TELEBIRR_APP_ID'), 
                appKey=config('TELEBIRR_APP_KEY'), 
                shortCode=config('TELEBIRR_SHORT_CODE'),
                publicKey=config('TELEBIRR_PUBLIC_KEY'), 
                receiveName=config('TELEBIRR_RECEIVE_NAME')
            )
            # Send the payment request to Telebirr
            response = telebirr.send_request(subject, totalAmount, nonce, outTradeNo, notifyUrl, returnUrl)
            print('Response from Telebirr APIi', response)
            
            if response.get('code') == 200 and 'data' in response and 'toPayUrl' in response['data']:
                # Redirect the user to the Telebirr H5 Web Payment URL
                # return redirect(response['data']['toPayUrl'])
                # return HttpResponseRedirect(response['data']['toPayUrl'])
                return JsonResponse({"toPayUrl": response['data']['toPayUrl']})
            else:
                return JsonResponse({"error": "An error occurred during payment processing"}, status=500)

        except Exception as e:
            logger.error(f"Error occurred during payment processing: {e}")
            return JsonResponse({"error": "An error occurred during payment processing"}, status=500)

    
class DecryptByPublicKey(object):
    """
         the modulus factor is generated first 
         the rsa public key is then generated 
         then use the rsa public key to decrypt the incoming encryption str
    """
    def __init__(self, publicKey):
        public_key =  RSA.import_key(base64.urlsafe_b64decode(publicKey))
        self._modulus = public_key.n   
        self._exponent = public_key.e 
        try:
            rsa_pubkey = rsa.PublicKey(self._modulus, self._exponent)
            self._pub_rsa_key = rsa_pubkey.save_pkcs1() 
        except Exception as e:
            raise TypeError(e)

    def decrypt(self, b64decoded_encrypt_text) ->str:
        """
        decrypt msg by public key
        """
        public_key = rsa.PublicKey.load_pkcs1(self._pub_rsa_key)
        encrypted = rsa.transform.bytes2int(b64decoded_encrypt_text)
        decrypted = rsa.core.decrypt_int(encrypted, public_key.e, public_key.n)

        decrypted_bytes = rsa.transform.int2bytes(decrypted)
        if len(decrypted_bytes) > 0 and list(six.iterbytes(decrypted_bytes))[0] == 1:
            try:
                raw_info = decrypted_bytes[decrypted_bytes.find(b'\x00')+1:]
            except Exception as e:
                raise TypeError(e)
        else:
            raw_info = decrypted_bytes
        return raw_info.decode("utf-8")


class TelebirrWeb:
    def __init__(self, appId, appKey, shortCode, publicKey, receiveName) -> None:
        self.appId = appId
        self.appKey = appKey
        self.shortCode = shortCode
        self.publicKey = publicKey
        self.receiveName = receiveName
        self.url = "https://app.ethiomobilemoney.et:2121/ammapi/payment/service-openup/toTradeWebPay"
        print("Public Key:", publicKey)
    def send_request(self, subject, totalAmount, nonce, outTradeNo, notifyUrl, returnUrl=None):
        
        if totalAmount <= 0:
            raise TypeError("amount must be greater than 0.")

        timeoutExpress = 10
        timestamp = int(time.time() * 1000)
        
        stringA = f"appId={self.appId}&appKey={self.appKey}&nonce={nonce}&notifyUrl={notifyUrl}&outTradeNo={outTradeNo}&receiveName={self.receiveName}&returnUrl={returnUrl}&shortCode={self.shortCode}&subject={subject}&timeoutExpress={timeoutExpress}&timestamp={timestamp}&totalAmount={totalAmount}"
        logger.info(f"Constructed stringA: {stringA}")
        print('Constructed stringA:', stringA)

        ussdjson = {
            "appId":self.appId,
            "nonce":nonce,   
            "notifyUrl":notifyUrl,
            "outTradeNo":outTradeNo,
            "receiveName":self.receiveName,
            "returnUrl":returnUrl,
            "shortCode":self.shortCode,
            "subject":subject,
            "timeoutExpress":timeoutExpress,
            "timestamp":timestamp,
            "totalAmount":totalAmount,
        }
        logging.info(f"Shortcode value: {self.shortCode}")
        ussdjson = json.dumps(ussdjson).encode('utf-8')
        # Print the data before encryption
        print(f"data before encryption: {ussdjson}")
        public_key = RSA.import_key(base64.urlsafe_b64decode(self.publicKey))
        print('Public Keyyyyyyyyyyyyyyyyy:', public_key)
        encryptor = PKCS1_v1_5.new(public_key)

        maxEncryptSize = 245
        bufferSize = len(ussdjson)
        buffersCount = int(math.ceil(bufferSize / maxEncryptSize)) 
        dividedSize = int(math.ceil(bufferSize / buffersCount)) 

        try:
            result = []
            for bufNum in range(buffersCount):
                decrypted_cipher = encryptor.encrypt(ussdjson[bufNum * dividedSize: (bufNum + 1) * dividedSize])
                result.append(decrypted_cipher)
            encrypted_decode = b"".join(result)
            encrypted_encode = base64.b64encode(encrypted_decode)
            encrypted = str(encrypted_encode, "utf-8")
            print('Encrypted data:', encrypted)
        except Exception as e:
            print("Error during encryption:", e)
            raise TypeError(e)
        print('Encrypted data length:', len(encrypted))
        stringB = sha256(stringA.encode()).hexdigest().upper()
        print('StringB value:', stringB)
        data = {"appid": self.appId, "sign": stringB, "ussd": encrypted}
        print('data',data)
        headers = {
            "Content-Type": "application/json;charset=utf-8",
        }
        timeout = 30

        try:
            response = requests.post(url=self.url, json=data, headers=headers, timeout=timeout)
        except requests.exceptions.Timeout as e:
            raise e

        if not response.ok:
            raise TypeError("Telebirr Transaction Failed")

        response = response.json()
        logger.info(f"Received response from Telebirr API: {response}")

        return response
    

    def get_decrypt_data(self, data):
        try:
            data = base64.b64decode(data)
            print('Received encrypted data:', data)
        except Exception as e:
            raise TypeError(e)

        decryptor = DecryptByPublicKey(self.publicKey)
        maxEncryptSize = 256
        bufferSize = len(data)
        buffersCount = int(math.ceil(bufferSize / maxEncryptSize)) 
        dividedSize = int(math.ceil(bufferSize / buffersCount)) 
        result = []

        try:
            for bufNum in range(buffersCount):
                encrypted_text = decryptor.decrypt(data[bufNum * dividedSize: (bufNum + 1) * dividedSize])
                result.append(encrypted_text)
            message = "".join(result)
        except Exception as e:
            raise TypeError(e)
        
        response = json.loads(message)
        
        if response:
            return response
        else:
            raise TypeError("Invalid response")




