# IECSE-ML-Winter-2020

## The Winter Domain Bootcamp for Machine Learning project of IECSE 2020

**Instructions:**

## Configure Tooling
#### Configure user information for all local repositories

Sets the name you want attached to your commit transactions:

 ```$ git config --global user.name "[name]"``` 

Sets the email you want attached to your commit transactions:

  ```$ git config --global user.email "[email address]"``` 

This will be required to be done for any github processes over the net. You have to do it only once.

- Clone the IECSE ML Winter Project repository
```git clone https://github.com/agastya2002/IECSE-ML-Winter-2020.git```

- Initialize a repository in the directory(this is just for information, you won't need this for any task) ```git init <Project Name>```

- Type ```cd IECSE-ML-Winter-2020```

- Create a new branch with your name using the command ```git checkout -b <branch-name>```, with branch name in format ```<full name with '-' for space>. eg.- git checkout -b John-Doe```

- All commits should be made to your own branch, **Never commit to main.** To prevent this always check what branch you're on before committing any changes, command to check current branch ```git branch```, command to checkout(change to) a branch, ```git checkout <branch-name>```.

- To pull solutions after they are uploaded to main, change branch to main and do a git pull.
```git checkout main```
```git pull origin main```

- Steps to submit your code.
* Add files to be committed using the command ```git add .``` (the "." after add means all files in the current directory will be added)
* Add a descriptive commit message for the same. Command- ```git commit -m "<msg>"```.
Format - ```Task #<task-no.> : description```. Mention any errors or issues in the code in the commit message, if any.

- Finally, push your code. command - ```git push origin <branch-name>``` <br>
**Note:** While pushing your code, the above git command might ask your GitHub Id and password, enter the same, and then after successful verification only will git push your branch onto GitHub

## Summary 
### Initial Setup
 ```
 git config --global user.name "[name]"
 git config --global user.email "[email address]"
 git clone https://github.com/agastya2002/IECSE-ML-Winter-2020.git
 cd IECSE-ML-Winter-2020
 ```

### Creating your own branch
```
git checkout -b John-Doe
```
### Submitting your work
``` 
git checkout John-Doe	// to make sure you are in your own branch
git add .	// adds all files and subfolders to be committed in the current directory
git commit -m "Task #0: description"
git push origin John-Doe 
```

### Downloading the solutions once they are uploaded
```
git checkout main
git pull origin main
```

- All solutions will be uploaded to main.

- All tasks will be posted on the [wiki](https://github.com/agastya2002/wp2020temp/wiki).
