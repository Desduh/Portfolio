# Exemplificando a Implantação utilizando o Heroku

## Fabrício Galende M. de Carvalho

Para testar e implantar esse sistema:

I. Teste de execução local:
1. Clonar o repositório
2. Criar um ambiente virtual
```console
virtualenv env
```
3. Ativar o ambiente virtual (no windows o arquivo é o .bat):
```console
env/Scripts/activate.bat
```
4. Instalar as dependências:
```console
pip install -r requirements.txt
```
5. Executar a aplicação
```console
python src/app.py
```

II. Implantar no Heroku (supondo que já tenha a conta na plataforma)

1. Efetuar o login no Heroku
```console
heroku login
```
2. Criar uma aplicação / repositório remoto do Heroku
```console
heroku create nome-sua-aplicacao
```
3. Vincular ao repositório do Git o repositório do Heroku
```console
heroku git:remote -a meu-sistema
```
4. Enviar ao repositório do Heroku o conteúdo do repo local
```console
git push heroku master:main
```



