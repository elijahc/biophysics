
def human_bmr(body_mass, height, age, sex='male'):
    """Returns human basal metabolic rate
    Parameters
    ----------
    body_mass : float
        body_mass in kg
    height : float 
        Height in cm

    age : float
        Age in years

    sex : str
        One of 'male' or 'female'

    Returns
    -------
    bmr : float 
        Basal metabolic rate in kcal/day
    """
    if sex == 'male':
        return 66.4730 + (13.7516*body_mass) + (5.0033*height) + (6.75505*age)
    elif sex == 'female':
        return 655.0955 + (9.5635*body_mass) + (1.8496*height) + (4.6756*age)
    else:
        print("sex of '{}' not valid, must be 'male' or 'female'")

