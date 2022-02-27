# source: https://www.carbonfootprint.com/calculator.aspx

CARBON_PER_DOLLAR_CLOTHES_SHOES = 0.00029 

def estimate(data):
    """ Input: $X (spending in clothes or shoes)
    Output: X * CARBON_PER_DOLLAR_CLOTHES_SHOES (estimated tonnes of CO_2e output)
    """
    return data * CARBON_PER_DOLLAR_CLOTHES_SHOES

    