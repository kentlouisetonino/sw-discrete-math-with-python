def union():
    set_car_a = { 'honda', 'toyota', 'mazda'}
    set_car_b = { 'mazda', 'lamborghini', 'ferrari' }
    set_car_union_1 = set_car_a | set_car_b
    set_car_union_2 = set_car_a.union(set_car_b)
    print("[ Set Theory Example: Union ]")
    print('approach 1: ', set_car_union_1)
    print('approach 2: ', set_car_union_2)
