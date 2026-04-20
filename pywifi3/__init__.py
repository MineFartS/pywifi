from pywifi import PyWiFi

def Interface(x:int=0):
    return PyWiFi().interfaces()[x]