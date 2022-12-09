import os

# path=os.path.abspath(__file__)
# print(path)
path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"src","langType.txt")
print(path)