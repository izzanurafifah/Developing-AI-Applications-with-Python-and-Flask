def mean(numbers):
    """
    This function returns the mean of the given list of numbers.
    """
    return sum(numbers) / len(numbers) # return the mean value.

def median(numbers):
    """
    This function returns the median of the given list of numbers.
    """
    numbers.sort() # sort the list of numbers in ascending order.
    
    if len(numbers) % 2 == 0:
        median1 = numbers[len(numbers) // 2] # the higher index of the two middle values.
        median2 = numbers[len(numbers) // 2 - 1] # the lower index of the two middle values.
        
        mymedian = (median1 + median2) / 2 # average of the two middle values.
    else:
        mymedian = numbers[len(numbers) // 2] # the middle value for lists with an odd number of elements.
    
    return mymedian
