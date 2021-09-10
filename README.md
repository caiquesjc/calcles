# calcles
### Trabalho da Matéria *Laboratório de Engenharia de Software* 

---
#### Requisitos para rodar

----

* Python 3
* virtualenv
* Jinja2 3.0.1
* Flask 2.0.1



### Como iniciar o projeto
### __Processo feito em uma máquina com Windows 10__
---
Clone o repositório:
~~~
https://github.com/caiquesjc/calcles.git
~~~

Abra um terminal na pasta _src_
<br>
Crie um _ambiente virtual_ com o comando:

~~~
virtualenv venv
~~~

---
Ative o ambiente

Se usar cmd:
~~~
cd venv/Scripts && activate
~~~
Se usar powershell:
~~~
cd venv/Scripts
~~~
depois
~~~
 ./activate
~~~

Navegue até a página _src_ e instale as dependências:
--- ---
~~~
pip install -r requirements.txt
~~~


## Executar

Execute no terminal dentro da pasta _src_
~~~
python app.py
~~~
_copie o endereço ip e porta que está sendo exibido no terminal e cole no navegador_ 