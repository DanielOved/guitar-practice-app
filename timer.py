import time
import os #for ringing sound

class Timer:
    def __init__(self,max_val):
        self.max_val = max_val
        self.reset()
    def ring(self):
        duration = .12  # second
        freq = 950  # Hz
        for i in range(5):
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    def reset(self):
        self.time = 0.0
        self.stop = 1
    def start(self):
        self.start_time = time.time()
        self.stop = 0
    def stopTimer(self):
        self.stop = 1
    def update(self):
        if (self.stop != 1):
            current_time = time.time()
            self.time += current_time - self.start_time
            self.start_time = current_time
        if(int(self.time) == int(self.max_val)):
            self.ring()
            self.reset()
    def get_seconds(self):
        return int(self.max_val - self.time)
