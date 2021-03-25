import os
import time
from github import Github 
import subprocess

print('do you wanna create a repo - Y/N')
entry=input()
original_path=os.getcwd()
if entry=='Y':
    print("please enter repo name of the format  repo_name = featurename_weights")
    repo_name=input()
#     CHECK REPO
    g = Github()

    user = g.get_user("nishant537") # target user
    repos = user.get_repos()

    non_forks = []
    for repo in user.get_repos():
        if repo.fork is False:
            non_forks.append(repo.name)

    if repo_name in non_forks:
        print('repo already_exists, pass a different name or add to the existing repo')    
    else:
    # PUT main account's auth token
        g=Github('56d27d29be66a2a151df031dfaa9efd1ba5a9f08')
        user=g.get_user()
        repo=user.create_repo(repo_name)
    
    # Creation of templates    
    print('the master branch contains all the templates, wanna update or create master branch')
    template_entry=input()
    if template_entry=='Y':
        print('please give complete path for templates folder on your local system')
        path = input()
        os.chdir(path)
        # repo = g.get_user().get_repo('jingle')
        # repo.create_file('file.txt', "committing files", 'hi my name is nishant', branch="master")

        os.system('git init')
        os.system('git add *')
        os.system('git commit -m "templates added"')
        os.system(f'git remote add origin https://github.com/nishant537/{repo_name}.git')
        os.system('git push -u origin master')
        os.chdir(original_path)
    
# ----------------------------------------------------
print('wanna create another branch. Y/N')
entry1=input()
if entry1=='Y':
    print("please enter the repo_name you wanna attach your branch to")
    repo_name1=input()
    #     repoName = "jingle"
    #     source_branch = 'master'
    #     target_branch = 'hi'

    # repo = g.get_user().get_repo(repoName)
    # sb = repo.get_branch(source_branch)
    # repo.create_git_ref(ref='refs/head/' + target_branch, sha=sb.commit.sha)
    print("PLease enter the branch name. The format is featurename_sitename_hardware[cpu,gpu]")
    branch_name=input()
    print('please enter complete path for readme.txt and zip file to be pushed')
    path2=input()
    os.chdir(path2)
    os.system('git init')
    os.system('dvc init')
    os.system('git add readme.txt script.py')
    os.system('dvc add zip.zip')
    os.system('git add .gitignore zip.zip.dvc')
    os.system('dvc remote add myremote gdrive://1vhGKs8bioyI-eKc7b6i-JGvhHkbpxqJm')
    os.system('git add .dvc/config')
    os.system('dvc push -r myremote')
    os.system('git commit -m "v2"')
    os.system(f'git branch -M {branch_name}')
    os.system(f'git remote add origin https://github.com/nishant537/{repo_name1}.git')
    os.system(f'git push -u origin {branch_name}')
    os.chdir(original_path)