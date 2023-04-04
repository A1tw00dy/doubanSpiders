# python爬虫简单练手：豆瓣音乐top250

## 使用的库bs4和requests:
1. 通过requests发送网络请求
2. 通过bs4的beautifulsoup解析html

## 页面分析：
1. top250一共有10页，每页25个
2. 每个专辑都是一个table标签，里面有个a标签的title属性含有专辑名和歌手名

```python
from bs4 import BeautifulSoup
import requests

url = "https://music.douban.com/top250?start="
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62"
}
for num in range(0,250,25):
    res = requests.get(url+str(num),headers=header)
    html = res.text
    content = BeautifulSoup(html,"html.parser")
    tables = content.find_all("table")
    for table in tables:
        a = table.find("a")["title"]
        print(a)

```
## 最终结果
    结果只有247个，有几页没有25个专辑
```bash
Jason Mraz - We Sing. We Dance. We Steal Things.
Coldplay - Viva La Vida
陈绮贞 - 华丽的冒险
周杰伦 - 范特西
五月天 - 後。青春期的詩
孙燕姿 - 是时候
Lenka - Lenka
王若琳 - Start from Here
陈绮贞 - 旅行的意义
陈绮贞 - 太阳
Glen Hansard... - Once (Soundtrack)
Keren Ann - Not Going Anywhere
Green Day - American Idiot
张震岳 Csun Yuk - 思念是一种病
苏打绿 - 無與倫比的美麗
张悬 - 亲爱的...我还不知道
张悬 - 城市
Damien Rice - O
Green Day - Wake Me Up When September Ends
周杰伦 - 叶惠美
周杰伦 - 七里香
Adele - 21
张悬 - My Life Will...
王菲 - 寓言
苏打绿 - 你在煩惱什麼
林宥嘉 - 感官/世界
Nirvana - Nevermind
周杰伦 - 八度空间
周杰伦 - Jay
Coldplay - Parachutes
孙燕姿 - 我要的幸福
陈绮贞 - 还是会寂寞
Avril Lavigne - Let Go
周杰伦 - 十一月的萧邦
方大同 - 橙月
苏打绿 - 小宇宙
蔡健雅 - 若你碰到他
Lady & Bird - Lady & Bird
万能青年旅店 - 万能青年旅店
Linkin Park - Meteora
James Blunt - Back To Bedlam
苏打绿... - 苏打绿同名专辑
梁静茹 - 静茹&情歌 别再为他流泪
林宥嘉 - 美妙生活
Yann Tiersen - Le Fabuleux destin d'Amélie Poulain
王若琳 - Joanna & 王若琳
Tamas Wells - A Plea En Vendredi
田馥甄 Hebe - To Hebe
孙燕姿 - 逆光
王菲 - 只爱陌生人
Chris Garneau - Music For Tourists
孙燕姿 - The Moment
陈奕迅 - 七
苏打绿 - 春·日光
盧廣仲 - 100种生活
梁静茹 - 崇拜
陈绮贞 - 陈绮贞精选
Joe Hisaishi - 菊次郎の夏
Taylor Swift - Fearless
Mika - Life In Cartoon Motion
陈奕迅 - H³M
林宥嘉 - 神秘嘉宾
Bruno Coulais - Les Choristes
范晓萱&100% - 赤子
Damien Rice - 9
王菲 - 将爱
曹方 - 遇见我
李志 - 梵高先生
方大同 - Timeless 可啦思刻
周杰伦 - 依然范特西
孙燕姿 - 风筝
孙燕姿 - 完美的一天
The Weepies - Say I Am You
陶喆 - 黑色柳丁
Avril Lavigne - Under My Skin
孙燕姿 - Stefanie
Lady Gaga - The Fame
Jason Mraz - Mr. A-Z
五月天 - 为爱而生
Daniel Powter - Daniel Powter
Jason Mraz - I'm Yours
许巍 Wei Xu - 时光·漫步
朴树 - 生如夏花
周杰伦 - 我很忙
苏打绿 - 夏 / 狂热
范晓萱 - 绝世名伶
曹方 - 哼一首歌 等日落
孙燕姿 - 未完成
Radiohead - OK Computer
Lana Del Rey - Born to Die
Pink Floyd - The Wall
痛仰 - 不要停止我的音乐
Linkin Park - Hybrid Theory
Nirvana - MTV Unplugged in New York
陈绮贞 - After 17
Jack Johnson - In Between Dreams
五月天 Mayday - 神的孩子都在跳舞
五月天 - 离开地球表面Jump!
陈奕迅 - 不想放手
曲婉婷 - 我的歌声里
Ennio Morricone - The Legend of 1900
张楚 - 孤独的人是可耻的
徐佳莹 - 徐佳瑩La La首张创作专辑
Avril Lavigne - The Best Damn Thing
五月天 - 知足 just my pride 最真杰作选
The Beatles - 1
周杰伦 - 魔杰座
Coldplay - X&Y
Adele - 19
五月天 - 时光机
孙燕姿 - Yan Zi
陈奕迅 - Time Flies
陈绮贞 - 失败者的飞翔
田馥甄 - My Love
梁静茹 - 亲亲
王菲 - 你王菲所以我王菲
陈奕迅 - Stranger Under My Skin
Norah Jones - Come Away with Me
朴树 - 平凡之路
陈奕迅 - 认了吧
Green Day - 21st Century Breakdown
張懸 - 神的游戏
王菲 - 唱游
陈绮贞 - 花的姿态：演唱会经典实录
朴树 - 我去2000年
GALA - Young For You
孙燕姿 - 自选集
李宗盛 Jonathan - 理性与感性 作品音乐会
曹方 - 比天空还远
窦唯 - 黑梦
周杰倫... - 不能说的秘密
梁静茹 Fish - 丝路
James Blunt - All The Lost Souls
飞儿乐团 F.I.R. - F.I.R.
陈奕迅 - 上五楼的快活
Linkin Park - Minutes to Midnight
蔡健雅... - GOODBYE & HELLO
Adele - Someone Like You
苏打绿 - 迟到千年
Pink Floyd - The Dark Side of the Moon
王菲 - 王菲
逃跑计划 - 夜空中最亮的星
GALA - 追梦痴子心
莫文蔚 - 宝贝
陈奕迅 - 黑白灰
宋冬野 - 安和桥北
宇多田ヒカル - Prisoner of Love
陈绮贞 - Groupies 吉他手
The Innocence Mission - Now The Day Is Over
Timbaland... - Apologize
王菲 - 阿菲正传
周杰伦 - 跨时代
孙燕姿 - Leave
李志 - 被禁忌的游戏
陈奕迅 - What's Going On....?
五月天 - 第二人生 末日版
陶喆 - 樂之路
Maroon 5 - It Won't Be Soon Before Long
张悬 - 如果你冷
蔡健雅 Tanya Chua - 陌生人
王菲 - 浮躁
自然卷 - C'est La Vie
刘若英 - 在一起
Rosie Thomas - These Friends Of Mine
苏打绿 - 陪我歌唱
Lily Allen - It＇s Not Me It＇s You
手嶌葵 - The Rose~I Love Cinemas~
李志 - 我爱南京
大乔小乔 - 消失的光年
范晓萱 - 还有别的办法吗
卡奇社 - 日光倾城
冯曦妤 - A Little Love
Coldplay - Yellow
Keane - Hopes And Fears
陈奕迅 - U87
Maximilian Hecker - Lady Sleep
久石譲(Joe Hisaishi)... - 天空の城ラピュタ サウンドトラック 飛行石の謎
崔健 - 新长征路上的摇滚
棉花糖... - 小飞行
好妹妹乐队 - 春生
陈绮贞 - 讓我想一想
方大同 - 未来
方大同 - 爱爱爱
逃跑计划 - 世界
盧廣仲... - 七天
Nirvana - Nirvana
Coldplay - A Rush of  Blood to the Head
The Velvet Underground... - The Velvet Underground & Nico
Eminem... - Love The Way You Lie
王菲 - 天空
Original Soundtrack - The Boat That Rocked
Oasis - (What's The Story) Morning Glory?
陈绮贞 - PUSSY
Salyu - 呼吸
Evanescence - Fallen
黑豹 - 黑豹
苏打绿 - 十年一刻
梁静茹 - 恋爱的力量
Suede - Suede
Radiohead - The Bends
林海 - 琵琶相
陈奕迅 - ？
彭坦 - 少年故事
雷光夏 - 黑暗之光
范晓萱 - 我要我们在一起
五月天 - 人生海海
Owl City - Maybe I'm Dreaming
李志 - 工体东路没有人
The Beatles - Let It Be
Lily Allen - Alright,Still
林宥嘉 - 大小說家
牛奶@咖啡 - 越长大越孤单
梁静茹 - 燕尾蝶
戴佩妮 - 原谅我就是这样的女生
王菲 - 传奇
Daniel Powter - Under the Radar
五月天 - 知足 MV / Karaoke DVD
曲婉婷 - 我的歌声里
王菲 - 王菲
汪峰 - 信仰在空中飘扬
莫文蔚 - [i]
Maroon 5 - Songs About Jane
Amy Winehouse - Back To Black
陈绮贞 - Demo 3
孙燕姿 - 克卜勒
Mariah Carey - E=MC²
Damien Rice - 9 Crimes
陈珊妮 - 如果有一件事是重要的
郑钧 - 赤裸裸
张震岳 - 阿岳正传
朱玫玲... - 3颗猫饼干
Green Day - 21 Guns
蔡依林 Jolin Tsai - 看我72变
五月天 - 第二人生 明日版
Oasis - Definitely Maybe
宇多田ヒカル - First Love
张惠妹 - 阿密特
王力宏 Leehom Wang - 心·跳
The xx - xx
莫文蔚 - 回蔚
Tizzy Bac - 如果看見地獄，我就不怕魔鬼
五月天 - 我们是五月天
萧敬腾 - 王妃
Lady Gaga - Poker Face
唐朝 - 唐朝
周杰伦 - 寻找周杰伦
林俊杰 - 她说
```

