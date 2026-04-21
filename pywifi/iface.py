from pywifi.iface import Interface as __Interface


class Interface(__Interface):

    _scan_started = False

    @property
    def profiles(self):

        if not self._scan_started:
            super().scan()
            self._scan_started = True

        return super().scan_results()
