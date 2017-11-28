import re
import sys

try:
    file = open("D:\CSMM\L20171109.log")
    filename=file.name
    text = file.read()
    file.close()
except IOError:
    sys.exit("Brak pliku!!!!")
filename=filename.split("\\")
print("Pobrany plik nazywa się: %s" %(filename[len(filename)-1]))
print("Wczytany plik zawiera %d znaków." % len(text))
numerator,line_amount, line_digits, digits, input_liness_long, occurings=1,0,0,0,0,0
input_text=str(input('Wprowadź szukane słowo:'))
print("Wprowadziłeś słowo to: %s" %input_text)
input_liness_long=int(input('Wprowadź długość szukanej linii:'))
for line in (text.split("\n")):
    line_digits=re.search("[0-9]", line)
    liness_long = len(line)
    occurings=occurings+line.count(input_text)
    if occurings>0:
        line_amount+=1
    if line_digits is not None:
        digits+=1
    if input_liness_long==liness_long:
        print("To jest linia zawierająca %d znaków: %s" %(liness_long, line))
    numerator+=1
print("Słowo %s pojawiło się w tekście %d razy w %d liniach. Ilość wierszy z liczbami to: %s"%(input_text, occurings, line_amount, digits))