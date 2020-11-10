# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import xlrd
from Template import Template, Criteria


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def parse():
    book = xlrd.open_workbook("resources/test.xlsx")
    sh1 = book.sheet_by_name("selection criteria")
    store = []
    colnames = {}
    templates = []
    for rx in range(0, sh1.ncols):
        colnames[sh1.row(1)[rx].value] = rx

    for i in range(2,sh1.nrows):
        t = Template()
        t.sequence = i-1
        t.templateCode = sh1.row(i)[colnames['Template Code']].value

        for j in range(0,sh1.ncols):
            if j == colnames['Template Code']:
                pass
            else:
                cr = Criteria(sh1.row(i)[j].value)
                cr.name = sh1.row(1)[j].value
                if cr.value != 'N/A':
                    t.criteria.append(cr)
        templates.append(t)

        #print(t.toJson())
    #test = [i.toJson() for i in templates]
    test = list(map(lambda t: t.toJson(), templates))
    print(*test)
    #print(f'data:',{*templates})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




