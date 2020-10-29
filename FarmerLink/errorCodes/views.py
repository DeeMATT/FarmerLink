from enum import Enum, IntEnum
from errorCodes.models import Error
from django.db import IntegrityError


class ErrorCodes(IntEnum):
    USER = 1