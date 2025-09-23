numbers = list(range(1,10))
for num in numbers:
    if num == 1:
        suffix = "st"
    elif num == 2:
        suffix = "nd"    
    elif num == 3:
        suffix = "rd"
    else: 
        suffix = "th"    
    print(str(num) + suffix, end=" ")
    