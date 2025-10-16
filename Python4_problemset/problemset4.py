#!/usr/bin/env python3
taxa_string = "sapiens : erectus : neanderthalensis"
print(taxa_string)
taxa_list = taxa_string.split(":")
print(taxa_list)
print(taxa_list[1])
print(type(taxa_string))
print(type(taxa_list))
print(sorted(taxa_list, key=None, reverse=False))
print(sorted(taxa_list, key=len))

#problem4
number = 0
sum = 0
while number <=100:
    sum += number 
    number+=1
print("done")
print(sum)

#problem5
num = 1
fac = 1
while num <= 10:
    fac *= num 
    num +=1
print("done")
print(fac)

#problem6
numz = [101,2,15,22,95,33,2,27,72,15,52]
for num in numz:
    if num%2 == 0:
        print(num)

numz_sorted = sorted(numz, key=None, reverse=False)
print(numz_sorted)
even_sum = 0 
odd_sum = 0
for nm in numz_sorted:
    print(nm)
    if nm%2 == 0:
        even_sum+=nm
    else:
        odd_sum+=nm
print(f'sum of even numbers:{even_sum}\nsum of odds:{odd_sum}')

#problem8
# for kd in range(101):
#      print(kd)

#problem9
# l1 = list(range(100))
# l2 = list(range(101))
# for l in l1:
#     print(l)
# for m in l2:
#     print(m)

#problem10
for m in range(10):
    print(m)
