

import pywifi


def bies():
    wifi = pywifi.PyWiFi()

    iface = wifi.interfaces()[0]
    print(iface)

    iface.scan()
    bessis = iface.scan_results()

    print(bessis)

bies()

