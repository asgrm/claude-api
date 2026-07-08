def calculate_pi():
    """
    Calculate Pi up to 5 decimal places using the Leibniz formula.
    Returns Pi rounded to 5 decimal places.
    """
    # Using Leibniz formula: π = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ...)
    # We need many iterations for good accuracy
    pi_approx = 0
    iterations = 500000
    
    for i in range(iterations):
        pi_approx += ((-1) ** i) / (2 * i + 1)
    
    pi_approx *= 4
    
    # Round to 5 decimal places
    return round(pi_approx, 5)
