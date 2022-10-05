### create Virtual Env
'''cmd
vitualenv venv
'''
### create req text file
'''bash
pip install -r requirement.txt
'''
'''bash
git init
'''
'''bash
dvc init
'''
'''bash
dvc add data_given/winequality.csv
'''
## by doing this it will creat a .dvc file of the dataset and will not push the real dataset to git repo
'''bash
git add .
'''
'''bash
git commit -m "first commit"
'''

''''''