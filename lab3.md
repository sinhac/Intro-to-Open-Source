Your Lab report will be Lab3.Md
1. Part One [New Repository](https://github.com/sinhac/TrialRepoLabThree)
    1. [First.py](https://github.com/sinhac/TrialRepoLabThree/blob/master/first.py)
    2. [Mars Branch](https://github.com/sinhac/TrialRepoLabThree/tree/mars)
    3. [Jupiter Branch](https://github.com/sinhac/TrialRepoLabThree/tree/jupiter)
    4. gitk --all vs. git log
        * [Gitk All](https://github.com/sinhac/TrialRepoLabThree/blob/master/gitAll.png) 
        * [Git Log](https://github.com/sinhac/TrialRepoLabThree/blob/master/secondCommand.png)
2. Part Two
    1. [Forking the Spoon-Knife Repository](https://github.com/sinhac/TrialRepoLabThree)
    2. Successfully cloned Spoon-Knife
    3. [My Project Progress](https://github.com/sinhac/TrialRepoLabThree/blob/master/myprojectprogress.md)
    4. [Learn Git Branching Screenshot](https://github.com/sinhac/TrialRepoLabThree/blob/master/forking.PNG)
3. Part Three
    1. [Pull Request with ChandrikaSinha.Md](https://github.com/sinhac/TrialRepoLabThree/blob/master/ChandrikaSinha.md)
    2. Shows the differences between two files
        *between working directory and index: git diff
        *between working directory and most recent commit: git diff HEAD
        *between most recent commit and index: git diff –cached
    3. Git tagging is for tagging specific points in history as being important (e.g. a software release). The commit id can be found using git log.
    4. [Course Project Repository](https://github.com/sinhac/courseproject)
        *[References.md]()




Commands used will include git add, git commit, git pull, git checkout, git branch, git push, git log, git status, git diff , git tag, git rebase and git merge

Part 1

    Generate ssh keys if you have not done so.

    Follow these instructions for generating and adding ssh keys to Github (make sure you select the correct operating system at the top)

    Setup git
        Follow the instructions from slides 7 - 27 of https://github.com/rcos/Git-Introduction-Part-I by cloning the repository and opening index.html.
            Create a local repository lab3part1 using the command line
        Create a README.md file.
            This file should include, as a bullet-ed list:
                your name
                your photograph (Add it to your repository and use markdown to display it)
                your graduating year
                your project sub-area (the type of project that you are working on)

    

        (hint: you should be doing something like this):

git init
git add README.md
git commit
git remote add origin <repo url>
git push origin master

 .


Part 3

    Create a Github repository called courseproject.
        Create a file References.md
        Add any projects or websites that have interested you so far
        Please add a link to the repository in your Lab 3 report

    As a table: (one person per table)
        Fork the repository https://github.com/mskmoorthy/NewStory
        Create one branch for your table (Table1, Table2,....)
        you can push the branch the branch by doing git checkout -b feature_branch_name , edit files, git add and git commit and git push -u origin feature_branch_name
        Add each member of the table to the repository:
            Click 'Settings' on the repository page
            Click 'Collaborators'
            Add the username of each person
            Please add a link to the repository in your Lab 3 report

    Each member should clone the table's repository and checkout your table's branch
        Locally, each member should create a file called table_<number>.Md
            Write your project ideas inside.
        Push to your branch and fix any merge conflicts.
        Then each table merges with the master branch and submits a pull request to the upstream repository.

        Resolve any merge conflicts that occur along the way.
            You can update your repository to reflect changes in the upstream repository using git remote add upstream https://github.com/mskmoorthy/NewStory.git and git pull upstream

        Git Introduction Part II might be usefull for this (open index.html in the same way as the Introduction Part I slides)
