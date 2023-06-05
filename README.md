## Projeto criado para realizar a documentaçãodas das criações de tabelas que utilizam como padrão outras tabelas, fazendo assim o uso da linguagem sql para tal ação
* Para que você consiga emular o nosso projeto é necessario que contenha o interpretador do Python e do Angular. <p>
##### 🚨 se atente de ter a biblioteca do Flask e Docx no python,elas que iram possibilitar você de criar o servidor local e gerar tal documentação.
~~~
Servidor_Python: Dentro da respectiva pasta, você irá encontrar um arquivo denominado servidor.py, onde será
o principal responsavel por realizar a criação de um servidor em sua maquina local utilizando a biblioteca flask
~~~
  
~~~
Servidor_Angular:
~~~
  
>**Entenda que este projeto necessita que você realize a criação de 2 servidores, onde o servidor do angular irá fazer a comunicação com o servidor do python utilizando o HTTP Request**<p>
>Fluxo:
>>**Angular:** Utilizado para pegar o codigo sql passado pelo usuario e envia-lo para o servidor flask, com isso recebe um arquivo .docx de retorno e faz com que o usuario realize o download. <p>
>
>>**Python:** Recebe o texto enviado pelo servidor do angular e realiza tratamentos para que seja criado o arquivo documentacao.docx e retorna para o mesmo<p>
  
## Como Rodar?
  
1. Salve todos os arquivos em sua maquina local e instale as bibliotecas informadas anteriormente.
* Navegue para "Projeto/Servidor_Python/"
2. Execute o arquivo servidor.py com o devido interpretador e aguarde o servidor subir em sua rede
* Apos isso vá para: "Projeto/Servidor_Angular/"
3.
*
  
  
  
<div style="display: inline_block"><br>
<img align="center" alt="Python" height="40" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
<img align="center" alt="-Csharp" height="40" width="40" src="https://cdn.freebiesupply.com/logos/large/2x/angular-icon-logo-png-transparent.png">
</div>
