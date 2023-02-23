import math
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class StatisticalCalculation():

    def __init__(self, data):
        self.data = data
        self.data_set = set(self.data)
        self.sorted_set = sorted(list(self.data_set))
    def count_l(self):
        count=0
        for item in self.data:
            count += 1
        return(count)
    def sum(self):
        sum=0
        for item in self.data:
            sum += item
        return(sum)
    def min(self):
        self.data.sort()
        return self.data[0]
    def max(self):
        self.data.sort()
        return self.data[-1]
    def range(self):
        return data.max() - data.min()
    def mean(self):
        return (data.sum()/data.count_l())
    def mode(self):
        a= 0
        b= 0
        c= []

        for item in self.sorted_set:
            b=item
            if self.data.count(b) == self.data.count(a):
                c.append(a)
                c.append(b)
            elif self.data.count(b) > self.data.count(a):
                a = b
                c.clear
            elif self.data.count(b) < self.data.count(a):
                b = 0
        if bool(c):
            return f"The data is multimodal, and are: {c}, with a count of:{self.data.count(a)}"
        if bool(c) == False:
            return f"The mode is {a} with a count of: {self.data.count(a)}"
    def median(self):
        self.data.sort()
        n = data.count_l()
        if n % 2 == 0:
            median1 = self.data[n//2]
            median2 = self.data[n//2 - 1]
            median = (median1 + median2)/2
        else:
            median = self.data[n//2]
        return median
    def var(self):
        m=data.mean()
        x = 0
        n = data.count_l()
        for item in self.data:
            x += (item-m)**2
        variance = x/n
        return round(variance,1)
    def std(self):
        return round(math.sqrt(data.var()),1)
        




data = StatisticalCalculation(ages)
print('Count:', data.count_l())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Mode: ', data.mode())
print('Median: ', data.median())
print('Variance: ', data.var())
print('Standard Deviation: ', data.std())
