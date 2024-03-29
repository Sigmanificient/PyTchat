# Python Tchat

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Sigmanificient/PyTchat/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/Sigmanificient/PyTchat/?branch=main)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Sigmanificient/PyTchat)
![GitHub repo size](https://img.shields.io/github/repo-size/Sigmanificient/PyTchat)
![Lines of code](https://img.shields.io/tokei/lines/github/Sigmanificient/PyTchat)
![GitHub last commit](https://img.shields.io/github/last-commit/Sigmanificient/PyTchat)
![Github](https://shields.io/github/license/Sigmanificient/PyTchat)
![gitmoji](https://img.shields.io/badge/gitmoji-%20🚀%20💀-FFDD67.svg)

### A simple texts communication platform using pygame and sockets.

## How to install ?
*You need a python 3.8.6 server with at least one opened port*

- Download the source code from this repo.

### Server

- Run the Makefile main target.
  ```bash
  make server
  ```

### Or

```bash
cd server
```

- Install the required python packages
  ```bash
  python -m pip install requirements.txt
  ```  

- run the server using the `bat` file, the `sh` file or this command
  below:
  ```bash
  python -m pytchat [port]
  ```

### Client

- Make sure to have `node.js` installed on your computer.
- Download the source code from this repo.

- Run the client using
  ```sh
  make client
  ```

#### Or

```bash
cd client
```

- Install the required dependencies
  ```sh
  npm install
  ```

- Run the client using
  ```sh
  npm serve
  ```
