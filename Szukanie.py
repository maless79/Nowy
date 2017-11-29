#-*-coding: utf-8-*-
import re
import sys
import codecs
code ="utf-8"
try:
    typed_input=str(input("Wprowadź ścieżkę do pliku (np.: c:\Windows\):"))
    typed_file_name=input("Wprowadź nazwę pliku (np.: plik.txt):")
    print("Wprowadzona ścieżka do pliku to %s." %(typed_input+typed_file_name))
    file = codecs.open((typed_input+typed_file_name),"r",encoding=code)
    filename=str(file.name)
    text = file.read()
    file.close()
except IOError:
    sys.exit("Brak pliku!!!!")
filename=filename.split('\\')
print("Pobrany plik nazywa się: %s" %(filename[len(filename)-1]))
print("Wczytany plik zawiera %d znaków." %len(text))
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