from pywifi.profile import Profile as __Profile
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
        self.auth = profile.auth
        self.akm = profile.akm
        self.cipher = profile.cipher
        self.ssid: None|str = profile.ssid
        self.bssid = profile.bssid
        self.key = profile.key
        self.signal = profile.signal
        self.freq = profile.freq

        _p = (2 * (profile.signal + 100))
        self.percent: int = max(min(_p, 100), 0)
