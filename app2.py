from flask import Flask, render_template, request, send_file
import requests
import json
import urllib.request
from openpyxl import Workbook

app = Flask(__name__)


@app.route('/excelreports')
def input1():
    wb = Workbook()
    filepath = "excelreport.xlsx"
    sheet = wb.active
    wb.remove(wb.get_sheet_by_name('Sheet'))
    source = urllib.request.urlopen(
        'https://assignment-machstatz.herokuapp.com/excel').read()
    list_of_data = json.loads(source)
    data = []
    j = 0
    while True:
        i = 1
        if len(list_of_data) > 2:
            j += 1
            name = 'Sheet '+str(j)
            wb.create_sheet(name)
            sheet = wb.get_sheet_by_name(name)
            res = [("DateTime", "Length", "Quantity", "Weight")]
            day = list_of_data[1]["DateTime"][:11]
            d = len(list_of_data)
            while i < d:
                temp = []
                if day in list_of_data[i]["DateTime"]:
                    #print("Hello")
                    temp.append(list_of_data[i]["DateTime"])
                    temp.append(list_of_data[i]["Length"])
                    temp.append(list_of_data[i]["Quantity"])
                    temp.append(list_of_data[i]["Weight"])
                    res.append(tuple(temp))
                    list_of_data.pop(i)
                    d -= 1
                else:
                    i += 1
                    continue
            for row in res:
                sheet.append(row)

        else:
            break
    wb.save(filepath)
    return send_file(filepath,as_attachment=True)


if __name__ == '__main__':
    app.run()
