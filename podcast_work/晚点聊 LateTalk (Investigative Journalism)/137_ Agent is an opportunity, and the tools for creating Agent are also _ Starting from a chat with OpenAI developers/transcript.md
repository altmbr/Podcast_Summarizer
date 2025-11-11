# 137: Agent is an opportunity, and the tools for creating Agent are also | Starting from a chat with OpenAI developers

**Podcast:** 晚点聊 LateTalk (Investigative Journalism)
**Date:** 2025-10-16
**Video ID:** 68f1727052f01d1dd2a00523
**Video URL:** https://www.xiaoyuzhoufm.com/episode/68f1727052f01d1dd2a00523

---

[00:00:00] CAD GPT 的最主目標是VCAD GPT
[00:00:06] 比如說噴愛現在內部成立了一個新的叫做Future of Work的一個Team
[00:00:12] Henry In: 開始就是加所有AI的各種商業場景下面的落地
[00:00:16] 我覺得一個批評的聲音就是這次Agent Builder 其實就是和AGI的這個路線可能是有分歧的
[00:00:25] 歡迎收聽晚點聊 我是曼琪
[00:00:28] Manqi: 今天我邀請了兩位常駐規股的朋友AGI House 的合夥人
[00:00:31] Manqi: Henry In 和NawMisha 來一起聊Agent 工具鏈的發展趨勢和這個領域在美國的創業事件
[00:00:38] Manqi: 我們第一次錄製是在11之前而不久前的10月6日
[00:00:42] Manqi: 噴愛舉辦了第三次Dabday及開發走日
[00:00:45] Manqi: 發布了一系列與Agent 相關的新工具
[00:00:48] Manqi: 包括Agentic Kit New Evils 也就是新的一套評估工具
[00:00:53] Manqi: 這次噴愛也帶來了Apps in Chad GPT 和Apps SDK
[00:00:57] Manqi: 這是 Chad GPT 試圖變成操作系統的再一次嘗試
[00:01:01] Manqi: 所以本期節目也是分為兩部分
[00:01:03] Manqi: 前面我們討論了剛結束的開發走日的一些亮點
[00:01:06] Manqi: 第二部分則是對Agentic Tooling 及Agent 工具鏈的發展賣落和當前熱門環節的一些梳理
[00:01:13] Manqi: 兩部分有一些呼應
[00:01:14] Manqi: 比如在Dabday之前我們就重點討論了Evils G Evilsation 評估這個環節
[00:01:20] Manqi: 這也是 Open i 次次的更新之一
[00:01:22] Manqi: 下面我們正式進入節目吧
[00:01:27] 兩位可以和我們的聽游簡單打一個招呼 做介紹一下
[00:01:30] Manqi: 謝謝半天要請 大家好 我是Henry
[00:01:33] Henry In: 我是AJ House的聯合創始人間CTO
[00:01:36] Henry In: 我之前本科的時候畢業與清華搖搬 後來來Burgleetube
[00:01:40] Henry In: 研究方向是AI系統和重序分析
[00:01:43] Henry In: 讀到第三點的時候 我選擇了初學創業
[00:01:46] Henry In: 做了我第一家公司叫做司馬義 專注是用AI來提升開發者效率
[00:01:51] Henry In: 然後做工具的那幾年 讓我對於Agent的開發工作流
[00:01:55] Henry In: 還有開發者的生態有了比較直接的提感
[00:01:58] Henry In: 在AJ House 我們拒絕了一群頂尖的AI創業者和研究者
[00:02:03] Henry In: 包括像Open AI 扣放的Andrick Apathy
[00:02:06] Henry In: 像Google的創始人Suggibre and Shouji Keiya Jeff Ding
[00:02:10] Henry In: 還有Anthropic的聯合創始人Bangmei
[00:02:12] Henry In: 然後通過構建這個社區的過程讓我更早和更深的看到了
[00:02:16] Henry In: JayBoer AI的演化流程 尤其是從模型到應用
[00:02:21] Henry In: 然後再到如今Agent工具鏈的爆發
[00:02:24] Henry In: 所以目前的話我會更多的專注與思考和投資
[00:02:27] Henry In: Agent的方向的工具層和應用層
[00:02:29] Henry In: 非常高興今天有機會和大家分享一下我們看到的一些興趣式
[00:02:33] Henry In: 和一些有意識的新項目
[00:02:34] Henry In: 哈囉大家好 我是Nelmi
[00:02:36] Nawmisha: 然後之前是在我總上學院畢業之後
[00:02:39] Nawmisha: 就加入了GPMorgan的究竟山班公司
[00:02:41] Nawmisha: 然後主要是他第一個Hair for our AI的主要負責的這個Tim
[00:02:46] Nawmisha: 然後之前也負責早期投資
[00:02:48] Nawmisha: 然後也負責一些大型的公司的一些方Raging
[00:02:52] Nawmisha: 就是融資的項目比如說OPEN AI的方Raging
[00:02:54] Nawmisha: 也之前是我在負責
[00:02:56] Nawmisha: 然後現在就是加入了Agent
[00:02:58] Nawmisha: 要負責他早期投資的業務
[00:03:00] Nawmisha: 然後現在也已經投資了大概20多家公司
[00:03:03] Nawmisha: 然後包括Compose,Cautisha,Laptop, and Lama Index
[00:03:07] Nawmisha: 然後今天我們也會比較深的聊到其中的幾家公司
[00:03:11] Nawmisha: 接下來的一部分是我和Hair for our AI
[00:03:13] Manqi: 在10月6號之後補充了了OPEN AI開發者日的一些新的進展
[00:03:18] Manqi: 包括這個Agent的工具是有什麼構成的對創業生態的可能的影響
[00:03:23] Manqi: 以及從GPS到這一次的Apps in Chat Gpt
[00:03:27] Manqi: OPEN AI是怎麼試圖去變成一個操作系統的
[00:03:33] 10月6號的時候OPEN AI
[00:03:35] Manqi: 它辦了第三屆的開發者日
[00:03:37] 有很多發布其中有一個比較重貓的發布
[00:03:39] Manqi: 就是Agentique Keat
[00:03:41] Manqi: 這個和我們節前就是在討論的Agentique tooling的趨勢是很相關的
[00:03:45] Manqi: 所以正好趁這個機會我們可以補充再聊一聊
[00:03:47] Manqi: 包括我們也可以延展的了一下就是OPEN AI10月6號的整個
[00:03:51] Manqi: 是它第三次辦David的開發者日
[00:03:54] Manqi: 它有些什麼樣的進展和動作
[00:03:56] Manqi: 我們可以先從Agentique Keat
[00:03:59] Manqi: 就它這個跟Agent打造相關的一套工具開始聊
[00:04:03] Manqi: 我覺得這次發布Agentique
[00:04:05] Henry In: 給我的感覺其實是OPEN AI自己練出了一生武功
[00:04:09] Henry In: 然後現在想把他傳售給廣大的開發者
[00:04:11] Henry In: 這個Agentique這次涵蓋了整個Agent的開發的生命周期
[00:04:16] Henry In: 首先是從構建Agent的開始
[00:04:18] Henry In: 那麼它這次出了一個叫做Agent Builder
[00:04:21] Henry In: 實際上就是一個視覺化
[00:04:23] Henry In: 通過拖捉了這些小封塊
[00:04:26] Henry In: 然後能夠構建Agent的一個快速的一個方式
[00:04:29] Henry In: 發布的時候這個現場也有一個就是
[00:04:32] Henry In: 8分鐘以內的一個Christina做了一個Demo
[00:04:35] Henry In: 就是很快速的通過拖捉拉
[00:04:37] Henry In: 然後從零開始完成一個Production級別的Agent
[00:04:41] Henry In: 還是非常好用的
[00:04:42] Henry In: 然後第二個部分的話就是
[00:04:44] Henry In: 你 Builder好了Agent的以後
[00:04:46] Henry In: 你需要把它不屬給客戶
[00:04:48] Henry In: 那這次的話他們推出了這個ChapKit
[00:04:50] Henry In: ChapKit主要的一個就是前端的問題
[00:04:53] Henry In: 終於有了一個前端U1的SK
[00:04:56] Henry In: 然後可以很容易地去把這些ChapKit的component
[00:04:59] Henry In: 引拜得到比個Chad.pt
[00:05:02] Henry In: Chad.pt一個生態裡面
[00:05:04] Henry In: 這個也是對於用戶體驗
[00:05:06] Henry In: 非常重要的一件事情
[00:05:07] Henry In: 最後的話就是當你不屬給用戶以後
[00:05:10] Henry In: 那你需要去持續地去監控去評估
[00:05:13] Henry In: 然後以及優化
[00:05:14] Henry In: 所以這塊的話他們在E-VALS上面
[00:05:17] Henry In: 除了好幾個新功能
[00:05:19] Henry In: 包括就是 DataSets
[00:05:21] Henry In: 包括TraceGrading
[00:05:22] Henry In: 然後包括自動化的這個Proud優化
[00:05:25] Henry In: 然後以及後續真正去改進這個模型
[00:05:29] Henry In: 那麼就是他們新功能就是Reinforcement Fine tuning
[00:05:32] Henry In: 所以整個相當於流程都討通了
[00:05:35] Henry In: 這個對開發者來說還是一個非常
[00:05:37] Henry In: 非常 exciting的事情
[00:05:39] Manqi: 比如說他最開始做的這個
[00:05:41] Manqi: 造的這個部分就Beauter那個部分
[00:05:43] Manqi: 他是不是有點像
[00:05:44] Manqi: 之前的Define還有自己做的Code
[00:05:46] 我覺得其實是非常類似的
[00:05:48] Henry In: 這也是為什麼有一些人可能對這次發布
[00:05:50] Henry In: 可能會比較失望
[00:05:51] Henry In: 因為感覺這已經是一個
[00:05:53] Henry In: 非常成熟的市場
[00:05:54] Henry In: 那麼Apply的話呢
[00:05:55] Henry In: 只是他們自己也可能確實在一些細節方面
[00:05:58] Henry In: UIUIX做比較好
[00:06:00] Henry In: 但是可能確實並沒有說和Define
[00:06:03] Henry In: 或者N8N或者Zappier
[00:06:05] Henry In: 做出足夠度的差異化
[00:06:06] Henry In: 所以他的那個核心邏輯也是一個workflow
[00:06:09] Manqi: 就是他有一個工作流
[00:06:10] Manqi: 然後你去突突在座
[00:06:12] Manqi: 做成那個工作流
[00:06:13] Manqi: 然後變成一個Agent
[00:06:14] Manqi: 對比如說Demo的時候
[00:06:16] Henry In: 他第一步就是先做了一個classifier
[00:06:18] Henry In: 把這個Proud分一個類
[00:06:20] Henry In: 然後有一個Eathhouse
[00:06:21] Henry In: 後面接一個Eathhouse
[00:06:23] Henry In: 如果是Eath的話
[00:06:24] Henry In: Code一個Agent
[00:06:25] Henry In: 如果是EathCode另外一個Agent
[00:06:26] Henry In: 所以其實是一個完全人類手工
[00:06:29] Henry In: 來Craft這種工作流的一個形式
[00:06:31] Henry In: 然後我覺得你剛說第三部分
[00:06:33] Manqi: 就是這個持續優化的部分
[00:06:35] Manqi: 它像了一些評估的功能
[00:06:36] Manqi: 這個和我們上次聊的
[00:06:38] Manqi: 也挺相關的
[00:06:39] Manqi: 因為我們上次聊了
[00:06:40] Manqi: 有一些公司他首先是專門做這個
[00:06:42] 同時Open i就前段時間
[00:06:43] Manqi: 也有一個收購
[00:06:44] Manqi: 他11億美元收了一個公司叫SatSea
[00:06:47] Manqi: 那個公司做的
[00:06:48] Manqi: 也是一些相關的事
[00:06:50] Manqi: 這個大家也可以聽我們後面的內容
[00:06:52] Manqi: 這個我們有詳細展開來聊
[00:06:54] Henry In: 那麼這個事情的話
[00:06:55] Henry In: 我之前覺得是某一些Agent公司
[00:06:58] Henry In: 他們的護成和
[00:06:59] Henry In: 使得他們的Agent比別的公司更好
[00:07:01] Henry In: 但現在來看的話
[00:07:02] Henry In: 就是這些東西會逐漸的標準化
[00:07:04] Henry In: 想要拍IceNet就推出了
[00:07:06] Henry In: 就是Datacet Trace Grading和Reference 1.5.0
[00:07:09] Henry In: 聯合起來一起用的話
[00:07:10] Henry In: 我覺得可能會產生類似的效果
[00:07:12] Henry In: Trace Grading你可以解釋一下
[00:07:14] Manqi: 就是它具體是做什麼樣的
[00:07:16] Manqi: 一個Trace就是一次完整
[00:07:18] Henry In: 用戶和Agent交互的流程
[00:07:20] Henry In: 比如說用戶想讓Booking.com幫助它去
[00:07:23] Henry In: 訂一張機票
[00:07:25] Henry In: 那麼從用戶開始表達說
[00:07:27] Henry In: 我從哪年哪月
[00:07:28] Henry In: 哪日從那個城市飛到哪開始
[00:07:30] Henry In: 到最後完成
[00:07:31] Henry In: 這是訂票或者訂票失敗
[00:07:33] Henry In: 結束是一個Trace
[00:07:35] Henry In: 然後這個Trace Grading就是
[00:07:37] Henry In: 通過比如說寫一個Grading韓數
[00:07:41] Henry In: 然後能夠去判斷
[00:07:43] Henry In: 就是這一次和用戶和Agent的交互
[00:07:46] Henry In: 哪裡做得好
[00:07:47] Henry In: 哪裡做得不好
[00:07:48] Henry In: 然後可以給它大一些Label
[00:07:49] Henry In: 大一些分數
[00:07:50] Henry In: 所以這個現在是用韓數實現的
[00:07:52] Manqi: 不需要用模型來去給它大分什麼
[00:07:55] Manqi: 這個中間是可以用模型的
[00:07:57] Henry In: 這個是用戶來決定的
[00:07:59] Henry In: 如果要是你不需要模型就能大分的話
[00:08:01] Henry In: 那更簡單
[00:08:02] Henry In: 但是它是可以用RMS照出來大分的
[00:08:05] Henry In: 你剛才就提到它這個東西發了之後
[00:08:07] Manqi: 就有一種反饋是覺得這個比較失望
[00:08:10] Manqi: 那有什麼比較好的反饋嗎
[00:08:12] Henry In: 我覺得我身邊歸股很多朋友
[00:08:15] Henry In: 其實他們自己平時都是
[00:08:17] Henry In: 比如說Codexia來Build A整
[00:08:21] Henry In: 所以這種托拉拽的形式
[00:08:22] Henry In: 可能對他們的這個工作流的改變並不大
[00:08:26] Henry In: 但我覺得可能會對於很多企業裡面
[00:08:29] Henry In: 可能平時不是用CodeCode
[00:08:31] Henry In: 或者說不是那麼tech-cnico的這些工作人員的話
[00:08:34] Henry In: 會有表達的意義
[00:08:36] Henry In: 突夜無人員的對吧
[00:08:37] Manqi: 因為我看它這次確實
[00:08:38] Manqi: 它也找了一些公司來給它
[00:08:39] Manqi: 合作站台吧算是
[00:08:40] Manqi: 都是一些還表大的公司
[00:08:42] Manqi: Canva Figma之類的
[00:08:43] Manqi: 對我覺得這次他們和前兩年GVT-S
[00:08:47] Henry In: 做得比較好的一個點
[00:08:49] Henry In: 就是在於可能這次有更多的Lunching partner
[00:08:54] Henry In: 就更多更好的這個出使的應用
[00:08:56] Henry In: 能夠把這個應用的包耳拉的稍微高一點
[00:08:58] Henry In: 因為要不然的話
[00:08:59] Henry In: 就可能會出現兩年前GVT雷售大於點小
[00:09:02] Henry In: 最後大量的GVTStore裡面的GVT
[00:09:04] Henry In: 都質量比較低下的準期況
[00:09:06] Henry In: 這個本來也是我想問的
[00:09:08] Manqi: 因為它23年就是它第一次開這個開發者日的時候
[00:09:11] Manqi: 它當時推了一個市場還挺關注的東西
[00:09:13] Manqi: 就你剛剛說的GVT-S還有CHIGPTStore
[00:09:16] Manqi: 就那會大家想像中它
[00:09:18] Manqi: 像就是說大家可以在CHIGPT上
[00:09:21] Manqi: 把它做一個平台我們去開發不同的應用
[00:09:24] Manqi: 但實際上這個後面發展的不是特別成功
[00:09:27] Manqi: 就它不算一個很繁榮的生態
[00:09:29] Manqi: 你就覺得這一次它會有什麼不一樣嗎
[00:09:31] Manqi: 我覺得這次變化還是比較大的
[00:09:33] Henry In: 其實就是CHIGPT作為一個操作系統這個事情
[00:09:37] Henry In: 已經不是第一次害怕了
[00:09:39] Henry In: 真正的第一次害怕就是兩年前
[00:09:42] Henry In: 他們浪費GVTCASMGVTStore的時候
[00:09:45] Henry In: 然後那個時候的話
[00:09:47] Henry In: 我覺得它的主要問題在於首先這些GVT
[00:09:50] Henry In: 它最後大部分都變成了一個
[00:09:54] 就是Prompt的一個模板加上一顆自定義的logo
[00:09:58] Henry In: 原因是在於這些GVT他們不能就是比較可靠的
[00:10:03] Henry In: 比如說去調用第三方的服務
[00:10:05] Henry In: 然後他們也不能存儲狀態
[00:10:07] Henry In: 然後他們也不能比如說發送通知
[00:10:10] Henry In: 也不能去亂一些工作流
[00:10:12] Henry In: 從這些事情都是上一代做不了的
[00:10:14] Henry In: 那麼這一次的話我覺得真正有了這些AgentKity
[00:10:18] Henry In: 然後Apps and CHIGPT and Agenus App SDK
[00:10:21] Henry In: 現在有一個真正的平台了
[00:10:23] Henry In: 而不是只是一個就是Prompt包裝
[00:10:26] Henry In: 比如說Apps and SDK
[00:10:29] Henry In: 提供了真正的All-All-Style的這種授權
[00:10:33] Henry In: 然後它也可以去調用App的工具
[00:10:35] Henry In: 然後它也有了EVL
[00:10:37] Henry In: 也有了Versioning
[00:10:39] Henry In: 包括它這個City提供的EY的Building Blocks
[00:10:42] Henry In: 現在當於是給開發者提供了
[00:10:44] 構建一個完整應用體驗的所有工具箱
[00:10:48] Henry In: 所以我比較期待這次真正的Apps和生態能夠做起來
[00:10:53] 有什麼你印象比較深的就有出什麼應用嗎
[00:10:55] Henry In: 其實可以對比一下Kamba
[00:10:57] Henry In: 兩年前和Kamba這一次的應用
[00:11:00] Henry In: 其實我的應用體驗就好了不少
[00:11:02] Henry In: 這個是比較能對比的
[00:11:04] Henry In: 像其他的一些不均檔抗可能是新做出來的
[00:11:08] Henry In: 我覺得Kamba的話可能之前和現在可能現在是UiGo好一點
[00:11:12] Henry In: 但之前的話它也能夠就是給你生存一張圖
[00:11:16] Henry In: 但現在的話它會直接和你的Kamba帳號
[00:11:19] Henry In: 去做一個綁定和一個授權
[00:11:22] Henry In: 然後把你之前的Kamba這些帳號裡面的信息
[00:11:24] Henry In: 就是用到你這次的生存中
[00:11:27] Henry In: 這個是一個點
[00:11:28] Henry In: 另外的話就是我覺得兩年前可能像Kamba
[00:11:31] Henry In: 這樣的比較高質量的GPT-S是非常少的
[00:11:35] Henry In: 它雖然發布的時候說GPT-S它可以去調用外部的服務
[00:11:39] Henry In: 然後獨居外部的數據庫
[00:11:41] Henry In: 但其實大部分的GPT它都本質上做是一個propt
[00:11:45] Henry In: 那麼除了會出現非常良用不齊的這些應用的情況
[00:11:49] Henry In: 那這次的話我覺得這工具鏈的成熟
[00:11:52] Henry In: 會使得可能廣大的開發者們
[00:11:54] Henry In: 都能夠在不費太多時間和經驗情況下
[00:11:57] Henry In: 能夠開發出的質量上面和這些浪質的合作夥伴
[00:12:01] Henry In: 像Kamba統統質量或者說更好的這些應用
[00:12:05] Manqi: 你剛才講的就是你覺得這一次和二三年那一次的不同
[00:12:08] Manqi: 也是講到就是Apps in Chagetay還有Apps SDK
[00:12:11] Manqi: 這個也是他們這一次的表重爆的
[00:12:13] Manqi: 因為在Multima一上來就是先發的Apps SDK
[00:12:16] Manqi: 包括後面就是這個活動結束之後
[00:12:19] Manqi: Chagetay的負責人NikChulin它是接受了美國媒體的一些採訪
[00:12:23] Manqi: 它自己直接說了它說Chagetay是有錢
[00:12:26] Manqi: 你變成一個操作系統的
[00:12:28] Manqi: 那可以把這部分也延展的講不講
[00:12:30] Manqi: 就比如說Apps in Chagetay
[00:12:33] Manqi: 它都是一些什麼東西
[00:12:35] Manqi: 比如開發者可以怎麼用起來
[00:12:36] Manqi: 我覺得這個事情其實非常好理解
[00:12:38] Henry In: 它本身上的類比之前我們LS的這個SK
[00:12:41] Henry In: 這次的Apps SDK它其實是基於MCP協議構建的
[00:12:45] Henry In: 它除了MCP提供這些第三方的服務以外
[00:12:49] Henry In: 它還加上了EY的元素
[00:12:51] Henry In: 就是除了文字回覆
[00:12:53] Henry In: 現在還可以展示一個Intoactive交互式的組件
[00:12:58] Henry In: 然後來呈現一個類似原生App的這麼一種用不體
[00:13:02] Henry In: 全部都發生了Chagetay令
[00:13:04] Henry In: 所以我覺得這個是這次Apps SDK比較厲害的地方
[00:13:09] Henry In: 我覺得它對於現在這些應用的開發者來說
[00:13:13] Henry In: 最大的這個意義就是這個分發的這個紅利
[00:13:16] Henry In: 對吧因為這次也公布現在Chagetay
[00:13:19] Henry In: 它們大概有8億的周活
[00:13:21] Henry In: 那麼現在你只要比一個一個好的Apps在Chagetay裡面的話
[00:13:27] Henry In: 一下可能就會比如說把你的這個應用帶給大量的這個用戶
[00:13:33] Henry In: 然後你就不需要再去解決這些濃稽動的一些問題
[00:13:37] Henry In: 我覺得還會比比較大的還是覺得一個新人比數的問題
[00:13:40] Henry In: 比如說你要出唐公司去服務一些
[00:13:42] Henry In: 比較在乎安全和歸的這些企業
[00:13:45] Henry In: 那麼現在通過了有這麼一個Chagetay這個平台
[00:13:48] Henry In: 可能更容易讓這些出唐企業
[00:13:50] Henry In: 接入到這些安德佩斯的這些客戶的流程中去
[00:13:54] Henry In: 所以其實它相比二三年有兩個點
[00:13:57] Manqi: 由就是剛才我們已經提到的
[00:13:58] Manqi: 它在技術上它以前可能就是你只能高高Prompt的模板
[00:14:01] Manqi: 現在是可以做一個完整的應用
[00:14:03] Manqi: 另外一個就是你剛剛說的其實在分發或者說你的商業處達上
[00:14:07] Manqi: Chagetay已經有這麼多的用戶了
[00:14:09] Manqi: 它其實是可以給開發者更直接的激力的
[00:14:12] Manqi: 對
[00:14:13] Henry In: 就你可以幫他們賺錢說白了
[00:14:15] Manqi: 對 因為上次兩年前的話
[00:14:17] Henry In: 是說其實最後可能也沒有幾家真正從那裡賺到錢
[00:14:20] Henry In: 但我覺得這次應該是會有一些變化的
[00:14:23] Henry In: 對不過我看它的那個部落客戶發布會
[00:14:25] Manqi: 就是到底怎麼賺錢這個事
[00:14:27] Manqi: 我覺得它也說得比較模糊
[00:14:28] Manqi: 比如說像具體的怎麼分成什麼的或者廣告什麼的
[00:14:31] Manqi: 它現在這個還是比較模糊的
[00:14:33] Henry In: 對 現在應該還處於實驗期
[00:14:34] Henry In: 但我覺得未來可能就比如說抽百分之三十這種模式
[00:14:38] Henry In: ILS應該是抽百分之三十如果沒有記錯的話
[00:14:41] Henry In: 我們想像一下現在就是軟件市場的百分之三十
[00:14:45] Henry In: 應該還是一個很大的一個病
[00:14:47] Manqi: 你覺得為什麼 OpenI在這個時間點開始
[00:14:49] Manqi: 在開發者市場有更多動作
[00:14:51] Manqi: 我覺得我平時可能看到比較多的是
[00:14:53] Manqi: OpenI在凸C上是更激進的
[00:14:56] Manqi: 然後像Google和Andsarpie可能在凸B上是更激進的
[00:14:59] Manqi: 包括二四年當時有一個數據嗎
[00:15:01] Manqi: 是說Andsarpie其實是搶了不少 OpenI凸B的一些份額
[00:15:05] Manqi: 我覺得OpenI是不會放棄凸B的
[00:15:07] Henry In: 然後這次這個動作的話可能有幾方面的原因
[00:15:10] Henry In: 一方面是用戶規模
[00:15:11] Henry In: 就Tiger GT8E的周活已經是操作系統級別的用戶入口
[00:15:16] Henry In: 然後其次的話我覺得也有生態上面的壓力
[00:15:18] Henry In: 像OpenI被Google都是瘋狂的往安德Price
[00:15:21] Henry In: 還有開發者上面去推
[00:15:24] Henry In: 我覺得OpenI的話肯定不會以後侄靠這個凸C的
[00:15:28] Henry In: 這個我們也能從OpenI內部團隊的變化看見
[00:15:32] Henry In: 比如說OpenI現在內部成立了一個新的叫做
[00:15:34] Henry In: Future of Work的一個Team
[00:15:36] Henry In: 開始就是加速AI的各種商業場景下面的落地
[00:15:40] Henry In: 比如說克服比如說合同的這個聖合
[00:15:45] Henry In: 比如說數據分析
[00:15:47] Henry In: 比如說商業線索的轉化
[00:15:50] Henry In: 像這些他們都在自己內部做
[00:15:52] Henry In: OpenI在自己的頻道上面也發布了一系列
[00:15:55] Henry In: 就是OpenAI
[00:15:56] Henry In: OpenAI的這個視頻大家可以去看一下
[00:15:58] Henry In: 大概覆蓋了跟他我說的那幾個場景
[00:16:01] Henry In: 就是用OpenI自己的AI的這些能力
[00:16:04] Henry In: 去相當於這些B2B的這個全流程
[00:16:09] Henry In: 包括就是你去做銷售
[00:16:11] Henry In: 然後去賣單
[00:16:13] Henry In: 然後包括你後面去做這個克服
[00:16:15] Henry In: 做Custom Success
[00:16:17] Henry In: 所有東西用AI來做OpenI自己在那做了一遍
[00:16:20] Henry In: 所以他在B2的這些AZN的過程中
[00:16:23] Henry In: 這些經驗我覺得他們把他們轉化成了
[00:16:26] Henry In: AZN的Kit
[00:16:27] Henry In: 現在把它分散給其他的這些開放者
[00:16:29] Henry In: 可以舉一個例子
[00:16:31] Henry In: 就是他們做商業線索轉化
[00:16:34] Henry In: OpenI的話每個月現在大概有1萬3000個
[00:16:38] Henry In: 就是陰棒的這種銷售的線索
[00:16:41] Henry In: 那麼他們之前的話人力可能只能比如說
[00:16:44] Henry In: 對其中的1000個提供相對比較
[00:16:47] Henry In: 個性化的這種回復
[00:16:50] Henry In: 那麼現在的話有了AI以後
[00:16:52] Henry In: 他們這個效率就大幅度的提升了
[00:16:54] Henry In: 然後另外的話比如說克服
[00:16:55] Henry In: 現在比如說所有的這個Chachyp的這些克服
[00:16:58] Henry In: 都是AI來Power
[00:17:00] Henry In: 那麼這個AI的話它就會和他們內部的這個知識庫
[00:17:04] Henry In: 以及他們的這個政策庫
[00:17:06] Henry In: 去交互然後服用庫
[00:17:08] Henry In: 同時的話他們在這個服的過程中
[00:17:10] Henry In: 他們也在不斷做這個EVL
[00:17:12] Henry In: 現在不斷做這個改進
[00:17:14] Henry In: 所以他們其實這個AZN的這些TraceGrading的結果
[00:17:17] Henry In: 可能反過來會反躲他們的知識庫
[00:17:20] Henry In: 和他們的這個政策庫
[00:17:22] Henry In: 所以我覺得他們自己build了AZN多了
[00:17:24] Henry In: 他們自然而然他們的工具也打蒙都更好了
[00:17:27] Henry In: 所以最後就是呈現出來的形式就是這麼一個AZN Kit
[00:17:31] Henry In: 然後給我們所有的開發者
[00:17:33] Manqi: 就是你開頭說的它練了一生五功
[00:17:35] Manqi: 然後放出來給大家用
[00:17:37] 然後你剛剛說第一個原因
[00:17:38] Manqi: 就是你說它不會放棄這個Tubi
[00:17:40] Manqi: 和Tubi開發者的圖企業的市場
[00:17:42] Manqi: 這個事如果從商業上推驗的話
[00:17:44] Manqi: 如果它一塊做得不好
[00:17:45] Manqi: 對它來說會是個很大的危險嗎
[00:17:47] Manqi: 就除了我賺不到這一部分的錢之外
[00:17:49] Manqi: 我覺得數據對於模型的這個提升
[00:17:51] Henry In: 還是非常重要的
[00:17:53] Henry In: 因為它可能需要Cover
[00:17:55] Henry In: 像他們認為這個模型的Intel Engine
[00:17:57] Henry In: Multi 代曼師都對吧
[00:17:58] Henry In: 你在某一個代曼師
[00:17:59] Henry In: 你想要改進的話
[00:18:00] Henry In: 你只有它的數據上來了才可以
[00:18:02] Henry In: 我覺得就是它如果放棄Tubi的話
[00:18:04] Henry In: 最終的話這些缺少年數據可能也會影響模型整體的效果
[00:18:09] Henry In: 然後導致就是比如說TUC
[00:18:11] Henry In: 其實很多TouchyP的用戶
[00:18:12] Henry In: 還是Port of Tifsy Use Case
[00:18:14] Henry In: 最終也會影響這邊模型的效果
[00:18:16] Henry In: 因為這些Open Eye現在其實感覺
[00:18:18] Manqi: 它做的事越來越多了
[00:18:19] Manqi: 而且它做了很多事
[00:18:20] Manqi: 都是要非常大的投入的
[00:18:22] Manqi: 包括就是它9月29號發的Sour2
[00:18:26] Manqi: 對應的App這個也會少很多算力
[00:18:28] Manqi: 然後它又再做基礎模型的研發
[00:18:30] Manqi: 對吧肯定得往前推
[00:18:31] Manqi: 然後還有很多這種開發者的東西
[00:18:33] Manqi: 你覺得它同時幹這麼多事
[00:18:34] Manqi: 你覺得會影響它追求EJI的速度嗎
[00:18:36] Manqi: 我覺得他們的野心是非常大的
[00:18:38] Henry In: 當然Open Eye擴張的速度也是非常大的
[00:18:40] Henry In: 現在已經有好幾千人了
[00:18:42] Henry In: 但我覺得確實
[00:18:44] Henry In: 我覺得一個批評的聲音
[00:18:46] Henry In: 就是這次Agent Builder其實就是和
[00:18:48] Henry In: 比如說AGA的這個路線
[00:18:50] Henry In: 可能是有分歧的
[00:18:52] Henry In: 因為比如說AGA的路線追求的是
[00:18:54] Henry In: 說把這些人手工寫的死流程
[00:18:58] Henry In: 吃到模型裡面
[00:18:59] Henry In: 這樣的話中長期的話
[00:19:01] Henry In: 可能會這個改進的速度會更快一些
[00:19:04] Henry In: 那麼Agent Kit的話
[00:19:06] Henry In: 實際上是一個非常務實的一次
[00:19:08] Henry In: 轉身可以說是
[00:19:09] Henry In: 它其實讓目的是先把
[00:19:11] Henry In: 現在的開發者和企業的需求先吃住
[00:19:15] Henry In: 因為我覺得大部分人可以
[00:19:17] Henry In: 同意的是可能真正的終局
[00:19:19] Henry In: 是一個高度的autonomous
[00:19:22] Henry In: 然後能夠執行非常多部任務
[00:19:25] Henry In: 能夠持續使用工具的這種有狀態的智能體
[00:19:28] Henry In: 但它和實際上Agent Builder
[00:19:31] Henry In: 想要做的把流程畫成圖
[00:19:33] Henry In: 在塞給模型跑的這種Agentic Workflow
[00:19:35] Henry In: 其實是兩條路
[00:19:37] Henry In: 甚至是有點相反的
[00:19:39] Henry In: 我們可以看到就是
[00:19:41] Henry In: Anthropic他們這個Cloud Code的這個思路
[00:19:43] Henry In: 其實就是通用Agent思路
[00:19:45] Henry In: 核心就是讓盡量讓智能體自己跑
[00:19:49] Henry In: 然後少化這些流程圖
[00:19:51] Henry In: 這條路的好處的話
[00:19:52] Henry In: 就是說底膜只要杯子膜
[00:19:54] Henry In: 只要一升級的話
[00:19:55] Henry In: 智能體會直接受益
[00:19:57] Henry In: 那麼Agent Kit的話
[00:19:58] Henry In: 它更多的還是說
[00:20:00] Henry In: 我現在可能等不到Agent模型
[00:20:03] Henry In: 更好我現在就要的企業裡面落地
[00:20:05] Henry In: 那麼這個其實對於追求Agenti的這個
[00:20:07] Henry In: 尤其是RESERCELAR說它這個產品並不SEXY
[00:20:10] Henry In: 但對於比如說打客戶來說
[00:20:12] Henry In: 那它其實很安全
[00:20:14] Henry In: 好理解
[00:20:15] Henry In: 能落地所以我覺得它最後應該能賣單
[00:20:17] Henry In: 那我覺得它其實相同於都做了
[00:20:19] Manqi: 因為它在那個BuildAgent這個環節
[00:20:21] Manqi: 它其實給了你兩種選擇的
[00:20:23] Manqi: 一種就是它這次發了這個Builder
[00:20:25] Manqi: 是個可視畫可脫瘪的
[00:20:26] Manqi: 然後它之前就發過那個Agent SDK
[00:20:29] Manqi: 對 我覺得散步可能現在想的是
[00:20:31] Henry In: 我什麼都要
[00:20:32] Henry In: 人多了以後可能會有一些分差
[00:20:34] Henry In: 而且可能為了支撐這個月來月大了
[00:20:36] Henry In: 估值可能這個商業化和RESERCELAR的壓力
[00:20:39] Henry In: 可能也是越來越大的
[00:20:40] Henry In: 這是對OPENI這個公司來說
[00:20:42] Manqi: 它也有支撐估值的壓力嗎
[00:20:43] Manqi: 還有一種觀點是認為它已經裹寫了
[00:20:45] Manqi: 太多的投資
[00:20:46] Manqi: 包括它比如說又採購了
[00:20:48] Manqi: 因為打可能東西
[00:20:49] Manqi: 採購了假裹文 採購了MD
[00:20:51] Manqi: 這些大的公司之間這些投資方之間
[00:20:53] Manqi: 就商戶糾纏得很深
[00:20:55] Manqi: 就它已經到了一個大而不能倒的狀態
[00:20:57] Manqi: 我覺得它確實現在可能已經打到了
[00:21:00] Henry In: 一個TOPEAK TO FELL的狀態
[00:21:01] Henry In: 但是它可能野心還是非常大
[00:21:03] Henry In: 現在可能是五千億
[00:21:05] Henry In: 但是我想這個三可能肯定是不值五千億的
[00:21:08] Henry In: 對吧可能還要往上走一個數量級
[00:21:11] Henry In: 那我覺得還是需要一定的
[00:21:12] Henry In: 這個實際的商業價值的支撐的
[00:21:15] Manqi: 然後這次開發者發布之後
[00:21:17] Manqi: 你覺得就是在你周圍感受到的
[00:21:19] Manqi: 包括你們A.J.House社區裡的這些創業公司
[00:21:22] Manqi: 他們是怎麼來看這個事帶來的
[00:21:25] Manqi: 機會和可能的壓力的
[00:21:27] Manqi: 我覺得大部分人可能看到的還是機會
[00:21:31] Henry In: 我覺得有一個新的平台
[00:21:33] Henry In: 能夠讓開發者和用戶離得更近
[00:21:37] Henry In: 我覺得總體來說對開發者和創業者來說
[00:21:40] Henry In: 是一個很讓人興奮的事情
[00:21:42] Henry In: 壓力上面可能也有幾個方面
[00:21:46] Henry In: 比如說一個方面的話
[00:21:48] Henry In: 是我覺得存在一個數據和流存的一個不對稱
[00:21:51] Henry In: 因為現在比如說Apps的上下文和這些數據
[00:21:55] Henry In: 它還是主要偷管在Chaggbt的環境內
[00:21:58] Henry In: 那麼出上公司的話或者說
[00:22:00] Henry In: 開發者難得都可能只是有限的上下文調用
[00:22:03] Henry In: 而不是完整的用戶行為或者分析數據
[00:22:05] Henry In: 這個我覺得會讓開發者比較難以真正的建立一些
[00:22:09] Henry In: 用戶關係或者優化流存
[00:22:12] Henry In: 換句話說有點像是你在別人家的地基上建房
[00:22:16] Henry In: 可能這個根基不是很本
[00:22:17] Henry In: 第二個的話我覺得還存在一個平台
[00:22:21] Henry In: 自己來做以前事情的這種可能性
[00:22:24] Henry In: 因為現在Apps現在他們自己
[00:22:27] Henry In: Open Aya Open I Series對吧
[00:22:29] Henry In: 已經cover B2B整個流程了
[00:22:31] Henry In: 包括消瘦然後轉化
[00:22:34] Henry In: 客服
[00:22:36] Henry In: 平台上的一些
[00:22:37] Henry In: 他們也有完整的數據和用戶的對話歷史
[00:22:42] Henry In: 那麼一些平台上面比較探的機會
[00:22:44] Henry In: 也有可能存在Open Aya自己內建
[00:22:46] Henry In: 或者吃掉內藏的可能性
[00:22:48] Henry In: 你說到這個就是我上次和BioGru
[00:22:50] Manqi: Pokeye的城市
[00:22:51] Manqi: 然後他在講Google的時候
[00:22:52] Manqi: 他講了一個跟你剛才說的類似的想法
[00:22:55] Manqi: 因為Google也是做開發者做的比較多
[00:22:57] Manqi: 他就說可能存在一種對開發者的危險
[00:22:59] Manqi: 就是Google他看著覺得那個應用不錯
[00:23:02] Manqi: 他可能會自己做
[00:23:03] Manqi: 當我改一大對Google就沒那麼擔心
[00:23:05] Henry In: 因為Google就是自己做產品可能速度
[00:23:10] Henry In: 或者說各方面可能追不上Stard up
[00:23:12] Henry In: 但是可能Open Aya的速度可能還是
[00:23:15] Henry In: 可能會改進更快一些
[00:23:16] Henry In: 但其實這個反過來對Open Aya想做平台
[00:23:19] Manqi: 也是一個不利的因素
[00:23:21] Manqi: 就大家更祭擔它
[00:23:22] Manqi: 就看它後面怎麼去絕責了
[00:23:25] Henry In: 是把自己的定位放在哪裡
[00:23:28] Henry In: 我想現在所有這些Agent Katie
[00:23:30] Henry In: 都你都只能使用Open Aya的模型
[00:23:33] Henry In: 那麼如果Open Aya真正是說
[00:23:35] Henry In: 把AppsDK或者說Apps 成Gpt
[00:23:38] Henry In: 作為它為了平台做它的商業模式的話
[00:23:41] Henry In: 我想可能很多這種
[00:23:43] Henry In: Agent的Building過程中
[00:23:44] Henry In: 使用什麼樣的工具使用什麼樣的模型
[00:23:47] Henry In: 可能應該把它放開
[00:23:49] Henry In: 然後把自己更多的定位在一個平台的角色上面
[00:23:54] Henry In: 但目前的話就是可能還是在實驗過程中
[00:23:58] Henry In: 它這一次做哪部分是可以用第三方的模型
[00:24:00] Manqi: 哪部分是一定要用它自己的
[00:24:02] Manqi: 應該是就是EVAL的時候
[00:24:04] Henry In: 是可以用第三方模型的
[00:24:06] Henry In: 但其他時候比如說Agent Builder裡面
[00:24:08] Henry In: 應該是都只能有Open Aya的模型
[00:24:10] Henry In: 就是它優化評估的環節
[00:24:12] Manqi: 它可以引入第三方的模型
[00:24:13] Manqi: 對 可能這樣你比BeeBee就是Open Aya的模型
[00:24:15] Henry In: 比其他的模型可能更好看
[00:24:17] 那你覺得這種平台的機會可能會
[00:24:20] Manqi: 最後會有幾家有可能能做成
[00:24:22] Manqi: 可能最後這個市場如果比較穩定之後
[00:24:25] Manqi: 大概能容納多少這種平台
[00:24:27] Manqi: 我覺得看有幾個大的流量入口了
[00:24:30] Henry In: 目前來的看的話確實也就是
[00:24:32] Henry In: 可能最大的就是Jermenai or Chachypt
[00:24:36] 那在這兩個之間的話
[00:24:37] Manqi: 現代它們是一個什麼樣的態勢
[00:24:39] Manqi: 就比如說誰會在開發者這塊兒會搶一點
[00:24:41] Manqi: 前一天Jermenai就是已經是
[00:24:43] Henry In: 如果它們是全平台都
[00:24:46] Henry In: 計算在內的話它們的用戶量
[00:24:48] Henry In: 好像已經超過Chachypt了
[00:24:50] Henry In: 當然它們這個技術中可能也算了
[00:24:52] Henry In: 比如說Gmail裡面
[00:24:54] Henry In: 你打開來Jermenai寫郵件
[00:24:56] Henry In: 這可能也算是它們的用戶
[00:24:58] Henry In: 所以就是Jermenai的這個追趕的試頭
[00:25:01] Henry In: 還是比較猛的
[00:25:03] Henry In: 然後在開發者上面
[00:25:05] Henry In: 我覺得兩邊前進的速度都很快
[00:25:07] Henry In: 像這個Jermenai的AI Studio
[00:25:09] Henry In: 各種功能越來越完善
[00:25:11] Henry In: 然後當然這次Dev.2 Open.iG 這邊
[00:25:14] Henry In: 也發布了很多面向AZN的開發者的功能
[00:25:17] Henry In: And Sharpie就是它之前
[00:25:19] Manqi: 因為MCP這個生態
[00:25:20] Manqi: 可能現在是供據掉用力表主流的嗎
[00:25:22] Manqi: 它在這個形式裡面
[00:25:24] Manqi: 處於什麼位置
[00:25:25] Manqi: And Sharpie我覺得比較有意思
[00:25:27] Henry In: 一個是它可能現在Cloud
[00:25:29] Henry In: 並不是像Jermenai和Chachypt那樣
[00:25:32] Henry In: 比較大的有量入口
[00:25:34] Henry In: 第二個的話我覺得就是MCP
[00:25:37] Henry In: 它這個標準還是一個開放的標準
[00:25:41] Henry In: 大家都可以用
[00:25:42] Henry In: 所有人都可以從受益
[00:25:43] Henry In: 所以我覺得像MCP
[00:25:45] Henry In: 並沒有說給And Sharpie
[00:25:47] Henry In: 它有一個很強的
[00:25:49] Henry In: Compatitive advantage
[00:25:50] Henry In: OK
[00:25:51] 那今天非常感謝
[00:25:52] Manqi: 就是Henry的分享
[00:25:53] Manqi: 就關於Open.i.的這個Dev.2開發者
[00:25:56] Manqi: 我們做了一個補充
[00:25:57] Manqi: 接下來是9月下旬
[00:25:59] Manqi: 我與Henry和Nalmi一起
[00:26:01] Manqi: 討論他們觀察到的
[00:26:02] Manqi: AZN的工具鏈的一些趨勢
[00:26:04] Manqi: 我們也分享了他們自己投資的一些公司
[00:26:07] Manqi: 在美國的創業事件
[00:26:08] Manqi: 這一部分中我們提起了一些創業公司
[00:26:11] Manqi: 如Compose, Love Kate, Brain Trust等等
[00:26:14] Manqi: 也提到了美國突兵領域的一些上市公司
[00:26:16] Manqi: 如Octa, Data Dog
[00:26:18] Manqi: 這些公司的簡單介紹可以看
[00:26:20] Manqi: Sholo's的附路部分
[00:26:23] 這一次也是第一次邀請
[00:26:25] Manqi: AZN的兩位來分享
[00:26:26] Manqi: 我覺得我們也還有機會可以定期的
[00:26:28] Manqi: 來聊一聊在歸股在美國
[00:26:30] Manqi: AI最核心的區域
[00:26:31] Manqi: 在發生一些什麼樣的新的變化
[00:26:33] Manqi: 那Henry剛才也是有聊到
[00:26:35] Manqi: 就是你現在最關注的
[00:26:36] Manqi: 其實是這個智能體
[00:26:38] Manqi: 應用爆發之後
[00:26:39] Manqi: 帶來的工具鏈的一些機會
[00:26:41] Manqi: 那我們今天的主題
[00:26:42] Manqi: 也是來聊聊這個智能體的工具鏈
[00:26:44] Manqi: 或者可以叫AZN體的Tool-0
[00:26:46] Manqi: 我覺得你可以先講講就是
[00:26:48] Manqi: AZN體的Tool-0是什麼
[00:26:49] Manqi: 比如說大家哪些比較熟悉的公司
[00:26:52] Manqi: 產品或服務它是屬於
[00:26:54] Manqi: AZN的工具鏈或說工具箱的
[00:26:56] Manqi: 簡單說我覺得AZN體的Tool-0
[00:26:58] Henry In: 其實就是構建虛擬舒適的人
[00:27:00] Henry In: 需要用到的工具和身體部件
[00:27:02] Henry In: 就因為現在的大陸行公司
[00:27:04] Henry In: 其實都建制了AI對吧
[00:27:06] Henry In: 到底什麼是AI呢
[00:27:07] Henry In: 我覺得其實一種定義就是
[00:27:09] Henry In: 一個虛擬舒適的人
[00:27:10] Henry In: 因為過去的話
[00:27:11] Henry In: 計算機其實是工具
[00:27:13] Henry In: 但是是人來去適用這些機器
[00:27:16] Henry In: 我們得去學比如說
[00:27:17] Henry In: 如何打字
[00:27:18] Henry In: 如何用鼠標
[00:27:19] Henry In: 但現在其實發生了一些變化
[00:27:21] Henry In: 所以這個AI的發展
[00:27:23] Henry In: 計算機會越來越像人
[00:27:24] Henry In: 就變成反過來
[00:27:26] Henry In: 計算機來適應我們
[00:27:27] Henry In: 人機交互
[00:27:28] Henry In: 會逐漸變成人人交互
[00:27:30] Henry In: 我們會用就是最自然的
[00:27:32] Henry In: 這種對話的方式
[00:27:33] Henry In: 和計算機溝通
[00:27:34] Henry In: 但是如果要想實現這一點
[00:27:36] Henry In: 只有大模型這個聰明的大腦是不夠的
[00:27:39] Henry In: 它必須要有能聽
[00:27:41] Henry In: 能說能行動的身體
[00:27:43] Henry In: 我覺得這個就是
[00:27:44] Henry In: Agent tooling其實要解決的問題
[00:27:46] Henry In: 就具體來說的話
[00:27:47] Henry In: 這個數字人的身體
[00:27:49] Henry In: 可能對應著大家一些
[00:27:50] Henry In: 比較熟悉的公司和技術
[00:27:52] Henry In: 比如說股價
[00:27:53] Henry In: 其實就是Agent的框架
[00:27:55] Henry In: 這塊最有名的公司的話
[00:27:56] Henry In: 就是LineChang
[00:27:57] Henry In: 它其實起到一個負責協調
[00:27:59] Henry In: 還有調度各種Agent能力的一個作用
[00:28:02] Henry In: 然後Agent的左右手
[00:28:04] Henry In: 我覺得左手可能是比如說MCP
[00:28:07] Henry In: 使用這些工具
[00:28:08] Henry In: 然後Line手的話可能是Browthuse
[00:28:10] Henry In: 就是像人一樣
[00:28:11] Henry In: 去使用輪輪器
[00:28:12] Henry In: 或許信息
[00:28:13] Henry In: 然後交互操作
[00:28:14] Henry In: 像眼、耳、口
[00:28:16] Henry In: 這些器官其實就是Agent的這個框枝
[00:28:18] Henry In: 和交流的這個部件
[00:28:20] Henry In: 比如說公司像Elemin Labs
[00:28:22] Henry In: 他們提供高質量的這個雲和城
[00:28:24] Henry In: 現當於是數字人的嘴巴
[00:28:26] Henry In: 然後像LiveKit這樣做
[00:28:28] Henry In: 實實的音頻視頻
[00:28:30] Henry In: 交互的基礎設施
[00:28:31] Henry In: 是讓Agent有這個眼睛和耳朵
[00:28:34] Henry In: 然後能夠看和能夠聽
[00:28:36] Henry In: 然後實現這種實實的這種交互
[00:28:38] Henry In: 除了組成身體的部位以外
[00:28:40] Henry In: 就是還要一塊是單獨出來的
[00:28:42] Henry In: 身上於是Agent的這個教練
[00:28:44] Henry In: 就是這個數字人
[00:28:45] Henry In: 它如何表現
[00:28:46] Henry In: 其實是表現得好不好
[00:28:48] Henry In: 需要持續的這個評估和優化
[00:28:50] Henry In: 像這方面就有像Bring Trust
[00:28:52] Henry In: Gallia Layout這樣的公司
[00:28:53] Henry In: 專門去做Agent的評估
[00:28:55] Henry In: 然後監督它的這個表現
[00:28:57] Henry In: 保障它的可靠性
[00:28:58] Henry In: 那最起有什麼就是跟這個
[00:29:00] Manqi: Agent的圖案裡相關的一些事件
[00:29:03] Manqi: 能反映就是這個事了一些新的變化
[00:29:05] Manqi: 因為我知道有些投入資的時間
[00:29:07] Manqi: 包收購
[00:29:08] Manqi: 包括大公司可能有些業務的動作
[00:29:10] Manqi: 對確實最近關於Agent
[00:29:13] Nawmisha: 圖案還是挺多事情發生的
[00:29:15] Nawmisha: 我覺得可能有三個
[00:29:17] Nawmisha: 我個人覺得比較標誌性的事件
[00:29:19] Nawmisha: 然後也是在比較最近三個月發生的
[00:29:22] Nawmisha: 就第一個剛才就是
[00:29:23] Nawmisha: 還能聽到LiveLive
[00:29:24] Nawmisha: 就是這個做AI銀河床
[00:29:26] Nawmisha: 非常火的這家公司
[00:29:27] Nawmisha: 然後他們有一個員工的
[00:29:29] Nawmisha: Secondary Sound那一億美元作用
[00:29:31] Nawmisha: 然後大概是估值在
[00:29:33] Nawmisha: 六十六億美元
[00:29:34] Nawmisha: 然後這其實距離他們Cell的融資
[00:29:37] Nawmisha: 時候就是才九個月時間買
[00:29:39] Nawmisha: 就是已經翻了一倍
[00:29:40] Nawmisha: 所以說我覺得就是像這種
[00:29:42] Nawmisha: 作為智能體的這種嘴巴的
[00:29:45] Nawmisha: 這種底層的聲音設施
[00:29:46] Nawmisha: 然後其實可以看到它不僅是
[00:29:48] Nawmisha: Adoption就是它的增長非常快
[00:29:50] Nawmisha: 而且它的聲音化
[00:29:51] Nawmisha: 也是在有一個非常明顯的加速
[00:29:53] Nawmisha: 然後像比如說像Lunchen
[00:29:55] Nawmisha: 剛剛就是Han也提到
[00:29:56] Nawmisha: 就很多做AI銀的同學
[00:29:58] Nawmisha: 應該也因為他們的就是框架
[00:30:00] Nawmisha: 然後他們也剛剛正在
[00:30:02] Nawmisha: 扣新奧一個融資一億美元的
[00:30:04] Nawmisha: 新的融資碼
[00:30:05] Nawmisha: 然後被AVP在領頭
[00:30:07] Nawmisha: 然後差不多估值
[00:30:08] Nawmisha: 是在十一億左右
[00:30:10] Nawmisha: 然後像這種代理框架
[00:30:12] Nawmisha: 工具鏈
[00:30:13] Nawmisha: 這一層的開發者就是設施
[00:30:15] Nawmisha: 我覺得是持續在被
[00:30:17] 一些基金在大波檔
[00:30:19] Nawmisha: 在被資本持續加住的
[00:30:20] Nawmisha: 然後最近RESENTLY
[00:30:22] Nawmisha: 我覺得可能還有一個大家
[00:30:24] Nawmisha: 也就比較很多人在討論的
[00:30:25] Nawmisha: 就是OpenAI它全股收購了
[00:30:27] Nawmisha: 十一美元全股收購了Static
[00:30:30] Nawmisha: Static還是做什麼的呢
[00:30:32] Nawmisha: 它其實它做包括
[00:30:34] Nawmisha: 像ABTesting
[00:30:35] Nawmisha: 就是功能會不會發布
[00:30:37] Nawmisha: 然後一些數據指標的必環
[00:30:39] Nawmisha: 其實說把了就是說
[00:30:40] Nawmisha: 去評測這個模型
[00:30:42] Nawmisha: 就逐步去放量
[00:30:43] Nawmisha: 然後去看它的效果
[00:30:44] Nawmisha: 所以其實
[00:30:45] Nawmisha: 相當於OpenAI是
[00:30:46] Nawmisha: 就直接把這類能力
[00:30:48] Nawmisha: 從一個外掛的工具
[00:30:50] Nawmisha: 直接變成一個他們自己
[00:30:52] Nawmisha: 內置的組件
[00:30:53] Nawmisha: 如果我們把這三個時間放一塊看
[00:30:56] Nawmisha: 其實就可以看到一個相對
[00:30:58] Nawmisha: 比較就是清晰的節奏
[00:30:59] Nawmisha: 比如說就是在運行時的
[00:31:01] Nawmisha: 大規模落地的這種AZEN
[00:31:03] Nawmisha: 然後包括工具鏈的一些
[00:31:05] Nawmisha: 核心的組件
[00:31:06] Nawmisha: 被資本持續加住
[00:31:07] Nawmisha: 而且也有一些
[00:31:08] Nawmisha: 巨頭的這種戰略不許嘛
[00:31:09] Nawmisha: 所以其實現在
[00:31:10] Nawmisha: AZEN TOOLIN它已經不能說
[00:31:12] Nawmisha: 算是一個非常早期的概念
[00:31:15] Nawmisha: 剛才如果提到了Static
[00:31:17] Henry In: 這個點的話
[00:31:18] Henry In: 比較有意思的就是說
[00:31:19] Henry In: 我們看到很多之前
[00:31:20] Henry In: 做ABTesting的人
[00:31:21] Henry In: 現在都來立的
[00:31:23] Eval這件事情
[00:31:24] Henry In: 對那我們可以回到
[00:31:25] Manqi: 就是這個東西
[00:31:26] Manqi: AZEN的工具鏈
[00:31:27] Manqi: AZEN TOOLIN它發展的一個開端
[00:31:29] Manqi: 就是它是怎麼慢慢形成的
[00:31:30] Manqi: 因為就是從
[00:31:31] Manqi: Chag GT開始火之後
[00:31:33] Manqi: 其實陸陸續續的
[00:31:34] Manqi: 圍繞就是大模型
[00:31:35] Manqi: 剛才Henry說的
[00:31:37] Manqi: 就可能除了大腦
[00:31:38] Manqi: 之外給他提供了一些
[00:31:39] Manqi: 別的輔助的東西
[00:31:40] Manqi: 有好多好多概念出現的
[00:31:41] Manqi: 包括最開始的
[00:31:42] Manqi: Prompting Engine New Ring
[00:31:43] Manqi: 然後後面大家又講
[00:31:44] Manqi: 這個上下文工程等等等等
[00:31:46] Manqi: 就可以講講這個麥洛大
[00:31:47] Manqi: 還是怎麼發生的
[00:31:48] Manqi: 我覺得AZEN TOOLIN的發展
[00:31:50] Henry In: 其實是非常地
[00:31:51] Henry In: 圍繞著大模型能力的
[00:31:53] Henry In: 月前而發展的
[00:31:54] Henry In: 就像回到我們之前
[00:31:56] Henry In: 剛剛用的那個比喻吧
[00:31:57] Henry In: 就是AGA的話
[00:31:58] Henry In: 我覺得它是一個
[00:31:59] Henry In: 虛擬的數字人
[00:32:00] Henry In: 那麼過去這兩三年
[00:32:02] Henry In: 其實我們都在看
[00:32:03] Henry In: 這個數字人的大腦
[00:32:04] Henry In: 再進行一次又一次的升級
[00:32:06] Henry In: 而每次大腦的升級
[00:32:08] Henry In: 其實會暴露出它身體的殘缺
[00:32:10] Henry In: 從而催生出
[00:32:12] Henry In: 就是一波波的這個
[00:32:13] Henry In: 新的工具生態
[00:32:14] Henry In: 來為它補全這個身體的部件
[00:32:16] Henry In: 這個過程大概
[00:32:18] Henry In: 有六次主要的升級
[00:32:20] Henry In: 第一次的話
[00:32:22] Henry In: 我覺得就是刪GPT和GPD3.5的發布
[00:32:25] Henry In: 時間點就是2022年的年底
[00:32:28] Henry In: 那個時候
[00:32:29] Henry In: 其實是全世界意義上
[00:32:31] Henry In: 第一次真正認識到
[00:32:33] Henry In: 這個LRM的這個強大
[00:32:35] Henry In: 然後大家都想用它
[00:32:36] Henry In: 來去構建這個應用
[00:32:37] Henry In: 但其實很快就會發現
[00:32:39] Henry In: 你光有會聊天的腦子還不夠
[00:32:41] Henry In: 你還需要連接
[00:32:42] Henry In: 比如說外部數據
[00:32:43] Henry In: 你需要去做上下門的管理
[00:32:45] Henry In: 然後你需要去
[00:32:46] Henry In: 把多次這個LRM
[00:32:48] Henry In: 調用組合起來
[00:32:49] Henry In: 處理工負擔的問題
[00:32:50] Henry In: 所以這個時候
[00:32:51] Henry In: 就是LineChannel這樣的框架出現
[00:32:53] Henry In: 它提供的就是
[00:32:54] Henry In: 小手架
[00:32:55] Henry In: 幫助開發者
[00:32:56] Henry In: 能夠更快
[00:32:57] Henry In: 更容易的去構建這個大模型的這個應用
[00:33:00] Henry In: 那個時候我們還不管它叫AZN
[00:33:02] Henry In: 那個時候還是就是大模型的應用
[00:33:04] Henry In: 後面就很快就變成AZN
[00:33:06] Henry In: 然後第二次
[00:33:07] Henry In: 我覺得重要的升級的話
[00:33:09] Henry In: 是方式Calling
[00:33:11] Henry In: 這個時間點大概是2023年
[00:33:14] Henry In: 可能6月份
[00:33:15] Henry In: 也可以叫做工具使用
[00:33:18] Henry In: 然後這個時候是
[00:33:20] Henry In: OpenI當時的APR首次
[00:33:22] Henry In: 官方支持了方式Calling
[00:33:24] Henry In: 也就這個時候
[00:33:25] Henry In: LRM終於可以
[00:33:26] Henry In: 是根據上下門的需要
[00:33:28] Henry In: 去調用外圍工具了
[00:33:30] Henry In: 然後這個時候點開始後面
[00:33:32] Henry In: 會有越來越多的人去專門
[00:33:34] Henry In: 為LRM寫工具
[00:33:35] Henry In: 其實在很長一段時間
[00:33:37] Henry In: 我覺得寫一個AZN的
[00:33:39] Henry In: 百分之可能誇張一點的話
[00:33:41] Henry In: 8090的時間
[00:33:42] Henry In: 你是去寫一個好的工具
[00:33:44] Henry In: 然後另外一個重要的時間點
[00:33:46] Henry In: 是2024年的11月份
[00:33:48] Henry In: 這個時候是AntiRope發布了
[00:33:50] Henry In: 這個MCP的寫意
[00:33:52] Henry In: 使得就是工具
[00:33:53] Henry In: 更容易的在不同的模型之間
[00:33:56] Henry In: 去復用
[00:33:57] Henry In: 然後大部分之前的那些工具提供商
[00:33:59] Henry In: 也都順勢轉型
[00:34:01] Henry In: 成了MCPServer的提供商
[00:34:03] Henry In: 第三次升級
[00:34:04] Henry In: 我覺得是在語音的方面
[00:34:06] Henry In: 然後這個關鍵節點
[00:34:07] Henry In: 是2024年5月份
[00:34:09] Henry In: GPD4O的AdvancedWoodsmo的推出
[00:34:12] Henry In: 讓大家看到了
[00:34:13] Henry In: 就去這種非常高質量
[00:34:15] Henry In: 向人質語音交互的這個出型
[00:34:18] Henry In: 然後也帶起了
[00:34:19] Henry In: 對於這種實實的語音傳輸技術的需求
[00:34:23] Henry In: LiveK的當時
[00:34:24] Henry In: 就是因為它是
[00:34:25] Henry In: GPD4O背後使用的
[00:34:28] Henry In: 這個基礎設施
[00:34:29] Henry In: 所以它有一大波
[00:34:31] Henry In: 這個爆發性的增長
[00:34:32] Henry In: 第四次升級呢
[00:34:34] Henry In: 我覺得就是Coding了
[00:34:35] Henry In: 其實就是3.5和GPD4
[00:34:37] Henry In: 已經讓開發著很興奮了
[00:34:39] Henry In: 但我覺得這個
[00:34:40] Henry In: 歷史性的節點的話
[00:34:41] Henry In: 可能是2024年
[00:34:43] Henry In: Claw的3.5的發布
[00:34:45] Henry In: 讓這個AI變成徹底起飛
[00:34:47] Henry In: 我覺得Curser的成功
[00:34:49] Henry In: 應該和Claw
[00:34:50] Henry In: 3.5以及後面整個
[00:34:52] Henry In: ClawFamily系列的更新是分不開的
[00:34:55] Henry In: 因為這個AI寫代碼的能力大幅增強了
[00:34:59] Henry In: 能夠通過寫代碼
[00:35:01] Henry In: 去完成像是數據分析這樣的任務
[00:35:05] Henry In: 所以其實產生了對
[00:35:07] Henry In: 這種安全執行代碼的
[00:35:09] Henry In: 殺核環境的需求
[00:35:11] Henry In: 像這個領域的代碼公司
[00:35:13] Henry In: 比如說像E2B、Be2N
[00:35:15] Henry In: 第五次升級呢
[00:35:17] Henry In: 就是推理能力的突破
[00:35:19] Henry In: 像這個代表性的話
[00:35:21] Henry In: 大家都很熟
[00:35:22] Henry In: 就是2024年9月份
[00:35:23] Henry In: OpenAI發布這個O1PV
[00:35:25] Henry In: 像Rizning能力的提升
[00:35:28] Henry In: 使得AZN的終於可以
[00:35:30] Henry In: 自己做更多的規劃了
[00:35:32] Henry In: 而不是說像之前那樣開發者寫死了
[00:35:35] Henry In: 第一步做什麼
[00:35:36] Henry In: 第二步做什麼
[00:35:37] Henry In: 它現在會就是
[00:35:38] Henry In: 根據這個
[00:35:40] Henry In: 大家給的這個任務
[00:35:41] Henry In: 自己去規劃第一步做什麼
[00:35:42] Henry In: 第二步做什麼
[00:35:43] Henry In: 中間應該使用什麼樣的工具
[00:35:45] Henry In: 那麼這個轉變呢
[00:35:46] Henry In: 催生出了兩類工具
[00:35:48] Henry In: 第一類是
[00:35:49] Henry In: 這個Rizning能力是怎麼來的呢
[00:35:51] Henry In: 是大家在模型的基礎上
[00:35:54] Henry In: 做Reinforcement Learning
[00:35:55] Henry In: 強化學習做出來的
[00:35:56] Henry In: 所以大家看到了
[00:35:57] Henry In: 強化學習的這個好處
[00:36:00] Henry In: 對吧
[00:36:01] Henry In: 所以現在有像OpenAI
[00:36:03] Henry In: Fireworks
[00:36:04] Henry In: 就提供了這種
[00:36:06] Henry In: 用強化學習來
[00:36:07] Henry In: 非調模型的這種工具
[00:36:09] Henry In: 然後大家都不去
[00:36:10] Henry In: 用因為想要自己的這個AZN的
[00:36:12] Henry In: 模型更強大
[00:36:13] Henry In: 第二類的話就是
[00:36:15] Henry In: 因為現在AZN的自己
[00:36:17] Henry In: 會去做更複雜的
[00:36:18] Henry In: 更複雜
[00:36:19] Henry In: 更長的這種任務
[00:36:21] Henry In: 所以就更加需要的
[00:36:22] Henry In: 有更好的評估的工具
[00:36:24] Henry In: 來針對這整越來越複雜的任務
[00:36:26] Henry In: 做更好的監督
[00:36:28] Henry In: 所以像Bring Trust
[00:36:29] Henry In: Gallia Leo這樣的EVL
[00:36:31] Henry In: 或者做評估的公司
[00:36:32] Henry In: 就變得更重要了
[00:36:34] Henry In: 我覺得最後一次升級呢
[00:36:36] Henry In: 是計算機使用
[00:36:38] Henry In: 和BrowseR use能力的出現
[00:36:40] Henry In: 就這個關鍵節點
[00:36:41] Henry In: 是2024年10月份
[00:36:43] Henry In: 就Anthropic率先發布了
[00:36:45] Henry In: computer use的模型
[00:36:46] Henry In: 後面的話
[00:36:47] Henry In: OpenAI也發布了它的Operator
[00:36:49] Henry In: 這些模型呢
[00:36:51] Henry In: 讓AZN的真正具備來
[00:36:52] Henry In: 就是使用流冷器完成任務的能力
[00:36:55] Henry In: 然後也催生出了整個
[00:36:57] Henry In: 就是使用流冷器的這個車太系統
[00:37:00] Henry In: 有包括就是
[00:37:02] Henry In: 想提供這個雲端流冷器
[00:37:04] Henry In: 基礎設施的
[00:37:05] Henry In: 像BrowseR base
[00:37:06] Henry In: Anthropic Browser這樣的公司
[00:37:08] Henry In: 也有就是更上層
[00:37:09] Henry In: 直接給開發者提供這個API
[00:37:11] Henry In: 自然遠的API
[00:37:12] Henry In: 比如說
[00:37:13] Henry In: 幫我訂個外賣
[00:37:15] Henry In: 像這樣的公司
[00:37:16] Henry In: 我就有這個補充廠問的
[00:37:17] Manqi: 就剛才你提到
[00:37:18] Manqi: 就圖U字的這個邁洛
[00:37:19] Manqi: 其實23年6月
[00:37:20] Manqi: 就開始是OpenAI的方式Colin
[00:37:22] Manqi: 是它做還是提出來的
[00:37:23] Manqi: 現在我們看到其實
[00:37:24] Manqi: Anthropic做的這個MCP的協議
[00:37:27] Manqi: 它是更晚出現
[00:37:28] Manqi: 但它發展的更主流
[00:37:29] Manqi: 為什麼OpenAI它更早做這件事情
[00:37:31] Manqi: 它想到了這個事情
[00:37:32] Manqi: 但是它沒有Anthropic做得好
[00:37:33] Manqi: 我覺得Anthropic Cloud Cloud
[00:37:35] Henry In: 它有的時候可能在
[00:37:37] Henry In: Benchmark上不是最頂鮮的
[00:37:39] Henry In: 或者說在RM and Reenit上面
[00:37:41] Henry In: 但是開發者都很喜歡
[00:37:43] Henry In: 使用Anthropic的模型來變成
[00:37:45] Henry In: 我覺得這和Anthropic能力
[00:37:47] Henry In: 就是圖U字的能力很強
[00:37:49] Henry In: 是分不開的
[00:37:50] Henry In: 他們其實花了很多時間
[00:37:52] Henry In: 去提升圖U字
[00:37:54] Henry In: 讓這個Egentic的能力更強
[00:37:56] Henry In: 我覺得他們在自己
[00:37:58] Henry In: 弄明白
[00:37:59] Henry In: 圖U字這個能力
[00:38:00] Henry In: 變得更強的過程中
[00:38:02] Henry In: 其實進行了很多這方面的思考
[00:38:05] Henry In: 然後MCP其實我認為是他們
[00:38:08] Henry In: 給社區或者說整個AI ecosystem的
[00:38:11] Henry In: 一份禮物和慈善
[00:38:13] Henry In: 所以就有可能是
[00:38:15] Manqi: OpenAI雖然想到了這個
[00:38:16] Manqi: 但是它沒有Anthropic在這個上面
[00:38:18] Manqi: 花的精密多
[00:38:19] Manqi: 我覺得可以這麼說
[00:38:20] Henry In: 對 然後你剛才說的這個6次
[00:38:22] Manqi: 我可以在就幫廁有總結一下
[00:38:24] Manqi: 最開始是22年
[00:38:25] Manqi: 12月CHHGPT還有GPT3.5
[00:38:27] 然後下一個節點是
[00:38:28] Manqi: 就跟工具使用相關的是
[00:38:31] Manqi: 23.6月最開始的有方式Coling
[00:38:33] Manqi: 然後是到了24.11月的時候
[00:38:35] Manqi: 這個MCP的協議是這條工具使用
[00:38:37] Manqi: 麥洛上的一些發展
[00:38:38] Manqi: 然後第三個點就是
[00:38:40] Manqi: 語音這個是在24.5月
[00:38:42] Manqi: GPT4.0之後的一個變化
[00:38:44] Manqi: 第四個是Coling
[00:38:45] Manqi: 一個標誌性的時間是
[00:38:47] 24.6月
[00:38:48] Manqi: Sorry,3.5發布
[00:38:50] Manqi: 然後第五個講到的是推領
[00:38:52] Manqi: 這個標誌的模型上的節點是
[00:38:54] Manqi: 24.9月就是OpenAI發布
[00:38:55] Manqi: O系列推領能力的一個大幅提升
[00:38:57] Manqi: 然後第六個節點是你剛講到的
[00:38:59] Manqi: Computer Use
[00:39:00] Manqi: 還有Browser Use這個是在24.10月
[00:39:02] Manqi: 就我覺得看這些時間點也挺有意思的
[00:39:04] Manqi: 因為就開始22.12月到23.6月
[00:39:06] Manqi: 就這個會表吸輸嘛
[00:39:08] Manqi: 然後後面的那些笑話
[00:39:09] Manqi: 其實都是在24年就是交錯發生的
[00:39:11] Manqi: 就你感覺這個事越快了
[00:39:13] 對,是個非常XI的平台
[00:39:16] Manqi: 你覺得接下來它可能會怎麼發展
[00:39:18] Henry In: 現在這個時候預測未來會非常非常難
[00:39:21] Henry In: 因為很難有人就是說
[00:39:23] Henry In: 接下來能夠知道三個月六月發生什麼
[00:39:25] Henry In: 但我覺得相對確定性比較高的部分
[00:39:28] Henry In: 是Agentic的能力
[00:39:30] Henry In: 一定是所有大模型廠商在加強下注的
[00:39:33] Henry In: 這個主要就是分成兩部分
[00:39:35] Henry In: 一部分就是推理能力
[00:39:36] Henry In: 另外一部分就是使用工具的能力
[00:39:38] Henry In: 另外我覺得語音這塊
[00:39:41] Henry In: 也是所有大模型廠商
[00:39:43] Henry In: 現在在繼續加注的地方
[00:39:45] Henry In: 然後再有的話就是
[00:39:47] Henry In: 所有的模太融合在一起
[00:39:50] Henry In: 像我們最近看到就是
[00:39:52] Henry In: Image model和RMG合在一起
[00:39:54] Henry In: 有像這種Nanana 本來的
[00:39:56] Henry In: 這樣的很好的Image編輯的模型
[00:39:58] Henry In: 我覺得接下來我們可以通過一些具體的公司
[00:40:01] Manqi: 包括就是比較大的這種核心的AI公司
[00:40:04] Manqi: 他們在做什麼
[00:40:05] Manqi: 也包括就是其實這個領域
[00:40:07] Manqi: 就工具鏈本身出現了很多
[00:40:09] Manqi: 第三方的單組的創業公司
[00:40:11] Manqi: 他們在做什麼
[00:40:12] Manqi: 我覺得這樣可能給大家會有一個
[00:40:14] Manqi: 更指觀的感受
[00:40:15] Manqi: 但如果從現在這個時間點看的話
[00:40:17] Manqi: 就是以自己會表冠住的
[00:40:19] Manqi: 重點的工具鏈的方向有哪些
[00:40:22] Manqi: 包括這個裡面可能有哪些公司
[00:40:24] Manqi: 可以可以講講
[00:40:25] Manqi: 我覺得可能對應剛才我們說的
[00:40:27] Henry In: 這個模型能力可能增強的這幾個方向可能
[00:40:30] Henry In: 會關注首先
[00:40:32] Henry In: 如果要是Agentic能力增強了
[00:40:34] Henry In: 對吧
[00:40:35] Henry In: 那我覺得就是相應的
[00:40:36] Henry In: 它要使用的工具
[00:40:38] Henry In: 應該質量也會要更加的提高
[00:40:40] Henry In: 並且能夠支持
[00:40:42] Henry In: 更細和更複雜的操作
[00:40:44] Henry In: 因為現在我們看到的話
[00:40:45] Henry In: MCP server它更多的還是
[00:40:47] Henry In: 很多是Read only
[00:40:49] Henry In: 就MCP server現在比如說大家會用
[00:40:51] Henry In: Radity, Tweeter,Thumbgees,MCP server
[00:40:55] Henry In: 就做一些像Depri Search這樣的Jewscase
[00:40:57] Henry In: 但比如說真正去做一些寫
[00:41:00] Henry In: 操作的MCP server
[00:41:01] Henry In: 它的使用頻率是比較低的
[00:41:03] Henry In: 但如果說模型的Resonin和
[00:41:05] Henry In: To Use能力越強的話
[00:41:07] Henry In: 會避免這種小孩會大到的情況
[00:41:09] Henry In: 它可以 actually 去做一些
[00:41:11] Henry In: 風險的一些帶寫操作的事情
[00:41:14] Henry In: 所以我覺得就是
[00:41:15] Henry In: MCP server這塊是我會比較關注的一個領域
[00:41:19] Henry In: 這塊的公司的話
[00:41:21] Henry In: 我覺得有一家非常有意思的公司
[00:41:23] Henry In: 就是Compose有的
[00:41:24] Henry In: 對Compose有我們最近
[00:41:26] Nawmisha: 投了一家公司
[00:41:27] Nawmisha: 然後它其實就是一個
[00:41:29] Nawmisha: MCP的一個
[00:41:31] Nawmisha: 可以說一個節成倡也是一個
[00:41:32] Nawmisha: Marketplace的感覺
[00:41:33] Nawmisha: 其實一個Andreline的一個趨勢數
[00:41:35] Nawmisha: 可以看到就是我們
[00:41:37] Nawmisha: 正在從一個工具調用的時代
[00:41:39] Nawmisha: 到一個任務完成
[00:41:41] Nawmisha: 就是Task Compliation的時代
[00:41:43] Nawmisha: 像Compose它就是提供一個
[00:41:45] Nawmisha: 高質量的MCP server
[00:41:47] Nawmisha: 然後它其實不僅僅可以去調用工具
[00:41:49] Nawmisha: 一個工作的事情去保證
[00:41:51] Nawmisha: 它們可以更可靠的
[00:41:53] Nawmisha: 一個任務
[00:41:54] Nawmisha: 就相當於給Agent去提供了
[00:41:56] Nawmisha: 一套比較完整的操作系統
[00:41:58] Nawmisha: 可能要解釋一下
[00:41:59] Manqi: 就是這個MCP server或者說MCP集成商
[00:42:02] Manqi: 它大概是做什麼的
[00:42:03] Nawmisha: MCP形成的感覺像一個API接口一樣
[00:42:06] Nawmisha: 就有點像一個Marketplace去選擇
[00:42:08] Nawmisha: 什麼有哪些工具你銷去連接
[00:42:10] Henry In: Compose有它產品上又分為兩個部分
[00:42:13] Henry In: 一個部分是平台
[00:42:15] Henry In: 就是說開發者通過編程的方式
[00:42:18] Henry In: 去使用這些MCP server
[00:42:20] Henry In: 在他們的Agent裡面
[00:42:22] Henry In: 還有一個Presumer的一個產品
[00:42:25] Henry In: 叫做Rub
[00:42:27] Henry In: Rub最近它的用戶增長非常好
[00:42:31] Henry In: 因為它解決了一個問題
[00:42:33] Henry In: 比如說你在Compose裡面使用MCP server的話
[00:42:37] Henry In: 你能用的MCP server是有數量限制的
[00:42:40] Henry In: 這個也是因為上下文的限制
[00:42:42] Henry In: 大概你可能只能一次點亮三個MCP server
[00:42:45] Henry In: 但如果要使用很多MCP server同時使用
[00:42:48] Henry In: 你是用不了的
[00:42:49] Henry In: 所以他們有一個就是
[00:42:51] Henry In: 有點像那個模件那個概念
[00:42:52] Henry In: One-Rint Brutamo
[00:42:53] Henry In: 它是One-MCP server 都入Demo
[00:42:55] Henry In: 所以它提供了一個MathMCP server
[00:42:58] Henry In: 然後可以幫助你根據你的任務
[00:43:00] Henry In: 去選擇使用正確的MCP server
[00:43:03] Henry In: 所以現在大家都在這個Compose裡面
[00:43:05] Henry In: 去用Rub來接就是那幾百個MCP server
[00:43:09] Henry In: 所以一個MCP server就是個表小白的問題
[00:43:11] Manqi: 就是一個MCP server還是對應一個工具
[00:43:14] Manqi: 還是它是可能對應好幾個工具的
[00:43:16] 一個MCP server下面可能會暴露多個工具
[00:43:19] Henry In: 有幾百個就相當於那幾百個
[00:43:21] Manqi: 還要再沉溢一個數字
[00:43:23] Manqi: 它下面實際上能掉了總工具數字
[00:43:25] Henry In: 這是為什麼就是Compose
[00:43:26] Henry In: 現在應該是具體的數字可能需要確認一下
[00:43:29] Henry In: 但是我記得還是只允許你同時打開三個MCP server
[00:43:34] Henry In: 因為你每個Service下面有可能有到路多個工具
[00:43:37] Henry In: 然後你每個工具有好多參數
[00:43:38] Henry In: 所以他們還是很吃偷可能的
[00:43:39] Henry In: 現在一個MCP server裡面能有多少工具
[00:43:42] Manqi: 這個社會會受一些什麼技術上的限制嗎
[00:43:44] Manqi: 它會有平靜嗎
[00:43:45] Henry In: MCP server你設計
[00:43:47] Henry In: 所以設計下面有多少個工具
[00:43:49] Henry In: 其實完全就是看你
[00:43:50] Henry In: 比如說你做一個G-Milk的MCP server
[00:43:52] Henry In: 那和G-Milk這個產品的複雜度是相關的
[00:43:55] Henry In: 如果你想暴露G-Milk的所有的功能的話
[00:43:58] Henry In: 想逼你可能需要的MCP的工具
[00:44:01] Henry In: 這下面的兔可能也比較多
[00:44:03] Henry In: 因為這個產品可能比較複雜
[00:44:05] Henry In: 所以是看你的意圖是什麼
[00:44:06] Manqi: 但如果你設計太複雜
[00:44:08] Manqi: 可能它執行的成功率上是會有一些影響的什麼
[00:44:10] Manqi: 對這個是有Trade House的
[00:44:12] Henry In: 比如說你有兩個非常接近的工具
[00:44:14] Henry In: 那模型就會感覺很疑惑
[00:44:16] Henry In: 應該到底到有哪個對方他們區別是什麼
[00:44:18] Henry In: 那當我們也可以繼續講講
[00:44:20] Manqi: 比如說你們最愛是怎麼看到這個產品
[00:44:22] Manqi: 它成立多久了
[00:44:23] Manqi: 然後就為什麼你們當時覺得這個方向還挺有機會的
[00:44:27] Manqi: 以及我自己可能會有一個很自然的疑問
[00:44:29] And Sharpie的他為什麼還不自己幹這個事
[00:44:31] Manqi: 就好像比如說一個非常簡單的聯想
[00:44:33] Manqi: 但可能這個類語不恰到
[00:44:34] Manqi: 就蘋果的這個App Store還是我自己幹
[00:44:37] Nawmisha: 當時這個因為我們在E-Milk House會亂很多
[00:44:40] Nawmisha: 大型的Hack房然後其實我們有說
[00:44:42] Nawmisha: 很多是AIA.G.N.B.O.D.所以其實做AIA.G.N.的話
[00:44:46] Nawmisha: 請女生調到不同的工具
[00:44:48] Nawmisha: 然後當時就在想說如果是要做一個
[00:44:50] Nawmisha: 比如幾乎的AIA.G.N.它同時調用
[00:44:52] Nawmisha: 或者去Complete.Tas的時候
[00:44:54] Nawmisha: 其實需要一個同時去使用不同的MCP server
[00:44:57] Nawmisha: 然後當時我們就從這個
[00:44:58] Nawmisha: 肯定體裡面說起到的反饋
[00:45:00] Nawmisha: 就是一手的信息
[00:45:01] Nawmisha: 就是說Compose是一個比較 reliable的這樣一個平台
[00:45:05] Nawmisha: 我覺得Compose的最有意思的是
[00:45:06] Henry In: 它一開始是做AIA.G.N.的公司
[00:45:08] Henry In: 然後它後來變成了AIA.G.N.的凸鏈的公司
[00:45:11] Henry In: 它之所以它是AIA.G.N.的凸鏈公司
[00:45:13] Henry In: 我們覺得最有意思的是
[00:45:15] Henry In: 因為它A.G.N.的B.O.D.好
[00:45:16] Henry In: 它竟然A.G.N.的B.O.D.好
[00:45:17] Manqi: 它為下一步把AIA.G.N.的繼續做好了
[00:45:19] Manqi: 它現在竟然接著做AIA.G.N.的
[00:45:21] Henry In: 它之所以它有這麼多
[00:45:23] Henry In: Hack quality的AIA.G.N.的凸鏈
[00:45:25] Henry In: 就是MCP server是因為它整個寫
[00:45:27] Henry In: Serve的過程是AIA.G.N.自動的寫
[00:45:29] Henry In: 自動的感情
[00:45:30] Henry In: 所以它的AIA.G.N.是一個寫MCP server的A.G.N.對
[00:45:34] 對 就是我們是要不要後來
[00:45:36] Nawmisha: 他們轉型之後然後見到他們的
[00:45:38] Nawmisha: 他們一開始就是一個在印度
[00:45:40] Nawmisha: 然後它也不是做MCP的寫MCP的
[00:45:43] Nawmisha: Serve提供上
[00:45:44] Nawmisha: 它其實是在2023年的
[00:45:46] Nawmisha: 7月份手成立
[00:45:47] Nawmisha: 當時他們其實是想做一個
[00:45:49] Nawmisha: 就是集成的這樣的一個
[00:45:51] Nawmisha: Davon然後就是用AI自動生成
[00:45:53] Nawmisha: 就是DFD3方API的這種集成代碼
[00:45:56] Nawmisha: 但當時那個
[00:45:57] Nawmisha: 大魔性能力還不夠嘛
[00:45:59] Nawmisha: 所以就是其實生成代碼的準確率
[00:46:02] Nawmisha: 它打不到要求
[00:46:03] Nawmisha: 然後慢慢他們在
[00:46:05] Nawmisha: 就是敵代的過程中發現了一個
[00:46:07] Nawmisha: 就是更底層的問題
[00:46:09] Nawmisha: 就是其實A.G.N.不是
[00:46:10] Nawmisha: 不過寫代碼而是
[00:46:11] Nawmisha: 就不會特別穩定的
[00:46:12] Nawmisha: 掉用和使用這個工具
[00:46:14] Nawmisha: 所以他們當時就是做一個決定去PVIT
[00:46:18] Nawmisha: 就是不是在做這個集成自動化
[00:46:20] Nawmisha: 而是去構建一個AIA.G.N.的一個技能層
[00:46:23] Nawmisha: 就是把這些同用工具
[00:46:24] Nawmisha: 就是封裝成一個
[00:46:25] Nawmisha: AMAM能夠直接掉用的
[00:46:27] Nawmisha: 這樣的一個技能
[00:46:28] Nawmisha: 所以其實這個PVIT時間點
[00:46:30] Nawmisha: 其實發生在
[00:46:31] Nawmisha: 就是MCP協議
[00:46:32] Nawmisha: MCP協議的之前
[00:46:34] Nawmisha: 所以它其實很早的時候
[00:46:36] Nawmisha: 其實就摸到了
[00:46:37] Nawmisha: AIA.G.N.就是工具化的一個痛點
[00:46:40] Nawmisha: 而且他們其實這個
[00:46:41] Nawmisha: 非常SquarePIT的團隊
[00:46:43] Nawmisha: 當時其實還在印度
[00:46:44] Nawmisha: 也沒有什麼資源
[00:46:45] Nawmisha: 也沒有什麼聲量
[00:46:46] Nawmisha: 創始人就是瘋狂
[00:46:47] Nawmisha: 在推特上發尺片
[00:46:49] Nawmisha: 然後包括去演示這個Compose
[00:46:51] Nawmisha: 我怎麼去掉用工具
[00:46:53] Nawmisha: 然後出一個錯誤
[00:46:54] Nawmisha: 這些視頻就是在AI的
[00:46:56] Nawmisha: 開發者的社區就傳開了
[00:46:58] Nawmisha: 而他們整個團隊
[00:47:00] Nawmisha: 就是泡在各個社交媒體裡
[00:47:02] Nawmisha: 也就是說什麼Radiada Discord
[00:47:04] Nawmisha: 然後去看收金禍的反饋
[00:47:06] Nawmisha: 就是幫他們去親手
[00:47:07] Nawmisha: 去調適他們的一些
[00:47:08] Nawmisha: 集成的需求
[00:47:09] Nawmisha: 所以就是一個
[00:47:10] Nawmisha: 很小的這樣一個印度的團隊
[00:47:12] Nawmisha: 拿到了美國LyceP的
[00:47:14] Nawmisha: 就是領頭的
[00:47:15] Nawmisha: Series A的這樣融資
[00:47:17] Nawmisha: 展下一批包括很多
[00:47:18] Nawmisha: Vyce的團隊
[00:47:19] Nawmisha: 就是Click-up
[00:47:20] Nawmisha: 還有Gling這樣比較
[00:47:21] Nawmisha: 致命的用戶
[00:47:22] Nawmisha: 然後當時我們也是
[00:47:23] Nawmisha: 就是辦了很多場
[00:47:24] Nawmisha: 就是這種Hakata
[00:47:26] Nawmisha: 然後當時也是聽到
[00:47:27] Nawmisha: 很多的Divialoper
[00:47:28] Nawmisha: 去反饋這個名字
[00:47:29] Nawmisha: 見到了這些Founder
[00:47:31] Nawmisha: 然後去慢慢去Build out
[00:47:32] Nawmisha: 我們的Convection
[00:47:33] Nawmisha: 因為頭他們的時候
[00:47:34] Manqi: 他們公司有多少人
[00:47:35] Manqi: 他們其實現在團隊也不大
[00:47:37] Nawmisha: 好像先是三十人
[00:47:39] Nawmisha: 還挺緊勁的
[00:47:40] Manqi: 但他們這些人
[00:47:41] Manqi: 因為他們之前在印度
[00:47:42] Manqi: 他們是人在印度的時候
[00:47:43] Manqi: 就已經獲得了美國這個機構的
[00:47:45] Manqi: 就剛剛說的A-LUN的領頭
[00:47:46] Manqi: 他們現在是團隊也來到了美國
[00:47:49] Manqi: 他們整個團隊都搬過來了
[00:47:51] Nawmisha: 他們整體的這個團隊
[00:47:52] Nawmisha: 我還沒有見過一個非印度人
[00:47:54] Nawmisha: 還有人你有見過他們團隊
[00:47:56] Nawmisha: 非印度人嗎
[00:47:57] Nawmisha: 好像全部都是印度人
[00:47:58] Nawmisha: 不過好像也沒見過
[00:47:59] Henry In: 他們不是印度人的同事
[00:48:01] Henry In: 他們沒有說
[00:48:02] Nawmisha: 我們要來美國
[00:48:04] Nawmisha: 我們就要害美國人這樣子的概念
[00:48:06] Nawmisha: 他們就覺得我們就想
[00:48:07] Nawmisha: 我們會想要做
[00:48:08] Nawmisha: 做最高級的人
[00:48:09] Nawmisha: 如果他們覺得
[00:48:10] Nawmisha: 他們當下的印度團隊最憨軌
[00:48:12] Nawmisha: 然後他們就把那些
[00:48:13] Nawmisha: 印度的人才來到鬼谷在創意
[00:48:15] Nawmisha: 他們現在在鬼谷的什麼地方
[00:48:17] Nawmisha: 他們是在舊金山
[00:48:18] Nawmisha: 他們奧肺是在舊金山市裡
[00:48:20] Nawmisha: 對他們本來主要是
[00:48:21] Nawmisha: 因為想跟更加closed
[00:48:22] Nawmisha: 的去跟這些AI
[00:48:24] Nawmisha: 的團隊去結成交流
[00:48:26] Nawmisha: 因為這是他們的客戶
[00:48:27] Nawmisha: 然後也非常深入的
[00:48:29] Nawmisha: 去做Baltum App 到審
[00:48:31] Nawmisha: 就是所以我們也在
[00:48:32] Nawmisha: A.J.H.H.O.有很多次
[00:48:34] Nawmisha: H.K.F.的合作
[00:48:35] Nawmisha: 讓我們才慢慢進來的現人
[00:48:36] Nawmisha: 你們現在就A.J.H.H.H.S
[00:48:37] Manqi: 也是被死在舊金山的什麼
[00:48:39] Manqi: 我們是在半島
[00:48:41] Nawmisha: 就是說在鬼谷和舊金山
[00:48:43] Nawmisha: 市中心的中間位置
[00:48:44] Nawmisha: 對
[00:48:45] Manqi: 我感覺好像現在舊金山
[00:48:46] Manqi: 挺活躍的
[00:48:47] Manqi: 因為之前其實很多公司
[00:48:48] Manqi: 還是在鬼谷表動
[00:48:49] Manqi: 鬼谷和舊金山
[00:48:50] Manqi: 還是有一點距離
[00:48:51] Manqi: 但現在有很多這種
[00:48:52] Manqi: 一些復化器
[00:48:53] Manqi: 包括這種社區
[00:48:54] Manqi: 活動
[00:48:55] Manqi: 包括一些公司的辦公室
[00:48:57] Manqi: 其實很多就是在舊金山市區
[00:48:59] Nawmisha: A.J.H.H.O.P.O.P.的辦公室
[00:49:01] Nawmisha: 都是在舊金山
[00:49:03] Nawmisha: Daphne 也
[00:49:04] Nawmisha: SF 也在那裡
[00:49:05] Nawmisha: 而且他的Ren
[00:49:06] Nawmisha: 好像長了20-30%
[00:49:08] Nawmisha: 今年
[00:49:09] Manqi: 還有剛才我說的那個問題
[00:49:10] Manqi: 就是A.J.H.H.H.O.P
[00:49:11] Manqi: 為什麼不自己做這個手容
[00:49:13] Manqi: 就是我們不覺得
[00:49:14] Nawmisha: A.J.H.H.O.P
[00:49:15] Nawmisha: 他自己會做一個完整的
[00:49:17] Nawmisha: Compose
[00:49:18] Nawmisha: J.H.H.O.的一個原因
[00:49:20] Nawmisha: 在於他做這個事情
[00:49:22] Nawmisha: 並不會加強他自己
[00:49:24] Nawmisha: 核心的一個競爭力
[00:49:25] Nawmisha: 因為A.J.H.H.E.
[00:49:26] Nawmisha: 他是個大魔性公司
[00:49:27] Nawmisha: 然後他的主要的護城合
[00:49:29] Nawmisha: 還是在他的模型的advancement
[00:49:31] Nawmisha: 和他的
[00:49:32] Nawmisha: 比如說City
[00:49:33] Nawmisha: 那他不太會去想
[00:49:35] Nawmisha: 把他人力投入到
[00:49:37] Nawmisha: 第三方API的這個維護
[00:49:39] Nawmisha: 非常分散他的資源
[00:49:41] Nawmisha: 我覺得他還好
[00:49:42] Nawmisha: 而且他去做為一個
[00:49:43] 就是抵從平台
[00:49:44] Nawmisha: 他希望相對重力的
[00:49:46] 然後就是你們覺得整體上
[00:49:47] Manqi: MCP這個生態會怎麼發展
[00:49:49] Manqi: 因為就是剛才我們也聊到
[00:49:51] Manqi: 其實內六波裡面
[00:49:52] Manqi: 就是對人來說
[00:49:54] Manqi: 就廣義上來說使用工具
[00:49:55] Manqi: 其實Browse or Use
[00:49:56] Manqi: 包括現在大家也做到手機上
[00:49:58] Manqi: Full Use也是一種方法
[00:49:59] Manqi: 那前段時間
[00:50:00] Manqi: 其實我們有和這個致普
[00:50:02] Manqi: 就中國的一家大魔性公司
[00:50:04] Manqi: 他沒有做了一個在手機上
[00:50:06] Manqi: 可以去運行的Agent
[00:50:07] Manqi: 就幫你在手機上
[00:50:08] Manqi: 比如說點一些外賣
[00:50:09] Manqi: 或者買一些東西什麼的
[00:50:10] Manqi: 當然這個現在
[00:50:11] Manqi: 成功率可能沒有那麼高
[00:50:12] Manqi: 但他的那個思路就是
[00:50:13] Manqi: 他們認為其實在手機上
[00:50:15] Manqi: 你的GUI
[00:50:16] Manqi: 就圖形見面
[00:50:17] Manqi: Full Use 照長期存在了
[00:50:19] Manqi: 有一個原因就是
[00:50:20] Manqi: 有一些工具
[00:50:21] Manqi: 他其實不想被你吊有
[00:50:22] Manqi: 就甚至可能在網頁端
[00:50:23] Manqi: 也會有一些工具
[00:50:24] Manqi: 他不想被你吊有
[00:50:26] Manqi: 他不想就是被人家在上面蓋了一層
[00:50:28] Manqi: 所以長期來說
[00:50:29] Manqi: 比如說這個MCP
[00:50:30] Manqi: 他最後能滲透到多少工具了
[00:50:33] Manqi: 他真的能讓這個Agent
[00:50:34] Manqi: 作為一個虛擬的數字人
[00:50:36] Manqi: 在虛擬世界唱不通無足嗎
[00:50:38] Manqi: 我覺得第一個角度是
[00:50:39] Henry In: 現在Browse or Use
[00:50:41] Henry In: Competer Use或者Full Use
[00:50:42] Henry In: 他的這個可靠性的問題
[00:50:44] Henry In: 現在的最popular的Benchmark
[00:50:47] Henry In: 像台式就是Dusttop的話
[00:50:49] Henry In: 是OS World
[00:50:51] Henry In: 然後如果要是Browse or的話
[00:50:52] Henry In: 現在是Web Arena
[00:50:54] Henry In: 然後我們能看到現在最好的模型
[00:50:56] Henry In: 在這些Benchmark上面
[00:50:58] Henry In: 大概就是60%70%
[00:51:00] Henry In: 那你想像一下
[00:51:01] Henry In: 如果像一些
[00:51:02] Henry In: 很關鍵的工作流
[00:51:04] Henry In: 比如說在美國
[00:51:06] Henry In: Hellcare 場景
[00:51:07] Henry In: 我要給一個病人
[00:51:09] Henry In: 就是做Onboarding
[00:51:11] Henry In: 那你說我只有70%的成功改例
[00:51:13] Henry In: 這個事情就是可行
[00:51:15] Henry In: 我覺得是完全不可行的
[00:51:17] Henry In: 所以我覺得就是說
[00:51:18] Henry In: 在短期如果
[00:51:20] Henry In: Browse or Use
[00:51:22] Henry In: 準確率上不去的話
[00:51:24] Henry In: 我覺得像一些關鍵的工作流
[00:51:26] Henry In: 它必須得依賴於成功率
[00:51:27] Henry In: 更高的To Use
[00:51:29] Henry In: 但是我覺得Browse or Use的話
[00:51:31] Henry In: 它肯定是有它的這個價值的
[00:51:33] Henry In: 因為很定會有很多的
[00:51:35] Henry In: 這個服務和網站是
[00:51:36] Henry In: 不能被MCPcover的
[00:51:38] Henry In: 像之前我聽說過的一個
[00:51:40] Henry In: Browse or Use的 Use Case
[00:51:42] Henry In: 就是大家去喜歡去日本旅遊的人
[00:51:45] Henry In: 可能知道日本有很多不提克的酒店
[00:51:47] Henry In: 預定網站是都沒有接入那些OTA的
[00:51:50] Henry In: 所以就有專門人的人
[00:51:52] Henry In: 去用Browse or Use的方法
[00:51:54] Henry In: 去把他的這個
[00:51:55] Henry In: 哪些日子有空房
[00:51:57] Henry In: 用所有的這個組合
[00:51:59] Henry In: 把這個數據拉下來
[00:52:01] Henry In: 然後把它給這種搜索引擎
[00:52:03] Henry In: 然後搜索引擎的話
[00:52:04] Henry In: 就可以就是能搜到這些
[00:52:06] Henry In: 日本的這些精品酒店
[00:52:08] Henry In: 所以像這些長微的 Use Case
[00:52:10] Henry In: 我覺得可能Browse or Use
[00:52:12] Henry In: 應該還是更好的選擇
[00:52:14] 那那些特別大的這種
[00:52:16] Manqi: 超級應用了
[00:52:17] Manqi: 比如說在移動生態裡面
[00:52:19] Manqi: 其實App之間是相對要封閉一點的
[00:52:22] Manqi: 你覺得長期來說
[00:52:23] Manqi: 這些他們也會
[00:52:24] Manqi: 願意融入MCP的生態嗎
[00:52:26] Manqi: 我覺得有一個有意思的觀點就是
[00:52:28] Henry In: ChadGPT的最終目標是
[00:52:32] Henry In: WeChatGPT
[00:52:33] Henry In: 就是它在Biu的一個Super app
[00:52:35] Henry In: 就是因為大家想一想
[00:52:37] Henry In: 就是因為AI越來越像數字人
[00:52:39] Henry In: AJI是數字人
[00:52:40] Henry In: 那我們区域門半個各種事情的話
[00:52:43] Henry In: 叫做飛牙啥
[00:52:44] Henry In: 你都是和人沟通嘛
[00:52:46] Henry In: 其實本質上就是
[00:52:47] Henry In: 其實WeChat的大家
[00:52:48] Henry In: 微信大家裡面已經可以
[00:52:50] Henry In: 幹出各種各樣的事情了
[00:52:51] Henry In: 所以我覺得就是
[00:52:52] Henry In: OpenAI的ChadGPT的產品的最終形態
[00:52:54] Henry In: 可能就是WeChatGPT
[00:52:56] Henry In: 然後所有提供那些服務的人
[00:52:58] Henry In: 他們被迫需要
[00:52:59] Henry In: 提供一個給RM教貨的接口
[00:53:02] Henry In: 才能接入到這個生態裡面
[00:53:04] Henry In: 所以這倒不是一個
[00:53:05] Manqi: 你願不願意的問題什麼
[00:53:06] Manqi: 就是你覺得這是個趨勢
[00:53:07] Manqi: 對 我覺得這件事難以看我們大場的
[00:53:09] Manqi: 那剛才我們講的
[00:53:10] Manqi: 就是是這個工具使用
[00:53:12] Manqi: 還有就是Brother Use,Fone Use
[00:53:15] Manqi: 這些圖形界面的教貨的
[00:53:17] Manqi: AJI的圖靈能力
[00:53:18] Manqi: 你可以再講到
[00:53:19] Manqi: 就其他還有那些
[00:53:20] Manqi: 你比較關注的方向
[00:53:21] Manqi: 其實在最開始
[00:53:22] Manqi: 輸了一個麥洛的時候
[00:53:23] Manqi: 你提到了好好幾個方向
[00:53:24] Manqi: 還包括有記憶、評估呀
[00:53:26] Manqi: 我們還比較看好的方向就是
[00:53:28] Henry In: 語音幾個數據吧
[00:53:30] Henry In: 一個是就是目前
[00:53:31] Henry In: 全世界每天
[00:53:32] Henry In: 有One Trillian的Fone口
[00:53:35] Henry In: One Trillian應該是
[00:53:37] Henry In: 100億的吉劣
[00:53:38] Henry In: 然後這其中有
[00:53:39] Henry In: 很大一部分是那種
[00:53:41] Henry In: 商業的電話
[00:53:43] Henry In: 像那些東西
[00:53:44] Henry In: 很多都可以
[00:53:45] Henry In: 比如說客服呀之類的
[00:53:47] Henry In: 都可以被這個
[00:53:48] Henry In: AI打電話來取代
[00:53:50] Henry In: 所以我們覺得就是說
[00:53:52] Henry In: 語音這塊的話
[00:53:53] Henry In: 像B2B這樣的機會
[00:53:56] Henry In: 是很多的
[00:53:57] Henry In: 然後第二個的話
[00:53:58] Henry In: 就是像
[00:54:00] Henry In: Personal Assistant
[00:54:01] Henry In: 或者這種情感陪伴類的
[00:54:03] Henry In: 也是一個增長比較快的
[00:54:05] Henry In: 一個領域
[00:54:06] Henry In: 所以我就語音主要分為
[00:54:07] Henry In: 這兩個部分都增長
[00:54:08] Henry In: 前列都很大
[00:54:09] Henry In: 我們比較關注的
[00:54:11] Henry In: 一家公司呢
[00:54:12] Henry In: 之前可能也提到了
[00:54:13] Henry In: 叫LiveKit
[00:54:14] Henry In: 可能這家公司在
[00:54:16] Henry In: 國內可能用的
[00:54:17] Henry In: 還不是特別多
[00:54:19] Henry In: 但它的增長速度
[00:54:20] Henry In: 也是非常快
[00:54:21] Henry In: 像現在的話
[00:54:23] Henry In: 它一天會power
[00:54:25] 20 million
[00:54:26] Henry In: 就是2000萬的Fone口
[00:54:28] Henry In: 在一年前這個數字是
[00:54:31] Henry In: 100萬
[00:54:32] Henry In: 也就是說它這一年裡面
[00:54:34] Henry In: 成長了20歲
[00:54:35] Manqi: 可以講下LiveKit
[00:54:36] Manqi: 它主要是
[00:54:37] Manqi: 提供什麼能力嗎
[00:54:38] Manqi: 就是它提供語音上的
[00:54:39] Manqi: 有什麼能力
[00:54:40] Manqi: 或者說它的業務
[00:54:41] Manqi: 它的產品服務
[00:54:42] Manqi: 是什麼形態
[00:54:43] Henry In: 是從疫情時間開始做的
[00:54:46] Henry In: 它當時其實可能
[00:54:48] Henry In: 這開始的時候AI是關係不打的
[00:54:50] Henry In: 它是做的這個
[00:54:51] Henry In: 語音和視頻的
[00:54:53] Henry In: 實時傳輸
[00:54:54] Henry In: 用 WebRTC
[00:54:56] Henry In: 當時疫情期間
[00:54:57] Henry In: 就是大家這個
[00:54:58] Henry In: 都有這個 Remote 工作的需求
[00:55:00] Henry In: 對吧
[00:55:01] Henry In: 但是它的第一次
[00:55:02] Henry In: 就是AI方向的爆發
[00:55:03] Henry In: 就是我們剛才
[00:55:04] Henry In: 梳里麥若的時候提到的
[00:55:05] Henry In: GPT4O
[00:55:07] Henry In: 它是用它去做了
[00:55:08] Henry In: 後面語音傳輸的這一層
[00:55:10] Henry In: 然後後面的話
[00:55:11] Henry In: 它們就開始
[00:55:12] Henry In: 從底層
[00:55:13] Henry In: 往上
[00:55:14] Henry In: 去加強它們的這個產品的風速度
[00:55:16] Henry In: 所以現在的話
[00:55:17] Henry In: 其實已經可以
[00:55:18] Henry In: 很方便的
[00:55:19] Henry In: 用它的這個 SDK
[00:55:21] Henry In: 去創建一個語音的 agent
[00:55:23] Henry In: 那麼它們會幫你做好
[00:55:25] Henry In: 像這個 Turn Detaction
[00:55:28] Henry In: 這些 orchestration的工作
[00:55:30] 所以它則
[00:55:31] Manqi: 裡面其實是可以
[00:55:32] Manqi: 調不同的語音模型
[00:55:33] Manqi: 是什麼
[00:55:34] Manqi: 它不是Eleven Dabse那種
[00:55:35] Manqi: 它自己做一個語音模型
[00:55:36] Manqi: 然後聲稱它不是這種業務
[00:55:38] Henry In: 對像語音公司這塊的話
[00:55:39] Henry In: 應該可以分為兩個大類
[00:55:41] Henry In: 一個的話就是模型廠商
[00:55:42] Henry In: 像Eleven Dabse它
[00:55:44] Henry In: 其實可能一開始是模型廠商
[00:55:46] Henry In: 現在可能做得更廣的
[00:55:47] Henry In: 因為公司變大了
[00:55:48] Henry In: 像 OpenAI的話
[00:55:49] Henry In: 它也是就是
[00:55:50] Henry In: 偏模型廠商
[00:55:51] Henry In: 然後像 LiveKit它
[00:55:53] Henry In: 其實更偏的是
[00:55:54] Henry In: 就是基礎設施
[00:55:55] Henry In: 對
[00:55:56] 你剛剛說的
[00:55:57] Manqi: DabKit最開始那個業務
[00:55:58] Manqi: 聽著有一點像生亡的業務嗎
[00:55:59] Manqi: 對
[00:56:00] Henry In: 是有很大的想法性感
[00:56:01] Henry In: 除了像這個
[00:56:03] Henry In: OpenAI的這個 Advanced Voice Mode
[00:56:05] Henry In: 是後面是 LiveKit以外
[00:56:07] Henry In: 國外可能最貨的這種
[00:56:09] Henry In: 偏輕感陪伴的像
[00:56:10] Henry In: Cardic AI
[00:56:11] Henry In: 它背後還有就是
[00:56:13] Henry In: Elon Musk的Grock
[00:56:15] Henry In: 背後語音其實
[00:56:16] Henry In: 也都是 Power By LiveKit
[00:56:18] Henry In: 但我覺得這個故事
[00:56:19] Henry In: 非常有意思
[00:56:20] Henry In: 這也是當初為什麼
[00:56:21] Henry In: 我們決定投資它
[00:56:22] Henry In: 是因為它講就是
[00:56:23] Henry In: 它 Power By 12%
[00:56:25] Henry In: 5901的TRAFFIC
[00:56:26] Henry In: 然後大概每週
[00:56:27] Henry In: 能搶救一條人命回來
[00:56:29] Henry In: 它為什麼就打球
[00:56:30] Henry In: 要會需要 LiveKit呢
[00:56:31] Henry In: 是因為你打過去了以後
[00:56:32] Henry In: 然後它會發一條短信
[00:56:34] Henry In: 當你手機上
[00:56:35] Henry In: 然後你點開以後
[00:56:36] Henry In: 就可以實實的
[00:56:37] Henry In: 你用你的手機Stream
[00:56:38] Henry In: 你當時看到的情況
[00:56:40] Henry In: 和你的聲音
[00:56:41] 所以像那個
[00:56:42] Henry In: 911的那邊的
[00:56:43] Henry In: 那個就是
[00:56:44] Henry In: 它的那個
[00:56:45] Henry In: 工作人員
[00:56:46] Henry In: 就能看到你現場的情況是什麼樣的
[00:56:48] Henry In: 有的時候你需要心肺復俗
[00:56:49] Henry In: 它還能給你
[00:56:50] Henry In: 搞一個心肺復俗的教練過來
[00:56:52] Henry In: 當場教你看你現場的情況
[00:56:54] Henry In: 當場教你怎麼去做心肺復俗
[00:56:56] Manqi: 所以你說的這個
[00:56:57] Manqi: 就是搶救一條人命
[00:56:58] Manqi: 你指的是一些重點
[00:56:59] Manqi: 特別緊急的情況下
[00:57:00] Manqi: 它還是遠程
[00:57:01] Manqi: 給你有一些指導這種
[00:57:02] Manqi: 你剛才提到
[00:57:03] Manqi: Grog這些它的
[00:57:04] Manqi: power by這個LoveKate
[00:57:05] Manqi: 的意思就是它的
[00:57:06] Manqi: 基礎設施的部分
[00:57:07] Manqi: 於那基礎設施的部分
[00:57:08] Manqi: 就是這個LoveKate的提供的
[00:57:09] Manqi: 然後模型
[00:57:10] Manqi: 是Grog自己的
[00:57:11] Manqi: 語音模型的意思
[00:57:12] Henry In: 對
[00:57:13] Henry In: 接下來馬上會宣布的一個合作
[00:57:14] Henry In: 就是South Force
[00:57:15] Henry In: 外面國最大的CRM公司
[00:57:17] Henry In: 它的Agent Force的科福
[00:57:20] Henry In: 馬上就是這個Agent Voice Agent
[00:57:22] Henry In: 會是在LoveKate
[00:57:24] Henry In: 這個Agent的平台上面的
[00:57:26] 那這個平台上
[00:57:27] Manqi: 現在用了最多的模型
[00:57:28] Manqi: 還是以Love and Life是什麼
[00:57:29] Manqi: 這個上面有好幾家模型
[00:57:31] Henry In: 像OpenI的模型
[00:57:33] Henry In: 以Love and Life的模型
[00:57:34] Henry In: 還有CartyShare的模型
[00:57:36] Henry In: 也是之前
[00:57:37] Henry In: 聯合媒體到
[00:57:38] Henry In: 我們的投資的一家公司
[00:57:39] Henry In: 都會在用
[00:57:40] Henry In: 模型這塊
[00:57:41] Henry In: 可以稍微講一下
[00:57:42] Henry In: LiveKate的平台上面
[00:57:43] Henry In: 大概有兩個範式
[00:57:46] Henry In: 一種是Cuskate Voice Agent
[00:57:49] Henry In: 也就是說這個
[00:57:50] Henry In: Voice Agent它是
[00:57:51] Henry In: 拆成幾個環節的
[00:57:52] Henry In: 首先先是做STT
[00:57:54] Henry In: 就是Speech to Text
[00:57:56] Henry In: 的先把語音轉成文本
[00:57:58] Henry In: 然後文本去過大模型
[00:58:00] Henry In: 然後輸出再過
[00:58:03] Henry In: 文本轉語音
[00:58:04] Henry In: 才是
[00:58:05] Henry In: 這是一種方式
[00:58:06] Henry In: 你可以
[00:58:07] Henry In: 比如這樣的Agent
[00:58:08] Henry In: 好在LiveKate的平台上面
[00:58:10] Henry In: 那第二種方式的話
[00:58:11] Henry In: 就是Speech to Speech
[00:58:12] Henry In: 也就是
[00:58:13] Henry In: OpenAI他們的GPT RealTime
[00:58:16] Henry In: 就是它是直接從語音
[00:58:17] Henry In: 然後反而會給你語音
[00:58:19] Henry In: 所以它兩種都是
[00:58:21] Henry In: 兩種都有用回來
[00:58:22] Manqi: 用是不是因為
[00:58:23] Manqi: 前一種它
[00:58:24] Manqi: 其實比如說
[00:58:25] Manqi: 在有些場景
[00:58:26] Manqi: 它綜合成本
[00:58:27] Manqi: 是更好的
[00:58:28] Manqi: 反而它也夠用
[00:58:29] Manqi: 對其實這兩種的話
[00:58:30] Henry In: 我們可以看到
[00:58:31] Henry In: 首先大的判斷是
[00:58:33] Henry In: 終局一定是Speech to Speech
[00:58:35] Henry In: 對因為大家覺得
[00:58:36] Manqi: 這是更新的技術
[00:58:37] Manqi: 然後也效果更好
[00:58:38] Manqi: 效果更好
[00:58:39] Henry In: 對它能PKAP
[00:58:40] Henry In: 就比如說
[00:58:41] Henry In: 你的效果生亂
[00:58:42] Henry In: 你的情緒
[00:58:43] Henry In: 全部都在這個模型的
[00:58:44] Henry In: Context裡面
[00:58:45] Henry In: 但是
[00:58:46] Henry In: 現在還是有很多人
[00:58:48] Henry In: 會去使用前者
[00:58:49] Henry In: 就是這種Cuskate Mode
[00:58:51] Henry In: 拆成三個部分
[00:58:52] Henry In: 有幾個原因
[00:58:53] Henry In: 第一個原因是
[00:58:54] Henry In: 這種方式的
[00:58:55] Henry In: 可控性目前更好
[00:58:57] Henry In: 比如說你要
[00:58:58] Henry In: 加入一些這種
[00:58:59] Henry In: Guard Rails
[00:59:00] Henry In: 就是這種保護的這種機制
[00:59:02] Henry In: 那你可以在它
[00:59:03] Henry In: 變成本子的那個階段
[00:59:04] Henry In: 你去寫一些判斷的
[00:59:06] Henry In: 因為它畢竟是自負創
[00:59:07] Henry In: 你是沒有辦法
[00:59:08] Henry In: 在語音信號上面寫
[00:59:09] Henry In: 這些判斷的
[00:59:10] Henry In: 然後其次的話
[00:59:11] Henry In: 可能有些場景
[00:59:13] Henry In: 你也不需要它那麼向人
[00:59:15] Henry In: 比如說有的時候
[00:59:16] Henry In: 你去醫院
[00:59:17] Henry In: 你打一個電話
[00:59:18] Henry In: 然後你需要提供一些信息
[00:59:19] Henry In: 你知道你和AI在聊
[00:59:21] Henry In: 不那麼向人
[00:59:22] Henry In: 其實有的時候
[00:59:23] Henry In: 反而可能更好
[00:59:24] Henry In: 所以就是
[00:59:25] Henry In: 基於這些原因的話
[00:59:26] Henry In: 就是Cuskate這個方式
[00:59:27] Henry In: 還是有它自己的優勢
[00:59:29] Manqi: 然後我向補充
[00:59:30] Manqi: 問一下那個Boris的一些相關的
[00:59:31] Manqi: 其實之前我沒有聊到過
[00:59:32] Manqi: 你們有觀察到美國的
[00:59:34] Manqi: 一些核心的AI的
[00:59:36] Manqi: Top Labs都在加大對Boris的
[00:59:38] Manqi: 能力的投入
[00:59:39] Manqi: 就我理解的你覺得
[00:59:40] Manqi: Top Labs應該只是Google
[00:59:41] Manqi: 然後 OpenIG這些
[00:59:43] Manqi: 我覺得可能有兩個信號吧
[00:59:45] Henry In: 第一個信號的話
[00:59:46] Henry In: 是從現在有一類公司
[00:59:48] Henry In: 是專門給這些
[00:59:49] Henry In: Top AI Labs提供
[00:59:51] Henry In: 聲音的語音的數據
[00:59:53] Henry In: 這類公司
[00:59:54] Henry In: 就是最近成長的不錯
[00:59:55] Henry In: 農子也不錯
[00:59:56] Henry In: 有一個公司叫做 David AI
[00:59:58] Henry In: 它應該是最近
[01:00:00] Henry In: 幾個月內容的CUSA
[01:00:02] Henry In: 2500萬美元吧
[01:00:03] Henry In: 投資這邊是
[01:00:04] Henry In: 一個Signal
[01:00:05] Henry In: 另外一個Signal就是
[01:00:06] Henry In: OpenAI最近
[01:00:07] Henry In: 也可能是上週的事情
[01:00:10] Henry In: 然後它發布了GPT RealTime
[01:00:12] Henry In: MAPI的正式吧
[01:00:13] Henry In: 其實正式它在這個
[01:00:15] Henry In: 是去年10月份發布的
[01:00:17] Henry In: 所以大概哭了快整整一年的時間
[01:00:19] Henry In: 然後發布了現在的這個2.0版本
[01:00:21] Henry In: 然後它的主要的感濟
[01:00:23] Henry In: 可能分為幾個方面吧
[01:00:25] Henry In: 第一個方面的話
[01:00:26] Henry In: 就是更加的這個象人了
[01:00:28] Henry In: 像它的這個說話的語音與調
[01:00:30] Henry In: 然後表達的這個豐富程度
[01:00:32] Henry In: 然後以及就是它能夠
[01:00:35] Henry In: 很好的去執行開發者
[01:00:38] Henry In: 給的這個提示
[01:00:39] Henry In: 比如說你要更溫情
[01:00:41] Henry In: 或者你更職業化
[01:00:43] Henry In: 它都可以有
[01:00:44] Henry In: 很好的這種
[01:00:45] Henry In: Instruction Follow的能力
[01:00:46] Henry In: 這是第一
[01:00:47] Henry In: 然後第二的話
[01:00:48] Henry In: 它也可以就是
[01:00:49] Henry In: 更好的去理解
[01:00:51] Henry In: 比如說人家笑聲
[01:00:52] Henry In: 然後人家情緒
[01:00:54] Henry In: 然後以及它在說一半的時候
[01:00:56] Henry In: 比如說就換語音
[01:00:57] Henry In: 它也有更好的效果
[01:00:58] Henry In: 現在是不是像那個
[01:01:00] Manqi: Anthorpeak
[01:01:01] Manqi: 其實是不怎麼參與
[01:01:02] Manqi: 這個方面的競爭
[01:01:03] Manqi: 多摩泰的很做得比較少
[01:01:04] Manqi: 對我覺得這塊的話
[01:01:06] Henry In: 可能Anthorpeak沒有在排桌上
[01:01:08] Henry In: 還是GroG OpenAI
[01:01:11] Henry In: Google大版家
[01:01:12] Henry In: 我覺得Anthorpeak
[01:01:13] Henry In: 反正以前就是
[01:01:14] Henry In: O-In Coding了
[01:01:15] Henry In: 對我覺得語音這塊
[01:01:16] Manqi: 確實國內有很多開發者
[01:01:18] Manqi: 也用語音的模型表多
[01:01:20] Manqi: 像Mina Max像豆包的語音
[01:01:22] Manqi: 要去國內開發者
[01:01:23] Manqi: 用的表多的
[01:01:24] Manqi: 因為今年
[01:01:25] Manqi: 其實在中國的話
[01:01:26] Manqi: 也出現了挺多
[01:01:27] Manqi: 就是
[01:01:28] Manqi: Yorlalace語那種
[01:01:29] Manqi: 薄荷生成
[01:01:30] Manqi: 或者語音生成的
[01:01:31] Manqi: 這種Agent應用
[01:01:33] Manqi: 包括豆包自己也做了一個
[01:01:34] Manqi: 就你電腦豆包裡面
[01:01:35] Manqi: 它也可以直接
[01:01:36] Manqi: 給台片文章
[01:01:37] Manqi: 然後它給你生成一個
[01:01:38] Manqi: 35分鐘的薄殼
[01:01:39] Henry In: 對我覺得這塊
[01:01:40] Henry In: 咱們其實國內的模型
[01:01:41] Henry In: 在語音收藏這塊
[01:01:43] Henry In: 其實是處於領先地位的
[01:01:45] Henry In: 比如說Mina Max新發的這個
[01:01:47] Henry In: 語音模型
[01:01:48] Henry In: 像在Artificial Nanascist的
[01:01:50] Henry In: 榜單上面
[01:01:51] Henry In: 台名非常靠前
[01:01:53] Henry In: 可能在以Lalvan Labs之前的
[01:01:54] Henry In: 所以這塊的話
[01:01:55] Henry In: 可能在海外需要再
[01:01:57] Henry In: 更多的宣傳一下
[01:01:58] Manqi: 我們接下來可以想想
[01:01:59] Manqi: 就是記憶這塊的一些
[01:02:01] Manqi: 進展
[01:02:02] Manqi: 你今天也提到
[01:02:03] Manqi: 我覺得記憶是
[01:02:04] Manqi: Agent的圖靈很重要的一個方向
[01:02:05] Manqi: 然後這個領域可能
[01:02:06] Manqi: 也會有一些
[01:02:07] Manqi: 機會或者說
[01:02:08] Manqi: 有些自己做Agent
[01:02:09] Manqi: 或者做大模型的公司
[01:02:10] Manqi: 它們有些方面的動作和進展
[01:02:12] 我覺得我們可以從
[01:02:14] Henry In: 幾種記憶的類型
[01:02:16] Henry In: 然後它們是什麼
[01:02:17] Henry In: 然後它們怎麼能夠幫助
[01:02:19] Henry In: Agent的更好的
[01:02:20] Henry In: 完成它們的任務開始
[01:02:21] Henry In: 常見的記憶可能可以
[01:02:23] Henry In: 分為下面幾種一種的話
[01:02:25] Henry In: 就是說
[01:02:26] Henry In: 情景級
[01:02:27] Henry In: 舉例子就是說這個
[01:02:28] Henry In: 科普機器人
[01:02:29] Henry In: 它能記得就是上週
[01:02:30] Henry In: 你們倆兩個
[01:02:31] Henry In: 然後嘗試過這個解決方案
[01:02:33] Henry In: X
[01:02:34] Henry In: 那麼如果它
[01:02:35] Henry In: 記得住這個事的話
[01:02:36] Henry In: 作用就是它能避免
[01:02:37] Henry In: 比如說重複操作
[01:02:39] Henry In: 然後保持你們這個對話
[01:02:40] Henry In: 有連續性
[01:02:41] Henry In: 這個是情景級
[01:02:43] Henry In: 然後第二種的話
[01:02:44] Henry In: 就是說流程級
[01:02:46] Henry In: 那麼它這個是
[01:02:47] Henry In: 能夠記得住
[01:02:48] Henry In: 比如說搞定一個任務
[01:02:50] Henry In: 它需要完成步驟一二三四五
[01:02:52] Henry In: 它其實能夠獲得
[01:02:53] Henry In: 讓Agent獲得這個新的技能
[01:02:56] Henry In: 比如說做Demovs的Agent的技能
[01:02:58] Henry In: 就是說上週不屬的時候
[01:02:59] Henry In: 在第三步失敗了
[01:03:00] Henry In: 它就能避免
[01:03:01] Henry In: 比如說重複執行這個粗步驟
[01:03:03] Henry In: 然後學習有效的路徑是啥
[01:03:05] Henry In: 這個就比較適用於在自動化
[01:03:08] Henry In: 或者這個企業工作
[01:03:10] Henry In: 留這種多步制動的企業
[01:03:11] Henry In: 來學習怎麼完成一個工作
[01:03:13] Henry In: 第三種的話
[01:03:14] Henry In: 就是偏這種知識性的記憶
[01:03:17] Henry In: 它能存儲一些事實
[01:03:19] Henry In: 比如說有一個Agent
[01:03:21] Henry In: 它需要去查
[01:03:22] Henry In: 用戶勾勿的時候
[01:03:24] Henry In: 它有哪些打折
[01:03:27] Henry In: 能夠Apply
[01:03:28] Henry In: 它就需要去打折這個規則庫裡
[01:03:30] Henry In: 去查東西
[01:03:31] Henry In: 它去有規則庫的話
[01:03:33] Henry In: 它其實能夠其實是它的記憶的一部分
[01:03:35] Henry In: 它能夠減少它比如說
[01:03:37] Henry In: 有些幻覺
[01:03:38] Henry In: 想出來一個不存在的打折的規則
[01:03:41] Henry In: 最後一種的話
[01:03:42] Henry In: 就是偏這種角色記憶
[01:03:44] Henry In: 或者人格記憶
[01:03:45] Henry In: 它能夠記錄
[01:03:46] Henry In: 比如說一種人格
[01:03:48] Henry In: 或者說一種風格設定
[01:03:49] Henry In: 那這種的話
[01:03:50] Henry In: 就對於這種情感陪伴的很重要
[01:03:52] Henry In: 比如說你設定一個AI男朋友
[01:03:55] Henry In: 對吧
[01:03:56] Henry In: 它有一個
[01:03:57] Henry In: 它不能Out of Character
[01:03:58] Henry In: 它得保持它就這種交流的風格
[01:04:00] Henry In: 有這種長期的這種關係的感覺
[01:04:03] Henry In: 所以就說
[01:04:04] Henry In: 像剛才這四種記憶的話
[01:04:06] Henry In: 就是理性選擇
[01:04:08] Henry In: 合理的應用在你的Agent裡面
[01:04:10] Henry In: 有可能你是比如我們就做Business
[01:04:12] Henry In: 你不需要這種人格記憶
[01:04:14] Henry In: 你可能就需要比如說
[01:04:16] Henry In: 工作流記憶
[01:04:17] Henry In: 然後這個知識記憶
[01:04:19] Henry In: 所以記憶的話
[01:04:20] Henry In: 我覺得對於提升Agent的在
[01:04:22] Henry In: 特定的這種應用場景
[01:04:23] Henry In: 它的能力是起到一個
[01:04:24] Henry In: 很大很大的作用
[01:04:26] Henry In: 提到這個公司的話
[01:04:28] Henry In: 我們接觸比較多的一家
[01:04:31] Henry In: 然後也是最近成長比較快的一家
[01:04:33] Henry In: 叫做Latang
[01:04:35] Henry In: 然後它的這個兩個創始人
[01:04:37] Henry In: 也是Berkeley的
[01:04:39] Henry In: 兩個PhDB業以後
[01:04:40] Henry In: 然後創立的
[01:04:42] Henry In: 那麼他們的現在的這個產品的話
[01:04:45] Henry In: 就是專門幫助Agent的開發者
[01:04:48] Henry In: 開發這種
[01:04:49] Henry In: 他們叫做Stateful Agent
[01:04:51] Henry In: 就是有狀態的知道體
[01:04:54] Henry In: 然後他們還有一個很有意思的概念呢
[01:04:56] Henry In: 就叫做Sleep Time Compute
[01:04:59] Henry In: 因為可能大家都很熟悉
[01:05:01] Henry In: 就是這個Test Time Compute
[01:05:02] Henry In: 就是說你在做推理的時候
[01:05:04] Henry In: 你多寫一些投根這樣能夠幹得更好
[01:05:07] Henry In: 他們這個不是推理的時候
[01:05:09] Henry In: 多圖圖看
[01:05:10] Henry In: 而是他們說是在你的AI整個系統
[01:05:13] Henry In: 沒有用戶來查詢你
[01:05:15] Henry In: 或者說和你交互的時候
[01:05:16] Henry In: 他來花一些投根
[01:05:18] Henry In: 做一些之前的這些理解
[01:05:20] Henry In: 比如說你可能舉個例子
[01:05:22] Henry In: 你白天開了好多會
[01:05:23] Henry In: 然後你晚上夜生冷靜的時候
[01:05:26] Henry In: Sleep Time的時候
[01:05:27] Henry In: 你來回憶一下
[01:05:28] Henry In: 來Process一下
[01:05:29] Henry In: 你白天開的那些會
[01:05:31] Henry In: 然後把這些東西
[01:05:32] Henry In: 就是變成你的這個
[01:05:34] Henry In: 一些學習的一些內容
[01:05:35] Henry In: 對吧或者說一些你的這些InScience
[01:05:38] Henry In: 所以他本來是在睡覺的時候
[01:05:40] Henry In: 去花投肯
[01:05:41] Henry In: 然後去把一些
[01:05:42] Henry In: 之前的一些記憶
[01:05:43] Henry In: 整理成最有用的這些東西
[01:05:45] Henry In: 知識然後存下來
[01:05:46] Henry In: 所以我覺得這個是LITAR
[01:05:48] Henry In: 比較有意思的地方
[01:05:49] Henry In: 這個公司是怎麼拼的
[01:05:50] Manqi: METTTALITAR
[01:05:52] Henry In: 我本來以為這種東西
[01:05:54] Manqi: 是沒有單獨的公司做的
[01:05:55] Manqi: 我以為是做Agent的公司
[01:05:56] Manqi: 會自己做記憶的部分
[01:05:57] Manqi: 這個是不是會更出流一點
[01:05:59] Manqi: 比如說Malice他可能會自己做
[01:06:01] Manqi: 比如說Davent他可能會自己做
[01:06:02] Manqi: 這個記憶的部分
[01:06:03] Manqi: 包括一些陪伴類的Agent
[01:06:05] Manqi: 我覺得這個是
[01:06:07] Henry In: 很所有的時候比如早期的時候
[01:06:09] Henry In: 我覺得大家都會有一個探索的過程
[01:06:11] Henry In: 就是沒有人知道
[01:06:13] Henry In: 比如說這個記憶到底怎麼做比較好
[01:06:15] Henry In: 這個時候就會發現過海
[01:06:17] Henry In: 個險期等
[01:06:18] Henry In: 每個人就是會按照自己的這個場景
[01:06:20] Henry In: 去比我的自己的記憶的這個模塊
[01:06:22] Henry In: 但我覺得隨著大家對於記憶的
[01:06:25] Henry In: 哪種記憶應該怎麼
[01:06:26] Henry In: 又摸索的比較清楚以後
[01:06:28] Henry In: 我覺得可能會有一個相對標準化的產品
[01:06:30] Henry In: 想拿著這樣的產品出來
[01:06:32] Henry In: 然後幫大家把這些藏活類
[01:06:34] Henry In: 活都幹了這樣這個Agent的開發者
[01:06:36] Henry In: 能夠真正聚焦在
[01:06:38] Henry In: 自己的Agent它的核心進入力產品
[01:06:40] Henry In: 那像Data這種它是
[01:06:42] Manqi: 圖去提供一個記憶的標準化
[01:06:44] Manqi: 這種技術的模塊
[01:06:45] Manqi: 它這個會涉及到數據的問題嗎
[01:06:47] Manqi: 就是比如說Nyta去服務一個Agent公司
[01:06:50] Manqi: 然後這個Agent的公司的用戶
[01:06:52] Manqi: 給到Agent的一些數據
[01:06:54] Manqi: 如果Nyta要去優化
[01:06:55] Manqi: 就是它的記憶表現的話
[01:06:56] Manqi: 那這個Agent的公司
[01:06:57] Manqi: 應該把這個數據給Nyta而不給用
[01:06:59] Henry In: 它是需要能夠讀取這個對話內容的
[01:07:03] Henry In: 因為它的這個交後方式是這樣的
[01:07:06] Henry In: 就是它會有單獨的一個模型
[01:07:08] Henry In: 用戶需要定義一下
[01:07:09] Henry In: 你的這個記憶的Skima是什麼樣的
[01:07:12] Henry In: 比如說我是誰
[01:07:14] Henry In: 我的偏好是什麼
[01:07:15] Henry In: 我的生日是什麼
[01:07:16] Henry In: 然後你像定義這麼樣一個格式
[01:07:19] Henry In: 然後這樣的話
[01:07:20] Henry In: 你在對話的時候
[01:07:21] Henry In: 它就會自動地去更新你定義的這些信息
[01:07:26] Henry In: 然後並且自動地就是說
[01:07:28] Henry In: 在你需要這些的時候
[01:07:29] Henry In: 把它塞到創下的例子
[01:07:30] Henry In: 那我覺得這個
[01:07:31] Manqi: 如果它長期就往下去發展
[01:07:32] Manqi: 它可能會不會設計到
[01:07:33] Manqi: 就是一個數據的
[01:07:35] Manqi: 我到底給多少
[01:07:36] Manqi: 我給不給的問題
[01:07:37] Manqi: 我想到了一個例子
[01:07:38] Manqi: 就是在中國之前
[01:07:39] Manqi: 有很多科技創業公司
[01:07:41] Manqi: 是做高級赤能輔助駕駛的
[01:07:43] Manqi: 那他們的客戶就是車起
[01:07:45] Manqi: 然後他們想要去持續的幫車起
[01:07:47] Manqi: 優化他們給車起的
[01:07:49] Manqi: 智能駕駛的方案
[01:07:50] Manqi: 它其實需要一些這個司機的數據的
[01:07:53] Manqi: 但是在以前
[01:07:54] Manqi: 就是這個問題
[01:07:55] Manqi: 就是好像業里的一個
[01:07:56] Manqi: 比較老大男的問題
[01:07:57] Manqi: 就是到底給多少
[01:07:58] Manqi: 以及怎麼給
[01:07:59] Manqi: 可能你去服務每個車起的時候
[01:08:01] Manqi: 你都得單獨談
[01:08:02] Manqi: 當然車起是非常大的客戶了
[01:08:04] Manqi: 它不是那種分散的下有客戶
[01:08:06] Manqi: 可能它也和
[01:08:07] Manqi: 就是你最後這個生態裡面
[01:08:08] Manqi: 你每一層
[01:08:09] Manqi: 它的集中度有關
[01:08:10] Manqi: 對我最近可能又回到了
[01:08:11] Henry In: 剩下文工程這個問題
[01:08:13] Henry In: 因為剛才邁起提到
[01:08:15] Henry In: 就是說給不給多少
[01:08:17] Henry In: 剩下文工程本質上
[01:08:18] Henry In: 就是說糟糕
[01:08:19] Henry In: 什麼東西應該進入這個剩下文
[01:08:22] Henry In: 什麼樣的信息
[01:08:23] Henry In: 應該進入這個剩下文
[01:08:24] Henry In: 你說這個還是一個技術上的考慮
[01:08:26] Manqi: 我剛說那些車起
[01:08:27] Manqi: 給不給給多少
[01:08:28] Manqi: 就車起會覺得這個數據
[01:08:29] Manqi: 我給你給了之後
[01:08:30] Manqi: 你優化了這個方案
[01:08:31] Manqi: 然後因為你的客戶又不進入我
[01:08:33] Manqi: 你還服務別的車起
[01:08:34] Manqi: 車起是很大的企業
[01:08:35] Manqi: 所以他們是這種強勁
[01:08:36] Manqi: 你真的角度去思考的
[01:08:37] Manqi: 然後還有一些是會覺得
[01:08:39] Manqi: 這個數據會有些敏感的問題
[01:08:41] Manqi: 我覺得還好
[01:08:42] Henry In: 因為他們可能不太會遇到
[01:08:43] Henry In: 那種競爭關係
[01:08:45] Henry In: 我覺得可能就是跟現在
[01:08:46] Manqi: AZN的整個應用市場
[01:08:48] Manqi: 本身它表分散有關
[01:08:49] Manqi: 對
[01:08:50] Manqi: 也比較多樣化
[01:08:51] Manqi: 那你看到大公司
[01:08:52] Manqi: 在絕方面的一些動作是什麼樣
[01:08:53] Manqi: 因為其實像OPENI
[01:08:54] Manqi: 它今年不就是
[01:08:56] Manqi: 有像一個這種
[01:08:57] Manqi: 去義工能嗎
[01:08:58] Manqi: 我覺得OPENI的節奏
[01:08:59] Henry In: 我覺得OPENI的這個技藝的工能
[01:09:01] Henry In: 其實有一個比較長足的改進
[01:09:04] Henry In: 對
[01:09:05] Henry In: 可以舉個例子
[01:09:06] Henry In: 比如說
[01:09:07] Henry In: 今天我的媽媽
[01:09:09] Henry In: 給我做了我最喜歡的
[01:09:12] Henry In: 天典T-R-M-SOO
[01:09:14] Henry In: 以前的話
[01:09:15] Henry In: 可能是
[01:09:16] Henry In: 它直接把這整句話
[01:09:18] Henry In: 塞到這個Touchy PT的技藝裡面
[01:09:20] Henry In: 現在的話好像會差一踩
[01:09:23] Henry In: 比如說它不會直接說我
[01:09:25] Henry In: 它可能會說
[01:09:26] Henry In: 這很熱的生日
[01:09:27] Henry In: 是就越是8號
[01:09:28] Henry In: 這第一句
[01:09:29] Henry In: 記憶
[01:09:30] Henry In: 第二句記憶的話
[01:09:31] Henry In: 就是說
[01:09:32] Henry In: 很熱喜歡吃T-R-M-SOO
[01:09:33] Henry In: 第三句記憶的話
[01:09:34] Henry In: 就是說
[01:09:35] Henry In: 很熱的媽媽在
[01:09:36] Henry In: 很熱的生日那天
[01:09:37] Henry In: 給它做了它喜歡的
[01:09:38] Henry In: T-R-M-SOO
[01:09:39] Henry In: 它就會
[01:09:40] Henry In: 你看這樣的話
[01:09:41] Henry In: 它這個記憶的可用度
[01:09:43] Henry In: 在後面再去做茶旋的時候
[01:09:45] Henry In: 就會比直接把那一句話生進去
[01:09:47] Henry In: 也好很多
[01:09:48] Henry In: 因為你只會把那句話生進去的時候
[01:09:49] Henry In: 首先不知道我是誰
[01:09:50] Henry In: 其實不知道我的生日是那天
[01:09:52] Henry In: 大模型它隨著自己的能力進化
[01:09:54] Manqi: 它能自己解決自己的問題嗎
[01:09:56] Manqi: 就模型本身
[01:09:57] Manqi: 我覺得現在的大模型
[01:09:59] Henry In: 自己前進的方向
[01:10:00] Henry In: 其實和記憶是兩條單獨的線
[01:10:04] Henry In: 現在大模型
[01:10:05] Henry In: 如果說能力上和記憶比較相關的
[01:10:08] Henry In: 就是上下文長度的提升
[01:10:10] Henry In: 我們可能可以看到
[01:10:11] Henry In: 就剩下文還在不斷的加大
[01:10:13] Henry In: 但是我覺得對於上下文的使用的話
[01:10:16] Henry In: 即使上下文長度的不斷加大
[01:10:19] Henry In: 還是要非常的謹慎
[01:10:20] Henry In: 因為它不是免費的午餐
[01:10:23] Henry In: 因為這個不管是Cost
[01:10:25] Henry In: 還有它這個性能
[01:10:27] Henry In: 其實都會隨著你
[01:10:28] Henry In: 上下文長度增加而下降
[01:10:30] Manqi: 對剛才你也提到了一下
[01:10:31] Manqi: 上下文工程
[01:10:32] Manqi: 這個做開始就是
[01:10:33] Manqi: 我覺得是你們A.J.House
[01:10:34] Manqi: 就是你們有連接的成員
[01:10:35] Manqi: Angela Kappersley
[01:10:36] Manqi: 他代活的一個概念
[01:10:38] Manqi: 因為他之前我自己寫了一篇長文
[01:10:40] Manqi: 就是在講這個
[01:10:41] Manqi: Contacts Engineering
[01:10:42] Manqi: 像這個和記憶的關係是什麼
[01:10:44] Manqi: 我可以理解成記憶師
[01:10:45] Manqi: Contacts Engineering
[01:10:46] Manqi: 要其中要做的一件事情嗎
[01:10:48] Manqi: 對
[01:10:49] Henry In: 因為記憶最終要使用的話
[01:10:50] Henry In: 他也得再到上下文裡面
[01:10:52] Henry In: 所以可以認為
[01:10:53] Henry In: 就是說記憶的話
[01:10:54] Henry In: 是上下文工程的一部分
[01:10:57] Henry In: 我覺得上下文工程的話
[01:10:59] Henry In: 就是他的本質就是
[01:11:01] Henry In: 什麼東西
[01:11:02] Henry In: 什麼信息
[01:11:03] Henry In: 應該進入上下文
[01:11:04] Henry In: 什麼不應該
[01:11:05] Henry In: 那麼他的話有兩個
[01:11:07] Henry In: 循環
[01:11:08] Henry In: 有個內循環
[01:11:09] Henry In: 一個外循環
[01:11:10] Henry In: 內循環的話
[01:11:11] Henry In: 就是說這一次生成的時候
[01:11:12] Henry In: 什麼信息應該進入上下文
[01:11:15] Henry In: 然後外循環就是說
[01:11:17] Henry In: 長期來說
[01:11:18] Henry In: 我們如何逐漸地去
[01:11:20] Henry In: 改進我們
[01:11:21] Henry In: 把正確的信息
[01:11:22] Henry In: 塞進上下文的能力
[01:11:23] Henry In: 像這些努力
[01:11:24] Manqi: 現在其實也都是
[01:11:25] Manqi: 工具鏈的公司在做
[01:11:26] Manqi: 或者說他不是模型直接相關的
[01:11:29] Manqi: 對 他不是模型直接相關的
[01:11:30] Henry In: 補全他的
[01:11:31] Manqi: 殘缺身體的部分
[01:11:32] Manqi: 就是模型是跟大腦相關的
[01:11:34] Manqi: 對
[01:11:35] Henry In: 對
[01:11:36] Henry In: 這種
[01:11:37] Henry In: Long-Turve memory
[01:11:38] Henry In: 怎麼使用這些
[01:11:39] Henry In: 都是屬於
[01:11:40] Henry In: 其實對於人來說
[01:11:41] Henry In: 他是大腦的一部分
[01:11:42] Henry In: 但現在對於大腦
[01:11:43] Henry In: 想來說
[01:11:44] Henry In: 他其實是和大腦型
[01:11:46] Henry In: 是本身是分開的
[01:11:47] Henry In: 現在也是一個外接的
[01:11:49] Henry In: 硬盤那種感覺
[01:11:50] Henry In: 接下來還想跟你
[01:11:51] Manqi: 就展開了一下
[01:11:52] Manqi: 就是你剛才提到的
[01:11:53] Manqi: 這個
[01:11:54] Manqi: 評估的部分
[01:11:55] Manqi: 而且評估的部分
[01:11:56] Manqi: 確實也發生了最近
[01:11:57] Manqi: 就是比較受關注的交易
[01:11:59] Manqi: 做一些腦米提到的
[01:12:00] Manqi: Open I11
[01:12:01] Manqi: 美元收購了
[01:12:02] Manqi: Stats-C
[01:12:03] Manqi: 這個公司的創生
[01:12:04] Manqi: 也是個印度人好像
[01:12:05] Manqi: 反正是個印度意吧
[01:12:06] Manqi: 這個可以講講
[01:12:07] Manqi: 就比如說
[01:12:08] 就評估相關的工具
[01:12:10] Manqi: 這個我覺得他是
[01:12:11] Manqi: 比較容易被第三方
[01:12:12] Manqi: 或者標準化的
[01:12:13] Manqi: 應該是有一些創意的機會
[01:12:15] Manqi: 是吧
[01:12:16] Henry In: 評估是一個
[01:12:17] Henry In: 很有意思的
[01:12:18] Henry In: 很有這個
[01:12:19] Henry In: 爭議度的一個話題
[01:12:21] Henry In: 就是這個是一個
[01:12:22] Henry In: 矛盾點是
[01:12:23] Henry In: 在於說
[01:12:24] Henry In: 大部分人都會認為
[01:12:26] Henry In: 評估或者說意料
[01:12:27] Henry In: 這個事情很重要
[01:12:28] Henry In: 但是大部分公司
[01:12:29] Henry In: 現在都不會好好的
[01:12:30] Henry In: 去做意料
[01:12:31] Henry In: 這是個矛盾所在
[01:12:33] Henry In: 我給舉個例子
[01:12:34] Henry In: 這個其實是來自於
[01:12:36] Henry In: 就是我們和
[01:12:37] Henry In: LiveK的合作過程中
[01:12:38] Henry In: 獲得了一個例子
[01:12:39] Henry In: 他們一個比較大的客戶
[01:12:40] Henry In: 這已經不說名字了
[01:12:41] Henry In: 然後他們是
[01:12:42] Henry In: 做一個VACA
[01:12:43] Henry In: 做客服
[01:12:44] Henry In: 他們就發現這個客服
[01:12:46] Henry In: 他們這個打電話的時候
[01:12:47] Henry In: 很容易提前掛電話
[01:12:49] Henry In: 然後這個用戶體驗就很差
[01:12:50] Henry In: 所以他們就在
[01:12:51] Henry In: promp在裡面
[01:12:52] Henry In: 你不要那麼早掛電話
[01:12:54] Henry In: 他加完這句話以後
[01:12:55] Henry In: 他是離發覆之前
[01:12:57] Henry In: 他做了啥啥事
[01:12:58] Henry In: 當然他的工程師
[01:12:59] Henry In: 就照了這個新版門
[01:13:00] Henry In: 打了三四個電話
[01:13:01] Henry In: 感覺好像
[01:13:02] Henry In: 就是比之前
[01:13:03] Henry In: 掛的是要把
[01:13:04] Henry In: 那麼一點了
[01:13:05] Henry In: 就發覆
[01:13:06] Henry In: 然後就不說了
[01:13:07] Henry In: 再到Portarcher
[01:13:08] Henry In: 所以你看看
[01:13:09] Henry In: 這個公司其實還滿大的
[01:13:10] Henry In: 他不是這個創業團隊
[01:13:12] Henry In: 就是他其實開發這個
[01:13:13] Henry In: A證子的時候
[01:13:14] Henry In: 都是這種
[01:13:15] Henry In: 我們一個
[01:13:16] Henry In: 這個創業團隊
[01:13:17] Henry In: 他沒有一個
[01:13:18] Henry In: 說很嚴格的
[01:13:19] Henry In: 要科學的
[01:13:20] Henry In: 做評價的這麼一個環境
[01:13:22] Henry In: 對吧
[01:13:23] Henry In: 比如說至少好幾百次
[01:13:24] Henry In: 對吧
[01:13:25] Henry In: 然後再去布數
[01:13:26] Henry In: 他很不就是
[01:13:27] Henry In: 所以這個事情很不便
[01:13:28] Henry In: 可以看到的是
[01:13:29] Henry In: 不光是有專門做
[01:13:31] Henry In: 醫療的公司
[01:13:32] Henry In: 包括像其他的
[01:13:33] Henry In: 比如說像是
[01:13:34] Henry In: LiveKid這樣的
[01:13:35] Henry In: WiseA證子的平台
[01:13:37] Henry In: 他自己
[01:13:38] Henry In: 就是接下來
[01:13:39] Henry In: 加入這個醫療的這個組件
[01:13:41] Henry In: 對他們來說
[01:13:42] Henry In: 也是非常重要的
[01:13:43] Henry In: 這個組件
[01:13:44] Henry In: 大概幹什麼樣的事情呢
[01:13:45] Henry In: 就是說
[01:13:46] Henry In: 我如果有一個新的版本的
[01:13:48] Henry In: WiseA證子想要上限
[01:13:49] Henry In: 對吧
[01:13:50] Henry In: 上限之前
[01:13:51] Henry In: 我先有可能各種
[01:13:52] Henry In: 各樣的情景
[01:13:53] Henry In: 各種各樣的數據級
[01:13:54] Henry In: 你先讓我
[01:13:55] Henry In: 跑個幾百次電話
[01:13:57] Henry In: 然後看你這些
[01:13:59] Henry In: Live下來了以後
[01:14:00] Henry In: 你把我分析一下
[01:14:01] Henry In: 到底改進的情況怎麼樣
[01:14:03] Henry In: 你告訴我
[01:14:04] Henry In: 改進了沒有
[01:14:05] Henry In: 以後我再有信心的
[01:14:06] Henry In: 去上限這個新的功能
[01:14:08] Manqi: 你剛才說就是
[01:14:09] Manqi: 大家覺得重要
[01:14:10] Manqi: 但是不做原因是因為
[01:14:11] Manqi: 他很難做
[01:14:12] Manqi: 他這個長難在什麼地方
[01:14:13] 因為你要從蘋果
[01:14:14] Henry In: 你需要數據
[01:14:15] Henry In: 你需要可能是人工去
[01:14:17] Henry In: 標註一個數據級
[01:14:19] Henry In: 那麼這個
[01:14:20] 你越負擔的人物
[01:14:21] Henry In: 這個成本也高
[01:14:22] Henry In: 另外一個就是你
[01:14:23] Henry In: 這個團隊開發團隊
[01:14:25] Henry In: 對於你
[01:14:26] Henry In: 比如得出來的這個數據級
[01:14:27] Henry In: 有沒有共識
[01:14:28] Henry In: 還有一個很搞笑的情況就是說
[01:14:30] Henry In: 有的人他花了很長時間
[01:14:32] Henry In: 去做了一個數據級
[01:14:34] Henry In: 然後最後醫療說
[01:14:35] Henry In: 我變好了
[01:14:36] Henry In: 或者變差了
[01:14:37] Henry In: 他自己不信
[01:14:38] Henry In: 他會說
[01:14:39] Henry In: 雖然我們的數據級說
[01:14:40] Henry In: 我變好了
[01:14:41] Henry In: 但我感覺他變差了
[01:14:43] Manqi: 我聽說到這個
[01:14:44] Manqi: 就是哪些任務
[01:14:45] Manqi: 會相對更好蘋果
[01:14:46] Manqi: 哪些任務會不好蘋果
[01:14:47] Manqi: 大圓模型的一些任務的
[01:14:48] Manqi: 就是非對稱信
[01:14:49] Manqi: 就有的你是深層
[01:14:50] Manqi: 一個東西很難
[01:14:51] Manqi: 但你蘋果它是表容易的
[01:14:52] Manqi: 那有的任務就屬於
[01:14:54] Manqi: 你蘋果它
[01:14:55] Manqi: 可能比你做出這個任務
[01:14:56] Manqi: 花了時間還多
[01:14:57] Manqi: 舉個例子
[01:14:58] Henry In: 比如說
[01:14:59] Henry In: 我們可以看到
[01:15:00] OpenAI
[01:15:01] Henry In: DPC
[01:15:02] Henry In: 他們做強化學習
[01:15:04] 用的任務是啥
[01:15:06] Henry In: 就是Coding和數學
[01:15:08] Henry In: 編程和數學
[01:15:09] Henry In: 之所以用這些任務
[01:15:10] Henry In: 就是因為
[01:15:11] Henry In: 他們有很好的蘋果的信號
[01:15:13] Henry In: 這樣的和模型
[01:15:14] Henry In: 能夠最大程度
[01:15:15] Henry In: 從這些任務的蘋果中去學習
[01:15:17] Henry In: 像這些任務
[01:15:18] Henry In: 就屬於相對來說
[01:15:19] Henry In: 比較容易蘋果的
[01:15:21] Henry In: 比較難蘋果的
[01:15:22] Henry In: 比如說主觀性比較高的任務
[01:15:24] Henry In: 或者任務本身
[01:15:25] Henry In: 複雜度比較高的
[01:15:26] Henry In: 都會相對來說
[01:15:27] Henry In: 更難蘋果一些
[01:15:28] Manqi: 接下來就是想討論一下
[01:15:29] Manqi: 就是你們看到
[01:15:30] Manqi: 這個AZN2LIN的
[01:15:31] Manqi: 它的整個商業的情況
[01:15:33] Manqi: 比如包括市場規模一樣
[01:15:34] Manqi: 然後未來可能
[01:15:35] Manqi: 會是一個什麼樣的
[01:15:36] Manqi: 生態格局
[01:15:37] Manqi: 我們可以先說
[01:15:38] Manqi: 會市場規模吧
[01:15:39] Manqi: 就是它未來可能
[01:15:40] Manqi: 會是一般
[01:15:41] Nawmisha: 如果我們看全球的軟件市場的話
[01:15:43] Nawmisha: 它一年大概
[01:15:44] Nawmisha: 能賣6500億美元
[01:15:46] Nawmisha: 相對來說
[01:15:47] Nawmisha: Dive Tools
[01:15:48] Nawmisha: 它可能就是
[01:15:49] Nawmisha: 分走其中一塊嘛
[01:15:50] Nawmisha: 根據我們看的一些
[01:15:52] Nawmisha: 上市的一些公司
[01:15:53] Nawmisha: 然後看到
[01:15:54] Nawmisha: 這個行業Standard
[01:15:55] Nawmisha: 大概是
[01:15:56] Nawmisha: 中低各位數的百分比
[01:15:57] Nawmisha: 如果我們從
[01:15:58] Nawmisha: Ballpark
[01:15:59] Nawmisha: 大概差不多
[01:16:00] Nawmisha: 就是200到300億美元
[01:16:02] Nawmisha: 那個規模
[01:16:03] Nawmisha: 然後
[01:16:04] Nawmisha: AZN這一波
[01:16:05] Nawmisha: 它其實整個
[01:16:06] Nawmisha: 遊戲規模
[01:16:07] Nawmisha: 就是
[01:16:08] Nawmisha: 它其實整個
[01:16:09] Nawmisha: 遊戲規則
[01:16:10] Nawmisha: 其實有點改變
[01:16:11] Nawmisha: 之前我們看
[01:16:12] Nawmisha: 一個紅山的預測
[01:16:13] Nawmisha: 就是說
[01:16:14] Nawmisha: 它AI會把
[01:16:15] Nawmisha: 就是軟件市場的
[01:16:16] Nawmisha: 天花板
[01:16:17] Nawmisha: 就是有一個退高
[01:16:18] Nawmisha: 然後會把
[01:16:19] Nawmisha: 它從6000多億
[01:16:20] Nawmisha: 到
[01:16:21] Nawmisha: 退到一個
[01:16:22] Nawmisha: 10萬億美元的級別
[01:16:23] Nawmisha: 它主要的原因是
[01:16:24] Nawmisha: 因為它可以
[01:16:25] Nawmisha: 它扣
[01:16:26] Nawmisha: 就是切入一些
[01:16:27] Nawmisha: 服務業的這個蛋糕
[01:16:29] Nawmisha: 然後它會把原來
[01:16:30] Nawmisha: 就是靠
[01:16:31] Nawmisha: 人力的這種服務
[01:16:33] Nawmisha: 轉化成一個
[01:16:34] Nawmisha: 可以靠軟件的一個服務
[01:16:35] Nawmisha: 然後如果
[01:16:36] Nawmisha: 這個判斷的方向
[01:16:37] Nawmisha: 如果是對的話
[01:16:38] Nawmisha: 那如果我們去看
[01:16:39] Nawmisha: 就是為AI
[01:16:40] Nawmisha: AZN提供
[01:16:41] Nawmisha: 這個武器裝備的
[01:16:42] Nawmisha: AZN tooling的這個市場
[01:16:44] Nawmisha: 它也會有一個
[01:16:45] Nawmisha: 大的一個
[01:16:46] Nawmisha: Dapop
[01:16:47] Nawmisha: Apply
[01:16:48] Nawmisha: 一個Lace的這樣一個
[01:16:49] Nawmisha: Presentage的話
[01:16:50] Nawmisha: 那可能
[01:16:51] Nawmisha: 比如說
[01:16:52] Nawmisha: 站到這個
[01:16:53] Nawmisha: 新市場的5%
[01:16:54] Nawmisha: 這樣算的話
[01:16:55] Nawmisha: 可能是長期的市場規模
[01:16:56] Nawmisha: 可能會達到
[01:16:57] Nawmisha: 2100到5000億美元
[01:16:58] Nawmisha: 那跟現在
[01:16:59] Nawmisha: 2300億的開發者工具
[01:17:00] Nawmisha: 相比
[01:17:01] Nawmisha: 大概正好
[01:17:02] Nawmisha: 是一個10到15%
[01:17:03] Nawmisha: 被的一個增長
[01:17:04] Nawmisha: 所以我們其實
[01:17:05] Nawmisha: 覺得就是
[01:17:06] Nawmisha: 一個瓜費一個
[01:17:07] Nawmisha: 存量的市場
[01:17:08] Nawmisha: 更多是在
[01:17:09] Nawmisha: 創造一個增量市場
[01:17:10] Nawmisha: 這個市場
[01:17:11] Nawmisha: 你會出現
[01:17:12] Nawmisha: 那種特別大的公司嗎
[01:17:13] Manqi: 因為有的市場
[01:17:14] Manqi: 它是很大
[01:17:15] Manqi: 但是裡面可能
[01:17:16] Manqi: 沒有
[01:17:17] Manqi: 都很大
[01:17:18] Manqi: 會有年收入到
[01:17:19] Nawmisha: 100億美元的公司嗎
[01:17:20] Nawmisha: 對
[01:17:21] Nawmisha: 我覺得其實
[01:17:22] Nawmisha: 是已經在發生的事情
[01:17:23] Nawmisha: 然後我們其實可以
[01:17:24] Nawmisha: 從三個
[01:17:25] Nawmisha: 找我來看
[01:17:26] Nawmisha: 然後比如說
[01:17:27] Nawmisha: 第一個就是說
[01:17:28] Nawmisha: 這個市場
[01:17:29] Nawmisha: 它得有多大
[01:17:30] Nawmisha: 那我們剛剛
[01:17:31] Nawmisha: 也用了這個開發者
[01:17:33] Nawmisha: 就帶兔子公司
[01:17:34] Nawmisha: 做一個參考
[01:17:35] Nawmisha: 公司奧特
[01:17:36] Nawmisha: 它最近一年的收入
[01:17:37] Nawmisha: 大概是在
[01:17:38] Nawmisha: 20億美元
[01:17:39] Nawmisha: 然後
[01:17:40] Nawmisha: 推了它
[01:17:41] Nawmisha: 是一個
[01:17:42] Nawmisha: 雲童性去頭
[01:17:43] Nawmisha: 它高峰式的收入
[01:17:44] Nawmisha: 大概去年
[01:17:45] Nawmisha: 大概是在
[01:17:46] Nawmisha: 40億左右
[01:17:47] 那我們覺得
[01:17:48] Nawmisha: 就是AI
[01:17:49] Nawmisha: 的經濟可能會
[01:17:50] Nawmisha: 是一個
[01:17:51] Nawmisha: 實際經濟的
[01:17:52] Nawmisha: 實際被
[01:17:53] Nawmisha: 那服務於
[01:17:54] Nawmisha: 這個新經濟的
[01:17:55] Nawmisha: 這些
[01:17:56] Nawmisha: 因法比如說
[01:17:57] Nawmisha: 智能體的驗證
[01:17:58] Nawmisha: 然後
[01:17:59] Nawmisha: 它的
[01:18:00] Nawmisha: 市場空間
[01:18:01] Nawmisha: 也像剛才說的嘛
[01:18:02] Nawmisha: 可能會
[01:18:03] Nawmisha: 10倍上
[01:18:04] Nawmisha: 那如果說
[01:18:05] Nawmisha: 奧特能到
[01:18:06] Nawmisha: 這個200億的話
[01:18:07] Nawmisha: 那AI agent
[01:18:08] Nawmisha: 身份與調度
[01:18:09] Nawmisha: 可能就是一個
[01:18:10] Nawmisha: 數百億
[01:18:11] Nawmisha: 即便的市場
[01:18:12] Nawmisha: 相對方向的產品
[01:18:14] Nawmisha: 是
[01:18:15] Nawmisha: Compose-ill
[01:18:16] Nawmisha: 就現在
[01:18:17] Nawmisha: 比較AI內體的公司
[01:18:18] Nawmisha: 然後第二個話
[01:18:19] Nawmisha: 就是說可能
[01:18:20] Nawmisha: 也不是說
[01:18:21] Nawmisha: 所有的去頭都會
[01:18:22] Nawmisha: 被顛覆嘛
[01:18:23] Nawmisha: 也是在看
[01:18:24] Nawmisha: Paradigm Shift
[01:18:25] Nawmisha: 它這個
[01:18:26] Nawmisha: 範生在哪裡
[01:18:27] 那可能我們覺得
[01:18:28] Nawmisha: 真正的機會
[01:18:29] Nawmisha: 是來自於一些
[01:18:30] Nawmisha: AI agent帶來的
[01:18:31] Nawmisha: 一些全新的需求
[01:18:32] Nawmisha: 比如說
[01:18:33] Nawmisha: Observability
[01:18:34] Nawmisha: 就是AI agent的
[01:18:36] Nawmisha: 客觀測性
[01:18:37] Nawmisha: 傳統的這個
[01:18:38] Nawmisha: 看的是CPU內存
[01:18:39] Nawmisha: 但Agent
[01:18:40] Nawmisha: 可能更多的是看
[01:18:41] Nawmisha: 一個角色的
[01:18:42] Nawmisha: 電路
[01:18:43] Nawmisha: 那 DataDop
[01:18:44] Nawmisha: 大概是年數
[01:18:45] Nawmisha: 超過20億美元
[01:18:46] Nawmisha: 它就是做
[01:18:47] Nawmisha: 系統客觀測嘛
[01:18:48] Nawmisha: 那將來
[01:18:49] Nawmisha: 比如說面向
[01:18:50] Nawmisha: Agent的
[01:18:51] Nawmisha: 觀測平台
[01:18:52] Nawmisha: 可能
[01:18:53] Nawmisha: 也可能要更大
[01:18:54] Nawmisha: 然後比如說
[01:18:55] Nawmisha: Bring Trust
[01:18:56] Nawmisha: 就是把智能體的
[01:18:57] Nawmisha: 執行過程
[01:18:58] Nawmisha: 去做一個
[01:18:59] Nawmisha: 拆開
[01:19:00] Nawmisha: 就它不僅僅是看
[01:19:01] Nawmisha: 就是
[01:19:02] Nawmisha: 機的指標
[01:19:03] Nawmisha: 更多是可以讓你看
[01:19:04] Nawmisha: 這個回放
[01:19:05] Nawmisha: 調視AI的行為
[01:19:06] 然後另外一個就是
[01:19:08] Nawmisha: 就是說
[01:19:09] Nawmisha: Agent的一個
[01:19:10] Nawmisha: 實事通信
[01:19:11] Nawmisha: 然後推流它
[01:19:12] Nawmisha: 其實做人和人之間
[01:19:13] Nawmisha: 同學嘛
[01:19:14] Nawmisha: 它的收入大概
[01:19:15] Nawmisha: 40億元
[01:19:16] Nawmisha: 那AI agent
[01:19:17] Nawmisha: 就是人和
[01:19:18] Nawmisha: Agent
[01:19:19] Nawmisha: 然後和系統之間的
[01:19:20] Nawmisha: 交互
[01:19:21] Nawmisha: 就是LatinC的要求
[01:19:22] Nawmisha: 會更高
[01:19:23] Nawmisha: 然後對它的
[01:19:24] Nawmisha: 可能會發
[01:19:25] Nawmisha: 就會化的狀態
[01:19:26] Nawmisha: 會更複雜
[01:19:27] Nawmisha: 然後
[01:19:28] Nawmisha: 這個領域
[01:19:29] Nawmisha: 就是像
[01:19:30] Nawmisha: 剛剛提到的
[01:19:31] Nawmisha: 基本上也是
[01:19:32] Nawmisha: 在構建下一代的
[01:19:33] Nawmisha: 這個專用的一個
[01:19:34] Nawmisha: 通信層
[01:19:35] Nawmisha: 然後還有
[01:19:36] Nawmisha: 比如說像
[01:19:37] Nawmisha: CowCow
[01:19:38] Nawmisha: 這種自主編碼的
[01:19:39] Nawmisha: AutoNunus的
[01:19:40] Nawmisha: CodingAgent
[01:19:41] Nawmisha: 就是有點像
[01:19:42] Nawmisha: Gayhouse
[01:19:43] Nawmisha: Gayhouse
[01:19:44] Nawmisha: Gayhouse
[01:19:45] Nawmisha: Gayhouse
[01:19:46] Nawmisha: Gayhouse
[01:19:47] Nawmisha: Gayhouse
[01:19:48] Nawmisha: Gayhouse
[01:19:49] Nawmisha: Gayhouse
[01:19:50] Nawmisha: 它主要是
[01:19:51] Nawmisha: 面向是自主寫
[01:19:52] Nawmisha: 代碼的一個
[01:19:53] Nawmisha: 就是這種的AI agent
[01:19:54] Nawmisha: 它自己不會去
[01:19:55] Nawmisha: 替代
[01:19:56] Nawmisha: Gayhouse
[01:19:57] Nawmisha: 它會以拉動
[01:19:58] Nawmisha: 以系列的
[01:19:59] Nawmisha: 就是
[01:20:00] Nawmisha: 它們也在做這種
[01:20:01] Nawmisha: 可以組裝那種
[01:20:02] Nawmisha: Agent
[01:20:03] Nawmisha: 模塊
[01:20:04] Nawmisha: 和一個集成
[01:20:05] Nawmisha: 就是可以
[01:20:06] Nawmisha: 像
[01:20:07] Nawmisha: 偏樂高一樣
[01:20:08] Nawmisha: 把AI去裝進
[01:20:09] Nawmisha: 它們執行的
[01:20:10] Nawmisha: 現有的工作流
[01:20:11] Nawmisha: 這樣子去看的話
[01:20:13] Nawmisha: 什麼樣的公司
[01:20:14] Nawmisha: 可能
[01:20:15] Nawmisha: 最有可能去做成
[01:20:16] Nawmisha: 白衣美金
[01:20:17] Nawmisha: 它們一般
[01:20:18] Nawmisha: 應該不會是
[01:20:19] Nawmisha: 做這個
[01:20:20] Nawmisha: 工具的拼湊
[01:20:21] Nawmisha: 然後更多的是
[01:20:22] Nawmisha: 能不能形成
[01:20:23] Nawmisha: 一個網絡的效應
[01:20:24] Nawmisha: 和數據的畢類
[01:20:25] Nawmisha: 比如說它
[01:20:26] Nawmisha: 有沒有去
[01:20:27] Nawmisha: 有一個
[01:20:28] Nawmisha: 就是自己
[01:20:29] Nawmisha: 要去包含
[01:20:30] Nawmisha: Walve
[01:20:31] Nawmisha: 一個數據的畢環
[01:20:32] Nawmisha: 越用越好
[01:20:33] Nawmisha: 從越越高
[01:20:34] Nawmisha: 成本越低
[01:20:35] Nawmisha: 然後它有沒有去卡住一個
[01:20:36] Nawmisha: 我做得關鍵節點
[01:20:38] Nawmisha: 比如說
[01:20:39] Nawmisha: Lifet它是
[01:20:40] Nawmisha: 做實質充信
[01:20:41] Nawmisha: Brenchust
[01:20:42] Nawmisha: 奧姿勢的
[01:20:43] Nawmisha: 然後它
[01:20:44] Nawmisha: 調用量越大的話
[01:20:45] Nawmisha: 它的數據可能
[01:20:46] Nawmisha: 是越之前的
[01:20:47] Nawmisha: 就越用越長出一個
[01:20:48] Nawmisha: 就是白衣的公司
[01:20:50] Manqi: 你說這個
[01:20:51] Manqi: 我覺得其實它
[01:20:52] Manqi: 有兩類機會
[01:20:53] Manqi: 一個就是
[01:20:54] Manqi: 你剛才提到的一些
[01:20:55] Manqi: 已經存在
[01:20:56] Manqi: 或者說
[01:20:57] Manqi: 它是在
[01:20:58] Manqi: 做這個身份
[01:20:59] Manqi: 驗證的
[01:21:00] Manqi: Octa
[01:21:01] Manqi: 還有做通信的
[01:21:02] Manqi: 推流
[01:21:03] Manqi: 做官策的
[01:21:04] Manqi: Data Dog
[01:21:05] Manqi: 其實理論上
[01:21:06] Manqi: 它們也可以在自己
[01:21:07] Manqi: 本身的這種客戶
[01:21:09] Manqi: 關係的器物上
[01:21:10] Manqi: 它可以加AI
[01:21:11] Manqi: 之前二級
[01:21:12] Manqi: 市場有
[01:21:13] Manqi: 一些比較火的標題
[01:21:14] Manqi: 也是類似這種
[01:21:15] Manqi: Fotoshow
[01:21:16] Manqi: 然後另類可能就是
[01:21:17] Manqi: AI原生的新的公司
[01:21:18] Manqi: 比如說
[01:21:19] Manqi: 做Agent的
[01:21:20] Manqi: 狀態官策的
[01:21:21] Manqi: 跟Agent的
[01:21:22] Manqi: 想管的身份認證
[01:21:23] Manqi: 做Agent的通信
[01:21:24] Manqi: 最後是想請
[01:21:25] Manqi: 很瑞和
[01:21:26] Manqi: 來分享一下
[01:21:27] Manqi: 就是在歸股的
[01:21:28] Manqi: AI創業社區的
[01:21:29] Manqi: 一些情況
[01:21:30] Manqi: 比如說大家
[01:21:31] Manqi: 是一個什麼樣的
[01:21:32] Manqi: 氛圍是怎麼運轉的
[01:21:33] Manqi: 因為就是類似
[01:21:34] Manqi: 你們剛剛說的
[01:21:35] Manqi: Compose
[01:21:36] Manqi: 這種公司
[01:21:37] Manqi: 它們是從印度去了美國
[01:21:38] Manqi: 現在其實
[01:21:39] Manqi: 也有很多中國的
[01:21:40] Manqi: AI團隊
[01:21:41] Manqi: 它一開始
[01:21:42] Manqi: 就是一個
[01:21:43] Manqi: 全球化的定位
[01:21:44] Manqi: 像歸股
[01:21:45] Manqi: 舊金山
[01:21:46] Manqi: 肯定是大家
[01:21:47] Manqi: 會去的
[01:21:48] Manqi: 比較多的地方
[01:21:49] Manqi: 你們自己也接觸了
[01:21:50] Manqi: 比較多的
[01:21:51] Manqi: 國內的創始人
[01:21:52] Manqi: 你們可以講講
[01:21:53] Manqi: 就是在彎曲
[01:21:54] Manqi: 這個創業生態
[01:21:55] Manqi: 是怎麼互動起來的
[01:21:56] Manqi: 對
[01:21:57] Nawmisha: 我覺得其實
[01:21:58] Nawmisha: 它其實是
[01:21:59] Nawmisha: 我們有
[01:22:00] Nawmisha: 會 host
[01:22:01] Nawmisha: 各種不同的
[01:22:02] Nawmisha: 活動
[01:22:03] Nawmisha: 那一部分
[01:22:04] Nawmisha: 就是我們比較
[01:22:05] Nawmisha: 大的手中式
[01:22:06] Nawmisha: 在 researcher
[01:22:08] Nawmisha: 然後針對一些
[01:22:09] Nawmisha: researcher的活動
[01:22:10] Nawmisha: 比如說像 Henry
[01:22:11] Nawmisha: 他將會
[01:22:12] Nawmisha: 辦一些
[01:22:13] Nawmisha: 比較 technical discussions
[01:22:14] Nawmisha: 會把所有的 AI lab
[01:22:16] Nawmisha: 一些特別
[01:22:14] Nawmisha: 社區
[01:22:15] Nawmisha: 照自己來
[01:22:16] Nawmisha: 會做進行一個討論
[01:22:17] Nawmisha: 那他成在的形式
[01:22:18] Nawmisha: 可能是 paper reading
[01:22:19] Nawmisha: 然後還有
[01:22:20] Nawmisha: 我們像辦的
[01:22:21] Nawmisha: 一些大的
[01:22:22] Nawmisha: 哈克坊呢
[01:22:23] Nawmisha: 這種的話
[01:22:24] Nawmisha: 就是那種
[01:22:25] Nawmisha: 大的 AI lab 去合伴
[01:22:26] Nawmisha: 要不然就是去
[01:22:27] Nawmisha: 合一些比較
[01:22:28] Nawmisha: 有意思的創業公司
[01:22:29] Nawmisha: 然後有
[01:22:30] Nawmisha: 尤其是像
[01:22:31] Nawmisha: 做這種
[01:22:32] Nawmisha: Daptor Agent 做的公司
[01:22:33] Nawmisha: 這樣一個
[01:22:34] Nawmisha: 是有一個 marketing 的一個作用
[01:22:35] Nawmisha: 然後同時
[01:22:36] Nawmisha: 他們也可以
[01:22:37] Nawmisha: 去收集一些
[01:22:38] Nawmisha: 一線的這種
[01:22:39] Nawmisha: 對他們產品的反饋
[01:22:40] Nawmisha: 然後當然我們
[01:22:41] Nawmisha: 其實也跟
[01:22:42] Nawmisha: 非常多
[01:22:43] Nawmisha: 華人創業者
[01:22:44] Nawmisha: 有很多的合作
[01:22:45] Nawmisha: 就是之前
[01:22:46] Nawmisha: 拉伯爾
[01:22:47] Nawmisha: 然後 Melvin
[01:22:48] Nawmisha: 就是我覺得
[01:22:49] Nawmisha: 他是個非常有問小
[01:22:50] Nawmisha: 然後
[01:22:51] Nawmisha: 產品
[01:22:52] Nawmisha: Sense
[01:22:53] Nawmisha: 做他們的 launch 的時候
[01:22:54] Nawmisha: 我們團隊
[01:22:55] Nawmisha: 也去
[01:22:56] Nawmisha: 給他們
[01:22:57] Nawmisha: 就是支持
[01:22:58] Nawmisha: 幫他們帶了一些
[01:22:59] Nawmisha: 比如說
[01:23:00] Nawmisha: 當地的
[01:23:01] Nawmisha: 比如說 designer
[01:23:02] Nawmisha: 一些 local user
[01:23:03] Nawmisha: 然後去收集一些飛back
[01:23:04] Nawmisha: 基本上
[01:23:05] Nawmisha: 從國內
[01:23:06] Nawmisha: 然後到美國的一些公司
[01:23:07] Nawmisha: 其實都是相對來說
[01:23:08] Nawmisha: 就比較成長期的
[01:23:09] Nawmisha: 一個階段
[01:23:10] Nawmisha: 就已經有一些
[01:23:11] Nawmisha: 比較好的書記
[01:23:12] Nawmisha: 可以去看
[01:23:13] Nawmisha: 像 Office Clip 別說
[01:23:14] Nawmisha: 我們經常去合作了一個公司
[01:23:16] Nawmisha: 他們就是做長時間簡短的
[01:23:17] Nawmisha: 然後我們自己
[01:23:18] Nawmisha: 本身
[01:23:19] Nawmisha: H&H House 團隊
[01:23:20] Nawmisha: 所有的媒體簡介
[01:23:21] Nawmisha: 都是用 Office Clip
[01:23:22] Nawmisha: 因為我們
[01:23:23] Nawmisha: 跟一些
[01:23:24] Nawmisha: 本地的音樂
[01:23:25] Nawmisha: 同時的 community
[01:23:26] Nawmisha: 也是有一些合作
[01:23:27] Nawmisha: 所以也是可以
[01:23:28] Nawmisha: 在不同的角度
[01:23:29] Nawmisha: 不僅僅是說
[01:23:30] Nawmisha: Developer
[01:23:31] Nawmisha: 也跟一些 application
[01:23:32] Nawmisha: 的 users
[01:23:33] Nawmisha: 和這些
[01:23:34] Nawmisha: Pinion Leaders
[01:23:35] Nawmisha: 也有一些比較深度的早有
[01:23:36] Nawmisha: 我想問一下
[01:23:37] Manqi: 就是23年的
[01:23:38] Manqi: 這個 chat
[01:23:39] Manqi: GPT熱潮來了之後
[01:23:40] Manqi: 從什麼時候開始
[01:23:41] Manqi: 你們會感覺到
[01:23:42] Manqi: 國內去的團隊會變多了
[01:23:43] Henry In: 我覺得今年
[01:23:44] Henry In: 明顯感覺是
[01:23:46] 很多的
[01:23:47] Henry In: 很多是吧
[01:23:48] Henry In: 對 非常多
[01:23:49] 我覺得可能還看到一個區式
[01:23:51] Nawmisha: 例如多的中國創業者
[01:23:53] Nawmisha: 可能就是來美國創業
[01:23:55] Nawmisha: 尤其是他們做
[01:23:56] Nawmisha: 如果是做一個
[01:23:57] Nawmisha: Application的產品
[01:23:59] Nawmisha: 中國的創業者
[01:24:00] Nawmisha: 它其實是非常有
[01:24:01] Nawmisha: 產品
[01:24:02] Nawmisha: Sense和Application的
[01:24:03] Nawmisha: 觸覺的
[01:24:04] Nawmisha: 比如說如果我們去看
[01:24:05] Nawmisha: H&H House
[01:24:06] Nawmisha: 也是
[01:24:07] Nawmisha: 三番這邊
[01:24:08] Nawmisha: 比較有名的
[01:24:09] Nawmisha: 一個 Salary的Program
[01:24:10] Nawmisha: 過去三四屆
[01:24:11] Nawmisha: 我覺得至少都有
[01:24:13] Nawmisha: 30%
[01:24:14] Nawmisha: 20%到30%的
[01:24:16] Nawmisha: 就是他們的
[01:24:17] Nawmisha: Founding Team
[01:24:18] Nawmisha: 是中國背景的
[01:24:19] Nawmisha: 不是ABC
[01:24:20] Nawmisha: 中國中國背景
[01:24:21] Nawmisha: 而且他們的
[01:24:22] Nawmisha: Rap New Number
[01:24:23] Nawmisha: 增長得都很不錯
[01:24:24] Nawmisha: 然後通過
[01:24:25] Nawmisha: 就是這種
[01:24:26] Nawmisha: 復華器
[01:24:27] Nawmisha: 然後實現一個專行
[01:24:28] Nawmisha: 就是說他們有一些
[01:24:29] Nawmisha: 也是在中國之前
[01:24:30] Nawmisha: 創業
[01:24:31] Nawmisha: 但是從新
[01:24:32] Nawmisha: 就通過這個
[01:24:33] Nawmisha: 復華器的這種途徑
[01:24:34] Nawmisha: 去實現一個
[01:24:35] Nawmisha: 在美國
[01:24:36] Nawmisha: 去建立
[01:24:37] Nawmisha: 它的Connection
[01:24:38] Nawmisha: 然後去增長
[01:24:39] Nawmisha: 這樣的一個
[01:24:40] Nawmisha: 打法吧
[01:24:41] Nawmisha: 我們前幾期
[01:24:42] Manqi: 聊過有一個創始人
[01:24:43] Manqi: 就是麥克風
[01:24:44] Manqi: 是Falloround的
[01:24:45] Manqi: 創始人
[01:24:46] Manqi: 他就參加過HFZR
[01:24:47] Manqi: 包括國內
[01:24:48] Manqi: 有一個公司
[01:24:49] Manqi: 叫A Studio
[01:24:50] Manqi: 他也參加過
[01:24:51] Manqi: 我看他也分享過
[01:24:52] Manqi: 而且就是我後來發現
[01:24:53] Manqi: 這個復華器
[01:24:54] Manqi: 比較特別的一點
[01:24:55] Manqi: 是就是你
[01:24:56] Manqi: 從公開信息裡
[01:24:57] Manqi: 是查不到
[01:24:58] Manqi: 誰參加過這個復華器的
[01:24:59] Manqi: 他的歷史的
[01:25:00] Manqi: 就是參與者的
[01:25:01] Manqi: 名單是
[01:25:02] Manqi: 非公開的
[01:25:03] Manqi: 但是他會
[01:25:04] Manqi: 規股的投資人
[01:25:05] Manqi: 包括國內的
[01:25:06] Manqi: 一些投資人
[01:25:07] Manqi: 最後那個
[01:25:08] Manqi: Demondade的時候
[01:25:09] Manqi: 他們
[01:25:10] Manqi: 因為每一屆
[01:25:11] Nawmisha: 其實也只有十個公司
[01:25:12] Nawmisha: 而且他們
[01:25:13] Nawmisha: 就只收這種
[01:25:14] Nawmisha: Serial Andro
[01:25:15] Nawmisha: 就之前創業的
[01:25:16] Nawmisha: 所以本身
[01:25:17] Nawmisha: 他們的孤製
[01:25:18] Nawmisha: 就是產品團隊
[01:25:19] Nawmisha: 方面比較
[01:25:20] Nawmisha: 相對於
[01:25:21] Nawmisha: 這種MIC這種
[01:25:22] Nawmisha: 會更加Ready一些
[01:25:23] Nawmisha: 就是更
[01:25:24] Nawmisha: 更Experience一些
[01:25:25] Henry In: 我想說的是
[01:25:26] Henry In: 我感覺
[01:25:27] Henry In: 這一波AI創業
[01:25:28] Henry In: 就是華人創業者
[01:25:29] Henry In: 還是有很大的優勢的
[01:25:30] Henry In: 一個的話
[01:25:31] Henry In: 就是Nelmi剛才提到的
[01:25:32] Henry In: 我覺得
[01:25:33] Henry In: To C的產品力
[01:25:34] Henry In: 其實
[01:25:35] Henry In: 比很多美國團隊都要強
[01:25:36] Henry In: 第二個的話
[01:25:37] Henry In: 我覺得就是執行力
[01:25:38] Henry In: 因為現在
[01:25:39] Henry In: 大部分的
[01:25:40] Henry In: Agent Startup
[01:25:41] Henry In: 他們的這個
[01:25:42] Henry In: 護城盒
[01:25:43] Henry In: 來自於兩方面吧
[01:25:44] Henry In: 一方面
[01:25:45] Henry In: 是如果你是
[01:25:46] Henry In: Agent
[01:25:47] Henry In: 那麼你在這個垂直領域裡面
[01:25:48] Henry In: 有沒有專家的知識
[01:25:50] Henry In: 這是一方面
[01:25:51] Henry In: 另外一方面
[01:25:52] Henry In: 就是存執行力
[01:25:53] Henry In: 所以這方面
[01:25:54] Henry In: 我覺得歷史上
[01:25:55] Henry In: 咱們還是比較強的
[01:25:56] Henry In: 其實我跟
[01:25:57] Manqi: 就是去過那邊的一些人
[01:25:58] Manqi: 包括在那邊那些團隊交流
[01:25:59] Manqi: 我有一個模糊的印象
[01:26:00] Manqi: 我不知道對不對
[01:26:01] Manqi: 就是我感覺
[01:26:02] Manqi: 在美國的
[01:26:03] Manqi: 大部分主流的團隊
[01:26:04] Manqi: 可能還是在
[01:26:05] Manqi: 突避領域
[01:26:06] Manqi: 做AI創業的
[01:26:07] Manqi: 創業公司是最多的
[01:26:08] Manqi: 而且他們可能會有
[01:26:09] Manqi: 明確的退出路徑
[01:26:10] Manqi: 就必定是
[01:26:11] Manqi: 我要自己犯人到多大
[01:26:12] Manqi: 其實我可以
[01:26:13] Manqi: 到印程度
[01:26:14] Manqi: 被一個大公司收購
[01:26:16] Manqi: 而中國的
[01:26:17] Manqi: 一些野心伯伯的創始人
[01:26:19] Manqi: 他們其實提供了
[01:26:20] Manqi: 就是對投資機構來說的
[01:26:21] Manqi: 一個比較稀缺的類型吧
[01:26:24] Manqi: 就是真的想做的
[01:26:25] Manqi: 挺大的那種
[01:26:26] Manqi: Tusey的應用
[01:26:27] Manqi: 我覺得Miles就有了
[01:26:28] Manqi: 這個意思
[01:26:29] Henry In: 我覺得中美這邊是有互補的
[01:26:30] Henry In: 對
[01:26:31] Henry In: 就是歸古這邊
[01:26:32] Henry In: 做Tube
[01:26:33] Henry In: 實在是
[01:26:34] Henry In: 收藏環境實在是
[01:26:35] Henry In: 太好了
[01:26:36] Henry In: 所以就是做Tube的人
[01:26:37] Henry In: 會非常多
[01:26:38] Henry In: 然後做Tusey的人會少很多
[01:26:39] Henry In: 做Tusey硬件的人
[01:26:40] Henry In: 就是非常非常非常少
[01:26:42] Henry In: 像國內的話
[01:26:43] Henry In: 就可能會反過來
[01:26:44] Henry In: 那像Henry這邊
[01:26:45] Manqi: 因為你就是組織一些
[01:26:46] Manqi: 技術的討論比較多嗎
[01:26:47] Manqi: 最近我什麼
[01:26:48] Manqi: 你自己覺得比較好玩的
[01:26:50] Manqi: 或者說比較新印的
[01:26:51] Manqi: 這種技術趨勢嗎
[01:26:52] Manqi: 幾個方向吧
[01:26:53] Henry In: 可能也不能算是新營了
[01:26:55] Henry In: 因為我覺得這個趨勢
[01:26:56] Henry In: 是從可能去年9月份
[01:26:57] Henry In: 或者說
[01:26:58] Henry In: 去年Depth一個發布以後開始的
[01:27:00] Henry In: 就是這個
[01:27:01] Henry In: RL的第二春
[01:27:02] Henry In: 對
[01:27:03] Henry In: 然後現在大家就是
[01:27:04] Henry In: 有很多創業公司
[01:27:05] Henry In: 可能可以分為兩大類
[01:27:07] Henry In: 第一大類的話
[01:27:08] Henry In: 就是在去做這種
[01:27:10] Henry In: RL的環境
[01:27:12] Henry In: 然後賣給這些
[01:27:14] Henry In: 在訓練技術大模型的公司
[01:27:16] Henry In: 然後還有另外一類的話
[01:27:18] Henry In: 就是他們做一個
[01:27:21] Henry In: 叫做RLS Service
[01:27:22] Henry In: 他們去幫那些大企業
[01:27:25] Henry In: 去趕盡大模型
[01:27:27] Henry In: 在他們內部的那些
[01:27:28] Henry In: 應用場景
[01:27:29] Henry In: 然後通過RL的方式
[01:27:30] Henry In: 來趕盡他們的這個
[01:27:32] Henry In: 不管是模型的能力
[01:27:33] Henry In: 還是他們AZ的能力
[01:27:35] Henry In: 所以我們也在這邊
[01:27:36] Henry In: 做了很多相關的技術討論
[01:27:39] Henry In: 也許我們下次
[01:27:40] Manqi: 可以展開了這個
[01:27:41] Manqi: 那今天非常感謝
[01:27:43] Manqi: Hairway and Lamy做課完結聊
[01:27:44] Manqi: 分享了他們在
[01:27:45] Manqi: 規股怎麼去組織
[01:27:47] Manqi: 這種技術人員創始人的
[01:27:49] Manqi: 社區已經看到的一些趨勢
[01:27:51] Manqi: 那我們今天是
[01:27:52] Manqi: 比較詳細的聊了
[01:27:54] Manqi: AZENTIC TOOLING
[01:27:55] Manqi: 也就是
[01:27:56] Manqi: 智能體的工具
[01:27:57] Manqi: 練和工具相的機會
[01:27:58] Manqi: 這個領域
[01:27:59] Manqi: 有非常多的
[01:28:00] Manqi: 核心的大公司在投入
[01:28:01] Manqi: 然後也有很多
[01:28:02] Manqi: 新的第三方的創業的機會
[01:28:04] Manqi: 然後我們講了很多
[01:28:06] Manqi: 規股的一些公司
[01:28:07] Manqi: 準度教授
[01:28:08] Manqi: 突教授
[01:28:09] Manqi: 那雖然
[01:28:10] Manqi: 也目前來看
[01:28:11] Manqi: 在國內可能並沒有
[01:28:12] Manqi: 那麼好的去
[01:28:13] Manqi: 複製的方法
[01:28:14] Manqi: 但另一方面
[01:28:15] Manqi: 現在整個AI創業的
[01:28:16] Manqi: 氛圍是非常全球化的
[01:28:17] Manqi: 那也有可能
[01:28:18] Manqi: 大家能去
[01:28:19] Manqi: 規股去美國
[01:28:20] Manqi: 做一些教育和創業
[01:28:22] Manqi: 然後我覺得
[01:28:23] Manqi: 可能到時候
[01:28:24] Manqi: 大家也可以合作和教育
[01:28:26] Manqi: 今天謝謝兩位
[01:28:27] Manqi: 各位掰掰
[01:28:28] Henry In: 謝謝萬七
[01:28:30] 本期節目就到這裡
[01:28:31] Manqi: 歡迎收聽
[01:28:32] Manqi: 如果你對今天聊的話
[01:28:33] Manqi: 題有觀察好奇會疑問
[01:28:35] Manqi: 歡迎在評論區分享想法
[01:28:36] Manqi: 這也會成為我們節目的
[01:28:38] Manqi: 一部分讓整個討論更完整
[01:28:39] Manqi: 你也可以把我們的節目
[01:28:40] Manqi: 分享給對這個話題感興趣的朋友
[01:28:42] Manqi: 歡迎推薦更多
[01:28:43] Manqi: 你想聽的主題和嘉賓
[01:28:45] Manqi: 你可以從小宇宙
[01:28:46] Manqi: 蘋果泡的Cost
[01:28:47] Manqi: 等曲到
[01:28:48] Manqi: 關注晚點聊Late Talk
[01:28:49] Manqi: 也歡迎關注我們的
[01:28:50] Manqi: 公眾號
[01:28:51] Manqi: 晚點Late Post
[01:28:52] Manqi: 下期再見