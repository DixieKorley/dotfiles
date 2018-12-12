#!/bin/bash

function get_git_branch() {
	git_branch="$(git branch 2> /dev/null | grep '^*' | cut -c 3-)"
	branch_exists=${#git_branch} # will be 0 if not a git repo
	if [ "$branch_exists" != 0 ]; then
		echo " :: $git_branch"
	fi
}

PS1="\d :: \u :: \w\$(get_git_branch) \$ "

alias m="ssh -X dixiekorley@gmail.com"
