fo = open('q1.txt', 'w+')
for i in range(50,501):
    content =str(i)
    content_1 = fo.write(content + ' ')
number = int(content_1)
fo.seek(0)
read = fo.read()
print(read)
fo.close()
    
 
