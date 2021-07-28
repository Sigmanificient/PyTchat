# Python Tchat

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Sigmanificient/PyTchat/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/Sigmanificient/PyTchat/?branch=main)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Sigmanificient/PyTchat)
![GitHub repo size](https://img.shields.io/github/repo-size/Sigmanificient/PyTchat)
![Lines of code](https://img.shields.io/tokei/lines/github/Sigmanificient/PyTchat)
![GitHub last commit](https://img.shields.io/github/last-commit/Sigmanificient/PyTchat)
![Github](https://shields.io/github/license/Sigmanificient/PyTchat)

### A simple texts communication platform using pygame and sockets.

## How to install ?
*You need a python 3.8.6 server with at least one opened port*

- Download the source code from this repo.

### Server
- In your server, copy the `main.py` file from the `server` directory.
  
- Create a `.env` file and write which port you want to listen on as
  the `env.example` file.

- Install the required python packages
  ```bash
  python -m pip install requirements.txt
  ```  

- run the server using the `bat` file, the `sh` file or this command
  below:
  ```bash
  python -m python -m main.py
  ```

### Client

- On your local computer, open the `main.py` file from the `client` 
  directory.
  
- Create a file `.env` and write the address and port of your server 
  as the `.env.example` file.

- Install the required python packages
  ```bash
  python -m pip install requirements.txt
  ```

 - Run the client ( `main.py` )
