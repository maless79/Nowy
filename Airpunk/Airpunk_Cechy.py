


def cechy_postaci(refleks=1,cialo=1):
    nadmiar=0
    if refleks>10:
        nadmiar=nadmiar+(refleks-10)
        refleks=10
    if cialo>10:
        nadmiar=nadmiar+(cialo-10)
        cialo=10

    return(refleks,cialo,nadmiar)


print(cechy_postaci(12,15))

