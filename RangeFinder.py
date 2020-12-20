def limit_finder(number, difference):
    """Given a number and an another number that specifies the range length. This function will return 
    a lower limit of the range and so will return a upper limit.
    Functionality:-
    So, basically what this program does is takes the half of difference provided and finds a random number
    between the range 0 and the difference/2. What does the final outcome comes it then subtracts it from 
    the number and lower limit is obtained. The number obtained is also subtracted from the difference, 
    and what the value obtained adds to the number to obtain high limit."""
    import random
    
    if difference%2 != 0:       
        one_time_range_uniform = difference/2 + 0.5 
        one_time_range_uniform = int(one_time_range_uniform)
    else:
        one_time_range_uniform = difference/2
        one_time_range_uniform = int(one_time_range_uniform)
    
    one_time_range_random = random.randint(0, one_time_range_uniform)
    difference = difference - one_time_range_random

    low_limit = number-one_time_range_random
    high_limit = number+difference

    return low_limit, high_limit

# Testing Below:
# # To test uncomment 
# for x in range(3):
#     ranger = limit_finder(20, 3)
#     y = ranger[0]
#     print(y)
#     print(ranger)
