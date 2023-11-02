def quick_sort(elements):
    
    if len(elements) <= 1:
        return elements
    
    pivot = elements.pop()
    greater_than_elements = []
    lesser_or_equal_than_elements = []
    for element in elements:
        if (element > pivot):
            greater_than_elements.append(element)
        else:
            lesser_or_equal_than_elements.append(element)
    return quick_sort(lesser_or_equal_than_elements) + [pivot] + quick_sort(greater_than_elements)