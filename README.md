# spoof_mac_nick3499
Python3: Spoof MAC Address: datetime.date(), subprocess.run()

## Caution

`spoof_mac.py` can break a network connection, so users should avoid negative outcomes.

## Bang Line

`#! /snap/bin/pypy3` starts with a _shebang_ (`#!`), which functions as a [magic number](https://en.wikipedia.org/wiki/Magic_number_(programming)):

>[Unix](https://en.wikipedia.org/wiki/Unix) or [Linux](https://en.wikipedia.org/wiki/Linux) scripts may start with a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) (#!, `23` `21`) followed by the path to an [interpreter](https://en.wikipedia.org/wiki/Interpreter_directive), if the interpreter is likely to be different from the one from which the script was invoked.<sub>1</sub>

## PyPy3 Snap

In Ubuntu, `/snap/bin/pypy3` can be installed in the CLI: `$ snap install pypy3`. `python3` can be used otherwise.

## Index Daily MAC Address

`datetime.date.today().weekday()` returns an integer used to index the MAC
address of the day from `mac_list`.

```python
mac_list = [
    "9A:E9:30:BF:99:3E",
    "AA:F4:25:C5:0E:2E",
    "9E:FF:D2:A5:B4:6C",
    "9E:FF:D2:A5:B4:6D",
    "CA:F2:6D:CF:15:67",
    "02:4D:64:22:FE:70",
    "7E:AE:18:B4:32:19"
]
```

On Saturday, value returned by `datetime.date.today().weekday()` is `5`, which indexes `mac_list[5]` which returns `'02:4D:64:22:FE:70'`, the MAC address for Saturday MAC address.

## Run the Script

`$ python3 ~/Applications/py/spoof_mac/spoof_mac.py`

## Alternative: Shell Script

```shell
#! /bin/sh
# spoof MAC address
$HOME/scripts/spoof_mac/./spoof_mac.py

# check network device name with spoofed MAC address
sudo lshw -class network | egrep 'serial|logical name'
```

## gen_mac

`gen_mac.py` generates a pseudo-random MAC address. The first part of the spoofed MAC address comes from a list of organizationally unique identifiers.

1. [Magic_number_(programming): In_files](https://en.wikipedia.org/wiki/Magic_number_(programming)#In_files)
