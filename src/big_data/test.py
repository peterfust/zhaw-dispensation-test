def my_func(generator_funct,  N):
    sum = 0
    for _ in range(N):
        result = generator_funct()
        if result > 0:
            sum += result
    return sum

my_func(generator_fuct, 5)