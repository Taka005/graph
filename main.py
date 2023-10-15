import sympy as sp
import numpy as np
from flask import Flask, request, send_file
import io

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    formula = request.args.get("formula").split(",")

    x = sp.Symbol("x")

    if len(formula) == 1:
        img = sp.plotting.plot(formula[0],(x,-3,3),legend=True,show=False)
    elif len(formula) == 2:
        img = sp.plotting.plot(formula[0],formula[1],(x,-3,3),legend=True,show=False)
    elif len(formula) == 3:
        img = sp.plotting.plot(formula[0],formula[1],formula[2],(x,-3,3),legend=True,show=False)

    file = io.BytesIO()
    img.save(file)
    file.seek(0)
    return send_file(file,mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000)
