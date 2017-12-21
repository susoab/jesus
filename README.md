## hello guys

#### what kinda japanese food do you like?
 - like a seafood or sushi or karaage....somethings

#### my introduce
 - i'm ***
 - usually I went to anywhere but alone huh
 - if you dont understand japanese style, you don't care about me
 - be hunble shit down
 - I usually live in HCMC. But I was born in JP

 #### how to use git?(like a snippet)
 - change to branch
   - git checkout
 - 前回コミット(HEAD)からの差分
   - git diff HEAD
 - ステージングエリアとHEADとの差分
   - git diff --staged
   - git diff --cached
 - 自分がしたコミットを確認
   - git log -p --name-only (修正したファイル一覧)
   - git log -p (変更内容差分, ファイル名を引数で渡すと単体で指定可)
   - git log -p --ignore-space-change (スペースや改行で差分が見づらいとき)
 - masterブランチを最新に更新(masterブランチなう)
   - git  pull --rebase origin master
 - 修正したソースコードを再度コミットしてプッシュ
   - git add ***
   - git commit -m "***"
   - git push origin add-***
 - check into log
   - git log
   - git --no-pager log
 - 修正したファイルをすべてaddしたいなら、-u が便利
   - git add -u
 - コミット詳細
   - git show 
 - delate to file
   - git rm ***
 - masterの内容を開発ブランチに反映
   - git pull origin master
 - branchを作る上と同時にそこへcheckout
<<<<<<< HEAD
   - git checkout -b [branch name] origin/master
-----
 - branch snippet
   - git checkout -b [branch name] origin/master
   - git branch -a（for check)
     - まだmasterに何もない場合は何か作成
     - 既にmasterに何かあってpullしたい(git pull origin [?])
   - git add ***
   - git commit
   - git push origin [branch name]
   - git branch -a（for check)
   - git checkout master
   - git merge test
   - git push
-----
 - ****
=======
   - git checkout -b *** origin/master

 
>>>>>>> d09481d13ea68d363dd3106cc69eedc929d4658f

##### how to use anaconda?
 - Distribution of python
 - Into jupyter or spyder or something

##### how to use jupyter?
 - run call: control+enter
 - command: jupyter notebook + enter
 - how to up graph?: write markdown
 - 



