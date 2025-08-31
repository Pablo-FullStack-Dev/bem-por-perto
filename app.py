from flask import Flask, render_template, request, flash, redirect

# Explicação para quem não entende de Flask:
# Estaremos usando a biblioteca flask e função Flask e suas funções:

# render_template - em outras palavras iremos abrir a pasta templates e usar seus arquivos;

# request - seria requisitar. Usado em formulários, usaremos esses formularios para fazer o cadastro e o login do usuario;

# flash - seria uma 'notificação'. Todas vez que usarmos esse função uma noticação irá aparecer no arquivo html desejado;

# redirect - seria "redirecionar" e como o proprio nome diz ela redireciona para FUNÇÃO do arquivo html e não para pagina. Explicação: o render_template roda o arquivo html, mas o redirect roda a função: logo o render template roda o arquivo html, qualquer duvida me chama no zap.

# "app" = nome do arquivo python
app = Flask(__name__) #Nomei a variavel principal de app, igual o nome do arquivo, pois se mudarmos o nome do arquivo principal python mudar, teremos que mudar o nome da variavel principal. 

@app.route("/") # O "@" serve para "mencionar" a variavel principal. E toda vez que abrimos uma nova rota('route') temos que mencional por qual pagina devemos abrir.
def home(): # Para toda rota temos um definição, ou função se assim vc conseguir entender melhor. Nessa 'função' podemos colocar condições, variaveis e até paginas em html sendo escrita em python.
    return render_template('index.html') # para aqueles que não conhecem python. toda vez que crio uma função: o return cria o limite da função

if __name__ == '__main__': # o if e sua condição farão no arquivo python e o restante rodar
    app.run(debug=True)