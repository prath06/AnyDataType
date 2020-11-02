'''
Any dataType Search
This function search an element from a generic-type List
@Author: Prath06 (Priyansu Rath)
'''

def binary_search(inputData, no_of_Items, item_to_Search):
    Left = 0
    Right = no_of_Items - 1
    while Left <= Right:
        mid = (Left + Right) // 2
        if inputData[mid] < item_to_Search:
            Left = mid + 1
        elif inputData[mid] > item_to_Search:
            Right = mid - 1
        else:
            return mid
    return False

print(binary_search(['aaa', 'bbb', 'ccc', 'eee', 'mmm'], 5, 'eee'))

print(binary_search(['aaa', 'bbb', 'ccc', 'eee', 'mmm'], 5, 'fff'))

print(binary_search([1,4,6,8,9,22,27,77,79, 88], 10, 27))

print(binary_search([1,4,6,8,9,22,27,77,79, 88], 10, 107))

