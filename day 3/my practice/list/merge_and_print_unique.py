# 32. Merge two lists and print unique elements.

def merge_and_print_unique(l1,l2):
    l3=l1+l2
    print(set(l3))
merge_and_print_unique([1,2,3,4],[1,2,3,4,5,6,7])