from .struct import (
    CIPHER_TYPE_NONE,
    AKM_TYPE_NONE,
    AUTH_ALG_OPEN
)

class Profile:

    id: int = 0
    auth = AUTH_ALG_OPEN
    akm = [AKM_TYPE_NONE]
    cipher = CIPHER_TYPE_NONE
    ssid: str = None
    bssid: str = None
    key = None

    signal = None
    freq = None

    percent: int = None
