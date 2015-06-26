# Voice-Changing
##題目發想緣起
	童年受到日本動畫名偵探柯南的影響，對於柯南的變聲器非常有興趣，因此我們組別決定嘗試製作可作聲音轉換的變聲器
##實作所需材料（取得來源、價位）
	麥克風(借來的)
	自製蝴蝶結(5元)
	USB音效卡(網上購買50元)
	喇叭(借來的)
##使用的現有軟體與來源
	1.Python及相關套件：Pyaudio.Numpy
	2.程式碼-Stack overflow-Python Audio Frame Pitch Change
##實作過程（碰到哪些問題、如何解決）
	遇到問題：
1.SD卡容量不足：查找網路教學文件擴充 

2.IOError998

3.硬體不足：聲音斷點 聲音雜訊


##運用哪些與課程內容中相關的技巧
	Postfix－Raspberry Pi 開機自動寄信取得IP
	ssh
##組裝過程及製作教學（GPIO線材的安裝、3D列印後的組裝...）
	插入USB音效卡至raspberry pi USB孔
##操作教學（做出此產品之後該如何操作）
	
1.事前軟體安裝

安裝python及相套
> sudo apt-get install python 

> sudo apt-get install python-pyaudio 

> sudo apt-get install python-numpy 


2.USB音效卡插入後調整USB音效卡設定
音效卡插入後，輸入指令
> lsusb		#確認usb音效卡是否被偵測到了C-Media

在輸入指令aplay -l 檢視目前音效裝置
一般card0為預設使用的音效卡，我們pi上所接的usb音效卡要將他變成預設的
必須更改：alsa設定檔
> sudo vi /etc/modprobe.d/alsa-base.conf

將
options snd-usb-audio index=-2  註解掉並存檔
之後重新開機就會調整成功


3.編寫聲音處理python 檔sound.py

###操作教學（做出此產品之後該如何操作）

	執行檔案 輸入python sound.py

###工作分配表
	楊佳儒－報告呈現、資料查詢
	郭亞蓁－主程式修改（sound.py）
	余美儒－設備連接設定與測試
	教學文件及投影片為全組製作.

##參考來源
	1.Stack overflow
	2.https://people.csail.mit.edu/hubert/pyaudio/
	3.http://blog.itist.tw/2015/05/playing-audio-via-usb-sound-device-with-raspberry-pi.html

