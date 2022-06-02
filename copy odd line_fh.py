#store odd number of line in other file.
fp=open("C:\\Users\\Sujeet\\OneDrive\\Desktop\\s2.txt","r")
a=fp.readlines()
fo=open('s2w.txt','w')
for i in range (0,len(a)):
    if (i%2!=0):
        fo.write(a[i])
    else:
        pass
fo.close()
fo=open("C:\\Users\\Sujeet\\OneDrive\\Desktop\\practical\\s2w.txt",'r')
print(fo.readlines())
fp.close()
fo.close()

