from philh_myftp_biz.classtools import singleton
from pywifi.wifi import PyWiFi as __PyWiFi
from .iface import Interface

@singleton
class PyWiFi(__PyWiFi):

    @property
    def interfaces(self) -> list[Interface]:
        return [Interface(i) for i in super().interfaces()]

