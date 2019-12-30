import os
import time
import re
from watchdog.events import RegexMatchingEventHandler

class CSVRenameHandler(RegexMatchingEventHandler):
    FIXED_DEC_PLACES = 3
    FIXED_EXTENSION = '.csv'    
    CSV_REGEX = [r".*.csv$"]

    def __init__(self):
        super().__init__(self.CSV_REGEX)

    def on_created(self, event):
        self.process(event)

    def process(self, event):
        dir_path = os.path.dirname(event.src_path)
        dir_name = os.path.basename(dir_path)
        old_file_path = event.src_path

        is_not_saved = True
        index = 1

        while is_not_saved:
            try:
                if index > 999:
                    break

                new_file_name = f'{dir_name}{index:03}.csv'
                new_file_path = os.path.join(dir_path, new_file_name)
                os.rename(old_file_path, new_file_path)
                is_not_saved = False
            except:
                index += 1
        
        if not is_not_saved:
            print(f'File: {old_file_path}\nRenamed to: {new_file_path}')
            return

        print(f'File has not been renamed. Failed at index {index}.')