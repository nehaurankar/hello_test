
print("Hello, World!")

# Simple addition
a = 5
b = 3
sum_result = a + b
print("The sum of", a, "and", b, "is:", sum_result)

/perform any other commands after these for exp3


### Git Configuration & Setup
git --version
Verifies the installed Git version.

git config --global user.name "Your Name"
Sets the global username for commits.

git config --global user.email "your.email@example.com"
Sets the global email address for commits.

git config --list
Displays the current Git configuration.



### Repository Management
git init
Initializes a new Git repository.

git clone <repository_url>
Clones an existing repository from a remote URL.

git remote -v
Lists configured remote repositories.



### Staging and Committing Changes

git status
Shows the status of the working directory and staged changes.

git add <file_name>
Stages a specific file for the next commit.

git add .
Stages all changes (new, modified, or deleted files).

git commit -m "Commit message"
Commits staged changes with a descriptive message.

git commit --amend
Edits the last commit (useful for fixing commit messages).



### Branching and Merging

git branch
Lists all branches in the repository.

git branch <branch_name>
Creates a new branch.

git checkout <branch_name>
Switches to the specified branch.

git checkout -b <new_branch_name>
Creates and switches to a new branch.

git merge <branch_name>
Merges the specified branch into the current branch.

git branch -d <branch_name>
Deletes the specified branch locally.



### Pushing and Pulling Changes

git push origin <branch_name>
Pushes local commits to the remote branch.

git push
Pushes all local branches to their corresponding remote branches.

git pull
Fetches and merges changes from the remote branch.

git fetch
Downloads updates from the remote repository without merging.



### Tracking Changes & Comparing Versions

git log
Displays commit history.

git log --oneline
Shows a compact commit history with one-line summaries.

git diff
Shows differences between the working directory and the last commit.

git diff <branch1> <branch2>
Compares two branches.

git blame <file_name>
Displays who last modified each line of a file.



### Stash Changes

git stash
Temporarily stores uncommitted changes.

git stash list
Shows the list of stashes.

git stash apply
Applies the most recent stash without removing it from the stash list.



### Undoing Changes

git reset <file_name>
Unstages a file but keeps its changes in the working directory.

git reset --hard <commit_hash>
Resets the working directory and index to a specific commit.

git revert <commit_hash>
Reverts a specific commit by creating a new commit.



### Tagging

git tag <tag_name>
Creates a tag at the current commit.

git push origin <tag_name>
Pushes a specific tag to the remote repository.

git tag -d <tag_name>
Deletes a local tag.



### Collaborating with Remotes

git remote add origin <repository_url>
Adds a remote repository URL.

git push --set-upstream origin <branch_name>
Sets the upstream branch for future pushes.



### Cleaning Up

git clean -f
Removes untracked files from the working directory.

git gc
Optimizes the local repository by garbage collecting unnecessary files.
