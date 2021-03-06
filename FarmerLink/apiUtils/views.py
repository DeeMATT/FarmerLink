from django.shortcuts import render
htpfrom django.http import JsonResponse, HttpResponse

from http import HTTPStatus


def badRequestResponse(errorCode, message="", body={}):
    return errorResponse(HTTPStatus.BAD_REQUEST, errorCode, message=message, body=body)


def unAuthorizedResponse(errorCode, message="", body={}):
    return errorResponse(HTTPStatus.FORBIDDEN, errorCode, message=message, body=body)


def unAuthenticatedResponse(errorCode, message="", body={}):
    return errorResponse(HTTPStatus.UNAUTHORIZED, errorCode, message=message, body=body)


def resourceConflictResponse(errorCode, message="", body={}):
    return errorResponse(HTTPStatus.CONFLICT, errorCode, message=message, body=body)


def resourceNotFoundResponse(errorCode, message="", body={}):
    return errorResponse(HTTPStatus.NOT_FOUND, errorCode, message=message, body=body)


def internalServerErrorResponse(errorCode, message="", body={}):
    return errorResponse(HTTPStatus.INTERNAL_SERVER_ERROR, errorCode, message=message, body=body)


# error responnse
def errorResponse(httpStatusCode, errorCode, message="", body={}):
    return JsonResponse({'errorCode': errorCode, 'data': body, 'message': message}, status=httpStatusCode, safe=False)


# success responses
def createdResponse(message="", body={}):
    return successResponse(HTTPStatus.CREATED, message=message, body=body)


def successResponse(response, **kwargs):

    response = HttpResponse(response, content_type="text/plain")        
    return response


# # helper functions

# def getUserIpAddress(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip
