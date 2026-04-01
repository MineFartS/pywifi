from ctypes import (
    POINTER, Structure, c_uint, c_wchar_p,
    c_wchar, c_ulong, c_char, c_ushort, c_byte,
    c_bool, c_ubyte, c_long, c_ulonglong
)
from ctypes.wintypes import DWORD, HANDLE
from comtypes import GUID

handle = HANDLE()

WLAN_MAX_PHY_TYPE_NUMBER = 8
DOT11_MAC_ADDRESS = c_ubyte * 6

class WLAN_INTERFACE_INFO(Structure):

    _fields_ = [
        ("InterfaceGuid", GUID),
        ("strInterfaceDescription", c_wchar * 256),
        ("isState", c_uint)
    ]

class WLAN_INTERFACE_INFO_LIST(Structure):

    _fields_ = [
        ("dwNumberOfItems", DWORD),
        ("dwIndex", DWORD),
        ("InterfaceInfo", WLAN_INTERFACE_INFO * 1)
    ]

class DOT11_SSID(Structure):

    _fields_ = [
        ("uSSIDLength", c_ulong),
        ("ucSSID", c_char * 32)
    ]

class WLAN_RATE_SET(Structure):

    _fields_ = [
        ("uRateSetLength", c_ulong),
        ("usRateSet", c_ushort * 126)
    ]

class WLAN_RAW_DATA(Structure):

    _fields_ = [
        ("dwDataSize", DWORD),
        ("DataBlob", c_byte * 1)
    ]

class WLAN_AVAILABLE_NETWORK(Structure):

    _fields_ = [
        ("strProfileName", c_wchar * 256),
        ("dot11Ssid", DOT11_SSID),
        ("dot11BssType", c_uint),
        ("uNumberOfBssids", c_ulong),
        ("bNetworkConnectable", c_bool),
        ("wlanNotConnectableReason", c_uint),
        ("uNumberOfPhyTypes", c_ulong * WLAN_MAX_PHY_TYPE_NUMBER),
        ("dot11PhyTypes", c_uint),
        ("bMorePhyTypes", c_bool),
        ("wlanSignalQuality", c_ulong),
        ("bSecurityEnabled", c_bool),
        ("dot11DefaultAuthAlgorithm", c_uint),
        ("dot11DefaultCipherAlgorithm", c_uint),
        ("dwFlags", DWORD),
        ("dwReserved", DWORD)
    ]

class WLAN_AVAILABLE_NETWORK_LIST(Structure):

    _fields_ = [
        ("dwNumberOfItems", DWORD),
        ("dwIndex", DWORD),
        ("Network", WLAN_AVAILABLE_NETWORK * 1)
    ]

class WLAN_BSS_ENTRY(Structure):

    _fields_ = [
        ("dot11Ssid", DOT11_SSID),
        ("uPhyId", c_ulong),
        ("dot11Bssid", DOT11_MAC_ADDRESS),
        ("dot11BssType", c_uint),
        ("dot11BssPhyType", c_uint),
        ("lRssi", c_long),
        ("uLinkQuality", c_ulong),
        ("bInRegDomain", c_bool),
        ("usBeaconPeriod", c_ushort),
        ("ullTimestamp", c_ulonglong),
        ("ullHostTimestamp", c_ulonglong),
        ("usCapabilityInformation", c_ushort),
        ("ulChCenterFrequency", c_ulong),
        ("wlanRateSet", WLAN_RATE_SET),
        ("ulIeOffset", c_ulong),
        ("ulIeSize", c_ulong)
    ]

class WLAN_BSS_LIST(Structure):

    _fields_ = [
        ("dwTotalSize", DWORD),
        ("dwNumberOfItems", DWORD),
        ("wlanBssEntries", WLAN_BSS_ENTRY * 1)
    ]

class NDIS_OBJECT_HEADER(Structure):

    _fields_ = [
        ("Type", c_ubyte),
        ("Revision", c_ubyte),
        ("Size", c_ushort)
    ]

class DOT11_BSSID_LIST(Structure):

    _fields_ = [
        ("Header", NDIS_OBJECT_HEADER),
        ("uNumOfEntries", c_ulong),
        ("uTotalNumOfEntries", c_ulong),
        ("BSSIDs", DOT11_MAC_ADDRESS * 1)
    ]

class WLAN_CONNECTION_PARAMETERS(Structure):

    _fields_ = [
        ("wlanConnectionMode", c_uint),
        ("strProfile", c_wchar_p),
        ("pDot11Ssid", POINTER(DOT11_SSID)),
        ("pDesiredBssidList", POINTER(DOT11_BSSID_LIST)),
        ("dot11BssType", c_uint),
        ("dwFlags", DWORD)
    ]

class WLAN_PROFILE_INFO(Structure):

    _fields_ = [
        ("strProfileName", c_wchar * 256),
        ("dwFlags", DWORD)
    ]

class WLAN_PROFILE_INFO_LIST(Structure):

    _fields_ = [
        ("dwNumberOfItems", DWORD),
        ("dwIndex", DWORD),
        ("ProfileInfo", WLAN_PROFILE_INFO * 1)
    ]
