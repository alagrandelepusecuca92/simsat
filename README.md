# simsat
Satellite Simulator Game in python
git clone https://github.com/alagrandelepusecuca92/simsat

# Configuración del entorno de trabajo

Dependencias: vitrualenv
$ sudo apt-get install virtualenv

simsat/$ virtualenv -p python3 venv

# Primeros pasos sobre el entorno de trabajo
simsat/$ source venv/bin/activate
(venv) simsat/$ pip install ipython
(venv) simsat/$ python
```
>>> print("Hola")
```
(venv) simsat/$ ipython

```
In [1]: print('Hola')
In [2]: print("""Hola jose
   ...: como andas?""")
Hola jose
como andas?
```

# Como trabajar con git

simsat (master)$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	simsat.py
	venv/

no changes added to commit (use "git add" and/or "git commit -a")
simsat (master)$ git checkout -b logo_loco
simsat (logo_loco)$ git add simsat.py
simsat (logo_loco)$ git commit -m 'Agrego el logo del simsat'
simsat (logo_loco)$ git push --set-upstream origin logo_loco # Para pushear a un nuevo branch la primera vez en el repositorio remoto
