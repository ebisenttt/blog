#!/bin/zsh
echo "Start!"
diff=`git diff --name-only --cached --diff-filter=A`
python3 tweetNewArticle.py diff
