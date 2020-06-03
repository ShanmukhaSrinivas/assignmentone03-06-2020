from flask import Flask, render_template, request
import requests
import json
import urllib.request

app = Flask(__name__)


@app.route('/total')
def input():
    day = request.args.get('day')
    d = day.split('-')[::-1]
    d = '-'.join(d)
    source = urllib.request.urlopen(
        'https://assignment-machstatz.herokuapp.com/excel').read()
    list_of_data = json.loads(source)
    total_len = 0
    total_quantity = 0
    total_weight = 0
    for i in range(1,len(list_of_data)):
        if d in list_of_data[i]["DateTime"]:
            total_len+=list_of_data[i]["Length"]
            total_quantity+=list_of_data[i]["Quantity"]
            total_weight+=list_of_data[i]["Weight"]
    res = {"totalWeight":total_weight,"totalLength":total_len,"totalQuantity":total_quantity}
    res = json.dumps(res)

    return res


if __name__ == '__main__':
    app.run()
