from django.shortcuts import render
from .models import Users
from apiUtils.views import (
    badRequestResponse,
    unAuthorizedResponse, 
    unAuthenticatedResponse, 
    resourceConflictResponse, 
    resourceNotFoundResponse, 
    internalServerErrorResponse, 
    successResponse
)
import json
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def getUserByPhoneNumber(phoneNumber):
    try:
        user = Users.objects.get(phoneNumber=phoneNumber)
        return user

    except Users.DoesNotExist as e:
        logger.error("getUserByPhoneNumber@Error")
        logger.error(e)
        return None


def main(request):
    body = request.POST

    session_id   = body.get("sessionId", None)
    serviceCode  = body.get("serviceCode", None)
    phone_number = body.get("phoneNumber", None)
    text         = body.get("text", "default")


    if text == '':
        response = "CON Welcome to FarmLink \n"
        response += "What would you like us to help you do? \n"
        response += "1. BUY\n"
        response += "2. SELL\n"

    elif text == '1':
        # check if phone number is registered
        # user = getUserByPhoneNumber(phone_number)
        
        # if user == None:
        #     # response = "CON Your number is not registered with FarmLink \n"
        #     # response += "Would you like to register in order to buy?"
        #     # response += "11. YES"
        #     # response += "22. NO"
        #     pass
        
        # else:
        response = "CON What crop are you buying? \n"
        response += "1. YAM"
        response += "2. BEANS"
        response += "3. CASSAVA"
        response += "4. PAWPAW"
        response += "5. WATERMELON"
        response += "6. Next"
        response += "0. Back"
        response += "00. Main Menu"
    
    # elif text in ['1*1', '1*2', '1*3', '1*4', '1*5']:
    #     response = "CON What is the Quantity you would like to buy ?"
    #     response += ""

    # elif text == "1*11":
    #     response += "CON "

    elif text == '1*6':
        response = "CON What crop are you buying? \n"
        response += "1. CASHEW"
        response += "2. CUCUMBER"
        response += "3. ORANGE"
        response += "4. MANGO"
        response += "0. Back"
        response += "00. Main Menu"

    elif text == '1*6*0':
        response = "CON What crop are you buying? \n"
        response += "1. YAM"
        response += "2. BEANS"
        response += "3. CASSAVA"
        response += "4. PAWPAW"
        response += "5. WATERMELON"
        response += "6. Next"
        response += "0. Back"
        response += "00. Main Menu"

    elif text == '1*6*0*0' or text == '1*6*00' or text == '1*0*00':
        response = "CON Welcome to FarmLink \n"
        response += "What would you like us to help you do?"
        response += "1. BUY"
        response += "2. SELL"

    elif text in ['1*1', '1*2', '1*3', '1*4', '1*5', '1*6*1', '1*6*2', '1*6*3', '1*6*4', '1*6*5']:
        response = "END Your order has been received. \n"
        response += "One of FarmLink agent will reach out to you shortly."
        response += "Thanks."

    elif text == '2':
        response += "1. YAM"
        response += "2. BEANS"
        response += "3. CASSAVA"
        response += "4. PAWPAW"
        response += "5. WATERMELON"
        response += "6. Next"
        response += "0. Back"
        response += "00. Main Menu"

    elif text == '2*6':
        response == "CON What crop are selling?"
        response += "1. CASHEW"
        response += "2. CUCUMBER"
        response += "3. ORANGE"
        response += "4. MANGO"
        response += "0. Back"
        response += "00. Main Menu"

    elif text == '2*0':
        response += "1. YAM"
        response += "2. BEANS"
        response += "3. CASSAVA"
        response += "4. PAWPAW"
        response += "5. WATERMELON"
        response += "6. Next"
        response += "0. Back"
        response += "00. Main Menu"

    elif text == '2*6*0*0' or text == '2*6*00' or text == '2*0*00':
        response = "CON Welcome to FarmLink \n"
        response += "What would you like us to help you do?"
        response += "1. BUY"
        response += "2. SELL"

    elif text in ['2*1', '2*2', '2*3', '2*4', '2*5', '2*6*1', '2*6*2', '2*6*3', '2*6*4', '2*6*5']:
        response = "END Your order has been received. \n"
        response += "One of FarmLink agent will reach out to you shortly."
        response += "Thanks."

    else :
        response = "END Invalid choice"

    return successResponse(response)

