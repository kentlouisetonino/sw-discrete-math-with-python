def example():
    set_car_a = { 'honda', 'toyota', 'mazda'}
    set_car_b = { 'mazda', 'lamborghini', 'ferrari' }
    print("[ Set Theory Example: Union ]")
    print('approach 1: ', set_car_a | set_car_b)
    print('approach 2: ', set_car_a.union(set_car_b))
