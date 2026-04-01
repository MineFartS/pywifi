from ctypes import (
    _NamedFuncPointer, pointer, byref, POINTER, 
    cast, c_void_p, windll
)
from ctypes.wintypes import HANDLE, DWORD
from _ctypes import _CArgObject
from typing import Generator
from .struct import (
    WLAN_AVAILABLE_NETWORK_LIST,
    WLAN_BSS_LIST,
    WLAN_AVAILABLE_NETWORK,
    WLAN_BSS_ENTRY,
    AKM_TYPE_NONE,
    AUTH_ALG_OPEN,
    handle,
    GUID,
    DOT11_SSID,
    WLAN_RAW_DATA
)
from .profile import Profile

class Interface:

    def __init__(self,
        name:str, 
        guid:str
    ) -> None:
        self.name: str = name
        self.guid: _CArgObject = byref(guid)

    def scan(self) -> None:
        """Trigger the wifi interface to scan."""

        func: _NamedFuncPointer = windll.wlanapi.WlanScan

        func.argtypes = [
            HANDLE, 
            POINTER(GUID), 
            POINTER(DOT11_SSID), 
            POINTER(WLAN_RAW_DATA), 
            c_void_p
        ]
        
        func.restypes = [DWORD]
        
        func(handle, self.guid, None, None, None)

    @property
    def profiles(self) -> Generator[Profile]:
        """Get the AP list after scanning."""

        avail_network_list = pointer(WLAN_AVAILABLE_NETWORK_LIST())

        self._wlan_get_available_network_list(
            handle,
            self.guid, 
            byref(avail_network_list)
        )

        networks = cast(
            avail_network_list.contents.Network,
            POINTER(WLAN_AVAILABLE_NETWORK)
        )

        for i in range(avail_network_list.contents.dwNumberOfItems):

            if networks[i].dot11BssType == 1 and networks[i].bNetworkConnectable :

                ssid: str = ''
                for j in range(networks[i].dot11Ssid.uSSIDLength):

                    if networks[i].dot11Ssid.ucSSID != b'':

                        ssid += "%c" % networks[i].dot11Ssid.ucSSID[j]

                bss_list = pointer(WLAN_BSS_LIST())
                
                self._wlan_get_network_bss_list(
                    self._handle,
                    self.guid, 
                    byref(bss_list), 
                    networks[i].dot11Ssid, 
                    networks[i].bSecurityEnabled
                )

                bsses = cast(
                    bss_list.contents.wlanBssEntries,
                    POINTER(WLAN_BSS_ENTRY)
                )

                if networks[i].bSecurityEnabled:
                    akm = self._get_akm(networks[i].dot11DefaultCipherAlgorithm)
                    auth_alg = self._get_auth_alg(networks[i].dot11DefaultAuthAlgorithm)
                else:
                    akm = [AKM_TYPE_NONE]
                    auth_alg = [AUTH_ALG_OPEN]

                for j in range(bss_list.contents.dwNumberOfItems):
                    
                    network = Profile()

                    network.ssid = ssid

                    network.bssid = ''
                    for k in range(6):
                        network.bssid += "%02x:" % bsses[j].dot11Bssid[k]

                    network.signal = bsses[j].lRssi
                    network.freq = bsses[j].ulChCenterFrequency
                    network.auth = auth_alg
                    network.akm = akm

                    p = (2 * (bsses[j].lRssi + 100))
                    network.percent = max(min(p, 100), 0)

                    yield network
