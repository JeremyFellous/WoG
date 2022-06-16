from flask import Flask
from WoG.Utils import SCORES_FILE_NAME

# print(f"WoG/{SCORES_FILE_NAME}")

app = Flask(__name__)


@app.route('/')
def show_score():
    try:
        with open(f"C:\\Users\\PC\\PycharmProjects\\pythonProject\\1803\\WoG\\{SCORES_FILE_NAME}", 'r') as f:
            score = f.read()
            return f"""
    <!DOC TYPE html>
    <html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1>The score is <div id="score">{score}</div></h1>
    </body>
    </html>
    """
    except FileNotFoundError:
        return """"
<!DOC TYPE html>
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
    <body>
        <h1><div id="score" style="color:red">{ERROR}</div></h1>
    </body>
</html>
"""


if __name__ == '__main__':
    app.run(host='0.0.0.0')
