#Variance and Standard deviation of patients seen for recreation therapy daily
import statistics 
List = [5, 6, 7, 8, 10, 11, 12, 12, 8, 9, 10, 8, 4, 5, 12, 12, 5, 6, 7, 8, 10, 11, 12, 12, 8, 9, 10, 
 8, 4, 5, 12, 12, 10, 9, 8, 6, 5, 6, 7, 8, 10, 11, 12, 12, 8, 9, 10, 8, 4, 5, 12, 12, 10, 9, 8, 6,
 10, 11, 12, 11, 11, 9, 8, 9, 10, 11, 10, 12, 6, 5, 6, 3, 2, 8, 7, 6, 5, 10, 11, 12, 5, 8, 9, 10, 6,
 9, 8, 2, 10, 11, 12, 10, 2, 10, 11, 12, 11, 10, 9, 6, 10, 11, 12, 12, 16, 12, 10, 9, 6, 4, 10]
print('Standard deviation is:', statistics.pstdev(List))
print('Variance is:', statistics.pvariance(List))