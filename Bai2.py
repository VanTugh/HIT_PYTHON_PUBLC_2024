# toan tu 

my_set1={"hoa", "la","canh"}
my_set2={"nhuy","bong","hoa"}
#1. phep hop
my_union= my_set1 | my_set2
#  hoac my_union=my_set1.union(my_set2)
print(my_union)
#2. phep giao
my_intersection = my_set1 & my_set2 
# my_set1.intersection(my_set2)
print(my_intersection)
#3. phep hieu
my_difference= my_set1 - my_set2
# my_set1.difference
print(my_difference)
#4. phep khac biet doi xung
my_symmetric_difference= my_set1 ^ my_set2
print(my_symmetric_difference)
#my_set1.symmetric_difference(my_set2)