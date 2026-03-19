import datetime

log_file = "log.txt"
counter = 0
text = ''
with open(log_file, 'r', encoding="utf-8") as f:
    counter = int(f.readline())
counter += 1
with open(log_file, 'w', encoding="utf-8") as f:
    f.write(str(counter))
