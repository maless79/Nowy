#-*-coding: utf-8-*-
def logowanie_zdarzen(do_logu=""):
    import re
    airpunklog = open("D:\\airpunk.log", "a")

    if type(do_logu) is dict or list:
        airpunklog.write(str(do_logu))
    else:
        airpunklog.write(do_logu)
    airpunklog.close()
    print(do_logu)
    return ("Zapisałem i wyprintowałem")

