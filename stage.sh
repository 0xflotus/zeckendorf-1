#!/bin/sh

printf "Building Sphinx docs...\n\n"
sphinx-build -a docs docs/_build/html
printf "\n"

printf "Adding files to Git...\n\n"
git add * .gitignore
git status

printf "Ready for commit!\n"