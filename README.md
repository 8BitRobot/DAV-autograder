#  Welcome to DAV (DAV Automated Verification)!

##  VSCode Installation

Install VSCode if you haven't already; you can do this [here](https://code.visualstudio.com/download). 

##  Creating your team branch

Your VSCode will probably look something like this:

![image](https://github.com/user-attachments/assets/82888616-cfbf-4278-80c2-5b9ffe224917)

Make sure you have an empty folder prepared; I called mine "dav-autograder."
Open a terminal and change into your directory of choice using `cd <path>`.
Then, run the command: `git clone --branch team-0 --single-branch https://github.com/8BitRobot/DAV-autograder.git ./DAV-team-[num]` 
(be sure to replace that last team number). You can modify the target directory as you wish, or leave it out, in which case the branch will be
cloned in your current directory. You will probably need to open the cloned repository folder on the left sidebar afterwards.

Make sure you're in the correct directory; if you kept the `./DAV-team-[num]` from above, make sure to run `cd ./DAV-team-[num]` to get to the
correct directory. Then run `git branch`. You should see "team-0." This is where we'll be uploading skeleton files.

Run `git checkout -b team-[num]` to create your team's branch. You should automatically be directed to this branch, but verify this with `git branch`.

From here, you can publish your branch with `git push origin team-[num]`. Your branch will show up on the repository on GitHub!

##  Basics

When you make changes, getting those changes to show up on GitHub can be done as follows:

First, run `git pull`. This will sync your local clone with the "main" repository, and fetch other people's updates on your branch. 
Then, use `git add` to begin staging your changes. You can add files manually, or use the `-A` flag to add all changed files.
Then, use `git commit -m [message]` to commit your changes. [message] is a short blurb describing what you changed.
Finally, use `git push` to push your changes. Wait a moment, and your changes should show up on the repository.

##  Using the DAV

If you open `.github/workflows`, you'll notice two files: `main.yml` and `test-config.txt`. The first file contains instructions on 
installing various packages needed to run our test scripts. Don't change this file. The second file is much simpler: it contains
the names of whichever labs you wish to be tested. Include each new lab on a separate line.

In the "Actions" tab on GitHub, you'll see various "workflow runs" which contain the auto-grader results. 
