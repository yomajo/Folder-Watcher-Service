import sys
import os
import time
from watchdog.observers.polling import PollingObserver
from events import CSVRenameHandler

class CsvWatcher:
    def __init__(self, src_path):
        self.__src_path = src_path
        self.__event_handler = CSVRenameHandler()
        self.__event_observer = PollingObserver()

    def run(self):
        self.start()
        print(f'Watcher for folder: {self.__src_path} STARTED')

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(self.__event_handler, self.__src_path, recursive=True)