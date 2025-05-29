def  Convert_Persian_numbers_to_English(txt):
    persian_engilsh = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9'
    }
    for i in txt:
        print(persian_engilsh.setdefault(i,i),end='')
def execution():
    txt = input()
    Convert_Persian_numbers_to_English(txt)

execution()
