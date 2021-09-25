def unique_in_order(iterable):
    if not iterable:
        return []

    ans = [iterable[0],]
    
    for char in iterable[1:]:
        if char != ans[-1]:
            ans.append(char)
    return ans
    
"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""