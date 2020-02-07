import sys
import time

for i in range(50):
    # 写入
    sys.stdout.write('#')
    # 刷新
    sys.stdout.flush()
    time.sleep(0.5)
