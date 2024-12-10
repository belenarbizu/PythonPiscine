import time
import datetime

seconds = time.time()
print("Seconds since January 1, 1970: ", f'{seconds:,.4f}', "or", f'{seconds:.2e}', "in scientific notation")

date = datetime.datetime.now()
print(date.strftime("%b %d %Y"))