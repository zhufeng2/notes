>这几天发现sublime text预览公式的一个严重问题，当公式太长的时候，gs会一直报错，然后就算我不想预览了，只想继续打公式的时候，还是不断弹窗,严重影响我的使用体验，于是准备转vs code，之前还犹豫是否有公式预览功能，看了LaTexworkshop的官方文档后，发现其实是有公式的预览功能的，于是决定转vs code
## vs code中配置LaTex

在vs code中配置LaTex并不复杂，如果你下载的是texlive，那么只需要将texlive加入到环境变量中，然后安装latexworkshop，其实理论上执行完上述步骤之后，就可以编译latex文件了，就用默认的配置比较好，如果遇到什么细节的问题，在在网上寻找相应的教程修改。

但是如果你用的是mixtex，执行完上述步骤之后会报错，原因是缺少一样东西，直接去官网下载就好：[链接](https://strawberryperl.com/),这里建议最好不要修改安装路径，默认安装，后期出现问题的几率才更小。然后你就可以编译LaTex文档了。

## 公式预览
在打完公式后想要确认有没有问题，只需要将鼠标悬停在公式开始处即可。

## 公式环境下的快捷键
这里给出几个例子
| @ a |  $\alpha$ |@c|$\chi$|
| :----|:----:|:----:|----:|
|@b | $\beta$ |@d |$\delta$ |

<img src="https://raw.githubusercontent.com/zhufeng2/image/master/QQ%E6%88%AA%E5%9B%BE20210125220239.png" style="zoom:50%;" />

如需了解更详细的信息，请到官网查看相应的快捷键：[链接](https://github.com/James-Yu/LaTeX-Workshop/wiki/Snippets#Inserting-Greek-letters)

>今天的关于如何在vscode中配置latex就讲到这里，以后有什么对插件配置优化方案也会持续更新！


