# reverse of a number

'''def reverse(num):
   rev=0
   while(num>0):
      digit=num%10
      rev=(rev*10)+digit
      num=num//10
   return rev
n = int(input())
print(reverse(n))'''


#using string method

def reverse(num):
   st=str(num)
   rev_str=st[::-1]
   ans=int(rev_str)
   return ans
n = int(input())
print(reverse(n))
