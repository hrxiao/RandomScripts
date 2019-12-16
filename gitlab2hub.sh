git clone $1 repo
cd repo
git remote add github $2
git push github master
cd ..
rm -rf repo
