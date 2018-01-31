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
 - how to be anarchis
 - today is the last day of the lest of our f**kin life
 - hype crisis
 - "What is Geek And Nerd?” What the fashion industry really thinks of our impresario.
 - We’ll be the strongest of all like a top of the top
 - Some people feel the rain. Others just get wet. We wanna feel the rain anytime
 - Defeat? Lose? We(or I) don’t recognize the meaning of the word.
 - Before you point your fingers, make sure your hands are clean.
 - If you don’t input to something you don’t deserve to win, anymore.
 - Two wrongs don’t make a right. I wanna say someone about it. 
 - Fortune favors the bold. cuz we have to do like a try anyway. go geek.
 - You can’t make an feature without breaking a few your mind.
 - Actions speak louder than words.
 - Easy get something, easy lost anytime.
 - Badass things are in the eye of the beholder.]
 - Everyone can’t judge a face to face.
 - Dressing is a way of life.
 - In my knowledge a friend to all is a friend to none hah.
 - Hate to like a sucker (like a lair)
 - make a fast buck. 
 - You can cram it up your ass
 - What crawled up your ass?
 - We really like to act of darkness.
 - How’s your father (like a ...lol)
 - friend with benefits (like a fuck buddy)
 - I wanna get facts of life more than now
 - Netflix and chill (hahahaha)
 - Actually someone was way too uptigh.


自らの目的と立ち位置
Geek And Nerd(以下「我々」といいます)が提供するウェブサイト(https://xxxxxxxxxx.comドメインのウェブサイトを指します)(以下「当サイト」といいます)をご利用いただくお客様は、以下の内容を十分にお読みください。

※なお、サイトポリシーに関連する規定類は、予告になく変更させていただく場合がございますので、あらかじめご了承ください。

セキュリティ/個人情報の利用の目的
当サイトでは、メールでのお問い合わせいただく際の目的以外では利用いたしません。

セキュリティ/個人情報の第三者への開示
当サイトでは、個人情報は適切に管理し、以下に該当する場合を除いて第三者に開示することはありません。

本人のご了解がある場合
法令等への協力のため、開示が必要となる場合
免責事項(著作権・商標について)
当サイトで掲載している画像の著作権・肖像権等は各権利所有者に帰属致します。権利を侵害する目的ではございません。記事の内容や掲載画像等に問題がございましたら、各権利所有者様本人が直接メールでご連絡下さい。確認後、対応させて頂きます。

当サイトからリンクやバナーなどによって他のサイトに移動された場合、移動先サイトで提供される情報、サービス等について一切の責任を負いません。

当サイトのコンテンツ・情報につきまして、可能な限り正確な情報を掲載するよう努めておりますが、誤情報が入り込んだり、情報が古くなっていることもございます。

当サイトに掲載された内容によって生じた損害等の一切の責任を負いかねますのでご了承ください。

JavaScriptの有無
当サイトでは、より便利で快適にご利用いただくためにJavaScritpを利用しています。ご使用のブラウザー設定において、JavaScriptをオン（有効）にされていない場合は、正しく機能しない、もしくは正しく表示されない場合がございます。あらかじめご了承ください。

禁止事項
当サイトのご利用にあたって、以下の行為は固くお断りいたします。

・我々に対する以下の行為

誹謗、中傷、脅迫する行為
不利益、損害を与える行為
信用を毀損する恐れのある行為
・違法または違法な可能性を有する行為

##### rivacy Policy
 - This privacy policy has been compiled to better serve those who are concerned with how their 'Personally Identifiable Information' (PII) is being used online. PII, as described in US privacy law and information security, is information that can be used on its own or with other information to identify, contact, or locate a single person, or to identify an individual in context. Please read our privacy policy carefully to get a clear understanding of how we collect, use, protect or otherwise handle your Personally Identifiable Information in accordance with our website.
 - What personal information do we collect from the people that visit our blog, website or app?
 - We do not collect information from visitors of our site.
 - or other details to help you with your experience.
 - When do we collect information?
 - We collect information from you when you respond to a survey or enter information on our site.
 - How do we use your information?
 - We may use the information we collect from you when you register, make a purchase, sign up for our newsletter, respond to a survey or marketing communication, surf the website, or use certain other site features in the following ways:
   - To improve our website in order to better serve you.
   - To allow us to better service you in responding to your customer service requests.
   - To ask for ratings and reviews of services or products
   - To follow up with them after correspondence (live chat, email or phone inquiries)
   - How do we protect your information?
 - We do not use vulnerability scanning and/or scanning to PCI standards.
 - We only provide articles and information. We never ask for credit card numbers.
 - We do not use Malware Scanning.
 - We do not use an SSL certificate
 - We only provide articles and information. We never ask for personal or private information like names, email addresses, or credit card numbers.
 - Do we use 'cookies'?
   - We do not use cookies for tracking purposes
   - ou can choose to have your computer warn you each time a cookie is being sent, or you can choose to turn off all cookies. You do this through your browser settings. Since browser is a little different, look at your browser's Help Menu to learn the correct way to modify your cookies.
   -  If you turn cookies off, Some of the features that make your site experience more efficient may not function properly.that make your site experience more efficient and may not function properly.
 - Third-party disclosure
 - We do not sell, trade, or otherwise transfer to outside parties your Personally Identifiable Information.
 - Third-party links
 - Occasionally, at our discretion, we may include or offer third-party products or services on our website. These third-party sites have separate and independent privacy policies. We therefore have no responsibility or liability for the content and activities of these linked sites. Nonetheless, we seek to protect the integrity of our site and welcome any feedback about these sites.
 - Google
   - Google's advertising requirements can be summed up by Google's Advertising Principles. They are put in place to provide a positive experience for users. https://support.google.com/adwordspolicy/answer/1316548?hl=en
   - We have not enabled Google AdSense on our site but we may do so in the future.
   - California Online Privacy Protection Act
   - CalOPPA is the first state law in the nation to require commercial websites and online services to post a privacy policy. The law's reach stretches well beyond California to require any person or company in the United States (and conceivably the world) that operates websites collecting Personally Identifiable Information from California consumers to post a conspicuous privacy policy on its website stating exactly the information being collected and those individuals or companies with whom it is being shared. - See more at: http://consumercal.org/california-online-privacy-protection-act-caloppa/#sthash.0FdRbT51.dpuf
   - According to CalOPPA, we agree to the following:
   - Users can visit our site anonymously.
   - Once this privacy policy is created, we will add a link to it on our home page or as a minimum, on the first significant page after entering our website.
   - Our Privacy Policy link includes the word 'Privacy' and can easily be found on the page specified above.
 - You will be notified of any Privacy Policy changes:
   - On our Privacy Policy Page
   - Can change your personal information:
   - By logging in to your account
 - How does our site handle Do Not Track signals?
 - We honor Do Not Track signals and Do Not Track, plant cookies, or use advertising when a Do Not Track (DNT) browser mechanism is in place.
 - Does our site allow third-party behavioral tracking?
 - It's also important to note that we do not allow third-party behavioral tracking

##### for digg
 - コンパイル型プログラミング言語
 - 発展型言語
 - オブジェクト指向
 - 言語、フレームワーク、アーキテクチャ、ライブラリ、ツール、タスクorソースコード管理

##### 進捗
 - 従業員詳細のbug 
 - thanhにどれくらいで完了出来るか見積もる
   - タブ押すごとにではなく、従来通りに社会保険タブを対応出来るか
   - 必要な部分だけ更新するように
 - 未だ改善が必要な画面：従業員詳細、my pageプロフィール、申請管理（否認のみ）
   - それぞれ見積もりを出す
 - 給与明細の賃金台帳（link非活性にする）
 - 画面優先度1~6 まで磨きまくる
 - 使う側で試す（アカウント作成〜1 to 6を細かく触る）
 - 上記報告を細かくchatで
 - 17時にまたmtg