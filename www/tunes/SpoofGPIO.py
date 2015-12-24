import sys
# Spoof RPi.GPIO class for Raspberry Pi GPIO development

HIGH = True
LOW = False

OUT = 0
BOARD = 0

_pins = [11, 12, 15, 16]
_pin_state = {pin: None for pin in _pins}

def setmode(mode):
    pass

def setup(id, mode):
    pass

def output(id, value):
    # ignore the first output for each pin
    is_first = _pin_state[id] is None
    _pin_state[id] = value
    if not is_first:
        # print [___} or [###] for each note
        n = 3
        str = '     [' + '] ['.join('_' * n if _pin_state[id] else '#' * n for id in _pins) + ']'
        sys.stdout.write('\r')
        sys.stdout.write(str)
        sys.stdout.flush()

def cleanup():
    pass
