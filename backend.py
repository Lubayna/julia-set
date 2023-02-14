from flask import Flask, render_template,request, jsonify
import numpy as np
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="名前を入力してください。")


@app.route('/julia', methods=["GET"])
def julia_result_post():
    # POST送信の処理
    min_x = request.args.get('min_x', type=float)
    max_x = request.args.get('max_x', type=float)
    min_y = request.args.get('min_y', type=float)
    max_y = request.args.get('max_y', type=float)
    comp_const = request.args.get('comp_const', type=str)
    comp_x, comp_y = list(map(float, comp_const.rstrip('\r\n').split(',')))
    width, height, max_iter = 1000, 1000, 100
    x = np.linspace(min_x, max_x, width)
    y = np.linspace(min_y, max_y, height)
    z = x + y[:, np.newaxis] * 1j
    m = np.zeros((height, width))
    for i in range(max_iter):
        z = z * z + complex(comp_x,comp_y)
        m[np.abs(z) > 2] = i

    return render_template('result.html', julia_set=json.dumps(m.tolist()), width=width, height=height, max_iter=max_iter)#, plot_url=plot_url)


if __name__ == '__main__':
    app.debug = False
    app.run(port=4000, host='localhost')