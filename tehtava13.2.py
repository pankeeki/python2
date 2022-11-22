from flask import Flask
import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='Sanni',
    autocommit=True
)

app = Flask(__name__)


@app.route('/kentta/<icao>')
def funktio(icao):
    sql = f"SELECT name, municipality from airport where icao =%s"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()
    vastaus = {'nimi:', tulos[0]}
    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)