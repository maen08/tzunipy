from uni import university


"""
method-carrier/main class
"""

class TzUniPy():

    """
    method which returns all universities in Tanzania
    """
    def all_universities():
        # print(university)
        return university


    """
    method which returns all universities in a given region
    """
    def get_univeristy(region):
        uni_in_region = []
        for x in university:
            if region in x:
                uni_in_region.append(x)

        # print(uni_in_region)
        return uni_in_region

