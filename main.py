numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def merge_sort (arr):
  if len(arr) == 1:
    return arr

  # Split Array in into right and left
  if len(arr) > 1:
    length = len(arr)
    middle = length // 2
    left = arr[:middle]
    right = arr[middle:]
    merge_sort(left),
    merge_sort(right)

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        arr[k] = left[i]
        i += 1
        k += 1
      else:
        arr[k] = right[j]
        j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# def merge(left, right):
#   result = []
#   left_index = 0
#   right_index = 0
#   while left_index < len(left) and right_index < len(right):
#     if left[left_index] < right[right_index]:
#       result.append(left[left_index])
#       left_index += 1
#     else:
#       result.append(right[right_index])
#       right_index += 1
  




answer = merge_sort(numbers);
print(numbers)