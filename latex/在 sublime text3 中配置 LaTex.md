LaTex 基本功能的配置
-------------

国外的 sublime 的官网访问速度很慢，建议访问国内的镜像网站，

[http://www.sublimetext.cn/3​www.sublimetext.cn](https://link.zhihu.com/?target=http%3A//www.sublimetext.cn/3)

虽然仍然很慢，但是还可以接受。

### 下载安装 sublime tex 3

这里安装的过程我就不讲了。

### 下载安装 MikTex

这里也可以用 texlive，但是 sublime 中默认的是 miktex，操作起来也会更加简便。

### 安装 LaTex Tools 插件

由于 [http://packagecontrol.io](https://link.zhihu.com/?target=http%3A//packagecontrol.io) 容易被墙，访问不稳定，所以需要将 Sublime Text 安装插件的地址改为中文镜像的地址：

第一步：通过控制台安装插件代码，通过 `ctrl_+_`或`View _>_ Show Console` 打开控制台，将 Python 代码粘贴到控制台，回车。
Sublime Text3
```
import urllib.request,os,hashlib; h = 
'6f4c264a24d933ce70df5dedcf1dcaee' +
 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 
'Package Control.sublime-package'; ipp
 = sublime.installed_packages_path(); 
urllib.request.install_opener( urllib.request.build_opener( 
urllib.request.ProxyHandler()) ); 
by = urllib.request.urlopen( 'http://packagecontrol.cn/' + 
pf.replace(' ', '%20')).read(); dh = 
hashlib.sha256(by).hexdigest(); print('Error validating 
download (got %s instead of %s), please try manual 
install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```
Sublime Text2
```python
import urllib2,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); os.makedirs( ipp ) if not os.path.exists(ipp) else None; urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler()) ); by = urllib2.urlopen( 'http://packagecontrol.cn/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); open( os.path.join( ipp, pf), 'wb' ).write(by) if dh == h else None; print('Error validating download (got %s instead of %s), please try manual install' % (dh, h) if dh != h else 'Please restart Sublime Text to finish installation')
```
第二步：修改 Sublime Text 插件 channels，方法如下：
1. 打开 package control 配置文件
2. 修改 channels 地址：
![](https://pic1.zhimg.com/v2-80d7ef6506cff9042fe5fc422b7d9f9c_r.jpg)
在右边输入：
```
"channels":
	[
		"http://packagecontrol.cn/channel_v3.json"
	],
```
注意 https 要改为右边所示的 http，否则会出现 “There are no packages available for installation”
现在就可以在线下载 package 了
同时按下 SHIFT+CTRL+P，出现如图所示的样子，就证明你可以下载 package 了：
![](https://pic3.zhimg.com/v2-40af588c894dcecd41a542967f2a679e_r.jpg)
直接搜索 LaTex Tools，然后过一段时间，就下载完了。
### 将 SumatraPDF 添加到环境变量
将其文件路径加入到系统的环境变量，这样 sublime 才能调用 SumatraPDF
![](https://pic1.zhimg.com/v2-f316249d2060abd9f47606ada62992ac_r.jpg)
注意路径后面要打英文的分号
具体环境变量方法可参考：
[https://jingyan.baidu.com/article/47a29f24610740c0142399ea.html​jingyan.baidu.com](https://link.zhihu.com/?target=https%3A//jingyan.baidu.com/article/47a29f24610740c0142399ea.html)
这样就可以使用 sublime text 编译 latex 文件了。最后在讲一下一点点的优化方案。
### 公式预览
我们以 Mixtex 为例子，默认还没有下载 mathtools 和 preview 这两个 package
![](https://pic1.zhimg.com/v2-d631c9b8eaa510d7fa3fc37b09ff5f88_r.jpg)
在这个页面下载。
然后下载 Ghostscript
[Ghostscript: Downloads​ghostscript.com](https://link.zhihu.com/?target=https%3A//ghostscript.com/download.html)
直接安装就好。
然后我们就可以预览公式了，效果如图所示：
![](https://pic4.zhimg.com/v2-d34e02411ba97d32dd16d77e013edf57_r.jpg)
### 自动补全
![](https://pic2.zhimg.com/v2-7102ed6d680a6cd20d658e1b50223791_r.jpg)
下载这个插件就可以了。
基本的配置就讲完了，希望可以帮助到你。