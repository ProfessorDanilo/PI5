# website_PI2
Site desenvolvido para o Projeto Integrador 2

### Clonando o repositório:

No terminal, digite:
  ```bash 
  $ mkdir ~/git

  $ git clone https://github.com/ProfessorDanilo/pi5.git

  (digite suas credenciais)

  $ cd ~/git/website
  ```

### Para criar um ambiente virtual:
  ```bash 
  
  sudo python3 -m venv ~/git/pi5/venv
  
  source ~/git/pi5/venv/bin/activate
  ```

### Para instalar pacotes necessários:
  ```bash 
  
  pip install flask

  pip install sqlalchemy

  pip install flask-sqlalchemy
  ```

### Para atualizar o repositório:
  ```bash 
  git pull
  ```

### Antes de rodar exporte as seguintes variáveis de ambiente:
  ```bash
  export FLASK_APP=app
  export FLASK_ENV=development
  ```
### Para rodar o servidor:
  ```bash
  flask run
  ```
 Acessar o endereço 127.0.0.1:5000 de execução no navegador de internet.
 
 
