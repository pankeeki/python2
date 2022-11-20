from flask import Flask

app = Flask(__name__)


@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    isPrime = True

    if luku == 2:
        isPrime = True
    else:
        for x in range(2, luku, 1):
            if luku % x == 0:
                isPrime = False
                break
    if isPrime == True:
        vastaus = {
            "Numero": luku,
            "isPrime": True,
        }
        return vastaus
    else:
        vastaus = {
            "Numero": luku,
            "isPrime": False,
        }
        return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
