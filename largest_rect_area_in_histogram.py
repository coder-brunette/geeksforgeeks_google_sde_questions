# def largest_rect_in_hist(nums):

#     left = 0
#     right = len(nums) - 1
#     area = 0

#     while left < right:


#     return area


def largest_rect_in_hist(heights):

    stack = []
    index = 0
    max_area = 0
    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            print("tos: ",top_of_stack)
            width = index if not stack else index - stack[-1] - 1
            print("width: ", width)
            max_area = max(max_area, heights[top_of_stack] * width)
            print("max area: ", max_area)
        print("index: ", index)
        print("stack: ", stack)
    while stack:
        top_of_stack = stack.pop()
        width = index if not stack else index - stack[-1] - 1
        max_area = max(max_area, heights[top_of_stack] * width)

    return max_area

print(largest_rect_in_hist([6, 2]))

def max_area_histogram(histogram): 
  
    # This function calculates maximum 
    # rectangular area under given 
    # histogram with n bars 
  
    # Create an empty stack. The stack 
    # holds indexes of histogram[] list. 
    # The bars stored in the stack are 
    # always in increasing order of 
    # their heights. 
    stack = list() 
  
    max_area = 0  # Initialize max area 
  
    # Run through all bars of 
    # given histogram 
    index = 0
    while index < len(histogram): 
  
        # If this bar is higher 
        # than the bar on top 
        # stack, push it to stack 
  
        if (not stack) or (histogram[stack[-1]] <= histogram[index]): 
            stack.append(index) 
            index += 1
  
        # If this bar is lower than top of stack, 
        # then calculate area of rectangle with 
        # stack top as the smallest (or minimum 
        # height) bar.'i' is 'right index' for 
        # the top and element before top in stack 
        # is 'left index' 
        else: 
            # pop the top 
            top_of_stack = stack.pop() 
  
            # Calculate the area with 
            # histogram[top_of_stack] stack 
            # as smallest bar 
            area = (histogram[top_of_stack] *
                    ((index - stack[-1] - 1) 
                     if stack else index)) 
  
            # update max area, if needed 
            max_area = max(max_area, area) 
  
    # Now pop the remaining bars from 
    # stack and calculate area with 
    # every popped bar as the smallest bar 
    while stack: 
  
        # pop the top 
        top_of_stack = stack.pop() 
  
        # Calculate the area with 
        # histogram[top_of_stack] 
        # stack as smallest bar 
        area = (histogram[top_of_stack] *
                ((index - stack[-1] - 1) 
                 if stack else index)) 
  
        # update max area, if needed 
        max_area = max(max_area, area) 
  
    # Return maximum area under 
    # the given histogram 
    return max_area 


#print(max_area_histogram([6, 2, 5, 4, 5, 1, 6]))