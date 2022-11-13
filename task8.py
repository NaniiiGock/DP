#ls = [2, 5, -3, 3, 4, 1]

def max_level(ls):
        min_prod = 1
        max_prod = 1
        final = ls[0]
        # just take 1st element as max product for now

        for elem in ls:
            # renew max and min product;
            # p.s. if max product = 6 for instance,
            # while min product is -5, and elem is -3, the min_prod*elem = 15
            # which is greater than max product, so it will be taken as final instead
            options = max_prod*elem, min_prod*elem, elem
            max_prod = max(options)
            min_prod = min(options)
            # renew final result each time
            final = max(max_prod, final)

        return final
      
#print(max_level(ls))
