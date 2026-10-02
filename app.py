from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def calculo():
    nome = None
    imc = None
    faixa = None

    if request.method == 'POST':
        nome = request.form.get('nome')
        peso = float(request.form.get('peso'))
        altura = float(request.form.get('altura'))
    
        imc = peso / (altura **2)

        if imc <=17.30:
            faixa = 'Abaixo do Peso'
        elif imc < 27.86 and imc > 17.30:
            faixa = 'Peso normal'
        elif imc < 34.60 and imc > 27.86:
            faixa = 'Sobre Peso'
        else:
            faixa = 'Obesidade'

        resultado = {
            'nome': nome,
            'imc': imc,
            'faixa': faixa,
        }


    return render_template('index.html', nome=nome, imc=imc, faixa=faixa)

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

if __name__ == '__main__':
    app.run(debug=True)