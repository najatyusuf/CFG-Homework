Question 1


**GIT WORKFLOW FUNDAMENTALS**

Working Directory:
The working directory contains all the files and folders in your project that you are currently writing and editing. It is a filesystem where you are able to view files and make changes to them. 

Staging Area:
The staging area is an area where will be able to use the command ‘git add’ to add the version of a file to a rough draft area. This will be the area in which you will save in your next commit. 

Local Repo (head):
The local repository is a Git repository that is stored locally on your personal computer. This will track all the modifications and all the different versions of files and will display a built record built over time.

Remote Repo (master)
The remote repository is a Git repository that is stored remotely on another computer. This will be a repository that is shared by all members of your team and is used to display changes made to the project. The remote repository contains all the modifications and different versions of projects that you and your team members have contributed towards, that are hosted on the internet. 

**WORKING DIRECTORY STATES**

Staged:
The staged command allows you to make changes in the working directory. When interacting with Git, staging will enable you to record changes in small commits. Meaning as you progress in your file, staging will allow you to record these changes by doing a commit gradually. 

Modified:
As you edit and make changes to your file, it is seen as modified from Git. This is because your file is changed and different from your last commit. As you work, you will stage these changes selectively and then commit all of these staged changes. 

Committed:
When you commit you are storing ‘snapshots’ or ‘milestones’ that will form to show a timeline of your Git project. Commits are created by using the git commit command. This will capture the current condition of a project.


**GIT COMMANDS**

Git add:
The git add command will add and update the current version of a file from the working directory to the staging area. This command informs Git to include the updated file in the next commit. This will not affect the local repository until the command git commit is run. 

Git commit:
The git commit command submits files into the local repository. This command captures a current snapshot showcasing the project's current changes. 

Git push:
The git push command submits all the commits of a file from the local repository to the remote repository. 

Git fetch:
The git fetch command will download all the commits, files and refs in a project from a remote repository to the local repository. The git fetch command is called fetching and is used when you want to see what everyone in your team is currently working on.

Git merge:
The git merge command is used to join a branched history back together again. The git merge combines independent pieces of code from multiple different branches into a single branch.

Git pull:
The git pull command is an extension of the git fetch command. 

The git pull command works the same as the git fetch command. The only difference is that the git pull command fetches (git fetch) content from the remote repository and will also perform merging (git merge) to update to match the local repository. The git pull command is versatile and will enable you to fetch from and integrate with other local branches or repositories.

