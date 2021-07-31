from uni import university



def all_universities():
    return university


def get_univeristy(region):
    uni_in_region = []
    for x in university:
        if region in x:
            uni_in_region.append(x)
            # return x
    
    # print(uni_in_region)
    return uni_in_region




get_univeristy('Arusha')

# all_universities()