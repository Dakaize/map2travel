from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        # 替换为您的高德地图API Key
        api_key = "fd3aea9f353fbb311da1693d39a2dc3b"

        html_content = f"""
        <!doctype html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="initial-scale=1.0, user-scalable=no, width=device-width">
            <title>地图显示</title>
            <style>
                html, body, #container {{
                    width: 100%;
                    height: 100%;
                    margin: 0;
                    padding: 0;
                }}
            </style>
        </head>
        <body>
        <div id="container"></div>
        <script src="https://webapi.amap.com/maps?v=1.4.15&key={api_key}"></script>
        <script>
            var map = new AMap.Map('container', {{
                resizeEnable: true,
                zoom: 18,
                center: [118.709676, 32.197838]
            }});
        </script>
        </body>
        </html>
        """

        self.browser.setHtml(html_content)
        self.setWindowTitle("高德地图")
        self.resize(1920, 1080)


if __name__ == '__main__':
    app = QApplication([])
    window = MapWindow()
    window.show()
    app.exec_()