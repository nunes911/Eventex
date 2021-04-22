# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositorio
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependencias.
5. COnfigue a instancia com o .env
6. Execute os testes.

```console
git clone git@github.com:meugit wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma intancia no heroku
2. Envia as configuracoes parra o heroku.
3. Define uma SECRET_KEY segura para instancia.
4. Defina DEBUG=False.
5. Configure

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```