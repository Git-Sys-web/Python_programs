n=int(input("enter a number"));
result=0;
temp=n;
while(temp>0):
    digit=temp%10;
    result=result*10+digit;
    temp=temp//10;
if (n==result):
    print("is a palindrome");
else:
    print("is not a palindrome");