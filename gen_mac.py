#! /snap/bin/pypy3
'''`spoof_mac` module generates a random MAC address.'''

from random import randrange as rr

def spoof_mac():
    '''`spoof_mac()` method generates a random MAC address.'''
    oui = [
        "F4:BD:9E", "94:E6:F7", "40:55:82", "A4:E3:1B", "98:E7:43", "4C:1D:96",
        "10:32:7E", "30:FB:B8", "68:DB:F5", "24:46:C8", "44:D7:91", "84:46:FE",
        "D8:29:18", "D0:D0:03", "98:06:37", "8C:B8:4A", "98:E8:FA", "08:4F:A9",
        "08:4F:F9", "D4:6B:A6", "CC:05:77", "30:8B:B2", "30:86:2D", "60:8B:0E",
        "D4:62:EA", "54:BA:D6", "14:42:FC", "6C:5E:3B", "0C:B7:71", "50:E0:85",
        "24:16:6D", "94:0B:19", "70:C7:F2", "38:94:ED", "DC:A6:32", "88:F5:6E",
        "BC:97:E1", "C8:C2:FA", "88:B3:62", "08:47:D0", "08:9C:86", "7C:89:56"
    ]

    # keys/values for creating pseudo-random hex pairs
    hex_obj = {
        0: "0", 1: "1",  2: "2",  3: "3",  4: "4",  5: "5",  6: "6",  7: "7",
        8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
    }
    hex_pair_strings = []  # hex pair strings

    # append hex pairs
    for i in range(3):
        hex_pair_strings.append(
            ''.join([hex_obj[rr(0, 16, 1)], hex_obj[rr(0, 16, 1)]])
        )

    rand_pairs = ':'.join(hex_pair_strings)  # join hex pairs with colons
    rand_mac = ':'.join([oui[rr(0, 42, 1)], rand_pairs])  # join OUI w/rand

    print(rand_mac)

if __name__ == "__main__":
    spoof_mac()
