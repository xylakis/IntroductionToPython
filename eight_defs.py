def adjust_vat_eu(european_country):

    global fpa 

    if (european_country == 'Luxemburg'):
        fpa = 0.17
        return fpa
    elif (european_country == 'Hungary'):
        fpa = 0.27
        return fpa
    elif (european_country == 'Germany'): 
        fpa = 0.19 
        return fpa
    elif (european_country == 'Italy'):
        fpa = 0.22
        return fpa
    else:
        fpa = 0.24
        return fpa