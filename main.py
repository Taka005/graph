import sympy as sp
import numpy as np
from flask import Flask, request, send_file
import matplotlib.pyplot as plt
import japanize_matplotlib
import io

app = Flask(__name__)

@app.route("/",methods=["GET"])
def main():
    formula = request.args.get("formula").replace(" ","+").split(",")

    x = sp.Symbol("x")

    if len(formula) == 1:
        img = sp.plotting.plot(formula[0],(x,-8,8),ylim=(-8,8),legend=True,show=False)
    elif len(formula) == 2:
        img = sp.plotting.plot(formula[0],formula[1],(x,-8,8),ylim=(-8,8),legend=True,show=False)
    elif len(formula) == 3:
        img = sp.plotting.plot(formula[0],formula[1],formula[2],(x,-8,8),ylim=(-8,8),legend=True,show=False)

    file = io.BytesIO()
    img.save(file)
    file.seek(0)
    return send_file(file,mimetype="image/png")

@app.route("/line",methods=["POST"])
def line():
    data = request.get_json()

    plt.plot(data["x"],data["y"],color="red")
    plt.title(data["title"])
    plt.xlabel(data["xLabel"])
    plt.ylabel(data["yLabel"])
    plt.grid(True)
    plt.tick_params(axis="x",labelsize=data.get("xFont") or 12)
    plt.tick_params(axis="y",labelsize=data.get("yFont") or 12)

    file = io.BytesIO()
    plt.savefig(file,format="png")
    plt.clf()
    plt.cla()
    plt.close()

    file.seek(0)
    return send_file(file,mimetype="image/png")

@app.route("/pie",methods=["POST"])
def pie():
    data = request.get_json()

    plt.pie(data["data"],startangle=90,autopct="%.1f%%",counterclock=False,pctdistance=0.8,labels=data["label"],labeldistance=1.1,colors=data["color"])

    plt.title(data["title"],fontsize=18)

    file = io.BytesIO()
    plt.savefig(file,format="png")
    plt.clf()
    plt.cla()
    plt.close()
    file.seek(0)
    return send_file(file,mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000)