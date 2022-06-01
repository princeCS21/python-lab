#to count number of uppercase and lowercase.

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("original String : ", s)
    print ("no. of Upper case characters : ", d["UPPER_CASE"])
    print ("no. of Lower case Characters : ", d["LOWER_CASE"])

stg = "Hello World. Welcpome to this program"
string_test(stg)
