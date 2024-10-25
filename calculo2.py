from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sexo', methods=['POST'])
def sexo():
    # Coleta os dados do formulário
    sexo = request.form['sexo']
    peso = float(request.form['peso'])
    altura = float(request.form['altura']) * 100  # Converter altura para cm
    idade = int(request.form['idade'])

    # Calcular TMB (Taxa Metabólica Basal) com base no sexo
    if sexo == "M":
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    elif sexo == "F":
        tmb = (10 * peso) + (6.25 * altura) - (5 * idade) - 161

    # Coleta o nível de atividade e ajusta a TMB
    atividade = request.form['atividade']
    if atividade == "S":
        calorias = tmb * 1.2
    elif atividade == "L":
        calorias = tmb * 1.375
    elif atividade == "M":
        calorias = tmb * 1.55
    elif atividade == "A":
        calorias = tmb * 1.725
    elif atividade == "E":
        calorias = tmb * 1.9

    # Ajusta para ganho ou perda de peso
    objetivo = request.form['objetivo']
    if objetivo == "G":
        calorias += 500
    elif objetivo == "P":
        calorias -= 500

    # Exibe o resultado na página
    return render_template('index.html', resultado=round(calorias, 2))

if __name__ == '__main__':
    app.run(debug=True)
