# 1, 1, 2, 3, 5, 8, 13, 
i = 0
tal_n = -1
tal_n_plus_1 = 1


while i < 30:
    tal_nn = tal_n + tal_n_plus_1
    print (tal_nn)
    # tal_n få värdet av tal_n_plus_1  
    # tal_n_plus_1 får värdet av tal_nn
    tal_n = tal_n_plus_1
    tal_n_plus_1= tal_nn

    i = i + 1

