from pywifi.profile import Profile as __Profile
from philh_myftp_biz.num import clamp
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .iface import Interface

class Profile(__Profile):
    
    def __init__(self,
        iface: Interface,
        profile: __Profile
    ) -> None:
        
        self.iface = iface
        
        super().__init__()
        
        self.id: int = profile.id
        self.auth: int = profile.auth
        self.akm: list[int] = profile.akm
        self.cipher: int = profile.cipher
        self.ssid: None|str = profile.ssid
        self.bssid = profile.bssid
        self.key = profile.key
        self.signal = profile.signal
        self.freq = profile.freq

        self.percent: int|float = clamp((2*(profile.signal + 100)), 0, 100)

