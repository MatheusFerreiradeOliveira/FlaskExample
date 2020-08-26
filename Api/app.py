from flask import Flask, jsonify, request

app = Flask(__name__)

pokemons = [
    {
        "id": 1,
        "nome": "Charizard",
        "tipo": "Fogo",
        "ataque": "Rajada de fogo"
    },
    {
        "id": 2,
        "nome": "Pikachu",
        "tipo": "Trovão",
        "ataque": "Rajada do trovão"
    },
    {
        "id": 3,
        "nome": "Squirtle",
        "tipo": "Água",
        "ataque": "Rajada de água"
    }
]

newId = 4

@app.errorhandler(404)
def not_found(error):
    print('error', error)
    return jsonify({'error': 'Not found'}), 404

@app.route('/pokemons', methods=['GET'])
def get_all():
    allPokemons = [pokemon for pokemon in pokemons if pokemon['id'] != -1]
    return jsonify(allPokemons)

@app.route('/pokemons/<int:pokemon_id>', methods=['PUT'])
def put_one(pokemon_id):
    pokemon = [pokemon for pokemon in pokemons if pokemon['id'] == pokemon_id]
    data = (request.get_json());
    if(data['nome'] != None):
        pokemon[0]['nome'] = data['nome']
    if(data['ataque'] != None):
        pokemon[0]['ataque'] = data['ataque']
    if(data['tipo'] != None):
        pokemon[0]['tipo'] = data['tipo']
    return jsonify({'pokemon': pokemon[0]})

@app.route('/pokemons/<int:pokemon_id>', methods=['DELETE'])
def delete_one(pokemon_id):
    pokemon = [pokemon for pokemon in pokemons if pokemon['id'] == pokemon_id]
    pokemon[0]['id'] = -1;
    return jsonify({"Message": "Deletado com sucesso"})

@app.route('/pokemons', methods=['POST'])
def new_pokemon():
    data = request.get_json();
    newPokemon = {
        'id': len(pokemons) + 1,
        'nome': data['nome'],
        'tipo': data['tipo'],
        'ataque': data['ataque']
    }
    pokemons.extend([newPokemon])
    return jsonify({"Lista de pokemon": pokemons})

if __name__ == '__main__':
    app.run()