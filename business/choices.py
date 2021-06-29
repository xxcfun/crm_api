from django.db import models


class WinRate(models.IntegerChoices):
    """商机赢单率"""
    WINNING_NONE = 1, '0%'
    WINNING_ERSHI = 2, '20%'
    WINNING_WUSHI = 3, '50%'
    WINNING_BASHI = 4, '80%'
    WINNING_DONE = 5, '100%'
