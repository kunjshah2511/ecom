from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

import braintree
# Create your views here.

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="xzz6qv6h8prs78t2",
        public_key="cbb5pyzw2mv3pz6c",
        private_key="da156dae022646f584ea9cc7c27f3507"
    )
)


def validate_user_session(id,token):
    UserModel=get_user_model()

    try:
        user=UserModel.objects.get(pk=id)
        if user.session_token==token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def generate_token(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'error':'Invalid session, Please login again!'})
    return JsonResponse({'clientToken': gateway.client_token.generate(),'success':'True'})


@csrf_exempt
def process_payment(request,id,token):
    if not validate_user_session(id,token):
        return JsonResponse({'error':'Invalid session, Please login again!'})
    
    nonce_from_the_client=request.POST["paymentMethodNonce"]
    amount_from_the_client=request.POST["amount"]

    result=gateway.transaction.sale({
        "amount": amount_from_the_client,
        "payment_method_nonce":nonce_from_the_client,
        "options":{
            "submit_for_settlement":True
        }
    })

    if result.is_success:
        return JsonResponse({"success":result.is_success,'transaction':{'id':result.transaction.id,'anount':result.transaction.amount}})
    else:
        return JsonResponse({'error':True,'success':False})