# exceptions.py: [PowerText] custom exceptions.
# _*_ coding:utf8 _*_

class PowException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return str(self.message)
class UndefinedVariable(PowException):
    pass
class UndefinedFunction(PowException):
    pass
class InvalidParamCount(PowException):
    pass
class PowModuleNotFound(PowException):
    pass
class PowSyntaxError(PowException):
    pass
class PowTypeError(PowException):
    pass
class PowInterrupt(PowException):
    pass
class IllegalCharacter(PowException):
    pass
class PowRuntimeError(PowException):
    pass
