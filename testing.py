import math

def permutation(array):
    if not len(array) > 1:
        return array
    else:
        all_permutations = []
        for i in range(len(array)):
            current_element = [array[i]]
            other_elements = array[0:i] + array[i+1:]
            other_elements_permutations = permutation(other_elements)
            for p in other_elements_permutations:
                if type(p) != type([]): p = [p]
                all_permutations.append(current_element + p)
        return all_permutations

"""

[1, 2, 3]
[1, 3, 2]

"""

def perms(stack):
    results = [stack.pop()]
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results


a = perms([1, 2, 3])
print(a)