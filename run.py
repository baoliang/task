from tasks import *
import time
for i in range(525600):
  convert_task()
  time.sleep(60)
  update_task()
  time.sleep(60)

