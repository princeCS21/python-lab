fo = open('q2.txt', 'w+')
for i in range(50,101):
    content =str(i)
    content_1 = fo.write(content + '\n')

fo.seek(0,0)
number = int(content_1)
read = fo.read()
print(read)
fo.close()
    
