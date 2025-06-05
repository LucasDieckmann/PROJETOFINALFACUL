from flask import Flask, jsonify
from sqlite import session, Brawlhalla

app = Flask(__name__)

@app.route('/personagens', methods=['GET'])
def get_personagens():
    personagens = session.query(Brawlhalla).all()
    resultado = []
    for p in personagens:
        resultado.append({
            'id': p.id,
            'personagem': p.personagens,
            'preco': p.preco,
            'forca': p.forca,
            'defesa': p.defesa,
            'destreza': p.destreza,
            'agilidade': p.agilidade,
            'armaum': p.armaum,
            'armadois': p.armadois
        })
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
