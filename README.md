# Documentation

- [INTRODUCE WITH MINIFRAMEWORK DOTPY](#mini-framework-dotpy)
- [INSTALLATION](#installation)
- [QUICK START](#quick-start)
  - [CREATE PROJECT FILE](#create-project-file)
  - [REMOVE PROJECT FILE](#remove-project-file)
  - [RUNNING PROJECT]("#running-project")
- [LICENSE](https://github.com/Nofrisdan/mini-framework-dot-py/blob/main/LICENSE)

# MINI FRAMEWORK DOTPY

`Mini Framework DOTPY` is an MVC-based open source mini framework,, built using the Python programming language.

# INSTALLATION

1. CLONE MINI FRAMEWORK DOTPY

```
git clone https://github.com/nofrisdan/mini-framework-dotpy.git

```

2. INSTALL & SETUP VIRTUALENV

run the command below in the terminal / command line

- install

```
pip install virtualenv

```

- setup

```
python -m venv venv

```

```
venv\bin\activate # run in unix

venv\Scripts\activate # run in windows
```

3. INSTALL LIBRARY

```
pip install requirements.txt

```

# QUICK START

If you want to see all the CLI commands that can be used, please run the command below :

```
python cli.py --help

```

## Create Project File

```
python cli.py -m <yourfilename>

```

## Remove Project File

```
pyton cli.py -r <yourfilename>
```

## Running Project

```
python cli.py --serve main

```

If you see that the server is running well, please access `http://localhost:8000/docs` in your browser
