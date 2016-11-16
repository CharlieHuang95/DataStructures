def gcd(a,b):
    c=min(int(a), int(b)) #The highest number possible for the greatest common divisor is one of the numbers. This function picks the lowest of the two given numbers to start checking.
    while c>=1:
        rem_a = a % c #Find the remainer.
        rem_b = b % c
        if rem_a==0 and rem_b==0: #If both remainers are equal to zero, then 'c' is a divisor of both.
            return c
        c = c-1 #The function loops until 'c' is equal to zero. Each time the value used is one lower.

if __name__=="__main__":
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(gcd(a,b))
