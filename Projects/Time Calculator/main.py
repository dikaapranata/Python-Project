# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time


print(add_time("11:43 AM", "00:20"))
print(add_time("6:30 PM", "205:12"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 AM", "00:20"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("3:00 PM", "3:10"))
