from numpy import *
import matplotlib.pyplot as plt

# Challenge1
nums = arange(0, 20)
print(nums)

nums_mean = mean(nums)
nums_std = std(nums)
nums_variance = var(nums)

# Challenge2
bins = [0, 1, 2, 3, 4]
nums = [0.5, 0.7, 1., 1.2, 1.3, 2.1]

print("nums: {}".format(nums))
print("bins: {}".format(bins))
print("Result: {}".format(histogram(nums, bins)))

plt.title('Histogram of nums against bins')
plt.xlabel('nums')
plt.ylabel('bins')
plt.hist(nums, bins)
plt.show()
