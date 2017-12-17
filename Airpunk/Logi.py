#-*-coding: utf-8-*-
def logowanie_zdarzen(do_logu=""):
    import re
    import datetime

    airpunklog = open("D:\\airpunk.log", "a")

    if type(do_logu) is dict or list:
        airpunklog.write(str(datetime.datetime.now()) + " " +  str.replace(str(do_logu),"{","").replace("}","") +"\n")
    else:
        airpunklog.write(str(datetime.datetime.now()) + " " + do_logu)
    airpunklog.close()
    print(do_logu)
    return ("Zapisałem i wyprintowałem")

