def abs(number):
    if not isinstance(number, (float, int)):
        return number
    if number < 0:
        number = number * -1
    return number