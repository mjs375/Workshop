def solution(string, limit): 
    if len(string) <= limit:
        return string
    ans = string[0:limit] + "..."
    return ans
    
    
"""
The function must return the truncated version of the given string up to the given limit followed by "..." if the result is shorter than the original. Return the same string if nothing was truncated.

Example:

solution('Testing String', 3) --> 'Tes...'
solution('Testing String', 8) --> 'Testing ...'
solution('Test', 8)           --> 'Test'
"""
