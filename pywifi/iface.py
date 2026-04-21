from pywifi.iface import Interface as __Interface
from .profile import Profile

class Interface(__Interface):

    def __init__(self,
        iface: __Interface
    ) -> None:
        
        super().__init__(iface._raw_obj)

        self._wifi_ctrl = iface._wifi_ctrl

        self._scan_started = False

    @property
    def profiles(self) -> list[Profile]:

        if not self._scan_started:
            super().scan()
            self._scan_started = True

        return [Profile(self, p) for p in super().scan_results()]

