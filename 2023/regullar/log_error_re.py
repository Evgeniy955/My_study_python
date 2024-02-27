import logging
import re

log_file = "C:\\Users\\Yevhen\\Downloads\\Telegram Desktop\\yupdate.log"

class CriticalError(Exception):
    pass

def log_errors(log_file):
    error_lines = 0
    logging.basicConfig(filename="found_errors.log", level=logging.ERROR, format='%(message)s')
    try:
        with open(log_file) as f:
            lines = f.readlines()
            total_lines = len(lines)
            for line in lines:
                if re.search("error|Error|ERROR", line):
                    error_lines += 1
                    logging.error(line)
                    if re.search("critical error|Critical Error|CRITICAL ERROR", line):
                        print("CRITICAL ERROR: " + line)
        return total_lines / error_lines
    except ZeroDivisionError:
        print ('На ноль делить нельзя!')
    except FileNotFoundError:
        print(f"Error: {log_file} not found.")

if __name__ == "__main__":
    print(log_errors(log_file))
