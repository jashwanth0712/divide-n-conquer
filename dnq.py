from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

Logo="""
  ____    _           _       _
 |  _ \  (_) __   __ (_)   __| |   ___           _ __             ___    ___    _ __     __ _   _   _    ___   _ __ 
 | | | | | | \ \ / / | |  / _` |  / _ \  _____  | '_ \   _____   / __|  / _ \  | '_ \   / _` | | | | |  / _ \ | '__|
 | |_| | | |  \ V /  | | | (_| | |  __/ |_____| | | | | |_____| | (__  | (_) | | | | | | (_| | | |_| | |  __/ | |   
 |____/  |_|   \_/   |_|  \__,_|  \___|         |_| |_|          \___|  \___/  |_| |_|  \__, |  \__,_|  \___| |_|   
                                                                                           |_|
"""
print(Logo)

class Loader:
    def __init__(self, desc="Loading...", end="Dataset1 recieved!", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


if __name__ == "__main__":
    with Loader("Fetching Dataset1 ..."):
        for i in range(10):
            sleep(0.25)
    print("Completed Dataset1 training")
    for i in range(10): 
        sleep(0.25)
    print("Deleted Dataset1")
    loader = Loader("Fetching Dataset2", "Recieved Dataset 2!", 0.05).start()
    for i in range(10): 
        sleep(0.25)
    loader.stop()
    loader = Loader("Training Dataset2", "Process completed", 0.05).start()
    for i in range(10): 
        sleep(0.25)
    loader.stop()
