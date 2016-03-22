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