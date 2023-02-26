from flask import Flask, render_template,request, jsonify
import numpy as np
import json
import matplotlib as mpl
import matplotlib.cm as cm
from pylab import *
#from flask_cors import CORS
app = Flask(__name__)

@app.route('/satori/julia', methods=["GET"])
def index():
    return render_template('index.html')
#CORS(app)
@app.route('/', methods=["POST"])
def julia_result_post():
    # POST送信の処理
    try:
        # 入力フォームのデータをとる
        data = request.json
        min_x = data.get('min_x')
        max_x = data.get('max_x')
        min_y = data.get('min_y')
        max_y = data.get('max_y')
        colormap = data.get('colormap')
        width = data.get('width')
        height = data.get('height')
        max_iter = data.get('max_iter')
        comp_const = data.get('comp_const')
        comp_x = comp_const[0]
        comp_y = comp_const[1]

        # 適切ではない入力のエラー処理
        if min_x == None: return jsonify({'error': '最小実数部は数値でなければなりません'})
        if max_x == None: return jsonify({'error': '最大実数部は数値でなければなりません'})
        if min_y == None: return jsonify({'error': '最小虚数部は数値でなければなりません'})
        if max_y == None: return jsonify({'error': '最大虚数部は数値でなければなりません'})
        if width == None: return jsonify({'error': '幅は整数でなければなりません'})
        if height == None: return jsonify({'error': '高さは整数でなければなりません'})
        if max_iter == None: return jsonify({'error': '反復回数は整数でなければなりません'})
        if comp_x == None: return jsonify({'error': '複素定数実数部は数値でなければなりません'})
        if comp_y == None: return jsonify({'error': '複素定数虚数部は数値でなければなりません'})
        if min_x >= max_x:
            return jsonify({'error': '最小実数部は最大実数部より小さくなければなりません'})
        if min_y >= max_y:
            return jsonify({'error': '最小虚数部は最大虚数部より小さくなければなりません'})

        # 収束/発散のしきい値2でジュリアセットの生成
        x = np.linspace(min_x, max_x, width)
        y = np.linspace(min_y, max_y, height)
        z = x + y[:, np.newaxis] * 1j
        m = np.zeros((height, width))
        for i in range(max_iter):
            z = z * z + complex(comp_x, comp_y)
            m[np.abs(z) > 2] = i
        
        # 指定した配色のmax_iter種類の色のrgbhexを含む2進数のカラーバーを生成する
        color_bar = []
        cmap = cm.get_cmap(colormap, max_iter)  
        for i in range(cmap.N):
            rgba = cmap(i)
            color_bar.append(int(mpl.colors.rgb2hex(rgba)[1:], base=16))
        
        # グラフの幅と高さ、ジュリアセット、カラーバーを返す
        return jsonify({ "width": width, "height": height, "julia_set": json.dumps(m.tolist()), "colors": json.dumps(color_bar) })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.debug = False
    app.run(port=8080, host='localhost')
