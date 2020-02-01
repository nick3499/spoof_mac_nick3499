#! /snap/bin/pypy3
'''CAUTION: `spoof_mac` breaks network connection. Consider negative outcomes.
- spoofs MAC address based on indexed weekday number;
- imports `datetime.date()` and `subprocess.run()` methods.'''
from datetime import date
from subprocess import run


def spoof_mac():
    '''`spoof_mac()` method spoofs MAC address based on indexed weekday number;
(1) MAC address per weekday in `mac_addr`.'''
    mac_addr = [
        "9A:E9:30:BF:99:3E", "AA:F4:25:C5:0E:2E",  # Monday, Tuesday
        "9E:FF:D2:A5:B4:6C", "9E:FF:D2:A5:B4:6D",  # Wednesday, Thursday
        "CA:F2:6D:CF:15:67", "02:4D:64:22:FE:70",  # Friday, Saturday
        "7E:AE:18:B4:32:19"  # Sunday
    ]

    run(["sudo", "ip", "link", "set", "dev", "enp3s0", "address",
         mac_addr[date.today().weekday()]], check=True)


if __name__ == '__main__':
    spoof_mac()
