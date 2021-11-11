elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even_count=0
odd_count=0
for i in elements:
    if i%2==0:
     even_count=even_count+i
    else:
        odd_count=odd_count+i
print(even_count,"even numbers")
print(odd_count,"odd numbers")


