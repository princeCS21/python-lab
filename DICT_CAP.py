#CAPITALIZE THE KEY OIF DICTIONARY
D={'first':1,'second':2,'third':3}
D1=dict((k.upper(),v) for k,v in D.items())
print(D1)
