list1 = list(range(10000001))



def Binary_seq(list1, num):
    min = 0 
    max = len(list1)
    while min <= max:
        mid = (min + max) / 2
        guess = list1[int(mid)]
        if guess == num:
            return guess
            #guess was too high so we remove numbers above it
        elif guess > num:
            max = mid
            # guess was to low to we remove all numbers below it
        elif guess < num:
            min = mid
        else:
            return None
        break
    print(num)

Binary_seq(list1, 34098)