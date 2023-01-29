# from itertools import permutations
# list1 = list(map(str, input().split()))
# # print(list(permutations(list1)))
# print(list1)


import decimal 
def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        print(decimal.Decimal(i),oct(i).replace("0o", ""),hex(i).replace("0x", ""),bin(i).replace("0b", ""))
        
   
if __name__ == '__main__':
    n = int(input('number:'))
    print_formatted(n) 