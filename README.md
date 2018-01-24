## Hello guys
 - yoooo wazzap how's it going? Im looking foward to meeting with you haha. 
 - But sorry It's just kidding cuz I never see you lol
 - its mean like a ...nothing 
#### What's this & for what? 
 - This's a memo like a for output & memory

#### My introduce
 - if you dont understand japanese style, you don't care about me 
 - I just live in HCMC now. But I was born in Japan 
-----

### Memo(It's a snippet like how to every tech tool)
#### How to use git?(like a snippet)
 - change to branch
   - git checkout
 - HEAD
   - git diff HEAD
   - git diff --staged
   - git diff --cached
 - log
   - git log -p --name-only 
   - git log -p 
   - git log -p --ignore-space-change 
 - master
   - git  pull --rebase origin master
 - easy
   - git add ***
   - git commit -m "***"
   - git push origin add-***
 - check into log
   - git log
   - git --no-pager log
 - -u 
   - git add -u
 - bio
   - git show 
 - delate to file
   - git rm ***
 - pull
   - git pull origin master
 - checkout
   - git checkout -b [branch name] origin/master
 - branch snippet
   - git checkout -b [branch name] origin/master
   - git branch -a（for check)
   - git checkout -b *** origin/master
   - git remote add origin [url of repositorie] 
 - git commit → vim
   - u : like a cntl+z
   - :wq : finish(easy)
 - sample words for commit -m
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

##### How to use anaconda?
 - Distribution of python
 - Into jupyter or spyder or something

##### How to use jupyter?
 - run call: control + enter
 - command: jupyter notebook + enter
 - how to up graph?: write markdown
 - finish: control + c
 - $$(it's mean like a ...)

##### How to use spyder?
 - for python

##### how to get AWS record(maybe until afret a year)
 - learnnn

##### GraphQL
 - GraphQLはAPIへの問い合わせ言語(apiのインターフェース)
 - クライアントとサーバー間のデータのやり取りを容易に記述するためのクエリ言語
 - GraphQLはFacebookにより開発されたオープンソースの言語。API作成の仕組みとしてRESTの代わりに使える
 - GraphQLの定義に従ってクエリを書き, サーバーと通信を取ることでJSONになって戻る
 - APIといえばRESTfulなendpointを経由してリクエストを送ることが一般化
   - GraphQLはRESTとは違った方法でAPI提供者とデータのやりとりを行うことを可能とする
 - ユーザーは各社のAPIを利用する事で、各サービスのデータを検索したりサイトで利用したり出来る

##### REST(REpresentational State Transfer)
 - REST(REpresentational State Transfer)はWebサービスの設計モデル
 - Web APIの仕様を決める上でのアーキテクチャスタイル、つまり基本的な考え方
 - アーキテクチャスタイルというのは、日本語では「建築様式」、見方を変えるとそれはアーキテクチャに対する制約を意味する
 - RESTなWebサービスは、そのサービスのURIにHTTPメソッドでアクセスすることでデータの送受信を行う
 - RESTではこのようにデータとして扱いやすいJSON形式が一般的に利用されている
 - APIとして提供しているリソースを取得(GET)、リソースの登録(POST)、更新(PUT/PATCH)、削除(DELETE)などがRESTにより実現できる

 - RESTの設計原則
   - アドレス指定可能なURIで公開されていること
   - インターフェース(HTTPメソッドの利用)の統一がされていること
   - ステートレスであること
   - 処理結果がHTTPステータスコードで通知されること

 - RESTの考え方では、リソースはそれぞれ固有のURIを持つ
   - そしてそのURIにアクセスすることで、それぞれのリソースを操作することになる。
   - その際の操作はHTTPのメソッドを「正しく」使うことで行う
   - つまりHTTPの4つメソッド、すなわち「GET」「POST」「PUT」「DELETE」で何を行うかを伝える
   - 「リソース」とは、ブログの記事であったり、アップロードした写真であったり、もしくはWebページ全体のコンテンツであったりといった、ひとかたまりの情報を指す

 - CRUD操作：「生成（Create）」「読み取り（Read）」「更新（Update）」「削除（Delete）」のイニシャルを並べた用語のこと
 - これらの原則に則ったWebサービスをRESTfulなサービスというらしい
 - RESTは「リソース」を扱うための考え方

 - 過去のwebapiをまとめた上でデザインに起こす
 - おそらく数え切れないくらい....?
 - なぜRESTが使われるようになったか：Webアプリケーションの主流だったSOAPとWS-*の技術スタックの複雑になったから

##### How to use pmbok
 - yup

##### How to api into chatwork
 - api

```python
import requests
 
api_token = '***'
base_url = 'https://api.chatwork.com/v2'
 
room_id = '66869579'
message = 'wassap wake up right now!!!'
 
post_message_url = '{}/rooms/{}/messages'.format(base_url, room_id)
headers = { 'X-ChatWorkToken': api_token }
params = { 'body': message }
 
response = requests.post(post_message_url, headers=headers, params=params)
print(response)
```

##### How to ML
 - actually they use tool like a tensole flow, pandas,, something 
 
 - import numpy as np
   - def AND
   - def OR
   - def NAND
   - def XOR
   - def step_funcution
   - def sigmoid
   - def relu

##### I just read this one 
 - oreilly Deep Learning
 - this one is like a learn to ML...try anyway
 - it's like a not master cuz easy fo me
 - but math is so difficult...
 - https://wwws.kobe-c.ac.jp/deguchi/sc180/logic/gate.html

 ##### memo
 - how to be anarchis（
 - today is the last day of the lest of our f**kin life（クソみたいな人生の中で休むのは今日で終わり的な）
 - hype crisis（やばい）
 - "What is Geek And Nerd?” What the fashion industry really thinks of our impresario.（これに関しては中を変更するべき）
 - We’ll be the strongest of all like a top of the top（私たちは一番強い存在になるよ（mediaで））
 - Some people feel the rain. Others just get wet. We wanna feel the rain anytime（いつでも特別な感性を持っていたいという意）
 - Defeat? Lose? We(or I) don’t recognize the meaning of the word.（負けなんて知らん）
 - Before you point your fingers, make sure your hands are clean.（批判する前にお前の身を正せ的な）
 - If you don’t input to something you don’t deserve to win, anymore.（とりあえずインプットしまくれ、そうでなければこれ以上勝つことはない）
 - Two wrongs don’t make a right. I wanna say someone about it. （他人が悪事をしてもしてはいけない）
 - Fortune favors the bold. cuz we have to do like a try anyway. go geek.（頑張れば絶対幸運が味方する的な、いけgeeeek）
 - You can’t make an feature without breaking a few your mind.（型を破らなければ未来はない的な）
 - Actions speak louder than words.　（言葉より行動）
 - Easy get something, easy lost anytime.（簡単に得るものは簡単に失う）
 - Badass things are in the eye of the beholder.（内面が出るよ的な）
 - Everyone can’t judge a face to face.（顔を見ただけでは判断できないor見て判断してはいけない）
 - Dressing is a way of life.（服装は自分を造る的な）
 - In my knowledge a friend to all is a friend to none hah.（友達多いというやつほど友達いない）
 - Hate to like a sucker (like a lair)
 - make a fast buck. （手っ取り早く金稼ぐ）
 - You can cram it up your ass（糞食らえ的な）
 - What crawled up your ass?（なにイライラしてんの？的な）
 - We really like to act of darkness.（俺らはセックスが好き的な）
 - How’s your father (like a dick or pussy)
 - friend with benefits (like a fuck buddy)
 - I wanna get facts of life more than now
 - Netflix and chill (hahahaha)
 - Actually someone was way too uptigh.
