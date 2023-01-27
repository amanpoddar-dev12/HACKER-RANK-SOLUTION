# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()

lowers = sorted([x for x in s if x.islower()])
uppers = sorted([x for x in s if x.isupper()])
odd_digits = sorted([x for x in s if x.isdigit() and int(x)%2])
even_digits = sorted([x for x in s if x.isdigit() and int(x)%2==0])

print(*lowers, *uppers, *odd_digits, *even_digits,sep='')