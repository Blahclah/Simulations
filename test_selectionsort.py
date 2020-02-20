def selection_sort(arr):        
    for i in range(len(arr)):
        minimum = i
       
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front of the
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
           
    return arr


arr1 = [64, 34, 25, 12, 22, 11, 90]
arr2 = [64, 34, 25, 12, 22, 11]
arr3 = [-64, 34, 25]
arr4 = []
 
selection_sort(arr1)
selection_sort(arr2)
selection_sort(arr3)
selection_sort(arr4)
 
print ("Sorted array1 is:")
print(arr1)

print ("Sorted array2 is:")
print(arr2)

print ("Sorted array3 is:")
print(arr3)

print ("Sorted array4 is:")
print(arr4)

cards = ['5♣', '8♠', '4♠', '9♣', 'K♣', '6♣', '5♥', '3♣', '8♥', 'A♥', 'K♥', 'K♦', '10♣', 'Q♣', '7♦', 'Q♦', 'K♠', 'Q♠', 'J♣', '5♦', '9♥', '6♦', '2♣', '7♠', '10♠', '5♠', '4♣', '8♣', '9♠', '6♥', '9♦', '3♥', '3♠', '6♠', '2♥', '10♦', '10♥', 'A♠', 'A♣', 'J♥', '7♣', '4♥', '2♦', '3♦', '2♠', 'Q♥', 'A♦', '7♥', '8♦', 'J♠', 'J♦', '4♦']
selection_sort(cards)
print("Sorted cards:" )
print(cards)
