# git add deleted only files before adding untracked files
git ls-files --deleted | xargs git add --all