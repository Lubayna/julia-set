# ジュリアセット
このウェブアプリケーションは、PythonとJavaScriptを使用してジュリアセットを生成し表示するものです。
Python、JavaScriptを用いてジュリア集合の生成と描画をするウェブサイトアプリケーションを作成した。

## 使用方法

アプリケーションにアクセスするには、[http://localhost:8080/satori/julia]にアクセスし、適切な入力値を入力し、「ジュリアセットを描画する」ボタンをクリックして、指定されたカラーマップを使用してジュリアセットを表すグラフを表示します。不適切な値が入力された場合は、エラーがアラートで表示されます。

## 動作チェック

https://user-images.githubusercontent.com/56100529/221092164-b08d6fb7-4a1c-4cca-9d74-3e90776012ce.mov


## 構築環境

* Backend: Python 3.9.15
* Frontend: HTML Javascript CSS
* Web Application Framework: Flask 2.0.3
* JavaScriptはChromeバージョン110.0.5481.100でテストされました。

## ファイルの構成

  - backend.py
  - templates
    - index.html
  - static
    - scripts
        - myscript.js
    - styles
        - mystyle.css

## バックエンドとフロントエンドの説明

### バックエンド

　以下のパラメータを含むJavaScriptからJSONデータを受信します。
  - 実数部最小値min_x、
  - 実数部最大値max_x、
  - 虚数部最小値min_y、
  - 虚数部最大値max_y、
  - 複素定数comp_const
  - 反復回数max_iter
  - 幅width
  - 高さheight
  - Pythonのmatplotlibの配色colormap
  
 受信したパラメータに基づいて、エラーチェックし、エラーがあれば、エラーメッセージを返します。エラーがなければ、バックエンドは収束/発散のしきい値2で生成するジュリアセット、指定した配色のcolormapに基づいて生成するmax_iter範囲のRGBhex二進数表記のカラーバー、グラフの幅と高さを返します。

### フロントエンド

  - HTMLの受け持つ部分
    - 以下の値が入力可能である
    - 実数部最小値min_x、
    - 実数部最大値max_x、
    - 虚数部最小値min_y、
    - 虚数部最大値max_y、
    - 複素定数comp_const
    - 反復回数max_iter
    - 幅width
    - 高さheight
    - 以下の値が選択可能である
    - Pythonのmatplotlibの配色colormap: coolwarm、viridis、PiYG、PuOr、twilight、Spectral、RdGy

  以上の入力フォームはCSSが使用されてスタイルが適用されます。

  - HTMLの「ジュリアセットを描画する」ボタンを押すと、フロントエンドはJavaScriptファイル内の関数を呼び出し、Ajaxを使用してバックエンドと通信し、パラメータを送信します。バックエンドはエラーメッセージを返すか、ジュリアセット、カラーバーとグラフの幅と高さを返します。エラーメッセージが返される場合は、エラーメッセージがアラートで表示されます。ジュリアセット、カラーバーとグラフの幅と高さが返される場合は、指定配色のジュリアセットグラフを表現するキャンバスが作成され、作成したキャンバスがDOMに追加されます。



