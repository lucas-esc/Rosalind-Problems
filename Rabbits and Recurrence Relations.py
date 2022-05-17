def pop_calc(months, childs):
    child_pairs = 1
    adult_pairs = 0

    for n in range(months-1):
        nat_rate = adult_pairs * childs
        adult_pairs += child_pairs
        child_pairs = nat_rate
    return adult_pairs + child_pairs
        
print(pop_calc(29, 2))





