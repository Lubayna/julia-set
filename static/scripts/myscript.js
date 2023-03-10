async function clickedButton() {
    // ジュリアセットを描画するためのレスポンスデータを取得
    const data = await getJuliaData()
    if (data.error) {
        alert(`エラー: ${data.error}`)
        return
    }
    // レスポンスデータがエラーではない時、canvasに描画する
    const canvas = createCanvas(data)
    // 描画したcanvasをjuliaDiagramブロックに追加する
    addCanvas(canvas)
}

// 描画したcanvasを載せるjuliaDiagramをpresenterに追加する関数
function addCanvas(canvas) {
    const old = document.getElementById("juliaDiagram")
    // canvasを追加する時、もし古いcanvasがあれば、まず消す
    if (old !== null) {
        old.remove()
    }
    const c = document.createElement('div')
    c.setAttribute("id", "juliaDiagram")
    c.appendChild(canvas)
    document.getElementById("presenter").appendChild(c)
}

// バックエンドと通信し、パラメータを送信、レスポンスを取得する関数
async function getJuliaData() {
    const min_x = Number(document.getElementById("min_x").value)
    const max_x = Number(document.getElementById("max_x").value)
    const min_y = Number(document.getElementById("min_y").value)
    const max_y = Number(document.getElementById("max_y").value)
    const comp_const = JSON.parse("[" + document.getElementById("comp_const").value + "]")
    const max_iter = Number(document.getElementById("max_iter").value)
    const width = Number(document.getElementById("width").value)
    const height = Number(document.getElementById("height").value)
    const colormap = document.getElementById("colormap").value

    return await fetch("http://localhost:8080/", {
        method: 'POST',
        mode: "cors",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            min_x,
            max_x,
            min_y,
            max_y,
            comp_const,
            max_iter,
            width,
            height,
            colormap
        })
    }).then((response) => response.json())
    .catch((error) => {
        alert(`エラー: ${error}`)
    })
}

// レスポンスデータに基づいてジュリアセットをcanvasに描画する関数
function createCanvas(data) {

    const canvas = document.createElement('canvas')
    var julia_matrix = JSON.parse(data.julia_set)
    var colors = JSON.parse(data.colors)
    canvas.width = data.width
    canvas.height = data.height
    const ctx = canvas.getContext('2d')
    for (let i = 0; i < julia_matrix.length; i++) {
        julia_arr = julia_matrix[i]
        for (let j = 0; j < julia_arr.length; j++) {
            julia_num = julia_arr[j]
            var color = colors[julia_num]
            // カラーバーに基づいて色をcanvasに描画
            ctx.fillStyle = `#${color.toString(16)}`
            ctx.fillRect(j,i,1,1)
        }
    }

    return canvas
}
