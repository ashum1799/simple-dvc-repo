import os

os.path.join
dirs =[
    os.path.join('data','raw'),
    os.path.join('data','process'),
    os.path.join('notebooks'),
    os.path.join('saved_models'),
    os.path.join('src')
]

for dir in dirs:
    os.makedirs(dir, exist_ok=True)
    with open(os.path.join(dir,'.gitkeep'), 'w') as f:
        pass


files = [
    'dvc.yaml',
    'params.yaml',
    '.gitignore',
    os.path.join('src','__init__.py')

]

for f in files:
    with open(f,"w") as l:
        pass