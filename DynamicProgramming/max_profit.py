# Stock Price

# Given an array representing the stock price on any given day,
# figure out the optimal single buy/sell that you could have made

def get_max_profit(array):
    minimum = max(array)
    maximum = 0
    for x in xrange(len(array)):
        minimum = min(minimum, array[x])
        maximum = max(maximum, array[x] - minimum)
    return maximum

if __name__=="__main__":
    assert get_max_profit([1,2,3,4,5]) == 4
    assert get_max_profit([8,2,14,6,8]) == 12
