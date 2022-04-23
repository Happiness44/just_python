# python에서 package를 찾는 방법 및 원리
import sys
import time
from tqdm import tqdm

# print(sys.path)


for path in sys.path:
    print(path)


for n in tqdm(range(100)):
    time.sleep(0.1)
