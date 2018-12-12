# prompt variable for the shell

PS1="\d :: \u :: \w :: \$(git branch | grep '^*' | cut -c 3-) \$ "

