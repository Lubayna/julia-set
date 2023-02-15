from flask import Flask, render_template,request, jsonify
import numpy as np
import json
import matplotlib as mpl
from pylab import *
import sys
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/julia', methods=["GET"])
def julia_result_post():
    # POST送信の処理
    min_x = request.args.get('min_x', type=float)
    max_x = request.args.get('max_x', type=float)
    min_y = request.args.get('min_y', type=float)
    max_y = request.args.get('max_y', type=float)
    colormap = request.args.get('colormap', type=str)
    width = request.args.get('width', type=int)
    height = request.args.get('height', type=int)
    max_iter = request.args.get('max_iter', type=int)
    comp_const = request.args.get('comp_const', type=str)
    comp_x, comp_y = list(map(float, comp_const.rstrip('\r\n').split(',')))
  #  width, height, max_iter = 800, 600, 100
    x = np.linspace(min_x, max_x, width)
    y = np.linspace(min_y, max_y, height)
    z = x + y[:, np.newaxis] * 1j
    m = np.zeros((height, width))
    for i in range(max_iter):
        z = z * z + complex(comp_x,comp_y)
        m[np.abs(z) > 2] = i
    color_bar = []
    cmap = cm.get_cmap(colormap, max_iter)  # PiYG
    for i in range(cmap.N):
        rgba = cmap(i)
       # print(matplotlib.colors.rgb2hex(rgba), file=sys.stderr)
        color_bar.append(int(mpl.colors.rgb2hex(rgba)[1:], base=16))

    return render_template('result.html', julia_set=json.dumps(m.tolist()), colors=json.dumps(color_bar), width=width, height=height, max_iter=max_iter)#, plot_url=plot_url)


if __name__ == '__main__':
    app.debug = False
    app.run(port=4000, host='localhost')