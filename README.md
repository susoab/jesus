## Hello guys
 - Im looking foward to meeting with you~ 
#### What's this & for what? 
 - This's a memo like a for output & memory

#### My introduce
 - i'm *** 
 - usually I went to anywhere but alone huh
 - if you dont understand japanese style, you don't care about me
 - be hunble shit down
 - I usually live in HCMC. But I was born in JP
 - anytime I can do for anybody
-----
### Memo(It's a snippet like how to every tech tool)
#### How to use git?(like a snippet)
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
   - git checkout -b [branch name] origin/master
 - branch snippet
   - git checkout -b [branch name] origin/master
   - git branch -a（for check)
     - まだmasterに何もない場合は何か作成
     - 既にmasterに何かあってpullしたい(git pull origin master)
   - git add *** 
   - git commit
   - git push origin [branch name]
   - git branch -a（for check)
   - git checkout master
   - git merge test
   - git push
 - これ分からん
   - git checkout -b *** origin/master
 - githubであらかじめリポジトリを作っておいて、そこをpush先に指定。
   - git remote add origin [url of リポジトリ] 
 - git commit → vim
   - u : like a cntl+z
   - :wq : finish(easy)
 - sample words for commit -m
   - https://anond.hatelabo.jp/20160725092419
   - Add ~
   - Fix ~
   - Update	~
   - Remove ~
   - Use ~
   - Don't ~
   - Make	~
   - Move ~
   - Change ~
   - Rename ~
   - Improve ~
   - Avoid ~
   - Allow ~
   - Implement ~
   - Handle	~
 - 

##### How to use anaconda?
 - Distribution of python
 - Into jupyter or spyder or something

##### How to use jupyter?
 - run call: control+enter
 - command: jupyter notebook + enter
 - how to up graph?: write markdown
 - yup

##### How to use spyder?
 - for python

##### How to Oauth<br>
 - リクエストトークンを発行
 - リクエストトークンを使ってアプリ認証画面に飛ばす
 - コールバックURLでアクセストークンを取得
 - アクセストークンを使ってAPIを呼ぶ




