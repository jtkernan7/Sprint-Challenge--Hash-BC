#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    #for each 
    # h = {}
    # for i, num in enumerate(weights):
    #     n = limit - num
    #     if n not in h:
    #         h[num] = i
    #     else:
    #         #answer = [h[n], i]
    #         return [h[n], i]
    
    l=range(length)

    for i in l:
        hash_table_insert(ht, weights[i], i)
    for i in l:
        x = hash_table_retrieve(ht, limit-weights[i])
        if x is not None:
            return(x,i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
