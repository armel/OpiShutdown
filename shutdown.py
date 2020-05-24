#!/usr/bin/python3

from pyA20.gpio import gpio
from pyA20.gpio import port
import time
import subprocess
import sys
import os

if not os.getegid() == 0:
    sys.exit('Script must be run as root')

#CMD = '/sbin/shutdown -h now'
CMD = 'echo Hello'
POWER_BUTTON = port.PA14
LED = port.STATUS_LED

def main(argv):

    initial_button_state = 0

    gpio.init()
    gpio.setcfg(POWER_BUTTON, gpio.INPUT)
    gpio.pullup(POWER_BUTTON, gpio.PULLUP)
    gpio.setcfg(LED, gpio.OUTPUT)

    while True:
        # Returns a 1 if open and a 0 if pressed/closed
        current_button_state = gpio.input(POWER_BUTTON)

        print(initial_button_state, current_button_state)
        sys.stdout.flush()

        # Check if button state has changed 
        if current_button_state != initial_button_state:
            gpio.output(LED, 1)
            subprocess.call(CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        time.sleep(0.5)

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass