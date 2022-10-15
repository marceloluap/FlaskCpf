
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def CPF():
    variavel = 'Insira o número no formato padrão xxx.xxx.xxx-xx ou apenas números'
    ValorCPF = request.form.get("ValorCPF")

    if request.method == 'GET':
        return render_template("CPF.html", variavelPagina=variavel)

    else:
        chars = ["1","2","3","4","5","6","7","8","9","0"]
        numeros_cpf = ""

        for numeros in ValorCPF:
            if numeros in chars:
                numeros_cpf += numeros

        entrada = numeros_cpf

        # quantidade de caracteres digitados
        if len(ValorCPF) > 14 or len(entrada) < 11 or len(entrada) > 11:
            return render_template("CPF.html", resultado='CPF INVÁLIDO')

        # verificar os dígitos são iguais
        else:
            valid = 0
            for digito in range(0, 11):
                valid += int(entrada[digito])
                digito += 1
            if int(entrada[0]) == valid / 11:
                return render_template("CPF.html", resultado='CPF INVÁLIDO')

            # cálculos do dígito para verificar do CPF
            else:
                # verificação do décimo dígito
                soma = 0
                count = 10
                for i in range(0, len(entrada)-2):
                    soma = soma + (int(entrada[i])*count)
                    i+=1
                    count-=1
                digito1 = 11-(soma%11)
                if digito1 >= 10:
                    digito1 = 0

                # verificação do 11º dígito verificador
                soma = 0
                count = 10
                for j in range(1, len(entrada)-1):
                    soma = soma + (int(entrada[j])*count)
                    j+=1
                    count-=1
                digito2 = 11-(soma%11)
                if digito2 >= 10:
                    digito2 = 0

                # mensagem ao usuário
                if int(entrada[9]) != digito1 or int(entrada[10]) != digito2:
                    return render_template("CPF.html", resultado='CPF INVÁLIDO')
                else:
                    return render_template("CPF.html", resultado='CPF VÁLIDO')

            







@app.route("/<string:nome>")    
def erro(nome):
    variavel = f'Página ({nome}) não encontrada.'
    return render_template("erro.html", variavelPagina=variavel)

if __name__ == "__main__":
    app.run(debug=True)


