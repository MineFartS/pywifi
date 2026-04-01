from ctypes import pointer, POINTER, cast
from .interface import Interface
from _ctypes import _Pointer
from .struct import (
    WLAN_INTERFACE_INFO_LIST,
    WLAN_INTERFACE_INFO
)
from typing import Generator

def Interfaces() -> Generator[Interface]:

    _ifaces = pointer(WLAN_INTERFACE_INFO_LIST())

    interfaces: _Pointer[WLAN_INTERFACE_INFO] = cast(
        _ifaces.contents.InterfaceInfo,
        POINTER(WLAN_INTERFACE_INFO)
    )

    for i in range(0, _ifaces.contents.dwNumberOfItems):
        
        _iface = interfaces[i]

        yield Interface(
            guid = _iface.InterfaceGuid,
            name = _iface.strInterfaceDescription
        )