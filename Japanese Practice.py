import random

kanji = ["問題", "質問", "作品", "本文", "文中", "段落", "まとめ", "部分", "大部分", "の中から", "言葉", "意味", "理由", "説明", "両方", "以上", "以下", "以外", "以来", "前半", "後半", "正しいもの", "探しなさい", "選びなさい", 
         "つなげる", "つなげなさい", "について", "によると", "始める", "短く", "多い", "少ない", "それぞれ", "使う", "目的", "大切", "印象", "体験", "伝える", "気を使う", "なければいけません", "どの", "どれ", "どこ", "どう", 
         "どちら", "どんな", "どういう", "どうして", "いつまで", "何ですか", "どこですか", "どこにありますか", "どうしますか", "どう思っているようですか", "どんな印象を受けますか", "説明する", "意見", "発言", "文", "原文", 
         "テーマ", "例", "行", "手紙", "日記", "作文", "新聞", "学校新聞", "記事", "投書", "案内書", "発表", "レポート", "メール", "ホームページ", "ウェブサイト", "ブログ", "スピーチ", "プレゼンテーション", "会議", "アドバイス", 
         "予習をする", "読者", "下級生", "市長", "詳しく", "まとめる", "地球", "世界", "世界中", "国", "都市", "町", "街", "国際", "世界問題", "北米", "南米", "欧州", "中東", "アフリカ", "アジア", "オーストラリア", "南極大陸", 
         "アメリカ", "日本", "中国", "韓国", "台湾", "現地", "イギリス", "歴史", "政府", "大使館", "国際会議", "公式", "現在", "当時", "〜頃", "色々な", "沢山", "あちらこちら", "予定", "計画する", "協力する", "交流する", 
         "触れ合う", "触れ合い", "集める", "賛成する", "反対する", "影響する", "違い", "起こる", "現れる", "交換する", "配る", "逃げる", "壊れる", "競争する", "戦争", "争い", "危ない", "危険", "安全", "安心", "傷", "亡くなった人", 
         "橋", "〜すぎる", "技術", "理科", "科学", "理学", "生物学", "化学", "物理学", "科目", "将来", "数字", "研究", "計算", "発見する", "発達する", "開発する", "完成する", "準備する", "用意する", "参考する", "開始", "実験", 
         "図形", "工夫", "作り方", "作業", "実物", "原理", "利点", "開発者", "部品", "未来", "自然", "環境", "季節", "春", "夏", "秋", "冬", "海", "草", "花", "開花", "青空", "気候", "気温", "温度", "温暖化", "農業", "農場", 
         "農家", "里山", "工場", "津波", "地震", "防災", "無事", "大変", "節約", "リサイクル", "エコ", "プラ", "ペットボトル", "ごみ", "かんづめ", "涼しい", "暖かい", "寒い", "暑い", "星", "ビル", "建てる", "水力発電所", 
         "ロボット", "ロケット", "飛行士", "道路", "水道局", "自転車", "場所", "エンジニア", "調理員", "展覧会", "種類", "品物", "薬", "写真", "手袋", "はさみ", "時計", "まず", "できてきる", "打ち上げる", "跳ぶ", "飛ぶ", "降りる", 
         "向かう", "つぶす", "小さくする", "大きくする", "切る", "拭く", "火を通す", "計る", "手に入る", "組み合わせる", "行われる", "活躍する", "入る", "入れない", "働く", "止まる", "守る", "興味を持つ", "営業する", "出版される", 
         "世紀", "実際", "実話", "普通", "注意", "時速", "数回", "動き", "早い", "速い", "遅い", "軽い", "重い", "足りない", "かわいそう", "光る", "キラキラ", "いよいよ", "ぱっと", "知恵", "予想", "最近", "公開", "大会", "土俵", 
         "行事", "場面", "会社", "商品", "紹介する", "耳にする", "やってくる", "中継する", "優勝する", "人気", "流行", "流行る", "若者", "パソコン", "ノートパソコン", "タブレット", "携帯", "携帯電話", "スマートフォン", "ガラゲー", 
         "1台", "画面", "センチ", "ミリ", "はっきり", "映す", "写す", "〜やすい", "覚える", "暗記する", "調べる", "アイディア", "教材", "会話", "近所", "フルタイム", "アルバイト", "パート", "お客さん", "名人", "プロ", "予約", 
         "必要", "よく使われている", "現金", "値段", "値上がり", "社会", "社会に出る", "大人", "老人", "家庭", "おばあちゃん", "おじいちゃん", "両親", "お母さん", "お父さん", "兄", "姉", "弟", "妹", "叔母さん", "伯父さん", 
         "従姉妹", "従兄弟", "友達", "仲間", "相手", "話し相手", "他人", "生徒", "高齢化", "少子化", "育つ", "誘う", "訪ねる", "訪れる", "出会う", "仲良く", "仲がいい", "仲が悪い", "喧嘩する", "遠くはなれる", "反省する", 
         "お詫び", "力を合わせる", "話し合う", "言う事を聞く", "してもらいたい", "認める", "認めてもらいたい", "思いやり", "気配り", "一生懸命", "気持ちよく", "こもった", "こめられた気持ち", "受けつく", "渡す", "自信", "見た目", 
         "心", "明るい", "笑顔", "大よろこび", "嬉しい", "悲しい", "痛み", "心の痛み", "困る", "感動する", "経験", "機会", "行動", "態度", "一緒に", "贈り物", "届ける", "運ぶ", "ぬすむ", "手伝い", "びっくりする", "静かにする", 
         "じっと見る", "全体", "元々", "夢を叶える", "文化", "多様性", "理解", "国際理解", "知ろう", "関係がある", "様子", "イメージ", "特別な", "めずらしい", "すばらしい", "特徴", "重要", "時代", "活動", "役に立つ", "姉妹校", 
         "プログラム", "留学", "留学生", "ホームステイ", "ペンフレンド", "ボランティア", "外国語", "勉強", "専門家", "大学", "高校", "学年", "学期", "新学年", "新学期", "授業", "練習する", "復習する", "申し込む", "決まった場所", 
         "丁寧", "像", "暮らし", "日常生活", "習慣", "伝統", "伝統的", "洋風", "和風", "季節感", "日本中", "地元", "村人", "家", "毎週", "イベント", "中心", "来場する", "一員", "合わせる", "伝う", "広がる", "のこり", "挨拶", 
         "お礼", "語る", "人生が変わった", "心にのこる", "愛をこめる", "感想", "思い", "気持ち", "気がする", "予感する", "勇気", "真面目", "厳しい", "優しい", "易しい", "秘密", "音楽", "げき", "紙", "紙しばい", "物語", "お土産", 
         "飾る", "事務用品", "事務", "物", "専門店", "和食", "洋食", "中華", "韓国料理", "イタリア料理", "食品", "主食", "主菜", "ご飯", "朝ご飯", "昼ご飯", "夕食", "お茶", "弁当", "給食", "食堂", "お米", "新米", "味噌汁", 
         "お餅", "焼く", "香り", "美味しい", "美味しくない", "不味い", "甘い", "酸っぱい", "塩っぱい", "辛い", "半分", "キロ", "列", "はさむ", "生活", "生き方", "健康", "日用品", "体重", "食生活", "植える", "食べ物", "料理", 
         "動物", "餌", "肉", "魚", "野菜", "レシピ", "材料", "味", "匂い", "水分", "体にいい", "体に悪い", "良さ", "商品化", "もったいない", "無駄", "無い", "命", "生きる", "死ぬ", "この世を去る", "病気", "重い病気", "体温", 
         "入院", "年寄", "増える", "減る", "手足", "しなければいけない", "朝から晩まで", "長い間", "休む", "じっとする", "掃除する", "洗う", "手を洗う", "利用する", "チャレンジ", "余暇", "夏休み", "春休み", "冬休み", 
         "ゴールデンウィーク", "お正月", "夏がやってくる", "仕事", "暇", "ひまな時", "趣味", "興味", "関心", "やってみたいこと", "やったことがないこと", "自由", "不自由", "苦手", "得意", "出掛ける", "遊ぶ", "楽しめる", "楽しい", 
         "楽しくない", "つまらない", "旅行", "観光", "読書", "買い物", "店", "物価", "安い", "喫茶店", "雰囲気", "遊園地", "ライブ", "コンサート", "図書館", "博物館", "美術館", "写真展", "入館", "入館料", "有料", "無料", 
         "売り切れる", "開館", "閉館", "休館日", "アクセス", "部活", "生徒会", "クラブ", "音楽クラブ", "スポーツ部", "練習", "運動", "選手", "水泳", "水着", "潜る", "野球", "マネ", "歩く", "散歩", "山登り", "頂上", "途中", 
         "ゆっくり", "景色", "きれい", "眺める", "風", "桜", "咲く", "花びん", "お寺", "祭り", "夏祭り", "踊り", "わくわく", "参加する", "開かれる", "見かける", "打ち合わせ", "打ち合わせ場所", "説明会", "お問い合わせ", "描く", 
         "免許", "ハンディー"]
reading = ["もんだい", "しつもん", "さくひん", "ほんぶん", "ぶんちゅう", "だんらく", "x", "ぶぶん", "だいぶぶん", "のなかから", "ことば", "いみ", "りゆう", "せつめい", "りょうほう", "いじょう", "いか", "いがい", "いらい", 
            "ぜんぱん、ぜんはん", "こうはん", "ただしいもの", "さがしなさい", "えらびなさい", "x", "x", "x", "x", "はじめる", "みじかく", "おおい", "すくない", "x", "つかう", "もくてき", "たいせつ", "いんしょう", "たいけん", 
            "つたえる", "きをつかう", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "なんですか／なにですか", "x", "x", "x", "どうおもっているようですか", "どんないんしょうをうけますか", "せつめいする", "いけん", 
            "はつげん", "ぶん", "げんぶん", "x", "れい", "ぎょう", "てがみ", "にっき", "さくぶん", "しんぶん", "がっこうしんぶん", "きじ", "とうしょ", "あんないしょ", "はっぴょう", "x", "x", "x", "x", "x", "x", "x", 
            "かいぎ", "x", "よしゅうをする", "どくしゃ", "かきゅうせい", "しちょう", "くわしく", "x", "ちきゅう", "せかい", "せかいじゅう", "くに", "とし", "まち", "まち・がい", "こくさい", "せかいもんだい", "ほくべい", 
            "なんべい", "おうしゅう", "ちゅうとう", "x", "x", "x", "なんきょくたいりく", "x", "にほん", "ちゅうごく", "かんこく", "たいわん", "げんち", "x", "れきし", "せいふ", "たいしかん", "こくさいかいぎ", "こうしき", 
            "げんざい", "とうじ", "x", "いろいろな", "x", "x", "よてい", "けいかくする", "きょうりょうくする", "こうりゅうする", "ふれあい", "ふれあう", "あつめる", "さんせいする", "はんたいする", "えいきょうする", "ちがい", 
            "おこる", "あらわれる", "こうかんする", "くばる", "にげる", "こわれる", "きょうそうする", "せんそう", "あらそい", "あぶない", "きけん", "あんぜん", "あんしん", "きず", "なくなったひと", "はし", "x", "ぎじゅつ", 
            "りか", "かがく", "りがく", "せいぶつがく", "がかく", "ぶつりがく", "かもく", "しょうらい", "すうじ", "けんきゅう", "けいさん", "はっけんする", "はったつする", "かいはつする", "かんせいする", "じゅんびする", 
            "よういする", "さんこうする", "かいし", "じっけん", "ずけい", "くふう", "つくりかた", "さぎょう", "じつぶつ", "げんり", "りてん", "かいはつしゃ", "ぶひん", "みらい", "しぜん", "かんきょう", "きせつ", "はる", "なつ", 
            "あき", "ふゆ", "うみ", "くさ", "はな", "かいか", "あおぞら", "きこう", "きおん", "おんど", "おんだんか", "のうぎょう", "のうじょう", "のうか", "さとやま", "こうじょう", "つなみ", "じしん", "ぼうさい", "ぶじ", 
            "たいへん", "せつやく", "x", "x", "x", "x", "ゴミ", "かんづめ", "すずしい", "あたたかい", "さむい", "あつい", "ほし", "x", "たてる", "すいりょくはつでんしょ", "x", "x", "ひこうし", "どうろ", "すいどうきょく", 
            "じてんしゃ", "ばしょ", "x", "ちょうりいん", "てんらんかい", "しゅるい", "しなもの", "くすり", "しゃしん", "てぶくろ", "x", "とけい", "x", "できている", "うちあげる", "とぶ", "とぶ", "おりる", "むこう", "x", 
            "ちいさくする", "おおきくする", "きる", "ふく", "ひをとおす", "はかる", "てにはいる", "くみあわせる", "おこなわれる", "かつやくする", "はいる", "はいれない", "はたらく", "とまる", "まもる", "きょうみをもつ", 
            "えいぎょうする", "しゅっぱんされる", "せいき", "じっさい", "じつわ", "ふつう", "ちゅうい", "じそく", "すうかい", "うごき", "はやい", "はやい", "おそい", "かるい", "おもい", "たりない", "x", "ひかる", "x", "x", "x", 
            "ちえ", "よそう", "さいきん", "こうかい(する)", "たいかい", "どひょう", "ぎょうじ", "ばめん", "かいしゃ", "しょうひん", "しょうかいする", "みみにする", "x", "ちゅうけいする", "ゆうしょうする", "にんき", "りゅうこう", 
            "はやる", "わかもの", "x", "x", "x", "けいたい", "けいたいでんわ", "x", "からげー", "いちだい", "がめん", "x", "x", "x", "うつす", "うつす", "x", "おぼえる", "あんきする", "しらべる", "x", "きょうざい", "かいわ", 
            "きんじょ", "x", "x", "x", "おきゃくさん", "めいじん", "x", "よやく", "ひつよう", "よくつかわれている", "げんきん", "ねだん", "ねあがり", "しゃかい", "しゃかいにでる", "おとな", "ろうじん", "かてい", "x", "x", 
            "りょうしん", "おかあさん", "おとうさん", "あに", "あね", "おとうと", "いもうと", "おばさん", "おじさん", "いとこ", "いとこ", "ともだち", "なかま", "あいて", "はなしあいて", "たにん", "せいと", "こうれいか", 
            "しょうしか", "そだつ", "さそう", "たずねる", "おとずれる", "であう", "なかよく（する）", "なかがいい", "なかがわるい", "けんかする", "とおくはなれる", "はんせいする", "おわび", "ちからをあわせる", "はなしあう", 
            "いうことをきく", "x", "みとめる", "みとめてもらいたい", "おもいやり", "きくばり", "いっしょうけんめい", "きもちよく", "x", "こめられたきもち", "うけつく", "わたす", "じしん", "みため", "こころ", "あかるい", 
            "えがお", "おおよろこび", "うれしい", "かなしい", "いたみ", "こころのいたみ", "こまる", "かんどうする", "けいけん", "きかい", "こうどう", "たいど", "いっしょに", "おくりもの", "とどける", "はこぶ", "x", "てつだい", 
            "x", "しずかにする", "じっとみる", "ぜんたい", "もともと", "ゆめをかなえる", "ぶんか", "たようせい", "りかい", "せかいりかい", "しろう", "かんけいがある", "ようす", "x", "とくべつな", "x", "x", "とくちょう", 
            "じゅうよう", "じだい", "かつどう", "やくにたつ", "しまいこう", "x", "りゅうがく", "りゅうがくせい", "x", "x", "x", "がいこくご", "べんきょう", "せんもんか", "だいがく", "こうこう", "がくねん", "がっき", 
            "しんがくねん", "しんがっき", "じゅぎょう", "れんしゅうする", "ふくしゅうする", "もうしこむ", "きまったばしょ", "ていねい", "ぞう", "x", "にちじょうせいかつ", "しゅうかん", "でんとう", "でんとうてき", "ようふう", 
            "わふう", "きせつかん", "にほんじゅう", "じもと", "むらびと", "いえ・うち", "まいしゅう", "x", "ちゅうしん", "らいじょうする", "いちいん", "あわせる", "つたう", "ひろがる", "x", "あいさつ", "おれい", "かたる", 
            "じんせいがかわった", "こころにのこる", "あいをこめる", "かんそう", "おもい", "きもち", "きがする", "よかんする", "ゆうき", "まじめ", "きびしい", "やさしい", "やさしい", "ひみつ", "おんがく", "x", "かみ", 
            "かみしばい", "ものがたり", "おみやげ", "かざる", "じむようひん", "じむ", "もの", "せんもんてん", "わしょく", "ようしょく", "ちゅうか", "かんこくりょうり", "イタリアりょうり", "しょくひん", "しゅしょく", "しゅさい", 
            "ごはん", "あさごはん", "ひるごはん", "ゆうしょく", "おちゃ", "べんとう", "きゅうしょく", "しょくどう", "おこめ", "しんまい", "みそしる", "おもち", "やく", "かおり", "おいしい", "おいしくない", "まずい", "あまい", 
            "すっぱい", "しょっぱい", "からい", "はんぶん", "x", "れつ", "x", "せいかつ", "いきかた", "けんこう", "にちようひん", "たいじゅう", "しょくせいかつ", "うえる", "たべもの", "りょうり", "どうぶつ", "えさ", "にく", 
            "さかな", "やさい", "x", "ざいりょう", "あじ", "におい", "すいぶん", "からだにいい", "からだにわるい", "よさ", "しょうひんか", "x", "むだ", "ない", "いのち", "いきる", "しぬ", "このよをさる", "びょうき", 
            "おもいびょうき", "たいおん", "にゅういん", "としより", "ふえる", "へる", "てあし", "x", "あさからばんまで", "ながいあいだ", "やすむ", "x", "そうじする", "あらう", "手をあらう", "りようする", "x", "よか", 
            "なつやすみ", "はるやすみ", "ふゆやすみ", "x", "おしょうがつ", "なつがやってくる", "しごと", "ひま", "ひまなとき", "しゅみ", "きょうみ", "かんしん", "x", "x", "じゆう", "ふじゆう", "にがて", "とくい", "でかける", 
            "あそぶ", "たのしめる", "たのしい", "たのしくない", "x", "りょこう", "かんこう", "どくしょ", "かいもの", "みせ・てん", "ぶっか", "やすい", "きっさてん", "ふんいき", "ゆうえんち", "x", "x", "としょかん", 
            "はくぶつかん", "びじゅつかん", "しゃしんてん", "にゅうかん", "にゅうかんりょう", "ゆうりょう", "むりょう", "うりきれる", "かいかん", "へいかん", "きゅうかんび", "x", "ぶかつ", "せいとかい", "x", "x", "スポーツぶ", 
            "れんしゅう", "うんどう", "せんしゅ", "すいえい", "みずぎ", "もぐる", "やきゅう", "x", "あるく", "さんぽ", "やまのぼり", "ちょうじょう", "とちゅう", "x", "けしき", "x", "ながめる", "かぜ", "さくら", "さく", 
            "はなびん", "おてら", "まつり", "なつまつり", "おどり", "x", "さんかする", "ひらかれる", "みかける", "うちあわせ", "うちあわせばしょ", "せつめいかい", "おといあわせ", "かく", "めんきょ", "x"]
meaning = [
    ["question", "problem", "point"], ["question", "inquiry", "enquiry"], ["work", "performance", "production"], ["text (of document)", "body (of letter)"], 
    ["in document", "in sentence"], ["paragraph", "conclusion", "full stop"], ["summary"], ["part", "section"], ["greater part", "majority"], ["from among"], ["word"], 
    ["meaning", "significance"], ["reason"], ["description", "illustration", "explanation"], ["both"], ["more than", "no less than", "above-mentioned"], 
    ["not greater than", "below", "below-mentioned"], ["with exception of", "excluding"], ["since", "henceforth"], ["first half"], ["second half", "latter half"], 
    ["correct one", "right one"], ["find"], ["choose"], ["tie", "fasten", "connect", "transfer (phone call)"], ["connect them together", "tie them together"], ["about"], 
    ["according to"], ["start", "begin", "originate"], ["short", "briefly"], ["many", "numerous", "frequent"], ["few"], ["each", "every", "respectively"], ["use"], 
    ["purpose", "an aim", "an objective"], ["crucial", "important"], ["impression"], ["undergo an experience"], ["tell", "convey", "report"], 
    ["pay attention to", "take inconsideration"], ["must do"], ["which", "what"], ["which (of these)"], ["where", "what place"], ["how", "in what way", "how about"], 
    ["which", "where", "who"], ["what kind of", "what sort of"], ["how", "in what way", "why", "what kind of"], ["why", "for what reason"], ["How long? Till when?"], 
    ["What is it?"], ["Where is it"], ["Where can it be found?"], ["What would (you) do?", "what do about it"], ["What does he/she think of it?"], 
    ["What is your impression? What impression did you receive?"], ["explain something", "describe something"], ["an opinion", "view"], ["remark", "statement"], 
    ["sentence", "composition", "text"], ["original text"], ["theme"], ["an example"], ["line"], ["letter", "note"], ["diary", "journal"], ["essay", "composition"], 
    ["newspaper"], ["school newspaper"], ["an article", "news story", "report"], ["letter editor", "letter from reader", "contribution"], ["guidebook", "guide"], 
    ["announcement", "publication", "presentation"], ["report", "paper on something"], ["e-mail"], ["home page"], ["website"], ["blog"], ["speech"], ["presentation"], 
    ["meeting", "conference", "session", "assembly", "council", "convention", "congress"], ["advice"], ["prepare (for lesson)", "rehearse"], ["reader", "reading public", "audience"], 
    ["underclassmen"], ["mayor (of city)"], ["in detail", "fully", "minutely", "at length"], ["summarize", "collect", "bring conclusion", "finalize", "settle", "put in order"], 
    ["earth", "globe"], ["world"], ["around world", "throughout world"], ["country", "place of origin"], ["city", "town", "urban area"], ["town", "city"], ["city", "street", "district"], 
    ["international"], ["world problem"], ["North America"], ["South America"], ["Europe"], ["Middle East"], ["Africa"], ["Asia"], ["Australia"], ["Antarctica"], ["America"], ["Japan"], 
    ["China"], ["Korea"], ["Taiwan"], ["local", "on-site", "field"], ["England (sometimes Britain)"], ["history"], ["government"], ["embassy"], ["international conference"], 
    ["formal", "official", "formula"], ["currently", "at present time"], ["in those days", "at that time"], ["around that time", "time of year"], ["various"], ["many", "much", "plenty"], 
    ["here and there", "all over"], ["plans", "arrangement", "schedule"], ["plan", "organize"], ["cooperate with", "join"], ["interact"], ["come incontact with"], ["contact"], 
    ["collect", "gather"], ["agree with"], ["oppose", "disagree"], ["affect", "influence"], ["difference", "discrepancy"], ["occur", "happen"], ["appear"], ["exchange"], 
    ["distribute", "hand out"], ["escape", "run away"], ["be broken", "break"], ["compete"], ["war"], ["dispute", "conflict"], ["dangerous", "grave"], ["danger", "peril", "hazardous"], 
    ["safe"], ["relief", "feel at ease"], ["wound", "injury", "stain (on one's reputation)", "hurt feelings"], ["person(s) who died"], ["bridge"], 
    ["too (excessive)", "do something too much", "something is too (adjective)"], ["technology", "skill"], ["science", "natural science"], ["science", "scientific knowledge"], 
    ["physical science (e.g. chemistry, biology, etc.)", "natural philosophy"], ["biology"], ["chemistry"], ["physics"], ["(school) subject", "curriculum", "course"], ["future"], 
    ["number", "numeral", "figure"], ["research"], ["calculation", "computation"], ["discover"], ["develop", "progress"], ["develop", "exploit", "create solution (for an issue)"], 
    ["complete", "finish"], ["prepare"], ["arrange", "equip", "provide"], ["refer to", "consult (book)"], ["start, opening, beginning"], ["an experiment"], ["figure", "shape", "graphic"], 
    ["ingenuity", "device", "scheme"], ["how something is made"], ["work", "operation"], ["actual thing", "real thing"], ["principle", "theory", "fundamental truth"], 
    ["advantage", "merit", "point in favor"], ["developer"], ["parts", "accessories", "components"], ["future (usually distant)"], ["nature"], ["environment", "circumstance"], 
    ["season"], ["spring"], ["summer"], ["fall"], ["winter"], ["ocean", "sea"], ["grass"], ["flower"], ["blooming", "flowering"], ["blue sky"], ["climate"], 
    ["air (atmospheric) temperature"], ["temperature"], ["global warming"], ["agriculture"], ["farm"], ["farmer", "farm family"], ["undeveloped woodland near populated area"], 
    ["factory"], ["tsunami"], ["earthquake"], ["disaster prevention"], ["safety", "peace", "quietness"], ["serious", "grave", "difficult", "immense"], 
    ["economising", "saving (power, water, expenses)"], ["recycling"], ["eco'"], ["plastic"], ["plastic bottle"], ["trash", "rubbish"], ["canned goods"], ["cool (weather)"], 
    ["warm"], ["cold"], ["hot (weather)"], ["star"], ["building"], ["build", "construct", "erect"], ["hydroelectric plant", "power station"], ["robot"], ["rocket"], ["pilot", "airman"], 
    ["road", "highway"], ["waterworks bureau", "water department"], ["bicycle"], ["place", "location", "spot"], ["engineer"], ["cook"], ["exhibition"], ["variety", "kind", "type"], 
    ["goods"], ["medicine"], ["picture", "photograph"], ["hand gloves"], ["scissors"], ["clock"], ["first (of all)"], ["be made from", "be built"], ["launch", "shoot up"], 
    ["jump", "leap"], ["fly"], ["descend", "step down"], ["approach"], ["crush", "smash", "squash"], ["make smaller"], ["make larger"], ["cut"], ["wipe", "mop"], ["cook", "heat"], 
    ["measure", "weigh", "survey", "time"], ["come inpossession of"], ["combine"], ["take place", "be held"], ["be active in", "flourish"], ["enter"], ["omit", "be unable enter"], 
    ["work", "labor", "function", "be effective"], ["stop"], ["protect"], ["be interested in"], ["carry on business, operate"], ["be published", "appear in print"], ["century"], 
    ["in actuality", "actual conditions"], ["true story"], ["normal"], ["caution"], ["speed (per hour)"], ["few (several) times"], ["movement", "activity"], ["early"], ["fast"], 
    ["late", "slow"], ["light (i.e. not heavy)", "non-serious"], ["heavy", "serious"], ["insufficient", "not enough"], ["poor", "pitiable"], ["shine", "be bright"], 
    ["sparkle", "twinkle"], ["at last", "finally"], ["suddenly", "in flash"], ["wisdom"], ["an expectation", "speculation", "prediction"], ["recently", "lately", "nowadays"], 
    ["open public", "unveil", "release"], ["convention", "tournament", "mass meeting", "rally"], ["arena", "forum", "sumo ring"], ["event", "function"], ["scene", "situation"], 
    ["company"], ["product", "merchandise", "commodity"], ["introduce"], ["hear about", "hear by chance"], ["come around", "turn up"], ["relay", "transmit"], ["win"], 
    ["popular", "popularity"], ["prevalence", "prevalent", "epidemic"], ["be popular", "come infashion", "be prevalent"], ["young people"], ["personal computer"], ["laptop computer"], 
    ["tablet computer"], ["portable", "cell phone"], ["cell phone"], ["smart phone"], ["Galapagos cell phone", "Japanese 3G mobile phones"], ["one machine", "one device"], ["screen"], 
    ["centimeter"], ["millimeter"], ["clearly", "plainly", "distinctly"], ["project", "reflect", "cast (shadow)"], ["reproduce", "portray", "copy down", "film", "picture"], 
    ["easy", "be easy do"], ["remember", "learn", "memorize"], ["learn by heart", "memorize"], ["examine", "investigate", "study"], ["an idea"], ["teaching materials"], ["conversation"], 
    ["neighborhood"], ["full-time job"], ["part-time job"], ["part-timer"], ["guest", "customer"], ["master", "expert"], ["professional"], ["reservation", "advance order"], 
    ["necessary", "essential", "requirement"], ["used often"], ["cash"], ["price"], ["rise in price", "price hike"], ["society", "public"], 
    ["go out inworld", "become member of society"], ["adult"], ["old person", "senior citizen"], ["home", "family", "household"], ["grandmother"], ["grandfather"], ["parents"], 
    ["mother"], ["father"], ["older brother"], ["older sister"], ["younger brother"], ["younger sister"], ["aunt"], ["uncle"], ["female cousins"], ["male cousins"], ["friend"], 
    ["friend", "colleague", "an associate", "partner"], ["companion", "opponent", "other party"], ["someone talk to"], ["another pesron", "outsider", "stranger"], ["student"], 
    ["aging of population"], ["declining birth rates"], ["grow", "be brought up"], ["invite"], ["call on someone", "visit someone's house"], ["visit"], ["happen meet", "come across"], 
    ["make friends with", "getting along well"], ["get along well"], ["get along poorly"], ["quarrel"], ["separate widely from"], ["contemplation", "reflect on one's past conduct"], 
    ["apology"], ["cooperate", "join forces"], ["disscuss"], ["do what one is told to", "listen what someone says"], ["I would like you to～"], ["notice", "acknowledge"], 
    ["would like you (or someone) acknowledge/accept ~"], ["compassion", "thoughtfulness"], ["attentiveness", "consideration for others"], ["with utmost effort", "with all one's might"], 
    ["pleasantly", "comfortably"], ["be full of", "be filled with"], ["thought/feeling put insomething"], ["receive and continue", "inherit and continue"], ["hand over"], 
    ["self‐confidence"], ["(visual) appearance"], ["mind", "heart", "spirit"], ["cheerful", "bright"], ["smile"], ["be delighted", "very pleased"], ["happy"], ["sad"], ["pain"], 
    ["heartache", "emotional sufering"], ["be troubled", "be worried"], ["being deeply moved emotionally"], ["experience"], ["chance", "opportunity"], ["action", "behavior"], 
    ["attitude"], ["together"], ["present", "gift", "act of giving present"], ["deliver", "sent", "give notice"], ["carry", "transport"], ["steal"], ["help", "assist"], ["be suprised"], 
    ["be quiet"], ["stare at", "look at for long time"], ["entirely", "whole"], ["originally"], ["achieve one's dream", "realize one's dream"], ["culture"], ["diversity", "variety"], 
    ["understanding"], ["international understanding"], ["try learn about", "try know about"], ["relate to", "have something do with"], ["situation", "state of affairs"], 
    ["image", "impresion"], ["special"], ["unusual"], ["wonderful"], ["feature", "distinguishing characteristic"], ["important", "major", "essential"], ["period", "epoch", "era"], 
    ["activity", "activities"], ["useful"], ["sister school"], ["program"], ["study abroad"], ["foreign exchange student"], ["homestay", "living with local family"], 
    ["penfriend", "penpal"], ["volunteer"], ["foreign language"], ["study"], ["an expert", "specialist"], ["university"], ["High School"], ["year in school"], ["semester"], 
    ["new school year"], ["new semester"], ["class", "lesson"], ["practice"], ["review"], ["apply for", "make an application", "subscribe to"], ["specified place", "designated place"], 
    ["polite", "courteous"], ["statue"], ["life", "living", "livelihood"], ["daily life", "everyday life"], ["custom", "habit", "manners"], ["tradition", "convention"], ["traditional"], 
    ["European style", "western style", "foreign style"], ["Japanese style"], ["sense of seasons"], ["throughout Japan"], ["local", "home town"], ["villagers", "village folk"], 
    ["house", "home"], ["every week"], ["event"], ["focus", "center"], ["attend"], ["member (of an organization/group)"], ["join together", "match", "face"], 
    ["go along", "walk along", "follow"], ["spread (out)", "extend", "diffuse"], ["remnant", "left-over", "remaining"], ["greeting", "salutation"], ["thanks", "expression of gratitude"], 
    ["speak of", "tell", "narrate"], ["life was changed"], ["remain in one's heart"], ["with love", "put one's heart and love into"], ["impressions", "thoughts"], 
    ["thought", "feeling", "emotion"], ["feelings"], ["have feeling", "have hunch"], ["forsee"], ["courage", "bravery"], ["diligent", "serious", "honest"], ["severe", "strict"], 
    ["kind", "gentle"], ["easy", "simple"], ["secret"], ["music"], ["drama", "play"], ["paper"], ["traditional Japanese storytelling with pictures", "picture story show"], 
    ["tale", "story", "legend"], ["souvenir", "gift"], ["decorate", "ornament"], ["office supplies", "stationery"], ["business", "office work"], ["thing"], 
    ["specialty store", "store specializing in"], ["Japanese food"], ["Western food"], ["Chinese (e.g. food)"], ["Korean food"], ["Italian food"], ["foodstuff", "food"], 
    ["food staple (rice is staple food of Japanese)"], ["main dish (e.g. meat, fish, but not rice)"], ["meal", "rice"], ["breakfast"], ["lunch"], ["dinner"], ["tea"], 
    ["Japanese-style box lunch"], ["lunch service", "catering"], ["cafeteria", "dining hall"], ["rice"], ["new rice", "rice of new crop"], ["miso soup"], 
    ["rice cakes", "pounded mochi rice"], ["bake", "grill"], ["scent", "fragrance"], ["delicious"], ["unsavory"], ["unappetising"], ["sweet", "lenient"], ["sour"], ["salty"], ["spicy"], 
    ["half"], ["kilo-(grams)(meters)"], ["line (of people)", "queue"], ["interpose", "hold between", "insert"], ["life (one's daily existence)", "living"], ["way of life", "lifestyle"], 
    ["health", "well-being"], ["articles of daily use", "daily necessities"], ["body weight"], ["eating habits", "dietary life"], ["plant (i.e. flowers)", "grow"], ["food"], 
    ["dish", "cuisine", "cooking"], ["animal"], ["feed", "bait", "pet food"], ["meat"], ["fish"], ["vegetable"], ["recipe"], ["ingredients", "material"], ["taste", "flavor"], 
    ["smell", "odor"], ["moisture", "water content"], ["good for health"], ["bad for health"], ["goodness", "good", "good quality"], 
    ["commercialization (e.g. product)", "commodification"], ["wasteful", "more than one deserves"], ["useless", "futile", "wasteful"], ["nonexistent", "not being (there)"], 
    ["life", "one's life span"], ["live"], ["die"], ["die", "leave this world"], ["illness", "sickness"], ["serious illness"], ["body temperature"], 
    ["hospitalization", "be hospitalized"], ["old people", "aged"], ["increase"], ["decrease"], ["one's hands and feet", "limbs"], ["must do", "have to"], 
    ["from dusk dawn", "from morning till night"], ["for long time"], ["rest", "take break", "be absent", "take day off"], ["remain in place", "stand still"], ["clean"], ["wash"], 
    ["wash one's hands"], ["use"], ["challenge", "try something"], ["leisure", "leisure time"], ["summer vacation"], ["spring vacation"], ["winter vacation"], 
    ["Golden Week (early-May holiday season in Japan)"], ["New Year's"], ["summer is coming"], ["work"], ["free time", "time spare"], ["when one has free time"], 
    ["hobby", "pastime", "tastes", "preference"], ["interest (in something)", "curiosity (about something)"], ["concern", "interest"], ["something you would like try/do"], 
    ["something you have never done before"], ["freedom", "free", "latitude"], ["inconvenience", "disability"], ["not good (at)", "dislike (of)"], ["one's strong point"], ["go out"], 
    ["play", "spend time pleasantly"], ["be able enjoy"], ["fun"], ["not fun"], ["boring", "uninteresting"], ["travel"], ["sightseeing"], ["reading"], ["shopping"], ["store"], 
    ["(consumer) price"], ["inexpensive", "cheap"], ["cafe", "coffee shop"], ["atmosphere", "ambience"], ["amusement park"], ["live concert (i.e. rock or pop concert)"], 
    ["concert (i.e. for classical music)"], ["library"], ["museum"], ["art museum"], ["phoexhibition"], ["entry (e.g. library, school, museum)"], ["admission fee"], 
    ["toll", "fee", "admission-paid"], ["free of charge"], ["be sold out"], ["be open", "opening hall for that day's business (museum, library, etc.)"], 
    ["be closed", "closing hall for that day's business (museum, library, etc.)"], ["days closed"], ["access", "how get there"], ["(school) club", "club activities"], 
    ["student council"], ["club", "night club"], ["music club"], ["sports club"], ["practice", "training", "drill"], ["exercise"], ["athlete"], ["swimming"], ["swimsuit"], 
    ["dive (under water)"], ["baseball"], ["manager"], ["walk"], ["walk", "stroll"], ["mountain climbing", "mountaineering"], ["top", "summit", "mountain peak"], 
    ["on way", "in middle of"], ["slowly", "take one's time"], ["scenery", "landscape"], ["pretty"], ["gaze at"], ["wind"], ["cherry blossoms"], ["bloom"], ["(flower) vase"], 
    ["temple"], ["festival"], ["summer festival"], ["dance"], ["feel excited"], ["participate"], ["be open", "open"], ["notice", "catch sight of"], ["meeting", "appointment"], 
    ["meeting place"], ["information session"], ["inquiry"], ["draw"], ["license"], ["handicap", "handy"]
]
questions = []
correct_answers = []
correct_type = ""

def choose_quiz():
    print("This is a vocabulary and kanji quiz to prepare for the IB Japanese B exams!")
    print("There are 3 question types:")
    print("1. kanji -> meaning")
    print("2. kanji -> reading")

    while True:
        user_input = input("Choose the question type (1-2): ") 
        if user_input != "1" and user_input != "2":
             print("Please choose a valid type")
             continue
        else: break

    question_type = int(user_input)

    while True:
        user_input = input("Choose the number of question (1 - 100): ")
        try: 
            number_of_questions = int(user_input)
            if number_of_questions <= 0 or number_of_questions > 100:
                print("Please choose a number between 1 and 100.")
                continue
        except ValueError:
            print("Please choose a valid number")
        else: break

    get_working_sets(question_type)
    start_quiz(number_of_questions)

def start_quiz(number_of_questions):
    score = 0
    for i in range(number_of_questions):
        score += get_question()
    print(f"Your score is: {score}")
    print("Type: 'again' to do one more quiz or 'exit' to exit")
    while True:
        option = input("Choose an option: ")
        if option != "again" and option != "exit":
            print("Please choose a valid option")
        else:
            break
    if option == "again":
        choose_quiz()
    elif option == "exit":
        quit()

def get_question():
    question = random.randint(0, len(questions) - 1)
    print(questions[question])
    response = get_response()
    if check_answer(response, question):
        print("Correct")
        return 1
    else:
        print("Incorrect")
        print(f"The answer is {correct_answers[question]}")
        return 0

def get_working_sets(question_type):
    global questions
    global correct_answers
    global correct_type

    if question_type == 1:
        questions = kanji.copy()
        correct_answers = meaning.copy()
        correct_type = "meaning"

    elif question_type == 2:
        questions = []
        correct_answers = []
        for i in range(len(kanji)):
            if reading[i] != 'x':
                questions.append(kanji[i])
                correct_answers.append(reading[i])
        correct_type = "reading"

def get_response():
    return input(f"Type the correct {correct_type}: ") 

def check_answer(response, question):
    if response in correct_answers[question]:
        return True
    else:
        return False
    
choose_quiz()
