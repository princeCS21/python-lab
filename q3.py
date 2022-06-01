#print random number between
import random
f = open('q3','w+')
content = str(random.randint(100,200))
content_1 = f.write(content)
number = int(content_1)
f.seek(0)
r = f.read()
print(r)
f.close()
