import os
root_path = os.path.abspath(os.path.dirname(__file__)).split('lagou05')[0]
print(os.path.abspath(os.path.dirname(__file__)))
add1=1/2+1/3
print(add1)

try:
     "ss"/"s"
except Exception as e:
    print(e.__doc__)