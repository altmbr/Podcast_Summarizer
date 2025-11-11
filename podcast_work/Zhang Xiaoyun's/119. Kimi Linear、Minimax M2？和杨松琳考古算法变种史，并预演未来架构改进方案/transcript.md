# 119. Kimi Linear、Minimax M2？和杨松琳考古算法变种史，并预演未来架构改进方案

**Podcast:** Zhang Xiaoyun's
**Date:** 2025-11-05
**Video ID:** 858HR43pegk
**Video URL:** https://www.youtube.com/watch?v=858HR43pegk

---

[00:00:00] 我決定國內的算法創新肯定是更強的
[00:00:08] Yang Songlin: 先注意的模塊他們最後選到的是一個叫做KDA的這個模塊
[00:00:15] Yang Songlin: Kimi Data 和Tension這個名字感覺挺有耿的
[00:00:20] Yang Songlin: 他們應該是想對標Ducy Spass 的Tension
[00:00:23] Yang Songlin: 然後我就特意去了一個Kimi 開頭的一個名字
[00:00:27] Yang Songlin: 然後非常的對撞
[00:00:30] 我覺得每一次大家關心你兩參審
[00:00:34] Yang Songlin: 那肯定是因為大家碰到了一些Contest 我
[00:00:39] 我覺得我還是挺喜歡看最早的那些批判
[00:00:43] Yang Songlin: 我覺得那些批判現在都挺好的
[00:00:45] Yang Songlin: 我管這個叫做考古
[00:00:51] 先看看能不能把全局這個注意力把它幹掉吧
[00:00:57] Yang Songlin: 對這第一點就是因為它確實它是阻止這個Connecting Window
[00:01:03] Yang Songlin: Ducy Scale Up 上去的一個主要的平靜
[00:01:07] 我覺得這後面的話就是把換合的注意力
[00:01:11] Yang Songlin: 它裡面的全局的注意力把它換成Spass 的Tension
[00:01:17] Yang Songlin: 我覺得你論上只要Spass 的Tension 它能選得準的話
[00:01:22] 是完全可以取代不負擔身這個層的
[00:01:28] 哈囉大家好 歡迎收聽張小鈞商業訪談路 我是小鈞
[00:01:35] Zhang Xiaojun: 這是一檔由語言及世界工作室出品的深度訪談節目
[00:01:39] Zhang Xiaojun: 我們希望和你一起從這裡探索新世界
[00:01:43] Zhang Xiaojun: 今天這集節目我們將討論一個在當下非常關鍵的話題
[00:01:47] Zhang Xiaojun: 那就是人工智能的算法與價格衝心
[00:01:51] 嘉賓是我們的網期嘉賓反常
[00:01:53] Zhang Xiaojun: 它是MIT的在度博士楊松林
[00:01:56] Zhang Xiaojun: 研究方向是限性注意力機制
[00:01:58] Zhang Xiaojun: 我們將從最近剛發布的幾個新模型
[00:02:01] Zhang Xiaojun: Kimmy Linear
[00:02:03] Zhang Xiaojun: Linanax M2
[00:02:04] Zhang Xiaojun: Kimmy Linear 3nxt 切入
[00:02:06] Zhang Xiaojun: 松林參與了這集中Kimi和Chenwen的部分工作
[00:02:10] Zhang Xiaojun: 它是Kimmy Linear論文的作者之一
[00:02:13] Zhang Xiaojun: 算法創新為什麼在25年變得有位重要呢
[00:02:17] Zhang Xiaojun: 它背後的成因是數據算力和算法
[00:02:20] Zhang Xiaojun: 使驅動人工智能的三價馬車
[00:02:22] Zhang Xiaojun: 那在數據狀況的無奈前提之下
[00:02:25] Zhang Xiaojun: 各個模型公司都不得不重新開始
[00:02:28] Zhang Xiaojun: 雕模型價構以其Skill Love的模法繼續
[00:02:31] Zhang Xiaojun: 而由於中國的算力相對美國有限
[00:02:34] Zhang Xiaojun: 這反而讓中國的AI算法創新走在世界的前言
[00:02:38] Zhang Xiaojun: 這集節目你將聽到近幾年價構最大的突破
[00:02:42] Zhang Xiaojun: 是Ethic M.O.E.混合專家模型
[00:02:45] Zhang Xiaojun: 它讓M.O.E.成為了全球共識
[00:02:48] Zhang Xiaojun: 而下一個突破的重要方向可能是Attention注意力機制
[00:02:52] 中國公司已經在Attention上展開了不同的技術壓住
[00:02:56] Zhang Xiaojun: 顯示目前已經發布的這些模型中
[00:02:59] Zhang Xiaojun: Diffing正在探索的是Spositonscentre
[00:03:02] Zhang Xiaojun: 吸收注意力機制
[00:03:03] Zhang Xiaojun: Kimmy正在探索的是Linia Tenshin現行注意力機制
[00:03:07] Zhang Xiaojun: MiniMax在年初的M1版本中探索的是Linia Tenshin
[00:03:11] Zhang Xiaojun: 而在剛發布的M2版本中又重新回到了Fur Tenshin
[00:03:15] Zhang Xiaojun: 也就是全球注意力機制
[00:03:17] Zhang Xiaojun: 在節目中
[00:03:18] Zhang Xiaojun: 森林將講解它參與的這篇KimmyLinia的工作
[00:03:22] 並分析以上這些公司在Attention上的不同角色
[00:03:25] Zhang Xiaojun: 於同時它也將帶領大家考古人工晉能的算法
[00:03:29] Zhang Xiaojun: 變種史並預言未來
[00:03:31] Zhang Xiaojun: 算法與架構的改進方案
[00:03:33] Zhang Xiaojun: 等級比較多硬和或有一些些的專業難度
[00:03:37] Zhang Xiaojun: 大家可以根據自己的實際需要手聽
[00:03:40] Zhang Xiaojun: 也因為加兵的工作環境的原因
[00:03:43] Zhang Xiaojun: 所以會出現一些公英文的夾展
[00:03:45] Zhang Xiaojun: 還是希望代價能夠多多的理解和支持
[00:03:48] Zhang Xiaojun: 我們開始吧
[00:03:57] 哈囉 宋林 先給聽眾朋友們打個招呼
[00:03:59] Zhang Xiaojun: 把並且做一個簡單的做解稍
[00:04:01] Zhang Xiaojun: 哈囉 大家好
[00:04:03] Yang Songlin: 我叫楊聰林
[00:04:05] Yang Songlin: 我現在是MITCCO的一個PhD在讀
[00:04:10] Yang Songlin: 然後我的主要研究方向的話
[00:04:12] Yang Songlin: 就是NOTCHNAMERMODER的一些架構
[00:04:16] Yang Songlin: 然後主要是比較高效的注意力
[00:04:19] Yang Songlin: 及是最大的研究
[00:04:22] Yang Songlin: 跟具體來說的話
[00:04:23] Yang Songlin: 主要是在研究
[00:04:26] Yang Songlin: 就一類注意力模型叫做現心注意力
[00:04:30] 你們給大家講一下你的整個的研究的主線
[00:04:33] Zhang Xiaojun: 是怎麼地盡點
[00:04:35] Zhang Xiaojun: 你是怎麼走向林亮貞士的研究點
[00:04:37] Zhang Xiaojun: 像林亮貞士的話
[00:04:39] Yang Songlin: 就是最開始的時候
[00:04:42] Yang Songlin: 應該是到時候看到很多斯丹夫
[00:04:46] Yang Songlin: 一個一個
[00:04:48] Yang Songlin: research的一個Groper叫做Hazzy Research
[00:04:52] Yang Songlin: 就是吹到Airbird
[00:04:55] Yang Songlin: 他們在斯丹夫的那個Nab
[00:04:57] Yang Songlin: 然後到時候看到很多他們寫的寶克
[00:05:00] Yang Songlin: 然後覺得
[00:05:01] Yang Songlin: 虛列鍵模是一個非常有意思的問題
[00:05:04] Yang Songlin: 然後當初決定來做一些
[00:05:06] Yang Songlin: 虛列鍵模的一些問題
[00:05:08] 然後剛好
[00:05:11] Yang Songlin: 那時候最開始讀播的時候
[00:05:13] Yang Songlin: 就是微軟壓演員的話
[00:05:14] Yang Songlin: 他有一篇工作叫做Ragnite
[00:05:17] Yang Songlin: 那個時候就是
[00:05:19] Yang Songlin: 最開始的時候就想辦法來
[00:05:21] 提高Ragnite他的那個效率
[00:05:24] Yang Songlin: 然後他的那個Performance
[00:05:27] 然後之後的話就發現
[00:05:30] Yang Songlin: 提高效率的這一套
[00:05:32] Yang Songlin: 音劍、油畫、這種算法
[00:05:35] Yang Songlin: 可以擴展到很多這種
[00:05:38] Yang Songlin: 其他的這種類似的架構裡面
[00:05:41] Yang Songlin: 然後同時
[00:05:43] Yang Songlin: 就之後的一些工作
[00:05:45] Yang Songlin: 就是主要是去想辦法進一步的
[00:05:48] Yang Songlin: 就是在能夠
[00:05:50] Yang Songlin: 音劍高效性的同時能夠提高這種
[00:05:53] Yang Songlin: 細心最厲害的他家個的那個
[00:05:55] Yang Songlin: Performance的一些改進
[00:05:57] Yang Songlin: 這邊說
[00:05:58] Yang Songlin: 從門控機制
[00:06:00] Yang Songlin: 然後到那個
[00:06:02] Yang Songlin: 有一個叫做DataRoll的一個機制
[00:06:05] Yang Songlin: 然後後面的話
[00:06:06] Yang Songlin: 就是把這兩個東西
[00:06:07] Yang Songlin: 把它扛辦在一起
[00:06:09] 就是讓他合成一個
[00:06:11] 一個統一的一個弱
[00:06:13] Yang Songlin: 然後把它變成一個
[00:06:15] Yang Songlin: 安安的一個更新規則
[00:06:17] Yang Songlin: 同時的話
[00:06:18] Yang Songlin: 又可以去
[00:06:20] Yang Songlin: 就是有一些可以
[00:06:21] Yang Songlin: 音劍高效的算法來進行訓練
[00:06:25] 我看了算字
[00:06:26] Zhang Xiaojun: 我們節目發了以後
[00:06:27] Zhang Xiaojun: 很多人說你也是
[00:06:28] Zhang Xiaojun: 理念天聖之母
[00:06:29] Zhang Xiaojun: 這說什麼
[00:06:30] 可能是在
[00:06:32] Yang Songlin: 這個你於做很多工作
[00:06:34] Yang Songlin: 然後尤其是
[00:06:36] Yang Songlin: 還有一個那個開源庫
[00:06:38] Yang Songlin: 叫做Flash Neenial Tansion
[00:06:40] 這個庫的話感覺
[00:06:42] Yang Songlin: 這個 Neenial的人
[00:06:44] Yang Songlin: 裡面很多就是會用這個庫
[00:06:47] 然後包括業界也有很多
[00:06:49] Yang Songlin: 就是用這個庫
[00:06:50] Yang Songlin: 來進行一些
[00:06:51] Yang Songlin: Neenial Tansion的一些探索的
[00:06:53] 對 然後我那幾篇工作
[00:06:55] Yang Songlin: 應該還是比較
[00:06:57] Yang Songlin: 比較有影響力的
[00:06:59] Yang Songlin: 可能大家會這麼來教我
[00:07:01] Yang Songlin: 能怎麼跟通俗的
[00:07:03] Zhang Xiaojun: 去理解一下理念
[00:07:04] Zhang Xiaojun: 跟通俗的理解
[00:07:05] Yang Songlin: 你念的話
[00:07:06] Yang Songlin: 就是說
[00:07:07] Yang Songlin: 他中文是現行
[00:07:08] Zhang Xiaojun: 對吧
[00:07:09] Zhang Xiaojun: 現行注意的舉主
[00:07:10] Zhang Xiaojun: 現行的話
[00:07:11] Yang Songlin: 能踏主
[00:07:12] Yang Songlin: 意思就是
[00:07:13] Yang Songlin: 現行複雜度
[00:07:14] Yang Songlin: 對
[00:07:15] Yang Songlin: 現行複雜度
[00:07:16] Yang Songlin: 他對於的話
[00:07:17] Yang Songlin: 就是說是平方複雜度
[00:07:19] Yang Songlin: 也就是說我們平常的
[00:07:20] Yang Songlin: Sofemalice Tansion
[00:07:21] Yang Songlin: 他是平方複雜度
[00:07:23] Yang Songlin: 然後
[00:07:25] Yang Songlin: 就是我們大家都知道
[00:07:28] Yang Songlin: Sofemalice Tansion的話
[00:07:30] Yang Songlin: 他有三個舉證
[00:07:32] Yang Songlin: 他有QKV
[00:07:34] Yang Songlin: QQV
[00:07:36] 然後一般的話
[00:07:37] Yang Songlin: 他就是QK
[00:07:38] Yang Songlin: 先求一個舉證
[00:07:40] Yang Songlin: 相成
[00:07:41] Yang Songlin: 得到一個
[00:07:43] Yang Songlin: LBIO的一個舉證
[00:07:44] Yang Songlin: L的話是
[00:07:46] Yang Songlin: 修列長度
[00:07:47] Yang Songlin: 然後的話
[00:07:48] Yang Songlin: 就是對這個LBIO的舉證
[00:07:51] 做一個
[00:07:53] Yang Songlin: Masking
[00:07:54] Yang Songlin: 因為他基本上都是
[00:07:55] Yang Songlin: 智慧歸的一個
[00:07:56] Yang Songlin: 語言鍵模
[00:07:57] Yang Songlin: 所以我們要把未來的
[00:07:58] Yang Songlin: 消息把它
[00:07:59] Yang Songlin: mask掉
[00:08:00] Yang Songlin: 這樣的話
[00:08:01] Yang Songlin: 我們得到一個
[00:08:02] Yang Songlin: 下三角的一個
[00:08:03] Yang Songlin: LBIO的一個舉證
[00:08:04] Yang Songlin: 然後我們再
[00:08:06] 加一個Sofemalice
[00:08:07] Yang Songlin: 然後就讓我們
[00:08:08] Yang Songlin: 得到一個
[00:08:09] Yang Songlin: 朱利利的一個
[00:08:11] 分數的一個舉證
[00:08:12] Yang Songlin: 然後
[00:08:13] Yang Songlin: 最後再用這個
[00:08:14] Yang Songlin: 朱利利分數舉證
[00:08:15] Yang Songlin: 和那個
[00:08:16] 外流的舉證
[00:08:17] Yang Songlin: 做一個相成
[00:08:18] Yang Songlin: 得到一個
[00:08:19] Yang Songlin: Opport
[00:08:20] 這就是
[00:08:21] Yang Songlin: Sofemalice Tansion
[00:08:23] 他在這種
[00:08:24] Yang Songlin: 智慧歸
[00:08:25] Yang Songlin: 鍵模裡面的一個
[00:08:27] Yang Songlin: 比較一個
[00:08:28] Yang Songlin: 朱利利的介紹
[00:08:29] Yang Songlin: 對
[00:08:30] Yang Songlin: 因為他會有一個
[00:08:31] Yang Songlin: LBIO的一個舉證
[00:08:33] Yang Songlin: 所以他的
[00:08:34] Yang Songlin: 複雜都是
[00:08:35] Yang Songlin: 平方的
[00:08:36] 然後
[00:08:37] Yang Songlin: 先進出業的話
[00:08:38] Yang Songlin: 他
[00:08:39] Yang Songlin: 一般就是
[00:08:40] Yang Songlin: 把那個Sofemalice
[00:08:41] Yang Songlin: apprate
[00:08:42] Yang Songlin: 把它去掉
[00:08:43] Yang Songlin: 然後這樣子的話
[00:08:44] Yang Songlin: 我們就會得到
[00:08:45] Yang Songlin: 我們就把這個
[00:08:46] Yang Songlin: 非先進的
[00:08:47] Yang Songlin: Sofemalice Tansion的
[00:08:48] Yang Songlin: Sofemalice去掉了
[00:08:50] Yang Songlin: 然後我們可以
[00:08:51] Yang Songlin: 通過一些
[00:08:52] Yang Songlin: 那個等式的變化
[00:08:54] Yang Songlin: 然後我們可以
[00:08:55] Yang Songlin: 把它寫成一個
[00:08:56] Yang Songlin: 類似於
[00:08:57] Yang Songlin: 安安的一個
[00:08:58] Yang Songlin: 特利的一個形式
[00:08:59] Yang Songlin: 這個可能
[00:09:00] Yang Songlin: 他每一個
[00:09:01] Yang Songlin: Stab他的Cost
[00:09:02] Yang Songlin: 就是O-1
[00:09:03] Yang Songlin: 然後處理這個L
[00:09:04] 他這個
[00:09:05] Yang Songlin: 長度的
[00:09:06] Yang Songlin: 訓練的一個
[00:09:07] Yang Songlin: 畫能
[00:09:08] Yang Songlin: 他的整體的複雜度
[00:09:09] Yang Songlin: 就是
[00:09:10] Yang Songlin: OL
[00:09:11] Yang Songlin: 所以他是
[00:09:12] Yang Songlin: 跟長度的
[00:09:13] Yang Songlin: 大小他是
[00:09:14] Yang Songlin: 成一個
[00:09:15] Yang Songlin: 現性複雜度的一個關係
[00:09:16] Yang Songlin: 所以
[00:09:17] Yang Songlin: 大家會
[00:09:18] Yang Songlin: 把它
[00:09:19] Yang Songlin: 叫做現性訓練
[00:09:20] 如果
[00:09:21] Zhang Xiaojun: 把
[00:09:22] Zhang Xiaojun: 現在的
[00:09:23] Zhang Xiaojun: 做一個
[00:09:24] Zhang Xiaojun: 框
[00:09:25] Zhang Xiaojun: 將它有一個背景的話
[00:09:26] Zhang Xiaojun: 林鄭是
[00:09:27] Zhang Xiaojun: 應該放在哪個地方
[00:09:28] Yang Songlin: 我覺得
[00:09:29] Yang Songlin: 都在
[00:09:30] Yang Songlin: Transformer這個
[00:09:31] Yang Songlin: 基礎加構
[00:09:32] Yang Songlin: 裡面
[00:09:33] Yang Songlin: 在進行一些
[00:09:34] Yang Songlin: 模改吧
[00:09:35] Yang Songlin: 對
[00:09:36] Yang Songlin: 原模型的話
[00:09:37] Yang Songlin: 它的技術
[00:09:38] Yang Songlin: 這樣可能分成
[00:09:39] Yang Songlin: Pretraining
[00:09:40] Yang Songlin: Postraining
[00:09:41] Yang Songlin: 然後
[00:09:42] Yang Songlin: 之類的
[00:09:43] Yang Songlin: 然後
[00:09:44] Yang Songlin: 這些
[00:09:45] Yang Songlin: 加構的演繹的話
[00:09:46] Yang Songlin: 可能是在Pretrane
[00:09:47] 然後
[00:09:48] Yang Songlin: Pretrane
[00:09:49] Yang Songlin: 它還有
[00:09:50] Yang Songlin: 很多
[00:09:51] Yang Songlin: 其他類別的演繹
[00:09:52] Yang Songlin: 的話
[00:09:53] Yang Songlin: 然後像這種
[00:09:54] Yang Songlin: 基礎加構
[00:09:55] Yang Songlin: 然後還有一些
[00:09:57] Yang Songlin: Pretrane
[00:09:58] Yang Songlin: Data
[00:09:59] Yang Songlin: 然後之類的
[00:10:00] Yang Songlin: 東西
[00:10:01] Yang Songlin: 然後
[00:10:02] Yang Songlin: 現心最初的
[00:10:03] Yang Songlin: 應該就算在這個
[00:10:04] Yang Songlin: 基礎加構的演繹
[00:10:05] 然後
[00:10:06] Yang Songlin: 現在基礎加構的話
[00:10:07] Yang Songlin: 基本上它整體的
[00:10:09] Yang Songlin: 框架
[00:10:10] 還是
[00:10:11] Yang Songlin: Transformer
[00:10:12] Yang Songlin: 這種
[00:10:13] Yang Songlin: 它會有一個
[00:10:14] Yang Songlin: 注意力
[00:10:15] Yang Songlin: 機制
[00:10:16] Yang Songlin: 和一個
[00:10:17] Yang Songlin: 前饋
[00:10:19] Yang Songlin: Warnwell
[00:10:20] Yang Songlin: Fifleware
[00:10:22] Yang Songlin: 它會
[00:10:23] Yang Songlin: 在這兩個模塊裡面
[00:10:25] 然後
[00:10:26] Yang Songlin: 反覆的疊家
[00:10:27] Yang Songlin: 疊家很多次
[00:10:28] Yang Songlin: 就得到
[00:10:29] Yang Songlin: 最新的
[00:10:30] Yang Songlin: 一個Transformer
[00:10:31] 的一個演繹
[00:10:32] Yang Songlin: 然後一般的話
[00:10:33] Yang Songlin: 大家就是
[00:10:34] Yang Songlin: 會在
[00:10:35] Yang Songlin: 這個
[00:10:36] 框架
[00:10:37] Yang Songlin: 下面來進行一些
[00:10:38] Yang Songlin: 修改吧
[00:10:39] Yang Songlin: 像
[00:10:40] Yang Songlin: 最近幾年
[00:10:41] Yang Songlin: 的話
[00:10:42] Yang Songlin: 就是
[00:10:43] 會把
[00:10:44] Yang Songlin: 傳統的
[00:10:45] Yang Songlin: MLP
[00:10:46] Yang Songlin: 或者說
[00:10:47] Yang Songlin: Fifleware
[00:10:48] Yang Songlin: 來我
[00:10:49] Yang Songlin: 專家的一些
[00:10:50] Yang Songlin: Mokeware
[00:10:51] Yang Songlin: MicheofExper
[00:10:51] Yang Songlin: MLP的一些
[00:10:53] Mokeware
[00:10:53] 然後
[00:10:54] Yang Songlin: 的話
[00:10:55] Yang Songlin: 就是把傳統的
[00:10:56] Yang Songlin: Suffmax
[00:10:58] 的Tension
[00:10:58] 把它
[00:11:00] Yang Songlin: 換成一些
[00:11:01] Yang Songlin: 現新
[00:11:02] 福島多的一些
[00:11:03] Yang Songlin: Tension
[00:11:04] Yang Songlin: 當然
[00:11:05] Yang Songlin: 現在最近
[00:11:06] Yang Songlin: 更活了
[00:11:07] Yang Songlin: 所以
[00:11:08] Yang Songlin: 疑淚叫做
[00:11:09] Yang Songlin: Hybrid的一個架構
[00:11:10] Yang Songlin: 有一些層
[00:11:11] Yang Songlin: 它還是
[00:11:12] Yang Songlin: 一個Suffmax
[00:11:13] Yang Songlin: 的Tension
[00:11:14] Yang Songlin: 另外
[00:11:15] Yang Songlin: 大部分的層
[00:11:16] 就把它換成
[00:11:17] Zhang Xiaojun: 新興趣味
[00:11:18] Zhang Xiaojun: 最進參與的一個
[00:11:19] Zhang Xiaojun: 行工作
[00:11:20] Zhang Xiaojun: 就是
[00:11:21] Zhang Xiaojun: Timidini
[00:11:22] Zhang Xiaojun: 你是怎麼
[00:11:23] Zhang Xiaojun: Timidini
[00:11:24] Zhang Xiaojun: 的工作中點
[00:11:25] Zhang Xiaojun: 這個工作
[00:11:26] 應該是
[00:11:27] Yang Songlin: 始緣
[00:11:28] Yang Songlin: 底缸發布
[00:11:29] Yang Songlin: 應該
[00:11:30] Yang Songlin: 他們
[00:11:31] Yang Songlin: 應該是
[00:11:32] Yang Songlin: 年初
[00:11:33] 就
[00:11:34] Yang Songlin: 想開始
[00:11:35] Yang Songlin: 做
[00:11:36] Yang Songlin: 然後當時
[00:11:37] Yang Songlin: Flystinial
[00:11:39] Yang Songlin: Tension
[00:11:40] Yang Songlin: 這個
[00:11:41] Yang Songlin: 酷
[00:11:43] Yang Songlin: 另外一個主要的
[00:11:44] 作者
[00:11:45] Yang Songlin: 他
[00:11:46] Yang Songlin: 叫
[00:11:47] Yang Songlin: BossB
[00:11:48] Yang Songlin: 當時
[00:11:49] Yang Songlin: 他正好
[00:11:50] Yang Songlin: 就是在
[00:11:51] Timid
[00:11:52] Yang Songlin: 想做
[00:11:53] Yang Songlin: 混合
[00:11:54] Yang Songlin: 主要
[00:11:55] Yang Songlin: 然後
[00:11:56] Yang Songlin: 張宇
[00:11:57] Yang Songlin: 就是在做這個
[00:11:58] 項目
[00:11:59] Yang Songlin: 因為我
[00:12:00] Yang Songlin: 因為
[00:12:01] Yang Songlin: 他
[00:12:02] Yang Songlin: 就是FLA
[00:12:03] Yang Songlin: 開完
[00:12:04] Yang Songlin: Colored
[00:12:05] 然後
[00:12:06] Yang Songlin: 我會
[00:12:07] 幫他們
[00:12:08] Yang Songlin: 看一下
[00:12:09] Yang Songlin: 有些
[00:12:11] 現行主要的
[00:12:12] Yang Songlin: 一些
[00:12:13] Yang Songlin: 變種
[00:12:14] Yang Songlin: 他的那些
[00:12:15] Yang Songlin: 變形的算法
[00:12:16] Yang Songlin: 設計之類的
[00:12:17] Yang Songlin: 當時
[00:12:18] Zhang Xiaojun: 他們團隊遇到的
[00:12:19] Zhang Xiaojun: 核心問題是什麼
[00:12:20] Zhang Xiaojun: 為什麼開始決定
[00:12:21] Zhang Xiaojun: 要重新設計一下
[00:12:22] Zhang Xiaojun: 注意力
[00:12:23] 記者
[00:12:24] Yang Songlin: 就是年初的時候
[00:12:25] Yang Songlin: 我覺得
[00:12:26] Yang Songlin: 大背景的話
[00:12:27] Yang Songlin: 就是
[00:12:28] 向DFC
[00:12:29] Yang Songlin: R1
[00:12:30] Yang Songlin: 和KIMI1.5
[00:12:31] Yang Songlin: 那個時候
[00:12:32] Yang Songlin: 剛剛發
[00:12:33] Yang Songlin: 然後
[00:12:34] Yang Songlin: 他的核心
[00:12:35] Yang Songlin: 他會做些R1
[00:12:37] Yang Songlin: 然後
[00:12:38] Yang Songlin: 會得到
[00:12:39] Yang Songlin: 一些
[00:12:40] Yang Songlin: 非常長的
[00:12:41] Yang Songlin: 一些
[00:12:42] Yang Songlin: 思維念
[00:12:43] Yang Songlin: 就是
[00:12:44] Yang Songlin: Tranford
[00:12:45] Yang Songlin: 非常長的
[00:12:46] Yang Songlin: 思維念
[00:12:47] Yang Songlin: 來做這種
[00:12:48] Yang Songlin: Test and Scaling
[00:12:50] Yang Songlin: 對
[00:12:51] Yang Songlin: 然後來
[00:12:52] Yang Songlin: 解一些
[00:12:53] Yang Songlin: 比較
[00:12:54] 附帶的問題
[00:12:55] Yang Songlin: 然後
[00:12:56] Yang Songlin: 這個
[00:12:57] Yang Songlin: 思維念的長度
[00:12:58] Yang Songlin: 能
[00:12:59] Yang Songlin: 他往往
[00:13:00] Yang Songlin: 就是
[00:13:01] Yang Songlin: 能夠到
[00:13:02] 幾萬個
[00:13:03] Yang Songlin: 頭肯
[00:13:04] Yang Songlin: 這個長度
[00:13:05] 然後
[00:13:06] Yang Songlin: KIMI
[00:13:07] Yang Songlin: 就覺得
[00:13:08] Yang Songlin: 就是
[00:13:09] Yang Songlin: 如果我們用
[00:13:10] Yang Songlin: 每一層
[00:13:11] Yang Songlin: 都是
[00:13:12] Yang Songlin: 平方
[00:13:13] Yang Songlin: 的這個
[00:13:14] Yang Songlin: 因為首先
[00:13:15] Yang Songlin: 就是
[00:13:16] Yang Songlin: 每一層
[00:13:17] Yang Songlin: 他要存一個
[00:13:18] Yang Songlin: 大量的
[00:13:19] Yang Songlin: KV開始
[00:13:20] 然後
[00:13:21] Yang Songlin: 換他
[00:13:22] Yang Songlin: 每一步
[00:13:23] Yang Songlin: 現身的
[00:13:24] Yang Songlin: 這個
[00:13:25] Yang Songlin: 時間複雜度
[00:13:26] Yang Songlin: 如果DECO
[00:13:27] Yang Songlin: 的L
[00:13:28] 個
[00:13:29] Yang Songlin: 頭肯的話
[00:13:30] Yang Songlin: 他的時間複雜度
[00:13:31] 也是
[00:13:32] Yang Songlin: 一個平方的
[00:13:33] Yang Songlin: 所以
[00:13:34] Yang Songlin: 在這種
[00:13:35] Yang Songlin: 長的
[00:13:36] Yang Songlin: 思維念的
[00:13:37] Yang Songlin: 深層的
[00:13:38] Yang Songlin: 背景下面
[00:13:39] Yang Songlin: 然後
[00:13:40] Yang Songlin: 讓KIMI
[00:13:41] 覺得
[00:13:42] Yang Songlin: 就是
[00:13:43] Yang Songlin: 這個
[00:13:44] Yang Songlin: 資源
[00:13:45] Yang Songlin: 來探索一下
[00:13:46] 這種
[00:13:47] Yang Songlin: 注意力
[00:13:48] Yang Songlin: 因為
[00:13:49] Yang Songlin: 他能夠
[00:13:50] 把這個
[00:13:51] Yang Songlin: Inference
[00:13:52] Yang Songlin: 的
[00:13:53] Yang Songlin: Cost
[00:13:54] Yang Songlin: 把它
[00:13:55] Yang Songlin: 大低
[00:13:56] Yang Songlin: 很多
[00:13:57] Yang Songlin: 對
[00:13:58] 這一點
[00:13:59] Yang Songlin: 在這種長
[00:14:00] Yang Songlin: 思維念
[00:14:01] Yang Songlin: 弄串
[00:14:02] Yang Songlin: 色的這個
[00:14:03] Yang Songlin: 背景下面
[00:14:04] Yang Songlin: 然後
[00:14:05] 以及
[00:14:06] Zhang Xiaojun: 今年
[00:14:07] Zhang Xiaojun: 整體的這個
[00:14:08] Zhang Xiaojun: Agenity
[00:14:09] AI的這個
[00:14:10] Yang Songlin: 背景下面
[00:14:11] Yang Songlin: 他是
[00:14:12] Yang Songlin: 對
[00:13:58] 大概
[00:14:12] Yang Songlin: 那邊做完
[00:14:13] Yang Songlin: 然後
[00:14:14] Yang Songlin: 他們的目標
[00:14:15] Yang Songlin: 應該就是
[00:14:16] Yang Songlin: 就是跟
[00:14:17] Yang Songlin: 之前的那種
[00:14:18] Yang Songlin: 富爾探索
[00:14:19] Yang Songlin: 相比的話
[00:14:20] Yang Songlin: 就是
[00:14:21] Yang Songlin: Performance
[00:14:22] Yang Songlin: 要
[00:14:23] Yang Songlin: 不掉點
[00:14:24] Yang Songlin: 然後
[00:14:25] Yang Songlin: 同時
[00:14:26] Yang Songlin: 他的
[00:14:27] Zhang Xiaojun: Inference
[00:14:28] Zhang Xiaojun: 會快很多
[00:14:29] Zhang Xiaojun: 背
[00:14:30] Yang Songlin: 如果用富爾探索的話
[00:14:31] Yang Songlin: 就是這種
[00:14:32] Yang Songlin: 做長文本的
[00:14:33] Yang Songlin: DECOLEAN
[00:14:34] Yang Songlin: 的時候
[00:14:35] Yang Songlin: 他就是
[00:14:36] Yang Songlin: 非常的
[00:14:37] Zhang Xiaojun: 寒貴
[00:14:38] Zhang Xiaojun: 能不能
[00:14:39] Zhang Xiaojun: 視角
[00:14:40] Zhang Xiaojun: 給大家
[00:14:41] 像這篇文章
[00:14:43] Yang Songlin: 的話
[00:14:44] Yang Songlin: 他們的這個
[00:14:46] 就是這個
[00:14:47] Yang Songlin: 現新注意的
[00:14:48] Yang Songlin: 模塊
[00:14:49] Yang Songlin: 選到的是
[00:14:50] Yang Songlin: 一個叫做
[00:14:51] Yang Songlin: KDA的這個
[00:14:52] Yang Songlin: 模塊
[00:14:53] Yang Songlin: Kimi
[00:14:54] Yang Songlin: 的Tension
[00:14:55] Yang Songlin: 對
[00:14:56] 這個名字
[00:14:57] Yang Songlin: 感覺挺有耿的
[00:14:58] Yang Songlin: 他們應該是想
[00:14:59] Yang Songlin: 對標
[00:15:00] Yang Songlin: DECOLEAN
[00:15:01] Yang Songlin: Tension
[00:15:02] Yang Songlin: 然後我就
[00:15:03] Yang Songlin: 特意去了一個
[00:15:04] Yang Songlin: Kimi開頭的
[00:15:05] Yang Songlin: 一個名字
[00:15:06] Yang Songlin: 然後
[00:15:07] Yang Songlin: 非常的對象
[00:15:08] 對
[00:15:09] Yang Songlin: 然後這個
[00:15:10] 現新注意的
[00:15:11] Yang Songlin: 模塊
[00:15:12] Yang Songlin: 他
[00:15:13] Yang Songlin: 基本上就是
[00:15:14] Yang Songlin: 基於
[00:15:15] 我去年
[00:15:16] Yang Songlin: 有一個工作
[00:15:17] Yang Songlin: 叫做
[00:15:18] Yang Songlin: Gate Data Knight
[00:15:19] Yang Songlin: 然後
[00:15:20] Yang Songlin: 在這個
[00:15:21] Yang Songlin: 基礎上面
[00:15:22] Yang Songlin: 就是
[00:15:23] Yang Songlin: 進行那一些
[00:15:24] Yang Songlin: 改善
[00:15:25] Yang Songlin: 然後最後
[00:15:26] Yang Songlin: 形成
[00:15:27] Yang Songlin: 一個
[00:15:28] Yang Songlin: 叫做KDA的
[00:15:29] Yang Songlin: 一個模塊
[00:15:30] Yang Songlin: 總來說的話
[00:15:31] Yang Songlin: 就是
[00:15:32] Yang Songlin: 首先我沒有
[00:15:33] Yang Songlin: 一個叫做
[00:15:34] Yang Songlin: Data
[00:15:35] Yang Songlin: 入了一個東西
[00:15:36] Yang Songlin: 對
[00:15:37] Yang Songlin: 可以
[00:15:38] Yang Songlin: 之後
[00:15:39] Yang Songlin: 像
[00:15:41] Yang Songlin: Gate Data Knight的時候
[00:15:42] Yang Songlin: 就這個工作
[00:15:43] Yang Songlin: 就當時
[00:15:44] 收縣於
[00:15:46] Yang Songlin: Efficiency
[00:15:47] 然後
[00:15:48] Yang Songlin: 當時我就
[00:15:49] Yang Songlin: 用到了一個
[00:15:50] 像
[00:15:51] Yang Songlin: Mamba
[00:15:52] Yang Songlin: 2一樣的一個
[00:15:53] Yang Songlin: Skater
[00:15:54] 外流的一個Gate
[00:15:56] Yang Songlin: 這個的話
[00:15:58] Yang Songlin: 就是說
[00:15:59] Yang Songlin: 他的這個
[00:16:00] Yang Songlin: 門控
[00:16:01] Yang Songlin: 他的這個
[00:16:02] Yang Songlin: 就是對於一個
[00:16:04] Yang Songlin: Eternation
[00:16:05] Yang Songlin: Head
[00:16:06] Yang Songlin: 他說
[00:16:07] Yang Songlin: 他下面的
[00:16:08] Yang Songlin: 一個
[00:16:09] Yang Songlin: DK的一個
[00:16:11] Yang Songlin: 衰簡率
[00:16:12] Yang Songlin: 這的話
[00:16:13] Yang Songlin: 他是
[00:16:14] Yang Songlin: 可以在
[00:16:15] Yang Songlin: 計算上面
[00:16:16] Yang Songlin: 會帶來一些
[00:16:17] Yang Songlin: 簡化
[00:16:18] Yang Songlin: 所以
[00:16:19] Yang Songlin: 當時
[00:16:20] Yang Songlin: 的考慮
[00:16:21] Yang Songlin: 就是說
[00:16:22] Yang Songlin: Mamba
[00:16:23] Yang Songlin: 2的基礎上面
[00:16:24] Yang Songlin: 就是
[00:16:25] Yang Songlin: 加上
[00:16:26] Yang Songlin: 德塔入
[00:16:27] Yang Songlin: 然後
[00:16:28] Yang Songlin: 能讓他的這個
[00:16:29] Yang Songlin: 效率
[00:16:30] Yang Songlin: 有保證
[00:16:31] Yang Songlin: 所以
[00:16:32] Yang Songlin: 所以
[00:16:33] Yang Songlin: 當時
[00:16:34] 就是
[00:16:35] Yang Songlin: 用到了
[00:16:36] Yang Songlin: 他們那一種
[00:16:37] Yang Songlin: 門控的一個機制
[00:16:39] 對
[00:16:40] Yang Songlin: 所以這就是
[00:16:41] Yang Songlin: Gate的他
[00:16:43] Yang Songlin: Nine
[00:16:44] Yang Songlin: 然後像
[00:16:45] Yang Songlin: 張宇完的這個
[00:16:46] Yang Songlin: KDA
[00:16:47] Yang Songlin: 他
[00:16:48] Yang Songlin: 就是
[00:16:49] 把這個
[00:16:50] Yang Songlin: E度
[00:16:51] Yang Songlin: 比較
[00:16:52] Yang Songlin: 粗的一個
[00:16:53] Yang Songlin: 衰簡率
[00:16:54] Yang Songlin: 把它換成了
[00:16:55] Yang Songlin: 一個
[00:16:56] Yang Songlin: E度
[00:16:57] Yang Songlin: 比較
[00:16:58] Yang Songlin: 細了一個衰簡率
[00:16:59] Yang Songlin: 就是
[00:17:00] Yang Songlin: 現在
[00:17:01] Yang Songlin: 的話
[00:17:02] Yang Songlin: 就是
[00:17:03] 一個
[00:17:04] Yang Songlin: Tanzen
[00:17:05] Yang Songlin: 害了下面
[00:17:06] Yang Songlin: 不同的
[00:16:46] Yang Songlin: 位度
[00:17:06] Yang Songlin: 他有一個
[00:17:07] Yang Songlin: 自己的這個
[00:17:08] Yang Songlin: 衰簡率
[00:17:09] 這樣的話
[00:17:10] Yang Songlin: 就是
[00:17:11] Yang Songlin: 每一個
[00:17:12] Yang Songlin: 圍度
[00:17:13] Yang Songlin: 他對於
[00:17:14] Yang Songlin: 安的那個
[00:17:15] Yang Songlin: 機的那個
[00:17:16] 隱藏狀態的話
[00:17:18] Yang Songlin: 他就是
[00:17:19] 有自己
[00:17:20] Yang Songlin: 獨立的一套
[00:17:21] Yang Songlin: 更新的那個
[00:17:22] 頻率
[00:17:23] Yang Songlin: 這樣的話
[00:17:24] Yang Songlin: 就是
[00:17:25] Yang Songlin: 從此
[00:17:26] Yang Songlin: 就像
[00:17:27] Yang Songlin: 他看
[00:17:28] Yang Songlin: 他就是
[00:17:29] Yang Songlin: 能夠
[00:17:30] Yang Songlin: 更好的利用
[00:17:31] Yang Songlin: 這個
[00:17:32] Yang Songlin: 安有線的
[00:17:33] Heart and State
[00:17:34] Zhang Xiaojun: 能夠提高這個
[00:17:35] Zhang Xiaojun: 來源於什麼
[00:17:36] 我感覺
[00:17:37] Yang Songlin: 這個設計的話
[00:17:38] Yang Songlin: 其實
[00:17:39] Yang Songlin: 我覺得
[00:17:40] Yang Songlin: 像KD的話
[00:17:41] Yang Songlin: 他其實
[00:17:42] Yang Songlin: 就是我前兩個
[00:17:43] 工作的一個
[00:17:45] Yang Songlin: 就把之前
[00:17:46] Yang Songlin: 有兩個工作的
[00:17:47] Yang Songlin: 那種
[00:17:48] Yang Songlin: I'd
[00:17:49] Yang Songlin: 要把它
[00:17:50] Yang Songlin: 像我之前
[00:17:51] Yang Songlin: 還有一個
[00:17:52] Yang Songlin: 工作
[00:17:53] Yang Songlin: 叫做
[00:17:54] Yang Songlin: Nine
[00:17:55] Yang Songlin: Tanzen
[00:17:56] Yang Songlin: 他就是
[00:17:57] Yang Songlin: 有一個
[00:17:58] Yang Songlin: 這種
[00:17:59] Yang Songlin: E度
[00:18:00] 比較
[00:18:01] Yang Songlin: 細了一個
[00:18:02] 衰簡率
[00:18:03] Yang Songlin: 然後
[00:18:04] Yang Songlin: 當時之所以沒有
[00:18:05] Yang Songlin: 用到這種
[00:18:06] Yang Songlin: E度比較
[00:18:07] Yang Songlin: 細了這個
[00:18:08] Yang Songlin: 衰簡率
[00:18:09] 就是
[00:18:10] Yang Songlin: 算法
[00:18:11] Yang Songlin: 本身
[00:18:12] Yang Songlin: 和這個
[00:18:13] Yang Songlin: KD
[00:18:14] Yang Songlin: 優化
[00:18:15] Yang Songlin: 都沒有
[00:18:16] Yang Songlin: 優化到
[00:18:17] Yang Songlin: 一個比較好的狀態
[00:18:18] Yang Songlin: 所以
[00:18:19] Yang Songlin: 當時
[00:18:20] Yang Songlin: 就是考慮到
[00:18:21] Yang Songlin: 這個
[00:18:22] Yang Songlin: 效率的問題
[00:18:23] 就是
[00:18:24] Yang Songlin: Baple
[00:18:25] Yang Songlin: 就是
[00:18:26] Yang Songlin: 只能用
[00:18:27] Yang Songlin: Mamba
[00:18:28] Yang Songlin: Tune
[00:18:29] Yang Songlin: 那種
[00:18:30] Yang Songlin: E度
[00:18:31] Yang Songlin: 跟
[00:18:32] 除了一個
[00:18:33] Yang Songlin: 優化的層面的話
[00:18:34] Yang Songlin: 都是有一些
[00:18:35] Yang Songlin: 很多
[00:18:36] Yang Songlin: 進步的
[00:18:37] Yang Songlin: 然後
[00:18:38] 年初的
[00:18:39] Yang Songlin: 這個時間
[00:18:40] Yang Songlin: 點的話
[00:18:41] Yang Songlin: 就大家就覺得
[00:18:42] Yang Songlin: 是不是可以重新
[00:18:43] Yang Songlin: 來研究一下
[00:18:45] Yang Songlin: 能不能
[00:18:46] Yang Songlin: 把這個
[00:18:47] 翻棍
[00:18:48] Yang Songlin: DK
[00:18:49] Yang Songlin: 把這個
[00:18:50] Yang Songlin: 力度
[00:18:51] Yang Songlin: 比較細了這個
[00:18:52] Yang Songlin: 衰簡率
[00:18:53] Yang Songlin: 把它
[00:18:54] 引回到
[00:18:55] Zhang Xiaojun: KD
[00:18:56] Zhang Xiaojun: DK
[00:18:57] Zhang Xiaojun: DK
[00:18:58] Yang Songlin: 你們
[00:18:59] Yang Songlin: 設計完
[00:19:00] Yang Songlin: 最初
[00:19:01] Yang Songlin: 效果
[00:19:02] 它
[00:19:03] Yang Songlin: 它應該是
[00:19:04] Yang Songlin: 先試了
[00:19:05] Yang Songlin: 一大堆
[00:19:06] Yang Songlin: 這種
[00:19:07] Yang Songlin: 混合
[00:19:08] Yang Songlin: JR的這種
[00:19:09] Yang Songlin: 混法
[00:19:10] Yang Songlin: 然後它最開始
[00:19:11] Yang Songlin: 是
[00:19:12] 發現
[00:19:13] 混
[00:19:14] Yang Songlin: DK
[00:19:15] Yang Songlin: 那也特別
[00:19:16] Yang Songlin: 混其他的要好
[00:19:17] Yang Songlin: 然後
[00:19:18] Yang Songlin: 後面它
[00:19:19] Yang Songlin: 就是
[00:19:20] Yang Songlin: 因為他們
[00:19:21] Yang Songlin: KIMI
[00:19:22] Yang Songlin: 內部
[00:19:23] 它是有一個
[00:19:24] Yang Songlin: 叫做
[00:19:25] Yang Songlin: Skelling Light
[00:19:26] Yang Songlin: 的一個東西
[00:19:27] Yang Songlin: 就是說
[00:19:28] Yang Songlin: 你在
[00:19:29] Yang Songlin: 一個
[00:19:30] Yang Songlin: 規模
[00:19:31] Yang Songlin: 你就
[00:19:32] Yang Songlin: 到下面一個
[00:19:33] Yang Songlin: 規模去
[00:19:34] Yang Songlin: 繼續Skelling
[00:19:35] Yang Songlin: 就
[00:19:36] Yang Songlin: 有點像
[00:19:37] Yang Songlin: 通關
[00:19:38] Yang Songlin: 它有很多
[00:19:39] Yang Songlin: 很多關卡
[00:19:40] Yang Songlin: 過了一關
[00:19:41] Yang Songlin: 它
[00:19:42] Yang Songlin: 有到
[00:19:43] Yang Songlin: 下一關
[00:19:44] 就
[00:19:45] Yang Songlin: 繼續
[00:19:46] Yang Songlin: 跟
[00:19:47] Yang Songlin: 彈省
[00:19:48] Yang Songlin: 去比
[00:19:49] Yang Songlin: 然後
[00:19:50] Yang Songlin: 最開始的話
[00:19:51] Yang Songlin: 可能就發現
[00:19:52] Yang Songlin: 就是
[00:19:53] Yang Songlin: Habaret
[00:19:54] Yang Songlin: Gate
[00:19:55] Yang Songlin: 那
[00:19:56] 會
[00:19:57] Yang Songlin: 會
[00:19:58] Yang Songlin: 會
[00:19:59] Yang Songlin: 會
[00:20:01] Yang Songlin: 然後
[00:20:02] Yang Songlin: 後面的話
[00:20:03] Yang Songlin: 它就開始
[00:20:04] Yang Songlin: 玩了一下
[00:20:05] Yang Songlin: 就是那種
[00:20:06] 把
[00:20:07] Yang Songlin: DK
[00:20:08] Yang Songlin: 把它換成
[00:20:09] Yang Songlin: 這種
[00:20:10] Yang Songlin: 更加細率
[00:20:11] Yang Songlin: 的這個
[00:20:12] Yang Songlin: DK
[00:20:13] Yang Songlin: 然後它發現
[00:20:14] Yang Songlin: 就是在
[00:20:15] 它的
[00:20:16] Yang Songlin: 的提升
[00:20:17] Yang Songlin: 還挺大的
[00:20:18] Amy Linny
[00:20:19] Zhang Xiaojun: 的哼聲
[00:20:20] Zhang Xiaojun: Deafseek
[00:20:21] Zhang Xiaojun: Spass
[00:20:22] Zhang Xiaojun: 哼聲
[00:20:23] Zhang Xiaojun: 你自己覺得
[00:20:24] Zhang Xiaojun: 他們的表現
[00:20:25] Zhang Xiaojun: 哪個
[00:20:30] Yang Songlin: 其實是相結的問題是一個問題
[00:20:33] Yang Songlin: 就是在這種長文本的Coding下面
[00:20:36] Yang Songlin: 如何解決這個效率的問題
[00:20:39] 然後像Kimi他走的是這種混合Jury的路線
[00:20:44] Yang Songlin: 對 其實千萬他也走的是這一條
[00:20:47] Yang Songlin: 現在主要是在逃入這種混合Jury的這種路線
[00:20:51] 然後像DFC的話
[00:20:53] Yang Songlin: 他們主要就喜歡走這個西蘇蘇裏的這個路線
[00:20:57] Yang Songlin: 他們那個Kimi Spassal Tension
[00:20:58] Yang Songlin: 然後包括他們之前發的那個Late Spassal Tension
[00:21:03] Yang Songlin: 都是這種走的西蘇的路線
[00:21:05] Yang Songlin: 然後他們覺得可能西蘇是一種更好的方式
[00:21:09] Yang Songlin: 來降低這種DCoding的Cost
[00:21:14] Yang Songlin: 像DFC可能是Spassal Tension的話
[00:21:19] Yang Songlin: 他應該是沒有負了Tension的
[00:21:22] Yang Songlin: 所以他應該是每一層都是DFC Spassal Tension
[00:21:27] Yang Songlin: 但是他每一層的話
[00:21:29] Yang Songlin: 他都要把所有的KiriCatch把它全部存下了
[00:21:33] Yang Songlin: 然後他只能就是從一個Triple Point
[00:21:37] Yang Songlin: 然後來經過一些Junior
[00:21:40] Yang Songlin: 然後得到他的那個叫做Index的一個東西來選
[00:21:45] Yang Songlin: 那些Tobok的一個Token
[00:21:48] 最最DFC的Tension
[00:21:50] 然後像混合Jury的最一條路線的話
[00:21:53] Yang Songlin: 他還是有一些全局Jury Needle
[00:21:56] Yang Songlin: 然後他的那些比較快速的那些層
[00:22:00] Yang Songlin: 是一些線性Jury Needle層
[00:22:02] Yang Songlin: 然後這個好處的話
[00:22:03] Yang Songlin: 就是說他可以使很多的KiriCatch
[00:22:07] Yang Songlin: 然後混合Jury的話
[00:22:09] Yang Songlin: 他就是不僅他能減少KiriCatch
[00:22:13] Yang Songlin: 他能減少很多KiriCatch
[00:22:15] Yang Songlin: 因為他覺得都是層都是這種
[00:22:17] Yang Songlin: 類似Yahana的這種層
[00:22:19] 然後他同時也能提高DCoding的效率
[00:22:23] Yang Songlin: 然後因為他減少了KiriCatch的Size
[00:22:26] Yang Songlin: 所以他做DCoding的時候
[00:22:28] Yang Songlin: 可能就可以去用一些
[00:22:31] Yang Songlin: 更大的BatchSize
[00:22:33] Yang Songlin: 因為之前可能放不下
[00:22:35] Yang Songlin: 然後現在KiriCatch被減少了很多
[00:22:38] Yang Songlin: 然後這個時候可能就可以加到BatchS的Size
[00:22:43] 像DFCSBUSS的Tension的話
[00:22:44] Yang Songlin: 他是沒有減少KiriCatch的作用的
[00:22:50] Yang Songlin: 但是他可以通過Size的這個
[00:22:53] Yang Songlin: 機會來減少每一個頭肯深層的那個花肺
[00:22:58] Yang Songlin: 對
[00:22:59] 還有一個JAMINIMACS
[00:23:01] 他們最新也做了一個算法的選擇
[00:23:04] 對像MiniMax的話
[00:23:06] Yang Songlin: 他上一版是Linia Tension
[00:23:10] 他應該算是這種混合
[00:23:13] Yang Songlin: 這種混合線性和平方
[00:23:16] Yang Songlin: 助理的一個先曲
[00:23:18] Yang Songlin: 因為他年初發的M1的版本的話
[00:23:22] Yang Songlin: 是一個非常大規模的混合助理的一個時間
[00:23:28] Yang Songlin: 然後他們前幾天發了一個M2的模型
[00:23:32] Yang Songlin: 然後這個模型
[00:23:34] Yang Songlin: 他現在就變成了一個Full of Tension
[00:23:37] Yang Songlin: 他既不是這種混合助理
[00:23:40] Yang Songlin: 他也不用Size的Tension
[00:23:42] Yang Songlin: 他就乾脆把他退回了Full of Tension
[00:23:47] Yang Songlin: 對
[00:23:48] 這是為什麼呀
[00:23:49] Yang Songlin: 我覺得是
[00:23:52] 我覺得他們的這個負責團
[00:23:55] Yang Songlin: 對他們非常的 open
[00:23:58] Yang Songlin: 然後他們分享了很多這種經驗
[00:24:00] Yang Songlin: 然後我覺得這個經驗都是很寶貴的
[00:24:03] 就是比方說我知道他們說
[00:24:06] Yang Songlin: 就是他們第一版的
[00:24:08] Yang Songlin: 他們第一版的話
[00:24:10] Yang Songlin: 他們監控了一些指標
[00:24:12] Yang Songlin: 就是發現他們用到的Lighting Need
[00:24:15] Yang Songlin: Tension的模塊
[00:24:16] Yang Songlin: 在這些指標上面表現得很好
[00:24:18] Yang Songlin: 然後Lighting Need
[00:24:20] Yang Songlin: Tension他又效率更高一點
[00:24:21] Yang Songlin: 所以他們最後就上這個Lighting Need
[00:24:23] Yang Songlin: Tension
[00:24:24] Yang Songlin: 對
[00:24:25] 然後後面他們發現就是
[00:24:27] Yang Songlin: 如果他們在一些比方說
[00:24:29] Yang Songlin: 那種叫做
[00:24:31] Yang Songlin: Motivop Reasoning
[00:24:33] Yang Songlin: 就是多跳的這個
[00:24:35] Yang Songlin: Rhythm Need
[00:24:36] Yang Songlin: 上面這種Tasks的話
[00:24:38] Yang Songlin: 他發現這個調點會非常的大
[00:24:40] Yang Songlin: 對
[00:24:41] 然後這個的話
[00:24:42] Yang Songlin: 就當初用那個方的話
[00:24:44] Yang Songlin: 就是
[00:24:46] 因為他們最開始沒有去檢測這種
[00:24:49] Yang Songlin: 多跳推力的這個能力
[00:24:51] Yang Songlin: 然後他們主要只看那些
[00:24:53] Yang Songlin: 比方說MML UR
[00:24:54] Yang Songlin: 然後J的這種能力
[00:24:57] 然後他們就選了一個非常
[00:25:01] 就
[00:25:02] 結果來說的話
[00:25:02] 我覺得那個Nighting Need
[00:25:04] Yang Songlin: Tension的話
[00:25:04] Yang Songlin: 他其實是一個
[00:25:06] Yang Songlin: 比較弱的一個先行注意力
[00:25:08] Yang Songlin: 因為他那個機制就感覺
[00:25:11] Yang Songlin: 最近兩年先行注意力
[00:25:13] Yang Songlin: 這個領域發展了很多
[00:25:14] Yang Songlin: 然後他用到了那個
[00:25:16] Yang Songlin: 音量的Tension
[00:25:17] Yang Songlin: 就給人的感覺
[00:25:18] Yang Songlin: 就是像是兩年前的
[00:25:20] Yang Songlin: 一個音量的Tension
[00:25:21] Yang Songlin: 就那個技術的那個
[00:25:23] Yang Songlin: Highting Need
[00:25:24] Yang Songlin: 在兩年前
[00:25:25] Yang Songlin: 對
[00:25:26] 可能就是
[00:25:27] Yang Songlin: 他用可能就是因為他們
[00:25:28] Yang Songlin: 第一版他們的那個
[00:25:30] Yang Songlin: 做評價的那個Papenai
[00:25:33] Yang Songlin: 不夠
[00:25:34] Yang Songlin: 想盡吧
[00:25:35] Yang Songlin: 然後他們就選了這麼一套
[00:25:37] Yang Songlin: 比較
[00:25:38] Yang Songlin: 比較
[00:25:40] 略顯哪一部的一個方案
[00:25:42] Yang Songlin: 然後最近的話
[00:25:44] Yang Songlin: 他們可能是想
[00:25:47] Yang Songlin: 做了這種
[00:25:48] Yang Songlin: Agentic Toss
[00:25:49] Yang Songlin: 可能想做這種
[00:25:51] Yang Songlin: Coding吧
[00:25:52] Yang Songlin: 然後像多跳推理
[00:25:55] Yang Songlin: 這一個能力的話
[00:25:56] Yang Songlin: 就是會在這種場
[00:25:58] Yang Songlin: 你下面變得非常重要
[00:26:00] Yang Songlin: 然後他們就發現
[00:26:01] Yang Songlin: Line Need Tension
[00:26:02] Yang Songlin: 可能跟富爾Tension
[00:26:04] Yang Songlin: 他直接的這個
[00:26:07] Yang Songlin: Poformance的這個差距還挺大的
[00:26:09] Yang Songlin: 然後
[00:26:10] Yang Songlin: 他們就暫時退回了
[00:26:12] Yang Songlin: 這個
[00:26:13] 全部都是Somai's Tension
[00:26:14] Yang Songlin: 的這個富爾Tension的這個加勾
[00:26:17] 對
[00:26:17] 但他們說
[00:26:18] Yang Songlin: 他們還在繼續探索
[00:26:20] Yang Songlin: 這種混合處理的加勾
[00:26:23] Yang Songlin: 說不定他們下一版
[00:26:24] Yang Songlin: Ampsan又變成混合處理加勾
[00:26:27] Yang Songlin: 你怎麼看待就是
[00:26:28] Zhang Xiaojun: 大家在這種算法
[00:26:30] 上的不同的選擇
[00:26:31] Zhang Xiaojun: 或者是反覆
[00:26:32] Zhang Xiaojun: 像歷史的話
[00:26:33] Yang Songlin: 就會螺旋上升
[00:26:35] Yang Songlin: 就是一套技術方
[00:26:36] Yang Songlin: 就肯定是要
[00:26:37] Yang Songlin: 經過很多很多
[00:26:39] Yang Songlin: 驗證才能最後定下來的
[00:26:41] Yang Songlin: 對
[00:26:42] Yang Songlin: 像M1可能當時
[00:26:45] Yang Songlin: 就是沒有驗證
[00:26:46] Yang Songlin: 比較充分
[00:26:47] Yang Songlin: 所以當時就比較
[00:26:48] Yang Songlin: 草率的上
[00:26:50] Yang Songlin: 然後後面發現
[00:26:51] Yang Songlin: 他在這種對跳推理上面
[00:26:52] Yang Songlin: 他效果不好
[00:26:53] Yang Songlin: 然後就暫時退回了
[00:26:54] Yang Songlin: 這個也是
[00:26:56] 很正常的
[00:26:57] Yang Songlin: 對
[00:26:58] 規劃公司現在
[00:27:00] 對於混合處理
[00:27:01] Zhang Xiaojun: 以及制探的探索方向
[00:27:03] Zhang Xiaojun: 是什麼樣的
[00:27:04] 各家公司什麼樣
[00:27:05] Zhang Xiaojun: 這個我感覺
[00:27:07] Yang Songlin: 不能講了
[00:27:08] Zhang Xiaojun: 哦
[00:27:09] Open i什麼的可以講了
[00:27:11] Open i的話
[00:27:12] Yang Songlin: 我只能講有一些
[00:27:17] Yang Songlin: 就是有一些有
[00:27:18] Yang Songlin: paper的一些方案
[00:27:19] Yang Songlin: 就是沒有paper的方案
[00:27:20] Yang Songlin: 我是不會講的
[00:27:22] Yang Songlin: Open i的話
[00:27:22] Yang Songlin: 他是
[00:27:24] Yang Songlin: 他是
[00:27:24] Yang Songlin: 表示像GPD3的話
[00:27:26] Yang Songlin: 他在那個
[00:27:28] Yang Songlin: 他的那個
[00:27:28] Yang Songlin: Taglia和report裡面就講了
[00:27:31] 他會用到一個混合的
[00:27:33] Yang Songlin: 一個全局的一個注意力
[00:27:35] Yang Songlin: 和一個logo的一個slayer裡面的探索
[00:27:37] Yang Songlin: 這麼一個混合的一個方案
[00:27:39] Yang Songlin: 對
[00:27:40] Yang Songlin: 像這個的話
[00:27:41] Yang Songlin: 他是在GPD3的那個報告裡面
[00:27:44] Yang Songlin: 就已經明確地寫出來了
[00:27:45] Yang Songlin: 所以這個是可以講的
[00:27:47] Yang Songlin: 對
[00:27:47] Yang Songlin: 然後像他們最近的那個
[00:27:49] Yang Songlin: OSS的那個
[00:27:50] Yang Songlin: 發出來的那個
[00:27:52] 開源模型嗎
[00:27:53] Yang Songlin: 他們也是用到這種
[00:27:54] Yang Songlin: 華動注意力的這一套方案
[00:27:57] Yang Songlin: 對
[00:27:58] 所以他們應該
[00:27:59] Yang Songlin: 就一直在用這一套
[00:28:00] Yang Songlin: 華動注意力的方案吧
[00:28:02] Yang Songlin: 對
[00:28:03] 我倒後就講一下
[00:28:04] Zhang Xiaojun: 因為你剛才說
[00:28:05] Zhang Xiaojun: Linia 等於這兩年
[00:28:06] Zhang Xiaojun: 發展也有很多
[00:28:07] Zhang Xiaojun: 那給大家講一下
[00:28:08] Zhang Xiaojun: 他的這個發展線索
[00:28:10] 好
[00:28:11] Zhang Xiaojun: 好
[00:28:12] 像
[00:28:13] Yang Songlin: Linia 等於他誕生的話
[00:28:15] Yang Songlin: 他最開始的話
[00:28:16] Yang Songlin: 我覺得就是非常的
[00:28:17] Yang Songlin: Block
[00:28:18] Yang Songlin: 對
[00:28:19] Yang Songlin: 他就算他在短文
[00:28:20] Yang Songlin: 不能下面
[00:28:21] Yang Songlin: 他也Block
[00:28:22] 然後
[00:28:24] 因為他那個最早的
[00:28:25] Yang Songlin: Linia 等於是
[00:28:26] Yang Songlin: 12年12年
[00:28:26] Yang Songlin: 發明的嗎
[00:28:28] Yang Songlin: 然後我覺得他可能
[00:28:29] Yang Songlin: 這中間的這幾年
[00:28:31] Yang Songlin: 就是在Nanguage Modeling
[00:28:33] Yang Songlin: 原建模上面
[00:28:34] Yang Songlin: 他都沒有
[00:28:35] Yang Songlin: 效果沒有跑到很好
[00:28:37] 然後每一個表現
[00:28:38] Yang Songlin: 有代表現場的功能
[00:28:39] Yang Songlin: 就是RinLive
[00:28:40] Yang Songlin: 然後他就是通過
[00:28:42] Yang Songlin: 加一個
[00:28:43] Yang Songlin: E-Wall衰減的一個機制
[00:28:45] Yang Songlin: 然後就發現
[00:28:47] Linia Tanshan
[00:28:48] Yang Songlin: 他
[00:28:49] Skyl上去他
[00:28:51] Yang Songlin: 在原建模上面
[00:28:52] Yang Songlin: 還是可以取得
[00:28:54] Yang Songlin: 一個比較好的一個效果的
[00:28:56] Yang Songlin: 對
[00:28:57] Yang Songlin: 然後RinLive的話
[00:28:59] Yang Songlin: 他就是
[00:29:00] Yang Songlin: 往他加了一個
[00:29:02] Yang Songlin: 就是輸入無關的一個DK
[00:29:05] 輸入無關的DK的話
[00:29:06] Yang Songlin: 就是說
[00:29:08] Yang Songlin: 他那個E-Wall蕴
[00:29:09] Yang Songlin: 他是跟輸入沒有關係的
[00:29:12] Yang Songlin: 比方說他的E-Wall蕴是0.99
[00:29:15] Yang Songlin: 那樣子的話
[00:29:16] Yang Songlin: 他每過一個頭肯的話
[00:29:18] Yang Songlin: 他前面的那個
[00:29:20] Yang Songlin: Pedance Data
[00:29:20] Yang Songlin: 他就要沉上0.99
[00:29:23] 真的的話
[00:29:23] 他就以往掉
[00:29:24] Yang Songlin: 他1%的這個東西了
[00:29:26] Yang Songlin: 然後他在把新的這個東西
[00:29:27] Yang Songlin: 把它寫進去
[00:29:29] 這就是一個叫做
[00:29:30] Yang Songlin: 輸入無關的一個衰減
[00:29:32] 這就是RinLive他用到了一個技術
[00:29:35] 然後這種輸入無關的這種
[00:29:39] Yang Songlin: 以往的話
[00:29:40] Yang Songlin: 他在之後
[00:29:41] Yang Songlin: 應該是被逐漸替換成
[00:29:44] Yang Songlin: 那種輸入相關的一個衰減
[00:29:47] 就比如說像我
[00:29:49] 之前的一個叫
[00:29:50] Yang Songlin: Gating Linear Tanshan
[00:29:51] Yang Songlin: 前面也提到了
[00:29:52] Yang Songlin: 就是加了一個門控的一個機制
[00:29:56] 然後像Mamba和Mamba
[00:29:57] Yang Songlin: Tue的話
[00:29:58] Yang Songlin: 他們其實也是跟現行注意力的話
[00:30:00] Yang Songlin: 是很有很多年系的
[00:30:03] Yang Songlin: 尤其是Mamba Tue
[00:30:04] Yang Songlin: Mamba Tue的話
[00:30:05] Yang Songlin: 讓他基本上就可以看成是
[00:30:07] Yang Songlin: 現行注意力
[00:30:09] Yang Songlin: 然後他加了一個衰減
[00:30:11] Yang Songlin: 但是這個衰減跟RinLive非常像
[00:30:14] Yang Songlin: 然後他跟RinLive去
[00:30:15] Yang Songlin: 比如說那個衰減
[00:30:17] Yang Songlin: 他是有輸入來決定的
[00:30:20] Yang Songlin: 就是每一個頭肯
[00:30:22] Yang Songlin: 他的衰減率
[00:30:23] Yang Songlin: 他就可能不一樣
[00:30:24] Yang Songlin: 對
[00:30:25] Yang Songlin: 就比方說他遇到有一些頭肯
[00:30:28] Yang Songlin: 他覺得這些前面的內容
[00:30:30] Yang Songlin: 沒有標誤
[00:30:31] Yang Songlin: 他就把
[00:30:32] Yang Songlin: 可以把那個衰減率視為一
[00:30:34] Yang Songlin: 這樣子的話
[00:30:35] Yang Songlin: 前面就根本不去做這種衰減
[00:30:39] 然後如果他遇到一些頭肯
[00:30:41] Yang Songlin: 讓他覺得
[00:30:43] Yang Songlin: 前面這些信息已經沒有用了
[00:30:45] 那這樣子的話
[00:30:46] Yang Songlin: 他可以在那位置上
[00:30:48] Yang Songlin: 用一個
[00:30:49] 比如說讓他的衰減率等於
[00:30:51] 那個DK.0
[00:30:52] Yang Songlin: 這樣的的話
[00:30:53] Yang Songlin: 前面的那個State
[00:30:54] Yang Songlin: 就是被完全地把它忘掉了
[00:30:57] Yang Songlin: 因為他成了一個0上去
[00:30:58] Yang Songlin: 所以他前面的State
[00:30:59] Yang Songlin: 就完全沒有了
[00:31:01] 對
[00:31:01] 像這種輸入相關的這種DK
[00:31:04] Yang Songlin: 他就是比較靈活
[00:31:06] Yang Songlin: 能夠通過這個數據
[00:31:08] Yang Songlin: 來動態的血
[00:31:09] Yang Songlin: 什麼時候該去遺忘
[00:31:11] Yang Songlin: 然後什麼時候該去記
[00:31:13] Yang Songlin: 這前面這個State
[00:31:16] 然後這是
[00:31:17] Yang Songlin: 第一個比較大的改進
[00:31:20] Yang Songlin: 就是把這個衰減
[00:31:21] Yang Songlin: 從輸入無關變成輸入相關
[00:31:24] Yang Songlin: 然後第二個改進的話
[00:31:26] Yang Songlin: 就是
[00:31:28] Yang Songlin: 德塔奈這一種路線
[00:31:29] Yang Songlin: 就是把他的更新的那個公式
[00:31:32] Yang Songlin: 從最開始那個簡單的那個
[00:31:36] Yang Songlin: 相機量探訊
[00:31:37] Yang Songlin: 他用的其實應該叫做一個叫做
[00:31:39] Yang Songlin: Haven rule
[00:31:40] Yang Songlin: 對
[00:31:41] 這個路的話
[00:31:42] Yang Songlin: 他就是簡單的把Key和Value
[00:31:44] Yang Songlin: 他們的外籍
[00:31:46] 把他加到HavenState上面
[00:31:49] Yang Songlin: 對
[00:31:49] Yang Songlin: 他就是一個Haven的一個R rule
[00:31:52] 然後像德塔奈這一套模型
[00:31:55] Yang Songlin: 他用的是一個叫做
[00:31:56] Yang Songlin: DataR rule的一個東西
[00:31:58] Yang Songlin: DataR rule的東西的話
[00:31:59] Yang Songlin: 就是說每一步的時候
[00:32:02] Yang Songlin: 他先用這個Key去取出
[00:32:05] Yang Songlin: 那個Memory裡面
[00:32:08] Yang Songlin: 會返回一個值
[00:32:09] Yang Songlin: 這就是這個Key
[00:32:10] Yang Songlin: 他在這個Memory裡面
[00:32:12] Yang Songlin: 他本來對應的這個Value
[00:32:14] Yang Songlin: 我們管他叫做OtoValue
[00:32:16] 然後這個Key
[00:32:18] Yang Songlin: 他又會有一個輸入的一個Value
[00:32:20] Yang Songlin: 我們把它叫做InputValue
[00:32:23] Yang Songlin: 對
[00:32:24] 然後因為他是一個
[00:32:26] Yang Songlin: 有一個觀點記憶網絡的一個視角
[00:32:29] Yang Songlin: 然後每一個Key
[00:32:30] Yang Songlin: 我們想讓他只對應一個Value
[00:32:32] 然後模型也不知道
[00:32:34] Yang Songlin: 他應該是對應前面的Value
[00:32:36] Yang Songlin: 還是輸入的Value
[00:32:38] 這個後來我們有一個可以學習的
[00:32:40] Yang Songlin: 一個Tone叫做Bita
[00:32:42] Yang Songlin: BitaR我們可以看成
[00:32:44] Yang Songlin: 他是一個
[00:32:45] Yang Songlin: 值在0到1之間的一個系數
[00:32:49] Yang Songlin: 用來決定
[00:32:50] Yang Songlin: 我們要用多少的前面的OtoValue
[00:32:54] Yang Songlin: 然後要用多少這個輸入的Value
[00:32:57] Yang Songlin: 我們會做一個線性組合
[00:33:00] Yang Songlin: 通過這個系數
[00:33:01] Yang Songlin: 我們回來做一個線性組合
[00:33:03] Yang Songlin: 對
[00:33:03] Yang Songlin: 然後得到他最後的那個新的Value
[00:33:07] Yang Songlin: 然後把這個舊的Value和Key
[00:33:09] Yang Songlin: 他的外籍把他從Memory裡面剪去
[00:33:12] Yang Songlin: 然後把這個新的Value和Key
[00:33:15] Yang Songlin: 他的外籍把他加到這個觀點網絡裡面
[00:33:19] Yang Songlin: 對
[00:33:19] Yang Songlin: 這就是DataNet
[00:33:21] Yang Songlin: 他那個跟新公式的一個
[00:33:23] Yang Songlin: Hallel的一個Ido
[00:33:28] 然後相比於
[00:33:29] Yang Songlin: 你兩三成的話
[00:33:30] Yang Songlin: 他其實是有一個
[00:33:32] Yang Songlin: 剪法的一個操作在裡面的
[00:33:33] Yang Songlin: 他不但可以
[00:33:35] Yang Songlin: 就加法的話
[00:33:36] Yang Songlin: 可以把它想像成是
[00:33:38] 往這個記憶網絡裡面去把它
[00:33:40] Yang Songlin: 去寄東西
[00:33:42] Yang Songlin: 那麼剪法的話
[00:33:43] Yang Songlin: 就可以把它理解成
[00:33:44] Yang Songlin: 從這個記憶網絡裡面
[00:33:46] Yang Songlin: 把它刪除一些東西
[00:33:48] Yang Songlin: 對
[00:33:49] 像這個畫面就會比較
[00:33:51] Yang Songlin: 更加有針對性的來刪東西
[00:33:53] Yang Songlin: 像之前那個DK的話
[00:33:55] Yang Songlin: 可能就是很多圍圖一起在做DK
[00:33:57] Yang Songlin: 像現在的話
[00:33:58] Yang Songlin: 就是就是只取某一個分量
[00:34:01] 然後他有一些
[00:34:04] 非常有目標性的這種
[00:34:06] Yang Songlin: 刪東西的操作在裡面
[00:34:08] Yang Songlin: 嗯
[00:34:10] 對
[00:34:11] 所以這Data
[00:34:13] Yang Songlin: 如果也代表了
[00:34:14] Yang Songlin: 第二個改進的話
[00:34:15] Yang Songlin: 就應該是
[00:34:17] 尼尼爾探純這個領域
[00:34:19] Yang Songlin: 裡面最近的第二個改進了嗎
[00:34:22] 就包括像DataNet
[00:34:24] Yang Songlin: GateeDataNet
[00:34:26] 像RockleSiren
[00:34:27] Yang Songlin: 他們都用到這個DataRoo
[00:34:29] Yang Songlin: 對
[00:34:30] 為什麼尼尼爾探純從一開始
[00:34:31] Zhang Xiaojun: 效果不好
[00:34:32] Zhang Xiaojun: 到慢慢的一步改進
[00:34:33] Zhang Xiaojun: 大家就是相信他還是Promise
[00:34:36] Zhang Xiaojun: 我覺得每一次大家關心尼尼爾探純
[00:34:39] Yang Songlin: 那肯定是因為大家
[00:34:41] Yang Songlin: 碰到了一些ContextWorl
[00:34:43] Yang Songlin: 對
[00:34:44] 像大家最開始的時候
[00:34:45] Yang Songlin: 去研究尼尼爾探純
[00:34:48] Yang Songlin: 就是
[00:34:48] Yang Songlin: 比如說在2020年左右的時候
[00:34:50] Yang Songlin: 大家去研究尼尼爾探純
[00:34:52] 是因為那個時候
[00:34:54] Yang Songlin: 大家遇到第一個ContextWorl
[00:34:57] Yang Songlin: 就是遇到一個Context這種強
[00:35:00] Yang Songlin: 然後他就是撞到這個強
[00:35:04] Yang Songlin: 就是他如果想繼續提高Context
[00:35:06] Yang Songlin: 那就是能找一些
[00:35:08] 負責多小魚
[00:35:09] Yang Songlin: Softmas
[00:35:10] Yang Songlin: 小魚平方的一些
[00:35:12] Yang Songlin: 嗯
[00:35:12] Yang Songlin: 東西來了
[00:35:13] Yang Songlin: 對
[00:35:14] 因為當時像Burt在那個年代
[00:35:17] Yang Songlin: 他的那個訓練其實就是500以上
[00:35:19] Yang Songlin: 對
[00:35:20] 然後當時可能覺得2048
[00:35:23] Yang Songlin: 當時在當時的那個視角
[00:35:25] Yang Songlin: 可能8192就是一個算一個長文本了
[00:35:28] Yang Songlin: 因為那個地方就非常的慢嘛
[00:35:31] 然後後面就隨著Flash Irtension
[00:35:33] Yang Songlin: 這個技術的單身
[00:35:36] Yang Songlin: 然後就打破了這一毒牆
[00:35:38] Yang Songlin: 對
[00:35:38] Yang Songlin: 然後現在看了
[00:35:39] Yang Songlin: 就是8192
[00:35:40] Yang Songlin: 就是一個非常短的一個文本了嗎
[00:35:42] Yang Songlin: 就在這上面做訓練是沒有一點這個壓力的
[00:35:46] Yang Songlin: 但是在之前
[00:35:47] Yang Songlin: 就之前的話
[00:35:48] Yang Songlin: 他沒有Flash Irtension的時候
[00:35:50] 他是計算的話
[00:35:51] Yang Songlin: 他需要把這個
[00:35:53] 平方的這個Tension舉證
[00:35:56] Yang Songlin: 要把他
[00:35:57] Yang Songlin: 先把他
[00:35:59] 就是要把他使力化在那個
[00:36:02] Yang Songlin: Global Memory上面
[00:36:04] Yang Songlin: 然後要把他從Global Memory裡面
[00:36:06] Yang Songlin: 把它搬回那個
[00:36:08] 嗯
[00:36:09] Flash Memory裡面
[00:36:11] 這樣子的話
[00:36:11] 他那個
[00:36:12] Yang Songlin: Memory的那個毒血
[00:36:14] Yang Songlin: 他整體的那開箱非常的大的
[00:36:17] 然後同時
[00:36:17] 因為這個
[00:36:18] Yang Songlin: Tension舉證會被使力化在那個Global Memory裡面
[00:36:22] Yang Songlin: 他可能就是會帶來一個
[00:36:24] Yang Songlin: Out of Memory的一個問題
[00:36:26] Yang Songlin: 這就是最開始
[00:36:28] Yang Songlin: 大家研究
[00:36:29] Yang Songlin: 你量的Tension這個模特為止
[00:36:32] 然後隨著Flash Irtension的話
[00:36:34] Yang Songlin: 大家就發現這一毒牆
[00:36:36] Yang Songlin: 就其實已經破了嗎
[00:36:39] Yang Songlin: 就既然我們能用這種
[00:36:41] Yang Songlin: Exite方式來直接算這個SuffMind SuffMind SuffTension
[00:36:44] Yang Songlin: 那我們就沒必要找一些
[00:36:45] Yang Songlin: Ninliant的Tension去逼近他嗎
[00:36:47] Yang Songlin: 所以大家就
[00:36:49] Yang Songlin: Ninliant Tension的演技就開始
[00:36:51] Yang Songlin: 沒有那麼受關注了
[00:36:54] 然後直到最近吧
[00:36:56] Yang Songlin: 這邊要說
[00:36:58] Yang Songlin: 像這種長文本的Decoding
[00:37:01] Yang Songlin: 又重新成了一個需求量
[00:37:03] Yang Songlin: 非常大的一個東西
[00:37:05] 然後
[00:37:07] Yang Songlin: 就是這種
[00:37:07] Yang Songlin: Out of Memory mode
[00:37:08] Yang Songlin: 他要塗很多很多的偷肯
[00:37:10] Yang Songlin: 然後要都是這種Decoding
[00:37:12] Yang Songlin: 然後這個花消的話
[00:37:13] Yang Songlin: 就是就會讓人們又不由自主的
[00:37:16] Yang Songlin: 又重新來審視這一套的技術
[00:37:19] Yang Songlin: 然後這一套技術
[00:37:20] Yang Songlin: 他本身在學界就又有了這麼久的發生
[00:37:25] 尤其是在Flash Irtension之後
[00:37:27] Yang Songlin: 就學界其實也一時到就是說
[00:37:30] 如果像Ninliant Tension這一套模型
[00:37:33] 如果想讓大家被大家接受的話
[00:37:36] Yang Songlin: 那他硬件上面的效率是非常關鍵的
[00:37:39] 對
[00:37:39] 所以就是為什麼我最開始的時候
[00:37:41] Yang Songlin: 就是叫做Flash Ninliant Tension的一個Pro站
[00:37:44] Yang Songlin: 就是致力於就是把這些
[00:37:47] Yang Songlin: Ninliant Tension的這些變種
[00:37:49] Yang Songlin: 然後用Tryton
[00:37:51] Yang Songlin: 把它再
[00:37:52] 就寫了一個酷
[00:37:53] Yang Songlin: 然後寫了很多顆粒
[00:37:54] Yang Songlin: 讓它能夠在當代的硬件上面
[00:37:57] Yang Songlin: 主要是GPU上面能夠來快速運行
[00:38:00] Yang Songlin: 對
[00:38:01] 所以它核心是效率更高
[00:38:03] Zhang Xiaojun: 價格更低
[00:38:04] 就是每當Soft-Mise
[00:38:06] Yang Songlin: 它的效率變成一個平靜的時候
[00:38:10] Yang Songlin: 大家就會回來看Ninliant Tension
[00:38:12] Yang Songlin: 大家就是這樣子的一個歷史
[00:38:13] Yang Songlin: Ninliant Tension現在是公式了嗎
[00:38:17] Yang Songlin: 我覺得Ninliant Tension
[00:38:19] 我現在現在的公式的設計
[00:38:20] Yang Songlin: 就是說Tryton Ninliant Tension是不 work的
[00:38:23] Yang Songlin: 對
[00:38:23] Yang Songlin: 就是它在這種長文本下面
[00:38:26] Yang Songlin: 它是有一些比較翻到漫頭的一些缺陷的
[00:38:29] Yang Songlin: 對
[00:38:30] Yang Songlin: 然後
[00:38:31] Yang Songlin: 現在大家一般都不會去嘗試這種
[00:38:35] Yang Songlin: 純陷信的這種模型
[00:38:39] 然後像一些比較折磨的一些法案
[00:38:43] Yang Songlin: 像這種混合注意的話
[00:38:45] Yang Songlin: 它就是還是有很多很多的陷信注意力層
[00:38:49] 但是它還是有一定數目的這種
[00:38:54] 全局注意力層
[00:38:56] 這樣子的話
[00:38:57] Yang Songlin: 它這個模型它的下線是有保證的
[00:39:00] Yang Songlin: 對它處理長文本它也是有一定的保證的
[00:39:04] 因為它中規它還是有很多這種全局注意力層
[00:39:08] 像全線性的這個網絡的話
[00:39:10] Yang Songlin: 它可能從理論上面它就沒有辦法
[00:39:13] Yang Songlin: 做那種長文本Task
[00:39:16] Yang Songlin: 因為它的那個阿恩的那個狀態數目是
[00:39:20] Yang Songlin: 很定的
[00:39:21] Yang Songlin: 然後隨著那個Contest
[00:39:23] Yang Songlin: 它那個長度增加的話
[00:39:25] Yang Songlin: 那它早晚會存不下
[00:39:28] Yang Songlin: 那早晚會損失很多那種金度在裡面嗎
[00:39:33] Yang Songlin: 然後在實際上混合注意的話
[00:39:35] Yang Songlin: 它有很多那個全局注意力在裡面
[00:39:39] Yang Songlin: 所以還是可以通過這些全局注意力
[00:39:42] Yang Songlin: 來完成這些長文本的Task
[00:39:45] 對
[00:39:45] 然後像
[00:39:47] Yang Songlin: 表哥像Kimi Nino這個paper
[00:39:50] Yang Songlin: 然後像之前千萬三那個
[00:39:53] Yang Songlin: Kun 3 Next
[00:39:56] Yang Songlin: 它就是
[00:39:58] Yang Songlin: 它們那個長文本
[00:40:00] Yang Songlin: 比如說像如了
[00:40:02] Yang Songlin: 比如像其他Task那個表現
[00:40:04] Yang Songlin: 沒有掉點
[00:40:05] Yang Songlin: 對
[00:40:06] Yang Songlin: 所以它在長文本上面還是有一些
[00:40:08] Yang Songlin: 有一定的能力的
[00:40:10] Yang Songlin: 對
[00:40:11] 然後混合注意力就會收到很多
[00:40:13] Yang Songlin: 很多地方的關注吧
[00:40:16] Yang Songlin: 但是我也不知道它算不算共識
[00:40:18] Yang Songlin: 對
[00:40:18] Yang Songlin: 因為不同的地方還是在長世不同的方案嗎
[00:40:22] Yang Songlin: 比如說現在
[00:40:23] Yang Songlin: 比如說像Diff C 它就在長世這種
[00:40:25] Yang Songlin: Spassal 貪生的這種方案
[00:40:27] Yang Songlin: 嗯
[00:40:28] 在Kimi的這個論文裡面
[00:40:30] Zhang Xiaojun: 你們提出的是美三層的KDA
[00:40:33] Zhang Xiaojun: 也就是Kimi Delta 貪生
[00:40:35] Zhang Xiaojun: 增量注意力機制
[00:40:36] Zhang Xiaojun: 插入一層全注意力機制
[00:40:38] Zhang Xiaojun: 佛羅貪生
[00:40:39] Zhang Xiaojun: 這個比例是怎麼確定的
[00:40:41] Zhang Xiaojun: 這個比例重要嗎
[00:40:43] 我覺得三比一現在有快變成一個公司了吧
[00:40:46] 對
[00:40:47] Yang Songlin: 像Mini Max 它之前是一個
[00:40:49] Yang Songlin: 7B1的一個比例
[00:40:51] Yang Songlin: 對
[00:40:52] Yang Songlin: 然後7B1的話
[00:40:53] Yang Songlin: 可能Soft Maserate 貪生那個層數不夠
[00:40:56] Yang Songlin: 然後長文本的那個保證可能沒有那麼好
[00:41:00] 然後我記得之前
[00:41:02] Yang Songlin: 就是自己也發了一個
[00:41:05] Paper
[00:41:06] Yang Songlin: 就是來研究這個Hyper架構
[00:41:08] Yang Songlin: 它需要百分之多
[00:41:10] Yang Songlin: 吵的Soft Maserate 貪生
[00:41:13] 然後他們的簡論也是說
[00:41:15] Yang Songlin: 就他們做了很多Pretrent
[00:41:17] Yang Songlin: Fans Grash的一些實驗
[00:41:19] Yang Songlin: 然後他們就是通過
[00:41:21] Yang Songlin: 改那個不同的這個
[00:41:23] Yang Songlin: 力量貪生的這個模糾
[00:41:27] Yang Songlin: 然後它也改那個混合的比例
[00:41:30] 然後他們的簡論大概就是說
[00:41:32] Yang Songlin: 3B1的這個比例是最好的
[00:41:35] Yang Songlin: 然後GIGI.DON的這個模塊
[00:41:37] Yang Songlin: 就是比其他的那些
[00:41:39] Yang Songlin: 另外的那些看著的要好
[00:41:42] Yang Songlin: 對
[00:41:43] Yang Songlin: 所以3B1
[00:41:44] Yang Songlin: 然後後面千萬3
[00:41:46] Yang Songlin: Next的話
[00:41:47] Yang Songlin: 它也是用到3B1
[00:41:48] Yang Songlin: 然後混GIGI.DON的這個訪案
[00:41:51] Yang Songlin: 然後這個訪案應該是
[00:41:53] Yang Songlin: 不同的廠商
[00:41:54] Yang Songlin: 他們探索出來
[00:41:55] Yang Songlin: 都是覺得這個比例是更好的
[00:41:57] Yang Songlin: 對
[00:41:58] Yang Songlin: 然後這個可能是
[00:42:00] Yang Songlin: 最開始
[00:42:01] Yang Songlin: MiniMax沒有驗證重訪
[00:42:03] Yang Songlin: 就是現在也說
[00:42:03] Yang Songlin: 他們可能最開始的評測
[00:42:06] Yang Songlin: 還是有一些不足
[00:42:08] Yang Songlin: 所以他們用到一個
[00:42:10] Yang Songlin: 更加Egressive的一個訪案
[00:42:11] Yang Songlin: 就是7B1
[00:42:14] 然後現在的話
[00:42:15] Yang Songlin: 基本上就是都回到3B1
[00:42:17] Yang Songlin: 這個上面來了
[00:42:18] Yang Songlin: 然後我覺得3B1應該就是一個
[00:42:20] Yang Songlin: 在這個不共識的
[00:42:22] Yang Songlin: 這個Hybrid Nini裡面的一個共識
[00:42:24] Yang Songlin: 就是大家用3B1的一個比例
[00:42:26] Yang Songlin: 來混這個模型
[00:42:29] Yang Songlin: 是不是你們在算法設計的時候
[00:42:31] Zhang Xiaojun: 始終要平衡表達難力和計算效率
[00:42:34] Zhang Xiaojun: 這兩者是它的核心
[00:42:36] Zhang Xiaojun: 比如說北極新指標嗎
[00:42:38] 確實吧
[00:42:38] 我覺得還是有一些Trade of等
[00:42:40] Yang Songlin: 對
[00:42:42] Yang Songlin: 像全局主力的話
[00:42:44] Yang Songlin: 它如果太少的話
[00:42:45] Yang Songlin: 我感覺就表示像這種Resonant Tatsca
[00:42:49] Yang Songlin: 然後像長文本Tatsca
[00:42:51] Yang Songlin: 它肯定會說的影響表達
[00:42:55] 它可能一些說的Contest的一些Tatsca
[00:42:58] Yang Songlin: 沒有什麼影響
[00:42:59] Yang Songlin: 比如說MMU
[00:43:01] 但是那些長文本和推理的Tatsca
[00:43:04] Yang Songlin: 它應該是能看到的
[00:43:06] Yang Songlin: 那些人會比較大的
[00:43:09] 但是從另外一方面來說
[00:43:12] Yang Songlin: 也不是說Tanshen成越多越好嗎
[00:43:16] Yang Songlin: 因為像大家如果新晚之後
[00:43:18] Yang Songlin: 會發現覺得它多說Tanshen成
[00:43:20] Yang Songlin: 它可能就是沒有用的
[00:43:23] 然後它有一些關鍵的層的Tanshen
[00:43:25] Yang Songlin: 它是有用的
[00:43:27] Yang Songlin: 它不是每一層的
[00:43:28] Yang Songlin: Tanshen都有用的
[00:43:29] 然後這個網絡它本身自己
[00:43:31] Yang Songlin: 它就是有一個榮譽都在裡面的
[00:43:33] Yang Songlin: 這次它就給我們帶來一些機會
[00:43:36] Yang Songlin: 這比方說我們可以把一些層
[00:43:38] Yang Songlin: 把它換成一些現心層
[00:43:41] 所以混合的價格就不一定
[00:43:44] Yang Songlin: 我覺得它不一定代表
[00:43:45] Yang Songlin: 就是它比Global要差
[00:43:49] Yang Songlin: 然後它有很用可能就是說
[00:43:52] Yang Songlin: 它可能是一個全面
[00:43:54] Yang Songlin: 更好的一個替代方案
[00:43:56] Yang Songlin: 然後像Mini Max它
[00:43:58] Yang Songlin: 之前他們也發了
[00:44:00] Yang Songlin: 他說它成了一點
[00:44:01] Yang Songlin: 我覺得非常的好
[00:44:02] Yang Songlin: 就是說他們發現Hybrid Nino Tanshen
[00:44:06] Yang Songlin: 或者Hybrid這種華創墜率
[00:44:08] Yang Songlin: 在那個長文本的Motihop
[00:44:11] Yang Songlin: 多跳推理上面會有缺陷
[00:44:15] Yang Songlin: 像這個的話
[00:44:16] Yang Songlin: 就是我覺得這個
[00:44:18] Yang Songlin: 應該是現在Hybrid
[00:44:20] Yang Songlin: 它唯一的一個問題
[00:44:22] Yang Songlin: 因為它就是就我所知的話
[00:44:26] Yang Songlin: 我覺得我知道它在其他
[00:44:28] Yang Songlin: 它上面基本上是不會比全部都是
[00:44:32] Yang Songlin: Sofi Max Tanshen要差的
[00:44:34] Yang Songlin: 它只會在這個
[00:44:37] Yang Songlin: 這個也不要好理解
[00:44:39] Yang Songlin: 就像這種多跳推理的話
[00:44:41] Yang Songlin: 它就是比較吃這種
[00:44:42] Yang Songlin: 頭肯和頭肯之間的關係
[00:44:45] Yang Songlin: 所以它可能就比較吃
[00:44:47] Yang Songlin: 它Sofi Max Tanshen它的這個層數
[00:44:49] Yang Songlin: 對
[00:44:51] Yang Songlin: 這個就是
[00:44:53] Yang Songlin: 我覺得就是非常吃這個
[00:44:56] Yang Songlin: 全絕注意的層數的任務不是很多
[00:45:00] Yang Songlin: 可能就只有這種多跳推理
[00:45:03] Yang Songlin: 然後這種長文本做Rizzi你
[00:45:05] Yang Songlin: 這種會稍微吃一點
[00:45:08] Yang Songlin: 然後其他很多他自己
[00:45:10] Yang Songlin: 不吃的話
[00:45:11] Yang Songlin: 那他是完全不會受影響的
[00:45:14] 然後像這種多跳推理這個Tats的話
[00:45:17] Yang Songlin: 我覺得就是
[00:45:20] 就是如果我們去開發一些
[00:45:23] Yang Songlin: 音劍高效
[00:45:24] Yang Songlin: 但是它表達你更好的一些R&D的話
[00:45:28] Yang Songlin: 這個Gap它是有可能被
[00:45:31] Yang Songlin: 直接被縮小
[00:45:33] Yang Songlin: 甚至會晚超這個Gap的
[00:45:38] Yang Songlin: 就是比方說
[00:45:40] Yang Songlin: 像Kimi他最近這個
[00:45:43] Yang Songlin: 尼尼爾就張園之前完就發現
[00:45:46] Yang Songlin: 就是把這個
[00:45:48] Yang Songlin: 粒度浮的這個DK
[00:45:49] Yang Songlin: 換成粒度系的DK之後
[00:45:51] Yang Songlin: 他在這些Motihol Rizzi你
[00:45:54] Yang Songlin: Coding和Math這些Tats上面
[00:45:57] Yang Songlin: 他那個體系身還是比較可觀的
[00:46:00] Yang Songlin: 對
[00:46:01] Yang Songlin: 然後就說這些TatsK
[00:46:04] Yang Songlin: 就是Hyper可以做得更好
[00:46:06] Yang Songlin: 然後現在我覺得
[00:46:08] Yang Songlin: 混合現行最厲害只是
[00:46:10] Yang Songlin: 一個開始
[00:46:11] Yang Songlin: 對 然後我覺得整體的
[00:46:13] Yang Songlin: 還是很有可能做出
[00:46:16] Yang Songlin: 就是更好的這種
[00:46:18] Yang Songlin: 混合最厲害機制的
[00:46:19] Yang Songlin: 就是可以去掉一下
[00:46:21] Yang Songlin: 那個現行最厲害的那個模塊
[00:46:24] Yang Songlin: 你這過程中有給Kimi什麼算法見譯
[00:46:29] 對 我就是
[00:46:31] Yang Songlin: 就是張園想完那個
[00:46:33] Yang Songlin: 翻觀的DK嘛
[00:46:34] Yang Songlin: 然後我就
[00:46:35] Yang Songlin: 幫他想一個那個
[00:46:38] Yang Songlin: 就是創作那個
[00:46:40] Yang Songlin: 變形的那個算法
[00:46:41] Yang Songlin: 對 感覺這個應該可能就是
[00:46:43] Yang Songlin: 我對這個工作的唯一的
[00:46:45] 貢獻的方法
[00:46:46] Yang Songlin: 對 因為他這個
[00:46:48] Yang Songlin: 基本上都是張園在Kimi
[00:46:51] Yang Songlin: 做了很多很多oblacent study
[00:46:54] Yang Songlin: 基本上都他做的
[00:46:55] Yang Songlin: 對 所以Credit基本上都在他了
[00:46:58] Yang Songlin: 你不在我這裡
[00:46:59] Yang Songlin: 然後
[00:47:00] Yang Songlin: 然後像這個算法的話
[00:47:02] 我覺得其實也是
[00:47:05] Yang Songlin: 之前就是有一篇文章
[00:47:08] Yang Songlin: 叫做Combat
[00:47:09] Yang Songlin: 然後他就是設計了
[00:47:11] Yang Songlin: 一個新的算法
[00:47:12] Yang Songlin: 能夠把那個
[00:47:14] Yang Songlin: GateDK他那個
[00:47:15] Yang Songlin: 球膩的那個算法
[00:47:16] Yang Songlin: 把它減少一次
[00:47:18] Yang Songlin: 對 然後我看完那個算法
[00:47:21] Yang Songlin: 之後我就發現
[00:47:22] Yang Songlin: 那我就可以把那個
[00:47:25] Yang Songlin: 基定叫GateDK他那個球膩
[00:47:28] Yang Songlin: 把它減少一次
[00:47:29] Yang Songlin: 然後我又緊接著
[00:47:32] Yang Songlin: 我又推了一個
[00:47:33] Yang Songlin: 能夠
[00:47:34] 試用於KDK的這個算法
[00:47:36] Yang Songlin: 然後我就把這個算法
[00:47:37] Yang Songlin: 告訴張宇了
[00:47:38] Yang Songlin: 然後張宇的
[00:47:39] Yang Songlin: 他就去寫可能
[00:47:40] Yang Songlin: 去實現這個算法
[00:47:41] Yang Songlin: 然後就發現這個算法
[00:47:43] Yang Songlin: 還是
[00:47:44] Yang Songlin: 他的這個
[00:47:45] SkeletonB的題來說
[00:47:46] Yang Songlin: 還是比之前的那個
[00:47:48] Yang Songlin: 算法要好一點的
[00:47:50] Yang Songlin: 對
[00:47:51] Yang Songlin: 問一個很讚的問題
[00:47:53] Zhang Xiaojun: 是一個研究員想問你的
[00:47:54] Zhang Xiaojun: Antention到底應該怎麼設計
[00:47:56] Zhang Xiaojun: 這個問題的話
[00:47:58] 我覺得現在可能
[00:48:01] Yang Songlin: 就只有兩條
[00:48:03] Yang Songlin: 不要主流的路線吧
[00:48:06] Yang Songlin: 一種就是
[00:48:08] Yang Songlin: Hybrid線線
[00:48:09] Yang Songlin: 然後一種就是Spares
[00:48:10] Yang Songlin: 對
[00:48:11] Yang Songlin: 然後我覺得這兩種
[00:48:13] Yang Songlin: 他其實
[00:48:14] Yang Songlin: 都是非常的
[00:48:15] Yang Songlin: Promising的
[00:48:16] Yang Songlin: 對
[00:48:18] 然後
[00:48:19] 另外可能有一些
[00:48:21] Yang Songlin: 比較非主流的一些
[00:48:22] 彈省設計嗎
[00:48:23] Yang Songlin: 就比方說
[00:48:24] Yang Songlin: 我看上次
[00:48:26] Yang Songlin: Mata還放了一個論文
[00:48:27] 就是搞一個
[00:48:28] Yang Songlin: 三次方的彈省
[00:48:30] Yang Songlin: 就是寫平方
[00:48:32] Yang Songlin: 複雜度
[00:48:33] Yang Songlin: 他還不夠
[00:48:34] Yang Songlin: 他還要搞一個三次方的
[00:48:35] Yang Songlin: 嗯
[00:48:38] 然後像
[00:48:39] 有些地方
[00:48:40] Yang Songlin: 他有一些
[00:48:41] Yang Songlin: 比較有意思的一些
[00:48:42] Yang Songlin: 平方複雜度的
[00:48:43] Yang Songlin: 一些彈省的變種嗎
[00:48:45] Yang Songlin: 比方說
[00:48:46] 拜登是他之前
[00:48:47] Yang Songlin: 有一道
[00:48:48] Yang Songlin: DataFormor的
[00:48:49] Yang Songlin: 就像那就是
[00:48:50] Yang Songlin: 把DataRoo的思想
[00:48:52] Yang Songlin: 把他引入到
[00:48:53] Yang Songlin: Somice的彈省
[00:48:54] Yang Songlin: 能夠讓他表達
[00:48:55] Yang Songlin: 那更強
[00:48:56] Yang Songlin: 然後像這個
[00:48:57] Yang Songlin: 工作我覺得
[00:48:58] Yang Songlin: 也非常有意思
[00:48:59] Yang Songlin: 對
[00:49:00] 然後
[00:49:01] 嗯
[00:49:02] Yang Songlin: 改進註列的話
[00:49:03] Yang Songlin: 能他要么
[00:49:04] Yang Songlin: 就是把
[00:49:05] Yang Songlin: Somice的
[00:49:06] Yang Songlin: 他做得更好嗎
[00:49:07] Yang Songlin: 要不然的話
[00:49:08] Yang Songlin: 就是做一些
[00:49:09] Yang Songlin: 更加高效的
[00:49:10] Yang Songlin: 一些
[00:49:11] Yang Songlin: Wireland
[00:49:12] Yang Songlin: 比如說Spaasa彈省
[00:49:13] Yang Songlin: 或者是
[00:49:14] Yang Songlin: 混合現性的這種
[00:49:15] Yang Songlin: 而彈省
[00:49:16] 然後這兩種
[00:49:17] Yang Songlin: 我覺得他也是
[00:49:18] Yang Songlin: 可以結合的嘛
[00:49:19] Yang Songlin: 對
[00:49:20] Yang Songlin: 有點和各自的缺點嗎
[00:49:21] Yang Songlin: 像Spaasa彈省的
[00:49:22] 的話
[00:49:23] Yang Songlin: 能他
[00:49:24] Yang Songlin: Rooq
[00:49:25] Yang Songlin: 一定要更強一點嗎
[00:49:26] Yang Songlin: 要缺點就是說
[00:49:27] Yang Songlin: 他KV開始
[00:49:28] Yang Songlin: 他不能省
[00:49:29] Yang Songlin: 然後像現性的話
[00:49:31] Yang Songlin: 能他
[00:49:32] Yang Songlin: 可以省很多KV開始
[00:49:33] Yang Songlin: 嗯
[00:49:34] Yang Songlin: 所以我之前
[00:49:35] Yang Songlin: 起來了一個
[00:49:36] Yang Songlin: 指揮的回答
[00:49:37] Yang Songlin: 我就說
[00:49:38] Yang Songlin: 這兩種方案
[00:49:39] Yang Songlin: 為什麼我們不能
[00:49:40] Yang Songlin: 把它結合到一起呢
[00:49:41] Yang Songlin: 就比方說
[00:49:42] Yang Songlin: 我們可以
[00:49:43] Yang Songlin: 讓Spaasa彈省
[00:49:44] Yang Songlin: 去取代
[00:49:45] Yang Songlin: 這種混合
[00:49:46] Yang Songlin: 注意力
[00:49:47] Yang Songlin: 裡面的那個
[00:49:48] Yang Songlin: 全局的那個注意力層
[00:49:49] Yang Songlin: 這樣的話
[00:49:50] Yang Songlin: 我們就
[00:49:51] Yang Songlin: 不需要有一個
[00:49:52] Yang Songlin: 全局
[00:49:53] Yang Songlin: 注意力的那個
[00:49:54] Yang Songlin: 複雜都在了
[00:49:55] 那個KV開始
[00:49:56] Yang Songlin: 但剩下很多層的
[00:49:57] KV開始
[00:49:58] Yang Songlin: 就可以通過這個
[00:49:59] Yang Songlin: 現性注意力
[00:50:00] Yang Songlin: 把KV開始
[00:50:01] 的Size把它打下來
[00:50:02] Yang Songlin: 這樣子的話
[00:50:03] Yang Songlin: 呢
[00:50:04] Yang Songlin: 我覺得可能
[00:50:05] Yang Songlin: 就是我目前
[00:50:06] Yang Songlin: 心中
[00:50:07] Yang Songlin: 比較理想的一個
[00:50:09] Yang Songlin: 高校的一個
[00:50:10] 價格
[00:50:11] Yang Songlin: 就是
[00:50:12] Yang Songlin: 高校
[00:50:13] Yang Songlin: 不掉點
[00:50:14] Yang Songlin: 是這樣子的
[00:50:15] Yang Songlin: 所以
[00:50:16] Zhang Xiaojun: 裡面的陳聖和Spaasa
[00:50:17] Zhang Xiaojun: 的未來的關係
[00:50:18] Zhang Xiaojun: 可能是融合到
[00:50:19] Zhang Xiaojun: 一個統一的
[00:50:20] Zhang Xiaojun: 狂價裡面
[00:50:21] Zhang Xiaojun: 對吧
[00:50:22] 對
[00:50:23] Yang Songlin: 因為我覺得
[00:50:24] Yang Songlin: 現性的彈省
[00:50:25] 和Spaasa的彈省
[00:50:26] Yang Songlin: 它其實沒有什麼
[00:50:27] Yang Songlin: 競爭關係吧
[00:50:28] Yang Songlin: 我覺得現性的彈省的
[00:50:29] Yang Songlin: 這個競爭對手可能
[00:50:31] Yang Songlin: 更多的是Slighting window的彈省嘛
[00:50:33] Yang Songlin: 對
[00:50:34] 像比方說
[00:50:35] Yang Songlin: Size GPT3
[00:50:36] Yang Songlin: 他那個
[00:50:37] Yang Songlin: 洛文裡面
[00:50:38] Yang Songlin: 提到的那個
[00:50:39] Yang Songlin: 全局混
[00:50:40] Yang Songlin: Slighting window
[00:50:41] 那Slighting window的話
[00:50:42] Yang Songlin: 呢
[00:50:43] Yang Songlin: 他
[00:50:44] Yang Songlin: 如果
[00:50:45] Yang Songlin: 讓這個現性去取代
[00:50:46] Yang Songlin: Slighting window
[00:50:47] Yang Songlin: 能夠讓他
[00:50:48] Yang Songlin: 更好的換額
[00:50:49] Yang Songlin: 那
[00:50:50] 非常不可能
[00:50:51] Yang Songlin: 對吧
[00:50:52] Yang Songlin: 所以你覺得
[00:50:53] 我把裡面的
[00:50:54] Zhang Xiaojun: 陳聖和Spaasa
[00:50:55] Zhang Xiaojun: 能夠做更好的結合
[00:50:56] Zhang Xiaojun: 現在有人在探索這件事嗎
[00:50:58] Zhang Xiaojun: 公約見得
[00:50:59] Yang Songlin: 的話
[00:51:00] Yang Songlin: 我覺得我還
[00:51:01] Yang Songlin: 結果所知
[00:51:02] Yang Songlin: 我應該
[00:51:03] Yang Songlin: 沒有看到
[00:51:04] Yang Songlin: 有人在同時
[00:51:05] Yang Songlin: 去結合Spaasa
[00:51:07] Yang Songlin: 的彈省
[00:51:08] Yang Songlin: 和現性的彈省
[00:51:10] Yang Songlin: 但學界有一些
[00:51:12] Yang Songlin: 工作還是
[00:51:13] Yang Songlin: 有一些
[00:51:14] Yang Songlin: 這方面的探索的
[00:51:15] Yang Songlin: 對
[00:51:16] Yang Songlin: 有些
[00:51:17] Yang Songlin: 陳用Spaasa
[00:51:18] Yang Songlin: 有些陳用
[00:51:19] Yang Songlin: 你兩個探索
[00:51:20] Yang Songlin: 對
[00:51:21] 所以
[00:51:22] Depth也像
[00:51:23] Zhang Xiaojun: 選了Spaasa
[00:51:24] Zhang Xiaojun: 天神
[00:51:25] Zhang Xiaojun: Kimmy選了
[00:51:26] Zhang Xiaojun: Linia
[00:51:27] Zhang Xiaojun: 這其實
[00:51:28] Zhang Xiaojun: 可能也是
[00:51:29] Zhang Xiaojun: 階段性的
[00:51:30] Zhang Xiaojun: 對吧
[00:51:31] Zhang Xiaojun: 可能未來會
[00:51:32] Zhang Xiaojun: 就是大家
[00:51:33] Zhang Xiaojun: 一條新的路
[00:51:34] Zhang Xiaojun: 就是把
[00:51:35] Zhang Xiaojun: 現在
[00:51:36] Zhang Xiaojun: 也不是
[00:51:37] FaceGb的關係
[00:51:38] Yang Songlin: 對
[00:51:39] Yang Songlin: 換個註列的話
[00:51:40] Yang Songlin: 他
[00:51:41] Yang Songlin: 頂長度
[00:51:42] Yang Songlin: 上去之後
[00:51:43] Yang Songlin: 他的問題
[00:51:44] Yang Songlin: 就是說
[00:51:45] Yang Songlin: 他還是會被
[00:51:46] Yang Songlin: 這個拳擊
[00:51:47] Yang Songlin: 註列
[00:51:48] Yang Songlin: 他的這個
[00:51:49] 效率
[00:51:50] Yang Songlin: 把他
[00:51:51] Yang Songlin: 他的平靜就
[00:51:52] Yang Songlin: 主要在這個拳擊
[00:51:53] Yang Songlin: 注意了
[00:51:54] Yang Songlin: 效率上面了
[00:51:55] 這是
[00:51:56] Yang Songlin: 對
[00:51:57] Yang Songlin: 然後
[00:51:58] Yang Songlin: 像
[00:51:59] Yang Songlin: 全部都用
[00:52:00] Yang Songlin: 那種Spaasa
[00:52:01] Yang Songlin: 的攤繩的話
[00:52:02] Yang Songlin: 他平靜可能
[00:52:03] Yang Songlin: 是在KV開始的
[00:52:04] Yang Songlin: 觀念上面
[00:52:05] Yang Songlin: 對
[00:52:06] Yang Songlin: 不省KV開始
[00:52:07] Yang Songlin: 對
[00:52:08] 所以
[00:52:09] Yang Songlin: 長度上去
[00:52:10] Yang Songlin: 就可能要做
[00:52:11] Yang Songlin: 很多
[00:52:12] Yang Songlin: 各種各樣的KV開始
[00:52:13] Yang Songlin: 壓索
[00:52:14] Yang Songlin: 壓著的工作
[00:52:15] Yang Songlin: 對
[00:52:16] Yang Songlin: 然後
[00:52:17] Yang Songlin: 兩者
[00:52:18] Yang Songlin: 還是
[00:52:19] 有各自的問題
[00:52:20] Zhang Xiaojun: 比如說可能
[00:52:21] Zhang Xiaojun: 是不同的
[00:52:22] Zhang Xiaojun: 產業不同的
[00:52:23] Zhang Xiaojun: 天繩嗎
[00:52:24] 我覺得
[00:52:25] Yang Songlin: 最後一件
[00:52:26] Yang Songlin: 的話
[00:52:27] 就是
[00:52:28] Yang Songlin: 把
[00:52:29] Yang Songlin: 換合注意力
[00:52:30] Yang Songlin: 他
[00:52:31] Yang Songlin: 裡面的拳擊
[00:52:32] Yang Songlin: 注意力
[00:52:33] Yang Songlin: 把它換成
[00:52:34] Yang Songlin: Spaasa
[00:52:35] Yang Songlin: 彈繩
[00:52:36] Yang Songlin: 我覺得
[00:52:37] Yang Songlin: 你論上
[00:52:38] Yang Songlin: 只要Spaasa
[00:52:39] 彈繩
[00:52:40] Yang Songlin: 他能選得準的話
[00:52:41] Yang Songlin: 他是完全可以
[00:52:43] Yang Songlin: 取代
[00:52:44] Yang Songlin: 付了
[00:52:45] 他
[00:52:46] Yang Songlin: 這個程的
[00:52:47] Yang Songlin: 但
[00:52:48] Yang Songlin: 他
[00:52:49] Yang Songlin: 是一個問題
[00:52:50] Yang Songlin: 對
[00:52:51] Yang Songlin: 然後
[00:52:52] Yang Songlin: 這也是
[00:52:53] Yang Songlin: 為什麼
[00:52:54] Yang Songlin: 可能是
[00:52:55] Yang Songlin: 為什麼
[00:52:56] Yang Songlin: DFC
[00:52:57] Yang Songlin: 他
[00:52:58] Yang Songlin: 最近
[00:52:59] Yang Songlin: 放的
[00:53:00] Yang Songlin: DFC
[00:53:01] Yang Songlin: 他要用
[00:53:02] Yang Songlin: 遮留的方式
[00:53:03] 來
[00:53:04] Yang Songlin: 盡可能
[00:53:05] Yang Songlin: 那個
[00:53:06] Yang Songlin: 音
[00:53:07] Yang Songlin: Dexer
[00:53:08] Yang Songlin: 就是
[00:53:09] Zhang Xiaojun: 來
[00:53:10] Zhang Xiaojun: 選頭
[00:53:11] Zhang Xiaojun: 很
[00:53:12] Zhang Xiaojun: 一點
[00:53:13] 對
[00:53:14] Yang Songlin: 這也可能
[00:53:15] Yang Songlin: 是一個原因
[00:53:16] Yang Songlin: OK
[00:53:17] Yang Songlin: 選得準
[00:53:18] Yang Songlin: 他
[00:53:19] Yang Songlin: 可能
[00:53:20] Yang Songlin: 那個
[00:53:21] Yang Songlin: 踢肚不太準
[00:53:22] Yang Songlin: 他可能
[00:53:23] Yang Songlin: 學了
[00:53:24] Yang Songlin: 就
[00:53:25] Yang Songlin: 選不準
[00:53:26] Yang Songlin: 那個
[00:53:27] Yang Songlin: Block
[00:53:28] Yang Songlin: 他學會
[00:53:29] Yang Songlin: 選
[00:53:30] Yang Songlin: Block
[00:53:31] Yang Songlin: 還是
[00:53:32] 挺難的
[00:53:33] Yang Songlin: 還有
[00:53:34] Yang Songlin: 各種
[00:53:35] Yang Songlin: 吸收
[00:53:36] 踢肚的問題
[00:53:37] Yang Songlin: 像Spaasa
[00:53:38] Yang Songlin: 的話
[00:53:39] Yang Songlin: 他
[00:53:40] Yang Songlin: 經常
[00:53:41] Yang Songlin: 就會有這種問題
[00:53:43] Yang Songlin: 然後
[00:53:44] Yang Songlin: 像
[00:53:45] Yang Songlin: 真鍊的方式
[00:53:46] Yang Songlin: 他
[00:53:47] Yang Songlin: 來真鍊一個
[00:53:48] 他那個
[00:53:49] Yang Songlin: 偷看的選法
[00:53:50] 那這個已經
[00:53:51] Yang Songlin: 那就可以
[00:53:52] Yang Songlin: 就是選得
[00:53:53] Yang Songlin: 非常地好
[00:53:54] Yang Songlin: 這個從學上面
[00:53:55] Yang Songlin: 來說也是
[00:53:56] Yang Songlin: Mexenste
[00:53:57] Yang Songlin: 你覺得聽你這個工作
[00:53:58] 他相比
[00:53:59] Zhang Xiaojun: 年初的
[00:54:00] Zhang Xiaojun: MexM1的
[00:54:01] Zhang Xiaojun: 工作
[00:54:02] Zhang Xiaojun: 他的
[00:54:03] Zhang Xiaojun: 進步在哪裡
[00:54:04] Zhang Xiaojun: 他主要
[00:54:05] Zhang Xiaojun: 就是在於
[00:54:06] Yang Songlin: 注意
[00:54:07] Yang Songlin: 他那個
[00:54:08] Yang Songlin: 模塊
[00:54:09] Yang Songlin: 他
[00:54:10] 還是會
[00:54:11] Yang Songlin: 好很多的
[00:54:12] Yang Songlin: 對
[00:54:13] Yang Songlin: 就像我之前說
[00:54:14] Yang Songlin: 就是
[00:54:15] Yang Songlin: Lightning
[00:54:16] Yang Songlin: 給人的感覺
[00:54:17] 就像一個
[00:54:18] Yang Songlin: 兩年前的工作
[00:54:19] Yang Songlin: 對
[00:54:20] Yang Songlin: 就還挺有在
[00:54:21] Yang Songlin: Returnite
[00:54:22] Yang Songlin: 的那個
[00:54:23] Yang Songlin: 版本
[00:54:24] Yang Songlin: 然後
[00:54:25] Yang Songlin: 像
[00:54:26] Yang Songlin: 這兩年
[00:54:27] Yang Songlin: 的話
[00:54:28] Yang Songlin: 我記得
[00:54:29] Yang Songlin: 新興注意力
[00:54:30] Yang Songlin: 還是
[00:54:31] Yang Songlin: 有很多發展的
[00:54:32] Yang Songlin: 對
[00:54:33] Yang Songlin: 然後這些發展
[00:54:34] Yang Songlin: 我覺得
[00:54:35] Yang Songlin: 都是
[00:54:36] Roke的
[00:54:37] Yang Songlin: 就是
[00:54:38] Yang Songlin: 已經有
[00:54:39] Yang Songlin: 其實
[00:54:40] Yang Songlin: 就比方說
[00:54:41] Yang Songlin: 千萬
[00:54:42] Yang Songlin: 和Kimi
[00:54:43] 都發現
[00:54:44] Yang Songlin: 就是
[00:54:45] Yang Songlin: 對
[00:54:46] Yang Songlin: 所以
[00:54:47] Yang Songlin: 把這些
[00:54:48] Yang Songlin: 最新的進展
[00:54:49] Yang Songlin: 把它
[00:54:50] Yang Songlin: 融合進來
[00:54:51] Yang Songlin: 肯定
[00:54:52] Yang Songlin: 是更好的
[00:54:53] Yang Songlin: 然後
[00:54:54] Yang Songlin: 像Kimi
[00:54:55] Yang Songlin: 甚至在
[00:54:56] Yang Songlin: 之前的
[00:54:57] 工作的
[00:54:58] Yang Songlin: 技術
[00:54:59] Yang Songlin: 上面
[00:55:00] Yang Songlin: 新開發
[00:55:01] Yang Songlin: 一個
[00:55:02] KDA
[00:55:03] Yang Songlin: 然後
[00:55:04] 讓他的
[00:55:05] 模型的
[00:55:06] Yang Songlin: 能力
[00:55:07] Yang Songlin: 會更強
[00:55:08] 然後
[00:55:09] Yang Songlin: 另外
[00:55:10] Yang Songlin: 他
[00:55:11] Yang Songlin: 還有
[00:55:12] Yang Songlin: 其他
[00:55:13] Yang Songlin: 不同
[00:55:14] Yang Songlin: 應該用的是
[00:55:15] Yang Songlin: 翻櫃MOE
[00:55:16] Yang Songlin: 然後
[00:55:17] MO
[00:55:19] Yang Songlin: 我記得
[00:55:20] Yang Songlin: 他那個
[00:55:21] Yang Songlin: MOE
[00:55:22] Yang Songlin: 好像還比較
[00:55:23] Yang Songlin: 比較粗
[00:55:24] 他還沒有
[00:55:25] Yang Songlin: 用到這麼
[00:55:26] Yang Songlin: 翻櫃的
[00:55:27] Yang Songlin: 這個MOE
[00:55:28] 所以
[00:55:30] Yang Songlin: 就是
[00:55:31] Yang Songlin: 有很多種可能性
[00:55:33] 如何做一個
[00:55:34] 公平的
[00:55:35] Zhang Xiaojun: 比較
[00:55:36] Zhang Xiaojun: 一下
[00:55:37] Zhang Xiaojun: Linux
[00:55:38] Zhang Xiaojun: Slighting
[00:55:40] Yang Songlin: 和
[00:55:41] Yang Songlin: Linux
[00:55:42] Yang Songlin: 的話
[00:55:43] Yang Songlin: 我覺得
[00:55:44] Yang Songlin: 可以有兩種
[00:55:45] Yang Songlin: 你只能
[00:55:46] Yang Songlin: 花到
[00:55:47] 就比方說
[00:55:48] Yang Songlin: 控制
[00:55:49] Yang Songlin: 他的
[00:55:51] Yang Songlin: State
[00:55:52] Yang Songlin: Slighting
[00:55:54] Yang Songlin: 的話
[00:55:55] Yang Songlin: Kiri
[00:55:56] Yang Songlin: 開始的話
[00:55:57] Yang Songlin: 因為
[00:55:58] Yang Songlin: 他
[00:55:59] Yang Songlin: 是
[00:56:01] Yang Songlin: 上線
[00:56:02] Yang Songlin: 是
[00:56:03] Yang Songlin: Balanced
[00:56:04] 之後
[00:56:05] Yang Songlin: 我們就可以
[00:56:07] Yang Songlin: 把Kiri開始
[00:56:09] Yang Songlin: 上線
[00:56:10] Yang Songlin: Slighting
[00:56:12] Yang Songlin: 的
[00:56:13] Yang Songlin: State
[00:56:14] Yang Songlin: Size
[00:56:16] Yang Songlin: And
[00:56:17] Yang Songlin: 的話
[00:56:18] Yang Songlin: 他
[00:56:19] Yang Songlin: Slight
[00:56:20] Yang Songlin: Size
[00:56:21] Yang Songlin: Data
[00:56:22] Yang Songlin: Done
[00:56:23] Yang Songlin: 如果
[00:56:25] Yang Songlin: 這兩個
[00:56:26] Yang Songlin: 東西
[00:56:27] Yang Songlin: 大概在
[00:56:28] Yang Songlin: 一個Live
[00:56:29] Yang Songlin: 我覺得
[00:56:30] Yang Songlin: 就是
[00:56:31] Yang Songlin: 一個公平的
[00:56:32] Yang Songlin: 比較
[00:56:33] 因為
[00:56:34] Yang Songlin: 像Decoding
[00:56:35] Yang Songlin: 的時候
[00:56:36] Yang Songlin: Slighting
[00:56:37] Yang Songlin: 和
[00:56:38] Yang Songlin: Memory
[00:56:39] Yang Songlin: 所以
[00:56:40] Yang Songlin: 只要
[00:56:41] Yang Songlin: State
[00:56:42] Yang Songlin: Size
[00:56:43] Yang Songlin: 差不多
[00:56:44] Yang Songlin: Decoding
[00:56:45] Yang Songlin: 效率
[00:56:46] Yang Songlin: 不會
[00:56:47] Yang Songlin: 差
[00:56:48] 太多
[00:56:49] Yang Songlin: 因為
[00:56:50] Yang Songlin: Memory
[00:56:51] Yang Songlin: 幫了
[00:56:52] Yang Songlin: 他
[00:56:53] 只要
[00:56:54] Yang Songlin: 他們
[00:56:55] Yang Songlin: 這
[00:56:56] Yang Songlin: Decoding
[00:56:57] Yang Songlin: 基本上
[00:56:58] Yang Songlin: 差不多
[00:56:59] 因為
[00:57:00] Yang Songlin: Decoding
[00:57:01] Yang Songlin: 還是
[00:57:02] Yang Songlin: Memory
[00:57:03] 幫
[00:57:05] Zhang Xiaojun: Decoding
[00:57:06] Zhang Xiaojun: 說到
[00:57:07] Zhang Xiaojun: 算法
[00:57:08] Zhang Xiaojun: 或者
[00:57:09] Zhang Xiaojun: Svasar
[00:57:10] Zhang Xiaojun: 這種
[00:57:11] Zhang Xiaojun: 漸進式的
[00:57:12] Zhang Xiaojun: 創新
[00:57:13] Zhang Xiaojun: 你覺得
[00:57:14] Zhang Xiaojun: 優化
[00:57:15] Zhang Xiaojun: 最終的目標
[00:57:16] Zhang Xiaojun: 可能是什麼
[00:57:17] Zhang Xiaojun: 然後最終
[00:57:18] Zhang Xiaojun: 可能
[00:57:19] Zhang Xiaojun: 形成的
[00:57:20] Zhang Xiaojun: 一個
[00:57:21] Zhang Xiaojun: 算法的
[00:57:22] 公式
[00:57:23] Yang Songlin: 會是什麼樣的
[00:57:24] Yang Songlin: 我覺得
[00:57:25] Yang Songlin: 這些優化
[00:57:26] 基本上
[00:57:27] Yang Songlin: 就是
[00:57:28] Yang Songlin: 給你相同的
[00:57:30] Yang Songlin: flop
[00:57:31] Yang Songlin: 你怎麼
[00:57:32] Yang Songlin: 去更好的
[00:57:33] Yang Songlin: 利用這些
[00:57:35] flop
[00:57:36] Yang Songlin: 取得
[00:57:37] Yang Songlin: 就是
[00:57:38] Yang Songlin: 前兩年
[00:57:39] Yang Songlin: 可能
[00:57:40] Yang Songlin: 比如說
[00:57:41] Yang Songlin: 你要三年的時候
[00:57:42] Yang Songlin: 傳GPG
[00:57:43] Yang Songlin: 4.1M
[00:57:44] Yang Songlin: 但也有很多
[00:57:45] Yang Songlin: 地方
[00:57:46] Yang Songlin: 不太
[00:57:47] Yang Songlin: 感跟的
[00:57:48] Yang Songlin: 然後像
[00:57:49] Yang Songlin: 現在的話
[00:57:50] Yang Songlin: Memory
[00:57:51] Yang Songlin: 基本上
[00:57:52] Yang Songlin: 都是
[00:57:53] Yang Songlin: 已經變成
[00:57:54] Yang Songlin: 一個
[00:57:55] Yang Songlin: 顯學了
[00:57:56] Yang Songlin: 就是
[00:57:57] Yang Songlin: 每一家都會做
[00:57:58] 這種
[00:57:59] Yang Songlin: 犯規的Memory
[00:58:00] Yang Songlin: 對
[00:58:01] Yang Songlin: 現在Memory
[00:58:02] Yang Songlin: 的話
[00:58:03] Yang Songlin: 它其實
[00:58:04] Yang Songlin: 它可以
[00:58:05] Yang Songlin: 想像
[00:58:06] Yang Songlin: 這個
[00:58:07] Yang Songlin: 還發生了這個
[00:58:08] Yang Songlin: 參數量
[00:58:09] 然後同時
[00:58:10] Yang Songlin: 它又保證
[00:58:11] Yang Songlin: 它那個flop不變
[00:58:12] Yang Songlin: 這樣子的話
[00:58:13] Yang Songlin: 它付出相同的flop
[00:58:15] 它
[00:58:16] Yang Songlin: 在於訓練裡面
[00:58:17] Yang Songlin: 取得
[00:58:18] 訓練的
[00:58:20] Yang Songlin: 就會
[00:58:21] 越低
[00:58:22] Yang Songlin: 這就是一個點
[00:58:23] Yang Songlin: 然後
[00:58:24] Yang Songlin: 我覺得Memory
[00:58:25] Yang Songlin: 它可能
[00:58:26] Yang Songlin: 是近幾年
[00:58:27] Yang Songlin: 就是
[00:58:28] 突破
[00:58:29] Yang Songlin: 最大的一個
[00:58:30] Yang Songlin: 加個
[00:58:31] Yang Songlin: 方面
[00:58:32] Yang Songlin: 就是
[00:58:33] Yang Songlin: 突破
[00:58:34] Yang Songlin: 最大的一個
[00:58:35] Yang Songlin: 可能
[00:58:36] Yang Songlin: 就是在
[00:58:37] Yang Songlin: 一個
[00:58:38] 因為
[00:58:39] transform
[00:58:40] Yang Songlin: 就兩個
[00:58:41] Yang Songlin: 模塊
[00:58:42] Yang Songlin: iPhone
[00:58:43] Yang Songlin: 一個
[00:58:44] Yang Songlin: 現在
[00:58:45] Yang Songlin: iPhone基本
[00:58:46] Yang Songlin: 上已經
[00:58:47] Yang Songlin: 這種
[00:58:48] Yang Songlin: 翻-grn
[00:58:50] Yang Songlin: Memory
[00:58:51] Yang Songlin: 然後
[00:58:52] Yang Songlin: 而
[00:58:53] Yang Songlin: 單身
[00:58:54] Yang Songlin: 我覺得
[00:58:55] Yang Songlin: 大家
[00:58:56] Yang Songlin: 也是可以
[00:58:57] Yang Songlin: 來
[00:58:58] Yang Songlin: 掉一下
[00:58:59] Yang Songlin: 就是
[00:59:00] Yang Songlin: Y-N-O
[00:59:01] Yang Songlin: 這樣的話
[00:59:02] 它
[00:59:03] 表現
[00:59:04] Yang Songlin: 就是
[00:59:05] Yang Songlin: 減少flop
[00:59:06] 然後
[00:59:07] Yang Songlin: 能夠讓它
[00:59:08] Yang Songlin: 像iFi分的話
[00:59:09] Yang Songlin: 能夠減少flop
[00:59:10] Yang Songlin: 它就可以
[00:59:11] Yang Songlin: 去用
[00:59:12] Yang Songlin: 更大的
[00:59:13] Yang Songlin: 殘數量
[00:59:14] Yang Songlin: 更大規模的一個模型
[00:59:15] Yang Songlin: 就
[00:59:16] Yang Songlin: 比方說
[00:59:17] 你總
[00:59:18] Yang Songlin: 殘數量就可以對高了嗎
[00:59:19] Yang Songlin: 因為你這個iFi分的
[00:59:20] Yang Songlin: 算力減少了嗎
[00:59:21] Yang Songlin: 大家都知道
[00:59:22] 就是在大規模
[00:59:23] Yang Songlin: 訓練下面
[00:59:24] Yang Songlin: iFi分的
[00:59:25] 那個
[00:59:26] Yang Songlin: 計算是主導的嗎
[00:59:27] Yang Songlin: 然後
[00:59:28] Yang Songlin: 把它換成這種
[00:59:29] Yang Songlin: 翻-grnM1的話
[00:59:30] Yang Songlin: 能
[00:59:31] Yang Songlin: 其實是
[00:59:32] Yang Songlin: 能降低
[00:59:33] Yang Songlin: 對
[00:59:34] Yang Songlin: 然後
[00:59:35] Etansion它
[00:59:36] Yang Songlin: Skilled的
[00:59:37] Yang Songlin: 主要不是
[00:59:38] Yang Songlin: 殘數量
[00:59:39] Yang Songlin: 它Skilled的
[00:59:40] Yang Songlin: 就是那個
[00:59:41] Yang Songlin: Contest的
[00:59:42] Yang Songlin: Windowsize
[00:59:43] 然後
[00:59:44] 如果這個
[00:59:45] Yang Songlin: Tansion
[00:59:46] Yang Songlin: 它的flops
[00:59:47] Yang Songlin: 就在
[00:59:48] Yang Songlin: 場紋們下面
[00:59:49] Yang Songlin: 能夠
[00:59:50] 能夠
[00:59:51] Yang Songlin: 把它打下來
[00:59:52] Yang Songlin: 換了
[00:59:53] Yang Songlin: 那我們
[00:59:54] Yang Songlin: 就是做那種
[00:59:55] 場紋本的這種
[00:59:56] 生成
[00:59:57] Yang Songlin: 然後
[00:59:58] Yang Songlin: 表示
[00:59:59] Yang Songlin: 你有很多Agent
[01:00:00] Yang Songlin: 讓它
[01:00:01] Yang Songlin: 很多
[01:00:02] Contest給它
[01:00:03] Yang Songlin: 做了
[01:00:04] Yang Songlin: 這樣子的話
[01:00:05] Yang Songlin: 它
[01:00:06] Yang Songlin: 也會
[01:00:07] Yang Songlin: Bitiful
[01:00:08] 這個
[01:00:09] Yang Songlin: 更大的這個
[01:00:10] Yang Songlin: ContestWindows的
[01:00:11] 對
[01:00:12] Zhang Xiaojun: 如果
[01:00:13] Zhang Xiaojun: 把模型的
[01:00:14] Zhang Xiaojun: 架構
[01:00:15] Zhang Xiaojun: 比如說
[01:00:16] Zhang Xiaojun: 大腦的結構
[01:00:17] Zhang Xiaojun: 你覺得
[01:00:18] Zhang Xiaojun: Moe和Etansion
[01:00:19] Zhang Xiaojun: 它們分別
[01:00:20] Zhang Xiaojun: 代表的是
[01:00:21] Zhang Xiaojun: 大腦的
[01:00:22] Zhang Xiaojun: 什麼組織
[01:00:23] 能這樣去
[01:00:24] Yang Songlin: 形象化
[01:00:25] Yang Songlin: 去理解嗎
[01:00:26] Yang Songlin: 像
[01:00:27] 談生化
[01:00:28] Yang Songlin: 它應該
[01:00:29] Yang Songlin: 就像
[01:00:30] Yang Songlin: FIFN的話
[01:00:31] Yang Songlin: 就有點像那種
[01:00:33] Yang Songlin: 我忘記
[01:00:34] Yang Songlin: 人的大腦
[01:00:35] Yang Songlin: 存那種
[01:00:36] Yang Songlin: 消息的那種
[01:00:37] Yang Songlin: 做
[01:00:38] Yang Songlin: 對
[01:00:39] 可能就是
[01:00:40] Yang Songlin: 還嗎
[01:00:41] Yang Songlin: 就是
[01:00:42] Yang Songlin: 存儲這種
[01:00:43] Yang Songlin: 信息的
[01:00:44] Yang Songlin: 就是過去信息的
[01:00:45] Yang Songlin: 像FIFN
[01:00:46] Yang Songlin: 它
[01:00:47] Yang Songlin: 基本上
[01:00:48] Yang Songlin: 會被看成
[01:00:49] Yang Songlin: 是一個
[01:00:50] Yang Songlin: 箭子對的
[01:00:51] Yang Songlin: 一個
[01:00:52] Yang Songlin: 關聯網絡
[01:00:53] Yang Songlin: 它可以
[01:00:54] Yang Songlin: 機械
[01:00:55] Yang Songlin: 很多這種
[01:00:56] Yang Songlin: Lolage
[01:00:57] Yang Songlin: 就像
[01:00:58] Yang Songlin: 我的Lolage
[01:00:59] 會承下來
[01:01:00] Yang Songlin: 然後
[01:01:01] Yang Songlin: Tashr的話
[01:01:02] Yang Songlin: 就是
[01:01:03] Yang Songlin: 比如說
[01:01:04] Yang Songlin: 你在一個
[01:01:05] Yang Songlin: 新的場景
[01:01:06] Yang Songlin: 然後你遇到新的這種
[01:01:08] Yang Songlin: Count X
[01:01:09] Yang Songlin: 然後你會
[01:01:10] Yang Songlin: 讀到新的Count X
[01:01:11] Yang Songlin: FIFN
[01:01:12] Yang Songlin: 就動態的
[01:01:13] Yang Songlin: 來
[01:01:14] Yang Songlin: 處理這些信息
[01:01:16] Yang Songlin: 那就有點像
[01:01:17] Yang Songlin: 我們人的
[01:01:18] Yang Songlin: 工作
[01:01:19] Yang Songlin: 機
[01:01:20] Yang Songlin: Walking Memory
[01:01:21] Yang Songlin: 它跟
[01:01:22] Zhang Xiaojun: 篇一
[01:01:23] 即使信息
[01:01:24] Zhang Xiaojun: 對
[01:01:25] 對
[01:01:26] 當現在
[01:01:27] Zhang Xiaojun: 數據
[01:01:28] Zhang Xiaojun: 平靜比較明顯
[01:01:29] Zhang Xiaojun: 是不是算法的
[01:01:30] Zhang Xiaojun: 創新片的更重要
[01:01:31] Zhang Xiaojun: 我覺得
[01:01:32] Zhang Xiaojun: 是的
[01:01:33] Zhang Xiaojun: 就是
[01:01:34] Zhang Xiaojun: 因為
[01:01:35] Yang Songlin: 有算的數據
[01:01:36] Zhang Xiaojun: 裡面去
[01:01:37] Zhang Xiaojun: 壓縮更多的症
[01:01:38] Zhang Xiaojun: 對
[01:01:40] Yang Songlin: 我覺得之前的話
[01:01:42] Yang Songlin: 就不要說你
[01:01:43] Yang Songlin: SKILL的話
[01:01:44] Yang Songlin: 你談這個
[01:01:45] Yang Songlin: Data Efficiency
[01:01:46] Yang Songlin: 就是
[01:01:47] Yang Songlin: 沒有什麼
[01:01:48] Yang Songlin: 特別大的
[01:01:49] Yang Songlin: 那個用途
[01:01:50] Yang Songlin: 因為
[01:01:51] Yang Songlin: 大家別的原因
[01:01:52] 加這個數據
[01:01:53] Yang Songlin: 就行了
[01:01:54] Yang Songlin: 就讓它
[01:01:55] Yang Songlin: 模型進去SKILL
[01:01:56] App
[01:01:57] Yang Songlin: 所以
[01:01:58] Yang Songlin: 大家都不需要
[01:01:59] Yang Songlin: 去動算法了
[01:02:00] Yang Songlin: 然後大家
[01:02:01] Yang Songlin: 就只需要買卡
[01:02:02] Yang Songlin: 這個型
[01:02:03] Yang Songlin: 然後
[01:02:04] 現在如果有這種
[01:02:05] Yang Songlin: 數據強
[01:02:06] Yang Songlin: 然後還有這種
[01:02:08] Yang Songlin: 算力強的話
[01:02:09] Yang Songlin: 那可能
[01:02:10] Yang Songlin: 就到最終
[01:02:12] 還是要回到這個
[01:02:13] Yang Songlin: 算法
[01:02:14] Yang Songlin: 這種本質的東西
[01:02:15] Yang Songlin: 上面來的
[01:02:16] Yang Songlin: 我覺得這些
[01:02:17] Yang Songlin: 東西都是缺一不可的
[01:02:18] Yang Songlin: Data
[01:02:19] Yang Songlin: 像這種
[01:02:20] Yang Songlin: 算法
[01:02:21] Yang Songlin: 像這種算力
[01:02:22] Yang Songlin: 就像
[01:02:23] Yang Songlin: 有點像
[01:02:24] Yang Songlin: 三屁馬車
[01:02:25] Yang Songlin: 去動整個
[01:02:27] Yang Songlin: 人工症的發展
[01:02:28] Yang Songlin: 對
[01:02:29] Yang Songlin: 然後我記得
[01:02:30] 之前像
[01:02:31] Yang Songlin: Apple Eye的CTO
[01:02:33] 他也說
[01:02:35] 就可能
[01:02:36] Yang Songlin: 在這個節點
[01:02:37] Yang Songlin: 上面
[01:02:38] Yang Songlin: 算法的這個研究
[01:02:39] Yang Songlin: 重要性可能會被重新抬高
[01:02:40] Yang Songlin: 對
[01:02:41] Yang Songlin: 如果你記得
[01:02:42] Yang Songlin: 那個採訪的話
[01:02:43] Yang Songlin: 他應該是這麼熟過的
[01:02:44] Yang Songlin: 對
[01:02:45] Yang Songlin: 你覺得
[01:02:46] 現在的
[01:02:47] Zhang Xiaojun: 加購
[01:02:48] Zhang Xiaojun: 川斯風的加購
[01:02:49] Zhang Xiaojun: 他的添花板是什麼樣
[01:02:50] Zhang Xiaojun: 他的添花板
[01:02:53] Yang Songlin: 我覺得
[01:02:55] Yang Songlin: 還是先把
[01:02:57] Yang Songlin: Ephesion洗的問題解決掉吧
[01:02:59] Yang Songlin: 對
[01:03:00] Yang Songlin: 因為現在還沒有解決掉
[01:03:01] Yang Songlin: Ephesion洗的問題
[01:03:02] Yang Songlin: 他的處理
[01:03:03] Yang Songlin: 一個很長的一個
[01:03:05] Yang Songlin: CanticeWindow
[01:03:07] Yang Songlin: 還是有一些
[01:03:09] Yang Songlin: 舉線性
[01:03:10] 所以大家會做很多
[01:03:11] Yang Songlin: 上下文工程
[01:03:12] Yang Songlin: 做一些
[01:03:13] Yang Songlin: IG
[01:03:14] Yang Songlin: 來
[01:03:15] Yang Songlin: 通過一些其他的方式
[01:03:17] Yang Songlin: 來
[01:03:18] Yang Songlin: 來做這些問題
[01:03:19] Yang Songlin: 但如果
[01:03:20] Yang Songlin: 你這個Cantice的問題
[01:03:21] Yang Songlin: 把它解決掉
[01:03:22] Yang Songlin: 那你IG這一套
[01:03:24] Yang Songlin: 技術都不需要了嗎
[01:03:25] Yang Songlin: 你直接把它放到
[01:03:26] Yang Songlin: Cantice裡面
[01:03:27] Yang Songlin: 做了
[01:03:28] Yang Songlin: inCanticeIG就行了
[01:03:29] Yang Songlin: 對
[01:03:30] 然後我覺得
[01:03:31] Yang Songlin: 添花板的話
[01:03:32] 就先看看
[01:03:33] Yang Songlin: 能不能
[01:03:34] Yang Songlin: 就是把
[01:03:35] Yang Songlin: 全局這個注意力
[01:03:37] Yang Songlin: 把它幹掉吧
[01:03:38] Yang Songlin: 對
[01:03:39] Yang Songlin: 這第一點就是
[01:03:40] Yang Songlin: 因為它確實
[01:03:41] Yang Songlin: 它是阻止
[01:03:43] Yang Songlin: CanticeWindow
[01:03:45] Yang Songlin: 繼續 scale
[01:03:46] Yang Songlin: 上去的一個主要的平靜
[01:03:47] Yang Songlin: 所以這個平靜
[01:03:48] Yang Songlin: 我覺得是早晚
[01:03:49] Yang Songlin: 都要把它
[01:03:50] Yang Songlin: 弄掉的
[01:03:52] Yang Songlin: 這個是
[01:03:53] Yang Songlin: 第一點
[01:03:54] 然後調眼花
[01:03:55] 能可能
[01:03:56] Yang Songlin: 就是
[01:03:57] Yang Songlin: 抗聽牛能力嗎
[01:03:58] 對
[01:03:59] Yang Songlin: 然後像
[01:04:00] 穿衫的架構
[01:04:01] Yang Songlin: 還是沒法做
[01:04:02] Yang Songlin: 抗聽牛能力的嗎
[01:04:03] Yang Songlin: 對
[01:04:04] 之後抗聽牛能力
[01:04:05] 讓AI自己學習
[01:04:07] Yang Songlin: 這種
[01:04:08] Yang Songlin: 甚至
[01:04:11] 甚至大家不都想
[01:04:13] Yang Songlin: Pretrining這個
[01:04:14] Yang Songlin: 地方變成
[01:04:15] Yang Songlin: 直接從AR開始
[01:04:16] Yang Songlin: 讓
[01:04:17] Yang Songlin: 讓這個模型直接
[01:04:18] Yang Songlin: 從您開始學完
[01:04:19] Yang Songlin: 讓它為這種Pretrining
[01:04:21] Yang Songlin: 像這種新的
[01:04:22] Yang Songlin: 犯事可能
[01:04:23] Yang Songlin: 就是之後的這種
[01:04:24] Yang Songlin: 探索嘛
[01:04:25] 對
[01:04:26] 一個研究員問你
[01:04:27] 如何把
[01:04:28] Zhang Xiaojun: Linux-Tenshin
[01:04:29] Zhang Xiaojun: 的Transformer scale-up
[01:04:30] Zhang Xiaojun: 繼續擴展
[01:04:32] Zhang Xiaojun: 我覺得 scale-up
[01:04:34] Yang Songlin: 我覺得 scale-up
[01:04:35] Yang Songlin: 應該是沒有
[01:04:36] Yang Songlin: 什麼特別大的問題
[01:04:38] Yang Songlin: 然後我覺得可能
[01:04:40] Yang Songlin: 還有一點的話
[01:04:41] Yang Songlin: 就是說
[01:04:42] Yang Songlin: 就像說
[01:04:44] Yang Songlin: 那些
[01:04:46] Yang Songlin: 配套的這種
[01:04:47] Infra設施
[01:04:49] Yang Songlin: 還是需要繼續打的
[01:04:51] Yang Songlin: 對
[01:04:52] Yang Songlin: 像Flystining
[01:04:53] Yang Songlin: Tenshin
[01:04:54] Yang Songlin: 只是提供
[01:04:55] Yang Songlin: 一些Tri-Tens
[01:04:56] Yang Songlin: 那些可能
[01:04:57] Yang Songlin: 基本上就是
[01:04:58] Yang Songlin: 可以凑合用
[01:04:59] Yang Songlin: 但是
[01:05:00] 它的那個
[01:05:01] Yang Songlin: 效率
[01:05:02] Yang Songlin: 肯定不是最有的
[01:05:03] Yang Songlin: 因為它是Tri-Tenshin
[01:05:04] Yang Songlin: 對
[01:05:05] Yang Songlin: 所以如果
[01:05:07] Yang Songlin: 有支向
[01:05:09] Yang Songlin: 投入這個
[01:05:10] Yang Songlin: 領域的
[01:05:11] Yang Songlin: 不要說一些公司
[01:05:12] Yang Songlin: 或者可以
[01:05:14] Yang Songlin: 花一些急努
[01:05:15] Yang Songlin: 去優化
[01:05:16] Yang Songlin: 對
[01:05:17] Yang Songlin: 這個是
[01:05:18] Yang Songlin: 對繼續 scale-up
[01:05:19] Yang Songlin: 上學要好處嗎
[01:05:21] Yang Songlin: 然後像
[01:05:22] Yang Songlin: Inference那邊的那種
[01:05:24] Yang Songlin: 我覺得
[01:05:25] 現在像Inference那邊的
[01:05:26] Yang Songlin: 支持
[01:05:27] Yang Songlin: 已經在逐漸變多了
[01:05:29] Yang Songlin: 這比方說
[01:05:30] Yang Songlin: 像半年前
[01:05:32] Yang Songlin: 我參加
[01:05:34] Yang Songlin: Mini-Mine-Style
[01:05:35] 它有一個那個
[01:05:36] Yang Songlin: 原作討論樣的東西嘛
[01:05:38] Yang Songlin: 然後當時
[01:05:39] Yang Songlin: 主持人
[01:05:40] Yang Songlin: 是
[01:05:41] Yang Songlin: 金錢老師
[01:05:42] Yang Songlin: 金錢老師
[01:05:43] Yang Songlin: 問我這個領域
[01:05:44] Yang Songlin: 它除了
[01:05:45] Yang Songlin: 當時說是
[01:05:46] Yang Songlin: 英法的那個配套
[01:05:48] Yang Songlin: 沒有跟帳
[01:05:49] Yang Songlin: 對
[01:05:50] 然後
[01:05:51] Yang Songlin: 當時金錢老師
[01:05:52] Yang Songlin: 還覺得挺意外的
[01:05:53] Yang Songlin: 因為我會
[01:05:54] Yang Songlin: 回答一些
[01:05:55] Yang Songlin: 別的東西
[01:05:56] Yang Songlin: 對
[01:05:57] Yang Songlin: 然後
[01:05:58] Yang Songlin: 其實是像
[01:05:59] Yang Songlin: 這樣子
[01:06:00] Yang Songlin: 我覺得
[01:06:01] Yang Songlin: 算法層面
[01:06:02] Yang Songlin: 可以
[01:06:03] 就是說像
[01:06:04] Yang Songlin: 金兩人的這個發展
[01:06:05] Yang Songlin: 就已經可以
[01:06:07] Yang Songlin: 去大規模的來試了嘛
[01:06:08] Yang Songlin: 比方說
[01:06:09] Yang Songlin: 前問Style
[01:06:10] Yang Songlin: Nex
[01:06:11] Yang Songlin: 和Kimi-Mine
[01:06:12] Yang Songlin: 這些
[01:06:13] Yang Songlin: 都是
[01:06:14] Deploy的這種
[01:06:15] Yang Songlin: 平靜的話
[01:06:16] Yang Songlin: 可能就更多就是在這種
[01:06:17] Yang Songlin: 配套設施
[01:06:19] 因為
[01:06:20] 因為這兩家
[01:06:21] Yang Songlin: 發這兩個
[01:06:22] Yang Songlin: 模型
[01:06:23] 那開源設計
[01:06:25] Yang Songlin: 就是支持力度也挺大的嘛
[01:06:27] Yang Songlin: 像之前
[01:06:28] Yang Songlin: 比方說Style
[01:06:29] Yang Songlin: 它都不支持這種
[01:06:30] Yang Songlin: Hybrid mode
[01:06:31] Yang Songlin: 做inference嘛
[01:06:32] Yang Songlin: 然後
[01:06:33] 現在就是
[01:06:34] Yang Songlin: 趁這個機會
[01:06:35] Yang Songlin: 就可以把
[01:06:36] Yang Songlin: 錢問Style Nex
[01:06:37] Yang Songlin: 然後向Mini-Mine
[01:06:38] Yang Songlin: Style-Mine
[01:06:39] Yang Songlin: 萬一
[01:06:40] Yang Songlin: 這些模型
[01:06:41] Yang Songlin: 就是加一些
[01:06:42] 這種
[01:06:43] Yang Songlin: 推理引擎的
[01:06:44] 這種
[01:06:45] Yang Songlin: Support
[01:06:46] Yang Songlin: 我覺得這是一個
[01:06:48] Yang Songlin: 真相的一個
[01:06:49] Yang Songlin: 有一個
[01:06:50] Yang Songlin: 就是真相的一個
[01:06:51] Yang Songlin: 你與真相發展的一個
[01:06:53] Yang Songlin: 過程嘛
[01:06:54] Yang Songlin: 就像這些
[01:06:55] Yang Songlin: 做寂寞的廠商
[01:06:56] Yang Songlin: 他們去
[01:06:57] Yang Songlin: 做一些
[01:06:58] Yang Songlin: ProMizing的結果
[01:06:59] Yang Songlin: 然後
[01:07:00] Yang Songlin: 開源
[01:07:01] Yang Songlin: 把這些
[01:07:02] Yang Songlin: 為了把它發出來
[01:07:03] Yang Songlin: 然後
[01:07:04] 那些
[01:07:05] Yang Songlin: 就是
[01:07:06] Yang Songlin: 做推理引擎的人
[01:07:07] Yang Songlin: 就會有很多
[01:07:08] Yang Songlin: 動力來
[01:07:09] Yang Songlin: 想辦法來
[01:07:10] Yang Songlin: 東西嘛
[01:07:11] Yang Songlin: 然後
[01:07:12] Yang Songlin: 當這些
[01:07:13] Yang Songlin: 音法的配套
[01:07:14] Yang Songlin: 更好的時候
[01:07:15] Yang Songlin: 然後
[01:07:16] 比如說
[01:07:17] Yang Songlin: 別的公司可能
[01:07:18] Yang Songlin: 就是
[01:07:19] Yang Songlin: 覺得
[01:07:20] Yang Songlin: 向您聊探視
[01:07:21] Yang Songlin: 它的音法的
[01:07:22] Yang Songlin: 生態太差了
[01:07:24] Yang Songlin: 就是
[01:07:25] Yang Songlin: 可能就算
[01:07:26] Yang Songlin: 做出來
[01:07:27] Yang Songlin: 這個生態不好
[01:07:28] Yang Songlin: 可能它
[01:07:29] Yang Songlin: 實際上
[01:07:30] Yang Songlin: Deploy
[01:07:31] Yang Songlin: 它的成本也很高嘛
[01:07:32] 對
[01:07:33] Yang Songlin: 但現在
[01:07:34] Yang Songlin: 只要這個生態
[01:07:35] Yang Songlin: 做起來了
[01:07:36] 然後
[01:07:37] 就會
[01:07:38] Yang Songlin: 有一個
[01:07:39] Yang Songlin: 真相型環的
[01:07:40] Yang Songlin: 一個作用嘛
[01:07:41] Yang Songlin: 你覺得現在
[01:07:42] 中國的
[01:07:43] Zhang Xiaojun: 算法創新
[01:07:44] Zhang Xiaojun: 將對於
[01:07:45] Zhang Xiaojun: 歸過來說
[01:07:46] Zhang Xiaojun: 是
[01:07:47] Zhang Xiaojun: 差不多
[01:07:48] Zhang Xiaojun: 還是
[01:07:49] 落後的
[01:07:50] Yang Songlin: 我覺得
[01:07:51] Yang Songlin: 國內
[01:07:52] Yang Songlin: 算法
[01:07:53] Yang Songlin: 創新
[01:07:54] Yang Songlin: 肯定
[01:07:55] Yang Songlin: 是
[01:07:56] Yang Songlin: 更強的
[01:07:57] Yang Songlin: 主要是
[01:07:58] Yang Songlin: 英特爾
[01:08:00] Yang Songlin: 加購的話
[01:08:01] Yang Songlin: 肯定是
[01:08:02] 國內更強的
[01:08:03] Yang Songlin: 我覺得
[01:08:04] Yang Songlin: 這也是
[01:08:05] Yang Songlin: 有一些
[01:08:06] Yang Songlin: 生態
[01:08:07] 地位
[01:08:08] Yang Songlin: 不同
[01:08:09] Yang Songlin: 就像
[01:08:10] Yang Songlin: 所以它們
[01:08:11] Yang Songlin: 更有動力
[01:08:12] Yang Songlin: 來嘗試
[01:08:13] Yang Songlin: 這些
[01:08:14] Yang Songlin: 更高效的一些
[01:08:15] Yang Songlin: 你量它
[01:08:16] Yang Songlin: 它也
[01:08:17] 生這樣的變種
[01:08:18] Yang Songlin: 然後
[01:08:19] Yang Songlin: 像
[01:08:20] Yang Songlin: 規固
[01:08:21] Yang Songlin: 有些公司基本上
[01:08:22] Yang Songlin: 就是
[01:08:23] Zhang Xiaojun: 卡太多了
[01:08:24] Zhang Xiaojun: 它們就
[01:08:25] Zhang Xiaojun: 難得高
[01:08:26] Yang Songlin: 反正
[01:08:27] Yang Songlin: 你走
[01:08:28] Yang Songlin: 你走
[01:08:29] Yang Songlin: 就有
[01:08:30] 一定要跑得快一點
[01:08:31] Zhang Xiaojun: 對
[01:08:32] Zhang Xiaojun: 它們
[01:08:33] Zhang Xiaojun: 有算力
[01:08:34] Zhang Xiaojun: 那
[01:08:35] Zhang Xiaojun: 也能綽合跑嗎
[01:08:36] 對
[01:08:37] Yang Songlin: 腦子長
[01:08:38] Yang Songlin: 怎麼樣
[01:08:39] Yang Songlin: 公司會
[01:08:40] Yang Songlin: 更注重
[01:08:41] Yang Songlin: 優化一點
[01:08:42] Yang Songlin: 對
[01:08:43] Yang Songlin: 就像
[01:08:44] optimization
[01:08:45] Yang Songlin: 對
[01:08:46] Yang Songlin: 對
[01:08:47] 就像
[01:08:48] Yang Songlin: 對
[01:08:49] Yang Songlin: 像
[01:08:50] Yang Songlin: 國內公司
[01:08:51] Yang Songlin: 也感覺
[01:08:52] Yang Songlin: 在逐漸
[01:08:53] Yang Songlin: 在用
[01:08:54] Yang Songlin: 就像
[01:08:55] Yang Songlin: KIMIT
[01:08:56] Yang Songlin: 它
[01:08:57] Yang Songlin: 也是
[01:08:58] Yang Songlin: 最早吃
[01:08:59] Yang Songlin: 沒有
[01:09:00] Yang Songlin: 螃蟹的
[01:09:01] Yang Songlin: 一個地方
[01:09:02] Yang Songlin: 對
[01:09:03] Yang Songlin: 然後
[01:09:04] Yang Songlin: 給我的感覺
[01:09:05] 就是
[01:09:06] 美國
[01:09:07] 他們
[01:09:08] Zhang Xiaojun: 對
[01:09:08] Zhang Xiaojun: 去年
[01:09:09] Zhang Xiaojun: Dipstick
[01:09:10] Zhang Xiaojun: Sponsored
[01:09:11] Zhang Xiaojun: 真正的效果
[01:09:12] Zhang Xiaojun: 比那個更強
[01:09:13] 我覺得
[01:09:14] Yang Songlin: 就是
[01:09:15] Yang Songlin: 效果對比的話
[01:09:16] Yang Songlin: 需要
[01:09:17] 有個地方
[01:09:18] Yang Songlin: 來做一個
[01:09:19] Yang Songlin: IPO-TRIPOP的一個比较
[01:09:20] Yang Songlin: 對
[01:09:21] Yang Songlin: 因為這個東西
[01:09:22] 就是
[01:09:23] Yang Songlin: 非常地
[01:09:24] Yang Songlin: 非常地
[01:09:25] Yang Songlin: 不太好比
[01:09:26] Yang Songlin: 我覺得
[01:09:27] Yang Songlin: 不同的地方
[01:09:28] Yang Songlin: 迅速出來
[01:09:29] Yang Songlin: 不同的
[01:09:30] Yang Songlin: 它
[01:09:31] 可能
[01:09:32] 不能比
[01:09:33] Yang Songlin: 訓練
[01:09:34] Yang Songlin: 架構
[01:09:35] Yang Songlin: 那個
[01:09:36] Yang Songlin: Data
[01:09:37] Yang Songlin: 作品
[01:09:39] 作品
[01:09:40] 作品
[01:09:41] Yang Songlin: 作品
[01:09:43] Yang Songlin: 就是说他有一个AppleTriple的一个跟
[01:09:47] Yang Songlin: 附而贪胜的一个比较
[01:09:48] Yang Songlin: 对 他是有一个AppleTriple的比较的
[01:09:50] Yang Songlin: 但他没有AppleTriple
[01:09:53] Yang Songlin: 去Spasser贪胜的一个比较
[01:09:55] 要是有一个地方能做此善
[01:09:57] Yang Songlin: 来AppleTriple来比下让大家能更好的知道
[01:10:00] Yang Songlin: 就更好了
[01:10:01] Yang Songlin: 但现在因为没有人
[01:10:03] Yang Songlin: 在做一个AppleTriple的比较
[01:10:05] Yang Songlin: 所以这个问题我也不知道哪个会更好
[01:10:08] Yang Songlin: 对
[01:10:08] Yang Songlin: 我觉得很有意思
[01:10:09] Zhang Xiaojun: 为什么Keymeep不做这个比较
[01:10:10] Zhang Xiaojun: 还比较是4成是
[01:10:12] 他在看头写了说他们是第一个验证了
[01:10:14] Zhang Xiaojun: 就性能超越了
[01:10:16] Zhang Xiaojun: 附贪胜的混合临届层胜加购
[01:10:19] Zhang Xiaojun: 刚刚可能还是自然有限吧
[01:10:22] Yang Songlin: 对 如果只有那么多卡
[01:10:24] Yang Songlin: 那可能先投入一个路线去验证吗
[01:10:28] Yang Songlin: 对 然后如果验证出来
[01:10:29] Yang Songlin: 再去投入另外一个路线
[01:10:31] Yang Songlin: 看看有没有可能
[01:10:33] Yang Songlin: 比方说把全球处理力再把它替换掉
[01:10:35] Yang Songlin: 对
[01:10:37] Yang Songlin: 感觉就是没有这么多卡
[01:10:38] Yang Songlin: 来同时来跑一些
[01:10:42] 不同的方案的对比吗
[01:10:44] Yang Songlin: 然后像归谷的话
[01:10:47] 就有很多东西都必须了吗
[01:10:48] Yang Songlin: 所以你也不知道他们有没有跑一下AppleTriple的比较吗
[01:10:52] Yang Songlin: 对
[01:10:53] 你看Keymeep临届的路线
[01:10:55] Zhang Xiaojun: 你觉得还有哪些是指大家关注的
[01:10:58] 前面说就是这个线线注意的某块吗
[01:11:02] Yang Songlin: 然后还有可能就全级追逆他的那个
[01:11:06] 用肉跑还是用肉跑的一个比较吧
[01:11:08] Yang Songlin: 对
[01:11:09] 像Keymeep他选的是用肉跑
[01:11:13] Yang Songlin: 然后像前面三Ness的话
[01:11:16] Yang Songlin: 他选择是一个爬手肉跑
[01:11:19] Yang Songlin: 对
[01:11:20] 他就是25%肉跑
[01:11:23] Yang Songlin: 75%肉跑
[01:11:24] Yang Songlin: 对
[01:11:25] Yang Songlin: 我觉得在这种混合注意里面
[01:11:27] Yang Songlin: 大家都在砍肉跑吧
[01:11:29] Yang Songlin: 但是看大家砍多少吗
[01:11:31] Yang Songlin: 像前面三Ness赶着砍了75%
[01:11:35] Yang Songlin: 然后像Keymeep砍了百分之百
[01:11:37] Yang Songlin: 对
[01:11:38] 然后像这种长度外推
[01:11:40] Yang Songlin: 这种
[01:11:43] 就感觉像看起来的话
[01:11:44] Yang Songlin: 就是肉跑在这种
[01:11:48] 这种Hip hop里面可能会比较阻碍
[01:11:51] Yang Songlin: 这种长度外推
[01:11:53] Yang Songlin: 然后这个地方其实也没有共识
[01:11:56] Yang Songlin: 就是说大家也不知道是用
[01:11:58] 有些还是用肉跑
[01:12:00] Yang Songlin: 有些还是用肉跑
[01:12:00] Yang Songlin: 我觉得这个地方还是没有共识的
[01:12:03] 然后有些地方还用Parser肉跑
[01:12:05] 跟
[01:12:07] 提外话
[01:12:08] Zhang Xiaojun: 你有关注最近Dipsy的那个新的工作
[01:12:11] Zhang Xiaojun: 就是Dipsy他发一个OCA的paper
[01:12:16] 就知道大家就是说
[01:12:18] Yang Songlin: 其实
[01:12:20] 数据撞墙的时候
[01:12:22] Yang Songlin: 还是有很多那种
[01:12:25] 这书籍啊
[01:12:26] Yang Songlin: PDF里面有
[01:12:27] Yang Songlin: 有大量的数据的
[01:12:29] Yang Songlin: 所以他们做这个OCA
[01:12:30] Yang Songlin: 可以帮他们更好的洗一些Data出来
[01:12:32] Yang Songlin: 然后来做Pretrent
[01:12:34] Yang Songlin: 然后另外的话
[01:12:35] Yang Songlin: 他们说是由OCA来做这种Contest Compression
[01:12:41] 这一点的话呢
[01:12:44] 我觉得
[01:12:46] 是一个有意思的一个老动
[01:12:48] Yang Songlin: 对
[01:12:49] Yang Songlin: 但
[01:12:51] 我不确定这个方案怎么样
[01:12:52] Yang Songlin: 对
[01:12:54] 千万的工作你有差一秒
[01:12:57] 就千万三千万的话
[01:12:59] 啊我就基本上那次吧
[01:13:00] Yang Songlin: 就是我会
[01:13:02] 他们要是碰到什么问题啊
[01:13:04] Yang Songlin: 我就可以帮忙打一下对
[01:13:06] Yang Songlin: 就是不不参与他们
[01:13:08] Yang Songlin: 去模型什么的
[01:13:10] Yang Songlin: 就是如果他们有一些
[01:13:11] Yang Songlin: 学术上的讨论的话
[01:13:13] Yang Songlin: 我是
[01:13:14] 会跟他们讨论的对
[01:13:15] Yang Songlin: 我跟
[01:13:16] Yang Songlin: 千万三
[01:13:17] Yang Songlin: 那是那个
[01:13:18] Yang Songlin: 训练的那几个同学都还挺熟的
[01:13:20] Yang Songlin: 对
[01:13:21] Yang Songlin: 那个名字是差一秒
[01:13:23] 没有
[01:13:24] OK
[01:13:24] 所以你差一句什么
[01:13:25] Yang Songlin: 如果我看月了
[01:13:26] Yang Songlin: 他们应该不会用这个方案
[01:13:30] 我会觉得这个方案在开道场
[01:13:33] OK
[01:13:36] 我觉得你有次很好玩啊
[01:13:37] Zhang Xiaojun: 你总是在又
[01:13:38] Zhang Xiaojun: 就把这个价格玩一下
[01:13:40] Zhang Xiaojun: 或者雕一下这种词
[01:13:41] Zhang Xiaojun: 哎
[01:13:42] Zhang Xiaojun: 这个是一种研究原生的文化吗
[01:13:45] 嗯
[01:13:46] Yang Songlin: 我觉得雕这个字好像还挺常见的吧
[01:13:49] Yang Songlin: 就是
[01:13:51] 有一种雕花
[01:13:53] Yang Songlin: 等了一种字炒的那种
[01:13:55] Yang Songlin: 说法吧
[01:13:56] Yang Songlin: 哦
[01:13:57] Zhang Xiaojun: 就是要是另一节说
[01:13:58] Zhang Xiaojun: 不要史上雕花
[01:13:59] Zhang Xiaojun: 是吧
[01:14:00] Zhang Xiaojun: 现在没办法
[01:14:01] Zhang Xiaojun: 虽然也不够数据也有限了
[01:14:03] Zhang Xiaojun: 所以只能雕
[01:14:05] 但是对
[01:14:06] Yang Songlin: 但是我觉得雕价格还是挺有用的吗
[01:14:08] Yang Songlin: 像像DPC
[01:14:10] Yang Songlin: Moei那个雕出来之后
[01:14:12] Yang Songlin: 大家都已经成为一个公式了吗
[01:14:14] Yang Songlin: 基本上的一个公式了
[01:14:16] Yang Songlin: 就可能一般会用那个DPC
[01:14:18] Yang Songlin: 跟Moei的方案吗
[01:14:19] Yang Songlin: 对
[01:14:20] Yang Songlin: 如果在他之前
[01:14:22] 嗯
[01:14:23] 然后他
[01:14:23] 他在做那个呢
[01:14:24] Yang Songlin: 可能
[01:14:25] Yang Songlin: 大家也会说可能在雕Moei吗
[01:14:27] Yang Songlin: 对
[01:14:28] Yang Songlin: 然后感觉雕一进面成
[01:14:30] Yang Songlin: 一个常见的形容词的形容
[01:14:33] 我觉得他不是一个点一次了
[01:14:34] Yang Songlin: 我觉得他是一个
[01:14:35] Yang Songlin: 就是把一个模块把它
[01:14:37] 打模到
[01:14:38] Yang Songlin: 然后更好
[01:14:39] Yang Songlin: 对
[01:14:40] 对
[01:14:40] 如果数据的Skilling
[01:14:42] Zhang Xiaojun: 能够非常突出的话
[01:14:43] Zhang Xiaojun: 其实没有必要掉
[01:14:45] Zhang Xiaojun: 就对数据就好了
[01:14:46] Zhang Xiaojun: 当数据还很少的时候
[01:14:47] Zhang Xiaojun: 他比如说机器人领域
[01:14:48] Zhang Xiaojun: 现在就是数据
[01:14:49] Zhang Xiaojun: 就没什么数据啊
[01:14:50] Zhang Xiaojun: 那只要加数据
[01:14:52] Zhang Xiaojun: 他就能够显住的效果提升
[01:14:54] Zhang Xiaojun: 那就没有必要去
[01:14:56] Zhang Xiaojun: 做模型
[01:14:56] Zhang Xiaojun: 信算法的创新
[01:14:58] 对
[01:14:58] 这是一点吧
[01:14:59] Yang Songlin: 所以
[01:15:00] Yang Songlin: RoboNitsitang
[01:15:02] 最最应该做的应该
[01:15:03] Yang Songlin: 还是先把数据这个问题
[01:15:05] Yang Songlin: 把它搞定吧
[01:15:06] Yang Songlin: 对
[01:15:07] 然后数据搞定之后
[01:15:08] Yang Songlin: 再回来看这种
[01:15:10] efficiency的这种问题
[01:15:11] Yang Songlin: 也不吃吗
[01:15:12] Yang Songlin: 对
[01:15:14] 你做AI的researching
[01:15:16] Zhang Xiaojun: 新你的是什么
[01:15:17] Zhang Xiaojun: 好
[01:15:18] Yang Songlin: 真正
[01:15:19] Yang Songlin: 你是怎么记录AI说好一点
[01:15:21] Zhang Xiaojun: AI的好谈话就是
[01:15:25] Yang Songlin: 粉颗的时候就对模型的那样
[01:15:27] Yang Songlin: 底部能量挺有兴趣的
[01:15:29] Yang Songlin: 然后
[01:15:30] 然后当时master在上和大
[01:15:33] Yang Songlin: 念那个ARP吗
[01:15:34] Yang Songlin: 那个时候就已经进入AI了
[01:15:37] 然后
[01:15:38] Yang Songlin: 二三年
[01:15:39] Yang Songlin: 二二年就是删击PT这一波
[01:15:42] Yang Songlin: 就是那只两个是模等
[01:15:45] Yang Songlin: 蜂蜜开来吗
[01:15:46] Yang Songlin: 那那就做ARP的人
[01:15:48] Yang Songlin: 那就
[01:15:49] 基本上都来做那只两个是模等了吗
[01:15:51] Yang Songlin: 对
[01:15:52] 然后做AI
[01:15:53] Yang Songlin: 我觉得是
[01:15:55] Yang Songlin: 更有意思一点
[01:15:56] Yang Songlin: 就是比之前会更有意思一点
[01:15:59] 因为之前可能大家还是在分task来做吗
[01:16:03] Yang Songlin: 然后现在可能都
[01:16:06] Yang Songlin: 就是比较Ulify
[01:16:08] Yang Songlin: 然后可能就是会比较focus
[01:16:10] Yang Songlin: 更加同用的一些问题来了
[01:16:13] Yang Songlin: 对
[01:16:13] Yang Songlin: 就不需要去操心某些特定的task吗
[01:16:17] Yang Songlin: 因为你只要穿一个很好的机膜
[01:16:20] Yang Songlin: 然后
[01:16:21] Yang Songlin: 然后你对不同的task都可以用吗
[01:16:24] Yang Songlin: 你无非是PoseTrain的时候
[01:16:25] Yang Songlin: 你也要注意的地方不一样吗
[01:16:28] 然后现在的话就是
[01:16:30] 感觉就是自己做的东西的话
[01:16:31] Yang Songlin: 可能就是能看到更多的影响力嘛
[01:16:34] Yang Songlin: 然后
[01:16:35] Yang Songlin: 这一点感觉还是挺
[01:16:37] Yang Songlin: 就是看到自己的开发的东西被大家用还是挺开心的嘛
[01:16:41] Yang Songlin: 你过程中有遇到过什么样的错课没有
[01:16:45] 好像你觉得我
[01:16:46] Yang Songlin: 独PST好像这些工作都还挺顺的
[01:16:51] 没啥人
[01:16:52] 对
[01:16:53] 然后感觉就最小工作都还挺
[01:16:55] Yang Songlin: 年贯的吧
[01:16:56] Yang Songlin: 然后
[01:16:57] Yang Songlin: 然后挺顺的
[01:16:58] Yang Songlin: 我觉得还是
[01:17:00] Yang Songlin: 因为可能是独PST之前
[01:17:03] Yang Songlin: 就是花了半年的时间来
[01:17:06] Yang Songlin: 调研这些东西
[01:17:07] Yang Songlin: 然后可能对这些
[01:17:09] Yang Songlin: 这个领域的理解会生很多
[01:17:12] 然后就生根这个领域来做呢
[01:17:14] Yang Songlin: 其实问题也不是很多吧
[01:17:16] Yang Songlin: 因为
[01:17:17] 因为这个领域非常熟
[01:17:18] Yang Songlin: 然后碰到什么问题
[01:17:20] Yang Songlin: 大家也知道怎么去接
[01:17:21] Yang Songlin: 对
[01:17:22] Yang Songlin: 独PST之前花半年去调研
[01:17:24] Zhang Xiaojun: 这个是做的是你什么样的工作
[01:17:26] Zhang Xiaojun: 是入学之前的半年是
[01:17:29] 就之前申请完半年嘛
[01:17:31] Yang Songlin: 就
[01:17:32] Yang Songlin: 申请完之后有半年可以自由的时光
[01:17:36] Yang Songlin: 然后
[01:17:37] 当时就基本上就是在调研这种架构的这种
[01:17:40] Yang Songlin: paper
[01:17:41] Yang Songlin: 然后当时
[01:17:43] 独了很多比较老的paper
[01:17:45] 就比方说像德塔奈特
[01:17:47] Yang Songlin: 他最早是2021年
[01:17:50] 就是那个
[01:17:51] Yang Songlin: SGM之父
[01:17:54] Yang Songlin: 的那个paper
[01:17:56] 然后当时我就在这个工作有印象吗
[01:17:59] Yang Songlin: 然后后面的话就
[01:18:02] 后面就那年年底嘛
[01:18:04] Yang Songlin: 就做完那个Gating Needle探索
[01:18:06] Yang Songlin: 然后发现
[01:18:07] Yang Songlin: 这个领域的话
[01:18:08] Yang Songlin: 大家会对那个
[01:18:09] Yang Songlin: 银康态势
[01:18:11] require
[01:18:12] Yang Songlin: 就是从那个前面的文章里面去做一个日区
[01:18:14] Yang Songlin: will
[01:18:15] Yang Songlin: 这个task会感兴趣
[01:18:18] 然后这个就让我一下子
[01:18:19] Yang Songlin: 年想到了那个
[01:18:20] Yang Songlin: 2011年的一篇工作了
[01:18:22] Yang Songlin: 对
[01:18:23] 因为之前的
[01:18:24] Yang Songlin: 这个整个领域他把握得非常的
[01:18:27] 通撤嘛
[01:18:28] Yang Songlin: 所以我知道就是
[01:18:29] Yang Songlin: 如果领域大家其他
[01:18:31] Yang Songlin: 其他人关心这个问题的话
[01:18:33] Yang Songlin: 我应该从什么角度去切入
[01:18:35] Yang Songlin: 然后
[01:18:37] 然后我也知道他前面工作有什么问题吗
[01:18:39] Yang Songlin: 比方说
[01:18:40] Yang Songlin: 2021年德塔奈特的话
[01:18:42] Yang Songlin: 他是
[01:18:43] Yang Songlin: 没有hard
[01:18:44] Yang Songlin: hardware efficiency的一个保证
[01:18:46] Yang Songlin: 对
[01:18:46] Yang Songlin: 然后我就觉得
[01:18:47] Yang Songlin: 然后我后面就觉得就交易这个工作之后
[01:18:51] 做德塔奈的话我就知道
[01:18:53] 德塔奈特是一个很好的一个模型
[01:18:55] Yang Songlin: 然后他的缺点就是
[01:18:58] 现在大家还不能大规模用起了
[01:19:01] 然后如果我能开发出一个算法
[01:19:04] Yang Songlin: 能把他skill up
[01:19:05] Yang Songlin: 那就是一个非常有意义的工作
[01:19:07] Yang Songlin: 对
[01:19:08] Yang Songlin: 然后我大概就是
[01:19:10] Yang Songlin: 这套逻辑念吗
[01:19:11] Yang Songlin: 然后
[01:19:12] Yang Songlin: 就可能也是应器好吧
[01:19:14] Yang Songlin: 就三号
[01:19:15] 正好能推出一个能够把他skill up的一个算法
[01:19:18] Yang Songlin: 对
[01:19:19] Yang Songlin: 然后后面的话
[01:19:20] Yang Songlin: 就是
[01:19:22] 后面的话就可能就是像gg带带的话
[01:19:24] Yang Songlin: 就是也有这个工作做
[01:19:26] 因为当时发现
[01:19:28] Yang Songlin: 德塔奈特还是在很多他sk上面
[01:19:31] Yang Songlin: 是打不过这个memba2的对
[01:19:33] Yang Songlin: 然后我当时就觉得打不过就加入吗
[01:19:36] Yang Songlin: 那我就把memba2的他那个gating把他拿过来
[01:19:40] Yang Songlin: 然后
[01:19:41] Yang Songlin: 把德塔奈特再加回来
[01:19:43] Yang Songlin: 对
[01:19:43] Yang Songlin: 这样子的话就把他
[01:19:45] Yang Songlin: ajb变成一个get it.net
[01:19:47] Yang Songlin: 对
[01:19:48] Yang Songlin: 我觉得我做的东西就是
[01:19:51] Yang Songlin: 就会看这个领域他需要什么样的工作吗
[01:19:54] Yang Songlin: 然后
[01:19:55] Yang Songlin: 哪些
[01:19:56] Yang Songlin: 做什么样的东西会带来更多的这种
[01:20:00] Yang Songlin: 领域的影响力吗
[01:20:01] Yang Songlin: 然后还有业界的影响力吗
[01:20:02] Yang Songlin: 对
[01:20:03] Yang Songlin: 然后
[01:20:04] Yang Songlin: 就是如果当你很清楚你要做什么的时候
[01:20:07] Yang Songlin: 你其实不会遇到什么错误的
[01:20:10] 就是接触
[01:20:11] Yang Songlin: 接触的太可愿的那种川普
[01:20:13] Yang Songlin: 我觉得都是
[01:20:14] Yang Songlin: 有办法把他
[01:20:16] 搞定的
[01:20:17] Yang Songlin: 对
[01:20:17] Yang Songlin: 我觉得更大的参议就是你不知道你要做什么东西
[01:20:20] Yang Songlin: 你不知道做什么东西是有用的
[01:20:22] Yang Songlin: 我觉得这个才是最大的参议
[01:20:24] 问你和核心是从历史中学习的很多
[01:20:27] 对吧
[01:20:28] Yang Songlin: 我觉得我还是挺喜欢看
[01:20:31] 最早的那些paper
[01:20:32] Yang Songlin: 我觉得那些paper现在都挺好的
[01:20:34] Yang Songlin: 然后
[01:20:35] Yang Songlin: 我管这个叫做
[01:20:37] 考股
[01:20:38] Yang Songlin: 对
[01:20:38] Yang Songlin: 因为我就喜欢考那些古代的paper
[01:20:41] 就古代的话
[01:20:42] Yang Songlin: 可能要你要一年也算古代吗
[01:20:44] Yang Songlin: 因为
[01:20:45] 原来现在
[01:20:46] Yang Songlin: 一年前的paper叫老paper
[01:20:48] Yang Songlin: 那五年前的paper
[01:20:49] Yang Songlin: 那可以叫做古代的paper
[01:20:51] Yang Songlin: 对
[01:20:52] Yang Songlin: 那半年你读的最老的paper到什么时候
[01:20:56] 最近半年吗
[01:20:57] Yang Songlin: 就是你掉给了那半年
[01:20:59] 那半年
[01:21:01] Yang Songlin: 可能就是
[01:21:02] Yang Songlin: 读到表输2017年的文章吧
[01:21:07] 读了多数
[01:21:07] 因为
[01:21:09] 我觉得
[01:21:10] Yang Songlin: 我可以说这个里面的文章
[01:21:12] Yang Songlin: 我基本上都读过一篇
[01:21:13] Yang Songlin: 对
[01:21:14] 这个做到的人很少
[01:21:15] Zhang Xiaojun: 是吧
[01:21:17] 对
[01:21:17] 我觉得不同的人有不同的录色
[01:21:19] Yang Songlin: 是philosophy
[01:21:21] 我觉得
[01:21:22] Yang Songlin: 就一定要吧
[01:21:23] Yang Songlin: 只有你与里面值得看的文章
[01:21:25] Yang Songlin: 全部都看一遍
[01:21:26] Yang Songlin: 对
[01:21:28] Zhang Xiaojun: 你为什么在AI的
[01:21:29] Zhang Xiaojun: 众多领域分支里面
[01:21:30] Zhang Xiaojun: 你喜欢的是加购
[01:21:32] 因为我比较喜欢做散发嘛
[01:21:34] Yang Songlin: 然后
[01:21:35] 当时觉得
[01:21:36] Yang Songlin: 那身model
[01:21:37] Yang Songlin: 然后就可以
[01:21:38] Yang Songlin: 看出哪些东西是值得做的嘛
[01:21:41] Yang Songlin: 对
[01:21:42] 然后
[01:21:44] Yang Songlin: 就想做一些比较通用的
[01:21:45] Yang Songlin: 然后
[01:21:46] Yang Songlin: 整体
[01:21:47] Yang Songlin: 都是对这种那身model
[01:21:49] Yang Songlin: 有用的一些work
[01:21:50] Yang Songlin: 然后请我一下自己兴趣
[01:21:51] Yang Songlin: 然后发现
[01:21:53] 然后还正如最开始的说到嘛
[01:21:56] Yang Songlin: 就是像黑地鲁色尺
[01:21:58] Yang Songlin: 他们有很多伯克
[01:21:59] Yang Songlin: 然后
[01:22:01] Yang Songlin: 主要还自己喜欢做算法
[01:22:02] Yang Songlin: 然后
[01:22:03] Yang Songlin: 然后就发现这个领域很深
[01:22:04] Yang Songlin: 我来做
[01:22:06] 你说写什么很好
[01:22:07] Yang Songlin: 应该还挺好的
[01:22:08] Zhang Xiaojun: 对
[01:22:09] 为什么
[01:22:10] Zhang Xiaojun: 因为这篇文文里面
[01:22:11] Zhang Xiaojun: 这么多公事
[01:22:12] Zhang Xiaojun: 我觉得这些数学都不是很难
[01:22:14] Yang Songlin: 都是一些
[01:22:15] Yang Songlin: 举振的一些
[01:22:17] Yang Songlin: 主举振那些惩罚啊
[01:22:19] Yang Songlin: 这些东西
[01:22:20] Yang Songlin: 然后像
[01:22:22] 像
[01:22:23] Yang Songlin: 现心注意它
[01:22:25] Yang Songlin: 有安的形式的话
[01:22:27] 它会
[01:22:28] Yang Songlin: 有一些reconference
[01:22:29] Yang Songlin: 会有一些现心转移方程
[01:22:31] Yang Songlin: 那些公事嘛
[01:22:33] 然后兵型的话
[01:22:34] Yang Songlin: 那可能就是
[01:22:36] 兵型确实数据会比较多一点
[01:22:38] Yang Songlin: 对
[01:22:38] Yang Songlin: 那个东西比较
[01:22:40] tricky
[01:22:40] 对
[01:22:41] Yang Songlin: 所以它这个论文
[01:22:42] Zhang Xiaojun: 闲助比加论文的
[01:22:43] Zhang Xiaojun: 税工时是要更多的
[01:22:45] Zhang Xiaojun: 因为
[01:22:46] Yang Songlin: 我觉得现心最厉害的主要就是
[01:22:48] Yang Songlin: 一个玩举振变化的一个东西
[01:22:51] Yang Songlin: 他可以把一个平方的东西
[01:22:52] Yang Songlin: 变成一个现心的
[01:22:54] Yang Songlin: 然后他又
[01:22:56] Yang Songlin: 他就是玩这种举振变化
[01:22:58] Yang Songlin: 对
[01:22:58] Yang Songlin: 然后他从reconference
[01:23:00] Yang Songlin: 把它变成创可
[01:23:02] Yang Songlin: 他们都等价的吗
[01:23:03] Yang Songlin: 但他们都设计到很多这种
[01:23:05] Yang Songlin: 举振变化吗
[01:23:06] Yang Songlin: 所以他数学多一点
[01:23:08] Yang Songlin: 我觉得很正常吧
[01:23:09] Yang Songlin: 你刚才提到
[01:23:11] Zhang Xiaojun: 你读博士前半年
[01:23:13] Zhang Xiaojun: 做了很多算法的考古
[01:23:15] Zhang Xiaojun: 我们给大家讲讲
[01:23:16] Zhang Xiaojun: 就是算法是怎么一步
[01:23:17] Zhang Xiaojun: 不顾眼睛到今天的这段算法历史
[01:23:19] Zhang Xiaojun: 那我从
[01:23:21] transformal开始
[01:23:23] 讲吧
[01:23:23] 就说说了换他
[01:23:25] Yang Songlin: 给大家可能就
[01:23:27] 三个主要模块吧
[01:23:29] Yang Songlin: 他也就是
[01:23:30] Yang Songlin: 锁力继续
[01:23:32] Yang Songlin: 然后另外一个是
[01:23:34] Yang Songlin: 维持变吗
[01:23:34] Yang Songlin: 然后之后就是i5分
[01:23:38] 然后
[01:23:39] Yang Songlin: 最开始那几年我感觉可能
[01:23:41] Yang Songlin: 加个reset是非常多吧
[01:23:44] 然后有一些
[01:23:45] Yang Songlin: 价格的改进也确实
[01:23:47] Yang Songlin: 被用到的今天比方说
[01:23:50] 然后说像像的位置编码吗
[01:23:52] Yang Songlin: 比如像肉
[01:23:54] 他最开始的话
[01:23:56] Yang Songlin: 参加我的话
[01:23:56] Yang Songlin: 他是绝对位置编码
[01:23:59] Yang Songlin: 然后像今天进完都改成这种
[01:24:02] Yang Songlin: 像的位置编码吗
[01:24:05] Yang Songlin: 然后像
[01:24:07] m1的话
[01:24:08] Yang Songlin: 我觉得可能也是
[01:24:10] Yang Songlin: 从2011年左右
[01:24:13] Yang Songlin: 就开始发展了
[01:24:15] 然后可能中间
[01:24:17] 有段时间
[01:24:17] 大家可能就不怎么信按模一吗
[01:24:19] Yang Songlin: 然后后面
[01:24:20] Yang Songlin: 又发现
[01:24:22] Yang Songlin: 比如说像dips1
[01:24:23] Yang Songlin: 把m1做通了
[01:24:24] Yang Songlin: 然后大家又回来重新
[01:24:27] Yang Songlin: 做m1
[01:24:28] Yang Songlin: 现在m1应该就是
[01:24:30] Yang Songlin: 大家都会用的东西吗
[01:24:32] 然后像
[01:24:33] Yang Songlin: 摊上的话
[01:24:34] Yang Songlin: 摊上的这种变种
[01:24:36] Yang Songlin: 可能就更多了
[01:24:38] Yang Songlin: 像
[01:24:39] Yang Songlin: 前往也说到
[01:24:39] Yang Songlin: 像2010年前
[01:24:41] Yang Songlin: 后可能
[01:24:42] Yang Songlin: 我探生的变种就非常非常的多
[01:24:45] 然后其实也主要就是
[01:24:47] Yang Songlin: 两手变种吗
[01:24:48] Yang Songlin: 地头就先信注意你
[01:24:50] 然后第二的话就是西术术一例
[01:24:54] Yang Songlin: 他们先注意的话
[01:24:55] Yang Songlin: 他们就会搞很多那种
[01:24:58] 可能埋似的
[01:25:00] Yang Songlin: 去procimate
[01:25:01] Yang Songlin: service的肯定
[01:25:03] Yang Songlin: 然后在今天来看
[01:25:04] Yang Songlin: 我觉得这是一个非常
[01:25:06] 错误的方向
[01:25:07] Yang Songlin: 我觉得就不应该去用可能埋似的去
[01:25:10] Yang Songlin: 去估计这些
[01:25:12] Yang Songlin: service的肯定
[01:25:14] 然后有一些好工作的话可能就会
[01:25:17] Yang Songlin: 因为没有follow up
[01:25:19] Yang Songlin: 然后被埋摸在
[01:25:23] Yang Songlin: 文现海里面呢
[01:25:25] Yang Songlin: 比方说像
[01:25:26] Yang Songlin: data那这个工作
[01:25:28] Yang Songlin: 我前面说他上两年就有了吗
[01:25:31] 然后得他入那个东西
[01:25:34] Yang Songlin: 可能后面几年就根本没有人
[01:25:36] Yang Songlin: taggy seriously
[01:25:38] Yang Songlin: 就是没有什么follow work
[01:25:40] Yang Songlin: 然后从时间内也见上来说呢
[01:25:44] Yang Songlin: 也话来说呢
[01:25:45] Yang Songlin: 可能有一些技术比较时
[01:25:47] Yang Songlin: 像这种
[01:25:49] Yang Songlin: 系力度的这种疑望
[01:25:50] Yang Songlin: 可能很多年前就有了
[01:25:53] 比方说像这个
[01:25:55] Yang Songlin: 系力度的这种dk
[01:25:57] 至少
[01:25:58] Yang Songlin: i'mapp二年二年他可能就有一篇工作了
[01:26:02] 然后最早的话我可以考古的二年一六年
[01:26:06] 然后
[01:26:07] Yang Songlin: 但后面的话表现
[01:26:08] Yang Songlin: rein i2023年他反而用的是一个
[01:26:11] Yang Songlin: 疑望
[01:26:13] Yang Songlin: 数据
[01:26:14] Yang Songlin: 跟
[01:26:14] Yang Songlin: 数据的一个dk
[01:26:17] 所以我觉得可能就是之前的技术不能
[01:26:20] Yang Songlin: 更好的
[01:26:21] Yang Songlin: 传承下来吧
[01:26:23] 然后
[01:26:24] Yang Songlin: 然后我有比较喜欢把所有的之前
[01:26:27] Yang Songlin: 所有的技术全部重新
[01:26:28] Yang Songlin: 重新審视一遍
[01:26:29] Yang Songlin: 然后
[01:26:30] Yang Songlin: 悬言一下
[01:26:31] Yang Songlin: 我觉得最mexnc的技术来做
[01:26:32] Yang Songlin: 然后可能
[01:26:34] Yang Songlin: 这边说像得他入这个技术
[01:26:35] Yang Songlin: 又可以
[01:26:37] Yang Songlin: 重
[01:26:38] Yang Songlin: 现光芒吧
[01:26:39] Yang Songlin: 对
[01:26:40] Yang Songlin: 但如果
[01:26:42] 如果没有我来follow的话
[01:26:43] Yang Songlin: 可能就不好说了
[01:26:44] Yang Songlin: 可能
[01:26:45] Yang Songlin: 可能这一套技术路线可能就会
[01:26:49] Yang Songlin: 演藏在文线海里面
[01:26:51] Yang Songlin: 对
[01:26:52] Yang Songlin: 然后像spa set 坦识的话
[01:26:56] 他们这早可能就做一些
[01:26:59] Yang Songlin: static的一些spa set 坦识
[01:27:01] Yang Songlin: 像弄风
[01:27:02] Yang Songlin: 那种big bird
[01:27:04] Yang Songlin: 他们会有各种各样的
[01:27:06] Yang Songlin: spa set 坦识
[01:27:07] Yang Songlin: 然后好像后面就主建
[01:27:10] Yang Songlin: 收点到
[01:27:11] Yang Songlin: 用sletty 没走了
[01:27:12] Yang Songlin: 然后可能近年的话
[01:27:14] Yang Songlin: 他会有一些不一样的东西出来
[01:27:17] Yang Songlin: 就是
[01:27:19] 早几年比较少
[01:27:20] Yang Songlin: 但是最近有比较多的比较多
[01:27:22] Yang Songlin: 像
[01:27:23] 动态 西鼠
[01:27:24] Yang Songlin: 像kimilalmobo
[01:27:26] Yang Songlin: 然后dc 跟这种
[01:27:29] Yang Songlin: spa set 坦识都属于动态 西鼠
[01:27:32] Yang Songlin: 然后
[01:27:33] Yang Songlin: 总的来说就是
[01:27:36] Yang Songlin: 我感觉整体还是
[01:27:38] Yang Songlin: 伤害不断演进
[01:27:41] Yang Songlin: 然后可能他整个发展
[01:27:43] Yang Songlin: 就是需要
[01:27:45] 有一些技术可能需要
[01:27:47] Yang Songlin: rething 几次
[01:27:49] 然后
[01:27:50] Yang Songlin: 很多双手的话
[01:27:51] Yang Songlin: 感觉这个发展还是会有一些
[01:27:54] Yang Songlin: 有点逻学上升的味道在里面吧
[01:27:57] Yang Songlin: 对
[01:27:58] Zhang Xiaojun: 其实历史中已经有很多的工具
[01:28:00] Zhang Xiaojun: 但是今天我们需要拿哪些工具来
[01:28:02] Zhang Xiaojun: 应用推动今天的算法
[01:28:04] Zhang Xiaojun: 眼睛其实是一个很关键的事
[01:28:06] 对的
[01:28:06] 对 我觉得
[01:28:08] Yang Songlin: 其实很多历史的算法
[01:28:11] Yang Songlin: 他其实是很先进的
[01:28:12] Yang Songlin: 但是可能
[01:28:14] Yang Songlin: 当时同好没有意识到这个工作的
[01:28:19] Yang Songlin: 价值
[01:28:19] Yang Songlin: 然后可能那个工具不会买摸了
[01:28:22] 然后也有可能就是那个工作
[01:28:24] Yang Songlin: 他的配套
[01:28:25] Yang Songlin: 比如说那些代码开源代码
[01:28:27] Yang Songlin: 做的太难了
[01:28:28] Yang Songlin: 然后其他人想服务也没法服务吗
[01:28:31] Yang Songlin: 对 所以
[01:28:32] Yang Songlin: 对
[01:28:33] Yang Songlin: 所以总的来说就是
[01:28:36] 我觉得
[01:28:36] 如果今天做工作的话
[01:28:38] Yang Songlin: 可能的话就是
[01:28:40] 不然像我我就会
[01:28:41] Yang Songlin: 把这种
[01:28:43] Yang Songlin: 代码把它做的
[01:28:44] Yang Songlin: 让大家好用
[01:28:45] Yang Songlin: 所以这一套技术肯定能
[01:28:46] Yang Songlin: 把它让他流传下去
[01:28:48] Yang Songlin: 对
[01:28:50] 然后别人的工作
[01:28:51] Yang Songlin: 之前的话
[01:28:52] Yang Songlin: 我就会
[01:28:53] Yang Songlin: 会找一些
[01:28:54] Yang Songlin: 我觉得MexSense的一些工作
[01:28:55] Yang Songlin: 然后让他
[01:28:57] 让他
[01:28:59] 尽可能地看见他这个钱力有多大吧
[01:29:02] 对
[01:29:03] 然后又说回
[01:29:05] Yang Songlin: 就比方说
[01:29:05] Yang Songlin: 像加过里面的算法的话
[01:29:08] 因为他算法的
[01:29:10] Yang Songlin: 这种wareren子也太多了
[01:29:11] Yang Songlin: 然后是加过的话
[01:29:13] Yang Songlin: 那肯定还是
[01:29:14] Yang Songlin: 需要很多算议来试
[01:29:17] 然后
[01:29:18] Yang Songlin: 有很多算法可能是在小规模
[01:29:20] Yang Songlin: 下面有我
[01:29:21] Yang Songlin: 可能然后可能到大规模就不过
[01:29:23] Yang Songlin: 可能这就是非常常见的
[01:29:25] Yang Songlin: 对
[01:29:26] Yang Songlin: 然后
[01:29:27] Yang Songlin: 可能
[01:29:29] 对
[01:29:29] 可能比方说像今年
[01:29:31] Yang Songlin: 国内公司要对开源
[01:29:34] Yang Songlin: 重新有心情
[01:29:35] Yang Songlin: 可能今天可能会大家见到
[01:29:38] Yang Songlin: 加过的这种开源工作会更多一点
[01:29:40] Yang Songlin: 然后
[01:29:40] Yang Songlin: 变化可能会
[01:29:42] Yang Songlin: 相较劝烟来说
[01:29:43] Yang Songlin: 可能大家会觉得加过的
[01:29:44] Yang Songlin: 变化比去年会多很多吧
[01:29:47] 你的Delta Rule是什么给大家的灵感
[01:29:51] Yang Songlin: 就是二年二一年嘛
[01:29:52] Yang Songlin: 那个工作就
[01:29:54] 那工作是他们提出来的嘛
[01:29:56] Yang Songlin: 对
[01:29:57] 然后
[01:29:58] Yang Songlin: 我就想一个冰型算法吗
[01:30:00] Yang Songlin: 然后其实就停类似于
[01:30:04] FlySher坦神之于SurfmySher坦神
[01:30:07] Yang Songlin: 对
[01:30:07] Yang Songlin: 其实就是一个算法
[01:30:09] Yang Songlin: 能够让他
[01:30:10] Yang Songlin: 硬件靠小坦实现
[01:30:12] Yang Songlin: 对
[01:30:13] Yang Songlin: 就是如果没有FlySher坦神
[01:30:15] Yang Songlin: 那SurfmySher坦神也走不到今天吗
[01:30:18] Yang Songlin: 然后像没有那个冰型算法的话
[01:30:20] Yang Songlin: 那德特太肯定也不能走到今天
[01:30:22] Yang Songlin: 就大概是一个这样子的关系
[01:30:25] 然后我做Risers可能就是比较喜欢
[01:30:28] Yang Songlin: 从实际上的这种
[01:30:32] Yang Songlin: 硬件的这种亲和力来研究的就是看
[01:30:36] Yang Songlin: 因为我看有算法有没有潜力
[01:30:37] Yang Songlin: 我会来分析这个算法它的这个
[01:30:41] 冰型潜力有多大
[01:30:43] Yang Songlin: 然后
[01:30:44] Yang Songlin: 它的Skater beauty会有多大
[01:30:46] Yang Songlin: 对
[01:30:47] Yang Songlin: 然后我会在历史的
[01:30:50] Yang Songlin: 文先海里面找出一些
[01:30:53] Machine Learning上面的MakeSense
[01:30:55] Yang Songlin: 然后
[01:30:56] 同时我又能想办法把它冰型的一些算法来玩
[01:30:59] Yang Songlin: 对 就是我的
[01:31:01] 做Risers的思路
[01:31:03] Yang Songlin: 我觉得总的来说就是还是
[01:31:06] 就是Machine Learning上面的MakeSense
[01:31:08] Yang Songlin: 然后它这个算法
[01:31:10] Yang Songlin: 它又可以有冰型的算法
[01:31:12] Yang Songlin: 只是这样的算法才能
[01:31:14] Yang Songlin: 才能被
[01:31:15] Yang Songlin: 然后在
[01:31:16] Yang Songlin: 在这个年代被用到
[01:31:18] Yang Songlin: 因为
[01:31:19] Yang Songlin: 就在
[01:31:20] Yang Songlin: 那些什么的年代
[01:31:22] Yang Songlin: 就是Skater beauty左右
[01:31:24] Yang Songlin: 你肯定需要有一些
[01:31:25] Yang Songlin: 能够Skater beauty的算法
[01:31:27] Yang Songlin: 对
[01:31:28] 然后如果一个算法它
[01:31:30] 这个MakeSense
[01:31:31] Yang Songlin: 比如说像它
[01:31:32] Yang Songlin: 如果这个算法我觉得它们这个算法
[01:31:33] Yang Songlin: 就非常的MakeSense
[01:31:35] Yang Songlin: 然后同时用的Skater beauty
[01:31:37] Yang Songlin: 就比较好了话
[01:31:38] 那
[01:31:39] Yang Songlin: 就完全有可能
[01:31:40] Yang Songlin: 就是在
[01:31:41] Yang Songlin: 今天这个时代上面
[01:31:42] Yang Songlin: 是会有
[01:31:43] 带来一些不一样的一些
[01:31:45] Yang Songlin: 加购
[01:31:46] Yang Songlin: 就比较说
[01:31:47] Yang Songlin: 像千文三
[01:31:48] Yang Songlin: Nex和Kimining
[01:31:50] Yang Songlin: 就已经让我们
[01:31:51] Yang Songlin: 带来一些
[01:31:52] Yang Songlin: 星期相对
[01:31:53] Yang Songlin: 就做个新加购的原因
[01:31:55] 我前几天
[01:31:56] 做了一个
[01:31:57] Zhang Xiaojun: 论文的不可
[01:31:58] Zhang Xiaojun: 就提到
[01:31:59] Zhang Xiaojun: 川斯风们
[01:32:00] Zhang Xiaojun: 是这一代硬件的天选加购
[01:32:02] Zhang Xiaojun: 对啊
[01:32:03] Yang Songlin: 川斯风的它
[01:32:04] Yang Songlin: 我们肯定是天选嘛
[01:32:05] Yang Songlin: 比较说它当时
[01:32:06] Yang Songlin: 它设计川斯风
[01:32:07] Yang Songlin: 就是
[01:32:08] Yang Songlin: 为了让它硬件快
[01:32:10] Yang Songlin: 设计出来的嘛
[01:32:12] Yang Songlin: 像
[01:32:13] FF
[01:32:14] Yang Songlin: 肯定不用说了
[01:32:15] Yang Songlin: 就是大局任程房
[01:32:17] Yang Songlin: 肯定
[01:32:18] 快嘛
[01:32:19] Yang Songlin: 然后像
[01:32:21] Yang Songlin: Euthansion
[01:32:22] Yang Songlin: 它其实就是
[01:32:24] Yang Songlin: 之前Euthansion之前
[01:32:26] Yang Songlin: 大家讯为
[01:32:27] Yang Songlin: ISTM之中
[01:32:28] Yang Songlin: 他们这种
[01:32:29] Yang Songlin: 不能并行的
[01:32:30] Yang Songlin: 模块来做的
[01:32:32] Yang Songlin: 然后像
[01:32:33] Yang Songlin: ISTM它肯定硬件加速
[01:32:35] Yang Songlin: 就
[01:32:36] Yang Songlin: 更难搞嘛
[01:32:37] Yang Songlin: 然后像
[01:32:39] Yang Songlin: Euthansion
[01:32:40] Yang Songlin: 它就算它是
[01:32:41] Yang Songlin: 平方的复杂度
[01:32:42] Yang Songlin: 它复杂度比
[01:32:43] Yang Songlin: A&N搞了一个级别
[01:32:45] 但是它就可以
[01:32:46] Yang Songlin: 通过局任程法
[01:32:47] Yang Songlin: 然后来
[01:32:48] Yang Songlin: 算到那个
[01:32:49] Yang Songlin: OPU
[01:32:50] Yang Songlin: 所以它的硬件
[01:32:51] Yang Songlin: 清盒是比
[01:32:52] Yang Songlin: A&N要好
[01:32:54] Yang Songlin: 很多的
[01:32:55] Yang Songlin: 所以大家会
[01:32:56] Yang Songlin: 宁愿去用
[01:32:57] Yang Songlin: 理论复杂度
[01:32:58] Yang Songlin: 更高的
[01:32:59] Yang Songlin: Transformer
[01:33:01] Yang Songlin: 也不会来用这个
[01:33:02] Yang Songlin: 理论复杂度
[01:33:03] Yang Songlin: 更定的这个ISTM
[01:33:04] Yang Songlin: 因为他们这个硬件
[01:33:05] Yang Songlin: 清盒
[01:33:06] Yang Songlin: 表现完全不要嘛
[01:33:08] 对
[01:33:09] Yang Songlin: 然后我觉得
[01:33:10] Yang Songlin: 算法整体发展
[01:33:11] Yang Songlin: 就是要找到这些
[01:33:12] 硬件清盒
[01:33:14] Yang Songlin: 然后
[01:33:15] Yang Songlin: 又更好的一些
[01:33:17] Yang Songlin: 算法吧
[01:33:18] Yang Songlin: 因为
[01:33:19] Yang Songlin: 串丝红的它不但
[01:33:21] Yang Songlin: 那个单身它不但是
[01:33:23] Yang Songlin: 硬件跟清盒嘛
[01:33:24] Yang Songlin: 它确实也解决了一些
[01:33:25] Yang Songlin: 长成一来的关系的问题嘛
[01:33:27] Yang Songlin: 所以它才会
[01:33:29] Yang Songlin: 流行的这么开嘛
[01:33:31] Yang Songlin: 像今天的花力量
[01:33:33] Yang Songlin: 单身又重新跟上舞台
[01:33:35] Yang Songlin: 那肯定
[01:33:36] Yang Songlin: 也离不开
[01:33:37] Yang Songlin: 最系列的发展嘛
[01:33:39] Yang Songlin: 就比方说像那些
[01:33:41] Yang Songlin: 就是
[01:33:42] Yang Songlin: 把它分成创造可能那些
[01:33:44] Yang Songlin: 冰型的算法啊
[01:33:45] Yang Songlin: 然后
[01:33:46] Yang Songlin: 它更强的那些
[01:33:49] Yang Songlin: 设计啊
[01:33:51] Yang Songlin: 能让它从
[01:33:52] Yang Songlin: Motion Learning
[01:33:53] Yang Songlin: Performance这个角度来没
[01:33:54] Yang Songlin: 更加没盛上
[01:33:55] Yang Songlin: 这些
[01:33:56] Yang Songlin: 这些
[01:33:57] Yang Songlin: 这些才是
[01:33:58] Yang Songlin: 能推动它发展的原动力嘛
[01:34:01] Yang Songlin: 所以我还是非常主张
[01:34:03] Yang Songlin: 就是来做一些
[01:34:05] Yang Songlin: 就是一些非常
[01:34:07] Yang Songlin: Principal
[01:34:08] Yang Songlin: 就是
[01:34:09] Yang Songlin: 从Motion LearningPerformance
[01:34:11] Yang Songlin: 来说它是
[01:34:12] Principal
[01:34:13] Yang Songlin: 很有
[01:34:14] Yang Songlin: 就是它会
[01:34:15] Mathmetically
[01:34:17] Yang Songlin: 个Round date
[01:34:18] Yang Songlin: 就会有
[01:34:19] Yang Songlin: 就是从数据上
[01:34:20] Yang Songlin: 它是Masons的嘛
[01:34:21] Yang Songlin: 就比方说得到
[01:34:22] Yang Songlin: 如果它从数据
[01:34:23] Masons
[01:34:24] Yang Songlin: 然后同时
[01:34:25] Yang Songlin: Hallway
[01:34:26] Yang Songlin: 我来的一些模型
[01:34:27] 对
[01:34:28] Yang Songlin: 因为我觉得这模型
[01:34:29] Yang Songlin: 还是
[01:34:30] Yang Songlin: 肯定要结合当前硬件的
[01:34:32] Yang Songlin: 结会有些人说呀
[01:34:34] Yang Songlin: 那我设计一个算法
[01:34:36] Yang Songlin: 它足够好
[01:34:37] Yang Songlin: 那硬件公司来帮我优化呀
[01:34:39] Yang Songlin: 那怎么可能呢
[01:34:41] Yang Songlin: 那你这算法你是
[01:34:43] Yang Songlin: 金质座的还是
[01:34:45] Yang Songlin: 赢质座的
[01:34:46] Yang Songlin: 然后硬件公司来天天帮你优化呀
[01:34:48] Yang Songlin: 那是不可能的嘛
[01:34:49] 那你肯定你要
[01:34:50] Yang Songlin: 首先你要
[01:34:51] Yang Songlin: 让你的算法
[01:34:52] Yang Songlin: 先去
[01:34:53] 满足一些
[01:34:54] Yang Songlin: 非常
[01:34:55] Yang Songlin: 通用的原则嘛
[01:34:56] Yang Songlin: 像Hallway
[01:34:57] Yang Songlin: 我才有一些
[01:34:58] Yang Songlin: Principal
[01:34:59] Yang Songlin: 像Memory Haraki
[01:35:01] Yang Songlin: 这种东西
[01:35:02] Yang Songlin: 然后像
[01:35:03] Yang Songlin: 举政承法
[01:35:04] Yang Songlin: 更有
[01:35:05] 像这种东西的话
[01:35:06] Yang Songlin: 就是
[01:35:07] 你不论看
[01:35:08] Yang Songlin: 不同类型的哈利亚
[01:35:10] Yang Songlin: 它基本上都是会
[01:35:11] Yang Songlin: 增存这种原则嘛
[01:35:13] Yang Songlin: 就有一些
[01:35:14] Yang Songlin: Ulysses的一些Principal嘛
[01:35:16] 你这些算法你可能
[01:35:17] Yang Songlin: 没必要去专门
[01:35:18] Yang Songlin: 比方说针对Hallway
[01:35:20] Yang Songlin: 的去优化
[01:35:22] 但我觉得
[01:35:23] Yang Songlin: 做算法
[01:35:24] Yang Songlin: 至少要去
[01:35:25] Yang Songlin: 满足这些
[01:35:27] Yang Songlin: 硬件比较
[01:35:28] Yang Songlin: 通用的这种Principal
[01:35:29] Yang Songlin: 要不然
[01:35:30] Yang Songlin: 我觉得做的算法
[01:35:31] Yang Songlin: 就是
[01:35:32] Yang Songlin: 能在当今这个
[01:35:34] Yang Songlin: Belated所有你的这个
[01:35:36] Yang Songlin: 场景下面基本上就是
[01:35:38] Yang Songlin: 没有什么实际价值的
[01:35:41] Yang Songlin: 就存自于自乐吧
[01:35:43] Yang Songlin: 对
[01:35:44] KIMI的理念这个
[01:35:46] Zhang Xiaojun: 为硬件有做什么样的一物化没有
[01:35:48] Zhang Xiaojun: KIMI的
[01:35:49] Yang Songlin: 我觉得它等那个
[01:35:51] Yang Songlin: 算法
[01:35:52] Yang Songlin: 还是硬件轻合的吧
[01:35:54] Yang Songlin: 然后
[01:35:56] Yang Songlin: 可能的话
[01:35:58] Yang Songlin: 能它现在
[01:35:59] Yang Songlin: 应该还是
[01:36:00] Yang Songlin: 张玉玄的那个
[01:36:01] Yang Songlin: Trytter的算法嘛
[01:36:02] Yang Songlin: 对
[01:36:03] Yang Songlin: 我相信大家都没有那么多
[01:36:06] Yang Songlin: 就是
[01:36:08] 可能有化
[01:36:09] Yang Songlin: 它是一个非常好时的
[01:36:11] Yang Songlin: 一个公众对它
[01:36:13] Yang Songlin: 就非常的
[01:36:15] Yang Songlin: 非常的需要时间
[01:36:16] Yang Songlin: 要慢慢磨
[01:36:17] Yang Songlin: 就要老师傅
[01:36:18] Yang Songlin: 可能有化
[01:36:19] Yang Songlin: 慢慢来打磨
[01:36:21] Yang Songlin: 对
[01:36:22] Yang Songlin: 我觉得就是
[01:36:23] Yang Songlin: Iquate的点在
[01:36:24] Yang Songlin: 叠在的时候
[01:36:25] Yang Songlin: 大家因为用Trytter写一下
[01:36:27] Yang Songlin: Trytter用
[01:36:28] Yang Songlin: 就行了嘛
[01:36:29] Yang Songlin: 然后如果它
[01:36:30] Yang Songlin: 验出来
[01:36:31] Yang Songlin: 有用的话
[01:36:32] Yang Songlin: 后面来補一些
[01:36:34] 扣大克勒
[01:36:35] Yang Songlin: 也是可以的嘛
[01:36:37] Yang Songlin: 对
[01:36:38] 就我所知它们
[01:36:39] Yang Songlin: 现在应该
[01:36:40] 还在用Trytter的
[01:36:41] Yang Songlin: 扣在讯法
[01:36:42] Yang Songlin: 对
[01:36:43] Yang Songlin: 后面会不会
[01:36:44] Yang Songlin: 找人来写扣大克呢
[01:36:45] 从硬件轻合的
[01:36:47] Zhang Xiaojun: 角度你觉得
[01:36:48] Zhang Xiaojun: 下一代的算法会怎么演进
[01:36:50] 现在我觉得
[01:36:52] Yang Songlin: 这音件也就
[01:36:54] Yang Songlin: 它跟
[01:36:55] Yang Songlin: Transformer它是有一点
[01:36:58] 鞋桶演进了
[01:37:00] Yang Songlin: 就是
[01:37:01] Yang Songlin: 硬件会变成
[01:37:02] Yang Songlin: Transformer更喜欢的模样
[01:37:04] Yang Songlin: 对
[01:37:05] Yang Songlin: 所以其实对于一些
[01:37:06] Yang Songlin: Trytter的题目来说是
[01:37:08] Yang Songlin: 有一些
[01:37:09] 不好的
[01:37:10] Yang Songlin: 那种
[01:37:11] Yang Songlin: 因素在里面的嘛
[01:37:12] Yang Songlin: 因为现在要加个
[01:37:13] Yang Songlin: 硬件
[01:37:14] 大家会发现
[01:37:15] Yang Songlin: 它就是为了去优化举真成嘛
[01:37:17] Yang Songlin: 然后让它举真成
[01:37:18] Yang Songlin: 越快越好嘛
[01:37:19] Yang Songlin: 因为Transformer
[01:37:20] Yang Songlin: 你们有大量的举真成嘛
[01:37:21] Yang Songlin: 它就像
[01:37:23] Yang Songlin: 硬件就像搞一些
[01:37:24] Yang Songlin: 快速的举真成的东西嘛
[01:37:26] Yang Songlin: 就像
[01:37:27] Yang Songlin: 像Tanthcore
[01:37:29] 然后像这种
[01:37:31] TMI
[01:37:33] Yang Songlin: 这种东西
[01:37:35] Yang Songlin: 然后像最近的 Blackwell上面
[01:37:36] Yang Songlin: 它有一些
[01:37:37] Yang Songlin: 专门针对这种举真成
[01:37:38] Yang Songlin: 它有一些
[01:37:40] 单独的那种
[01:37:42] Yang Songlin: 类传上面单独的那种
[01:37:43] Yang Songlin: Mimery嘛
[01:37:44] Yang Songlin: 就是都是来
[01:37:45] Yang Songlin: 优化举真成的嘛
[01:37:47] 所以可能
[01:37:48] Yang Songlin: 大家会看到
[01:37:50] Yang Songlin: FlyShotanthson会越来越快
[01:37:52] Yang Songlin: Fa4嘛
[01:37:53] Yang Songlin: 它会
[01:37:54] Yang Songlin: 在 Blackwell上面会越来越快
[01:37:56] Yang Songlin: 对
[01:37:57] Yang Songlin: 然后
[01:37:58] Yang Songlin: 我觉得
[01:38:00] Yang Songlin: 既然这个硬件是这么
[01:38:02] Yang Songlin: 一握手的嘛
[01:38:04] 那从
[01:38:06] Yang Songlin: 设计算法的走来看
[01:38:08] Yang Songlin: 那你就必须要设计一些
[01:38:09] Yang Songlin: 能有举真成法的算法
[01:38:11] Yang Songlin: 要不然你这个硬件
[01:38:13] Yang Songlin: 效率肯定是
[01:38:14] Yang Songlin: 跟不上的
[01:38:15] Yang Songlin: 想拎辆谈刪它创个算法
[01:38:17] Yang Songlin: 有个好处
[01:38:18] Yang Songlin: 就是
[01:38:19] Yang Songlin: 它基本上都是一些举真成
[01:38:21] Yang Songlin: 当然它还会有一些
[01:38:23] Yang Songlin: 其他的偶尔害的
[01:38:25] Yang Songlin: 对那这个的话
[01:38:26] Yang Songlin: 那可能就是
[01:38:28] 得
[01:38:29] Yang Songlin: 可费一下
[01:38:31] Yang Songlin: 对
[01:38:32] Yang Songlin: 它可能比方说在
[01:38:33] Yang Songlin: Training的时候可能还是
[01:38:35] Yang Songlin: 不如
[01:38:36] Yang Songlin: FlyShotanthson4
[01:38:37] Yang Songlin: 这种
[01:38:38] Yang Songlin: 在 Blackwell上面高效
[01:38:40] 但
[01:38:41] Yang Songlin: 其实也无所谓
[01:38:42] Yang Songlin: 就可能地方也不靠
[01:38:44] Yang Songlin: 训练效率
[01:38:45] Yang Songlin: 它是靠那种
[01:38:46] Yang Songlin: Inference效率
[01:38:47] Yang Songlin: 所以
[01:38:48] Yang Songlin: 我觉得是要训练的时候
[01:38:50] Yang Songlin: 就是能
[01:38:51] Yang Songlin: 能以
[01:38:52] Yang Songlin: Reason of the Suits
[01:38:53] Yang Songlin: 来训
[01:38:54] Yang Songlin: 然后
[01:38:55] Yang Songlin: Decoating快的话
[01:38:56] Yang Songlin: 这种效果其实
[01:38:57] Yang Songlin: 也是有市场的
[01:38:58] Yang Songlin: 对
[01:38:59] Yang Songlin: 然后另外的话
[01:39:00] Yang Songlin: 这边说
[01:39:01] Yang Songlin: 像
[01:39:02] 翻悬Moe
[01:39:05] Yang Songlin: 然后
[01:39:06] Spassal贪伤这种
[01:39:07] Yang Songlin: 降Flow
[01:39:08] Yang Songlin: 然后又能
[01:39:09] Yang Songlin: 用举真成发
[01:39:10] Yang Songlin: 他们都是
[01:39:11] Yang Songlin: 属于
[01:39:12] Yang Songlin: 这种类型
[01:39:13] Yang Songlin: 他们肯定
[01:39:14] Yang Songlin: 还是要用举真成发的
[01:39:15] Yang Songlin: 然后
[01:39:16] Yang Songlin: 就是想不然
[01:39:17] Yang Songlin: 把Flow
[01:39:19] Yang Songlin: 然后同为一些
[01:39:20] Yang Songlin: 算法的这种
[01:39:21] Yang Songlin: 创新
[01:39:22] Yang Songlin: 来
[01:39:23] Yang Songlin: 把Flow
[01:39:26] Yang Songlin: 打下去
[01:39:27] 然后同时
[01:39:28] Yang Songlin: 保证
[01:39:29] Yang Songlin: 然后这里面有
[01:39:30] Yang Songlin: 大家的举真成
[01:39:31] 这一类
[01:39:32] Yang Songlin: 算法里面
[01:39:33] Yang Songlin: 基本上都举真成
[01:39:34] 基本上
[01:39:35] Yang Songlin: 这个算法也
[01:39:36] Yang Songlin: 它的不要也停
[01:39:37] Yang Songlin: 相当的
[01:39:38] Yang Songlin: 还是挺好
[01:39:39] Yang Songlin: 优化的嘛
[01:39:40] Yang Songlin: 因为
[01:39:41] 因为我觉得
[01:39:42] Yang Songlin: 这个印象
[01:39:43] Yang Songlin: 就是笨诊
[01:39:44] Yang Songlin: 往举真成发
[01:39:45] Yang Songlin: 越来越快的方向
[01:39:47] Yang Songlin: 再走了
[01:39:48] 甚至说
[01:39:49] Yang Songlin: 像
[01:39:50] Yang Songlin: Face
[01:39:52] Yang Songlin: 举真成
[01:39:53] Yang Songlin: 太快了
[01:39:54] Yang Songlin: 导致
[01:39:55] Yang Songlin: 那一首
[01:39:56] Yang Songlin: Math
[01:39:57] Yang Songlin: Folens
[01:39:58] Yang Songlin: 某块的
[01:39:59] Yang Songlin: 变成一个
[01:40:00] Yang Songlin: 平静
[01:40:01] Yang Songlin: 然后
[01:40:02] Yang Songlin: 他们就用一些
[01:40:03] Yang Songlin: 的话
[01:40:04] Yang Songlin: 他就用一些
[01:40:05] Yang Songlin: Approxy
[01:40:06] Yang Songlin: 方法
[01:40:07] Yang Songlin: 来做
[01:40:08] Yang Songlin: EXP
[01:40:09] Yang Songlin: 这个也挺
[01:40:11] Yang Songlin: 挺好笑的
[01:40:12] Yang Songlin: 举真成
[01:40:14] Yang Songlin: 太快了
[01:40:15] Yang Songlin: 我们
[01:40:16] Yang Songlin: 现在还是要去
[01:40:18] 经常去
[01:40:19] Yang Songlin: 利用举真成
[01:40:20] Yang Songlin: 快速的这个
[01:40:21] Yang Songlin: 性质
[01:40:22] Yang Songlin: 然后是在一些
[01:40:23] Yang Songlin: 生活
[01:40:24] 我觉得
[01:40:25] Yang Songlin: 像Divisic
[01:40:26] Yang Songlin: Tanthan
[01:40:27] Yang Songlin: 他那个
[01:40:28] Yang Songlin: 就已经用到了
[01:40:29] Yang Songlin: 这种性质
[01:40:30] Yang Songlin: 我觉得Divisic
[01:40:31] 他是一个
[01:40:32] Yang Songlin: 非常出重
[01:40:33] Yang Songlin: 这种
[01:40:34] Yang Songlin: 硬件和算法
[01:40:35] Yang Songlin: 鞋桶
[01:40:36] Yang Songlin: 设计的
[01:40:37] Yang Songlin: 一个公司
[01:40:38] Yang Songlin: 像Divis
[01:40:39] Yang Songlin: Spassal
[01:40:40] Tanthan的话
[01:40:41] Yang Songlin: 他会有一个
[01:40:42] Yang Songlin: 那个
[01:40:43] Yang Songlin: 他就是
[01:40:44] Yang Songlin: Fp8
[01:40:45] Yang Songlin: 来
[01:40:46] 做这个
[01:40:47] Yang Songlin: 算这个
[01:40:48] Yang Songlin: Tanthan
[01:40:49] 他不需要
[01:40:50] Yang Songlin: Softmax
[01:40:51] Yang Songlin: 他只需要
[01:40:52] Yang Songlin: 算那个
[01:40:53] Yang Songlin: Loget
[01:40:54] Yang Songlin: 然后来做
[01:40:55] Tanthan
[01:40:56] Yang Songlin: 可以来选Score吗
[01:40:57] Yang Songlin: 所以首先
[01:40:58] Yang Songlin: 他就是
[01:40:59] Yang Songlin: Fp8
[01:41:00] Yang Songlin: 然后他
[01:41:01] Yang Songlin: 又可以
[01:41:02] Yang Songlin: 把那个
[01:41:03] Yang Songlin: 昂贵的
[01:41:04] Yang Songlin: ExpoNanShow
[01:41:05] Yang Songlin: 的那个
[01:41:06] Yang Songlin: 操作
[01:41:07] Yang Songlin: 把它去掉
[01:41:08] Yang Songlin: 这样的话
[01:41:09] Yang Songlin: 他就是
[01:41:10] Yang Songlin: 基本上就是
[01:41:11] Yang Songlin: 一大堆举真成
[01:41:12] Yang Songlin: 然后他没
[01:41:13] Yang Songlin: 所以说
[01:41:14] Yang Songlin: 他那个
[01:41:15] Yang Songlin: 他那个
[01:41:16] Yang Songlin: Dex
[01:41:17] 的话
[01:41:18] Yang Songlin: 作作
[01:41:19] Yang Songlin: 作作
[01:41:20] Yang Songlin: 作作
[01:41:21] Yang Songlin: 作作
[01:41:22] Yang Songlin: 作作
[01:41:23] Yang Songlin: 你只有有可能可以作為一個下一代加個的一個CANY date的嗎
[01:41:27] Yang Songlin: 對
[01:41:29] 相對來說
[01:41:30] Zhang Xiaojun: DipSek和KIMIN的一個在硬件傾合上做得很好
[01:41:32] Zhang Xiaojun: 聽起來是KIMIN的
[01:41:34] Zhang Xiaojun: DipSek
[01:41:36] Yang Songlin: OK
[01:41:37] 因為沒有把這個做一個重要的有好目標
[01:41:40] Zhang Xiaojun: 不太確定
[01:41:42] Yang Songlin: 我覺得KIMIN肯定還是SKERRUP的這種硬件上面的東西嗎
[01:41:48] Yang Songlin: 但是沒有DipSek那麼追求吧
[01:41:50] Yang Songlin: 對
[01:41:51] Yang Songlin: DipSek我覺得他們非常追求這種
[01:41:54] Yang Songlin: 比如說這個SAN版的MUNDAF P8上面跑呀這種之類的
[01:41:59] Yang Songlin: 我覺得他們Infer應該在他們算法
[01:42:02] Yang Songlin: 跌在的過程中應該換以前會比較高一點
[01:42:05] Yang Songlin: 我覺得這個都是就是
[01:42:08] 英國公司而已了吧
[01:42:09] Yang Songlin: 就有些公司他Infer的話語權會高一些
[01:42:12] Yang Songlin: 就一些公司他算法的換以前會高一些
[01:42:15] Yang Songlin: 感覺SAN法就今天會高一些讓Infer不闖的東西出來
[01:42:19] Yang Songlin: 對
[01:42:21] 你覺得如果年輕的研究者想要進入
[01:42:24] Zhang Xiaojun: 諸麗基之或者架構算法這些領域的話
[01:42:27] Zhang Xiaojun: 你對他沒有什麼建議
[01:42:28] Zhang Xiaojun: 他應該是從哪些地方還是入手
[01:42:30] Zhang Xiaojun: 現在的話
[01:42:31] Zhang Xiaojun: 現在的話
[01:42:32] 找個公司去實習
[01:42:36] OK
[01:42:36] 就是跟他
[01:42:37] Zhang Xiaojun: 因為我覺得
[01:42:38] Zhang Xiaojun: 因為我覺得做架構必須要算你
[01:42:41] Yang Songlin: 沒有算你就沒法做架構
[01:42:43] Yang Songlin: 所以我覺得
[01:42:45] Yang Songlin: 還是先找個Lib去實習吧
[01:42:48] Yang Songlin: 對
[01:42:51] 好了
[01:42:52] 今天的節目就是這樣
[01:42:54] 這裡是商業訪談錄
[01:42:56] 是一檔由語言及世界工作室出品的
[01:42:59] Zhang Xiaojun: 深度訪談節目
[01:43:00] Zhang Xiaojun: 你可以到公眾號關注我們的工作室
[01:43:02] Zhang Xiaojun: 或取更多的信息
[01:43:04] Zhang Xiaojun: 我們的公眾號是語言及世界
[01:43:06] Zhang Xiaojun: Language is world
[01:43:08] Zhang Xiaojun: 我們希望和你一起
[01:43:10] Zhang Xiaojun: 從這裡探索新的世界
[01:43:13] 我們希望和你一起
[01:43:15] Zhang Xiaojun: 從這裡探索新的世界
[01:43:20] Language is world