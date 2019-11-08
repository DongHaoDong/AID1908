# 一、BOM
## 1. BOM介绍 
BOM全称为"Browser Object Model",浏览器对象 模型。提供一系列操作浏览器的属性和方法。核心对象为windows对象，不需要手动创建，跟随网页运行自动产生，直接使用，在使用时可以省略书写。
## 2. window对象常用方法
### 1. 网页弹框
```html
alert()         // 警告框
prompt()        // 带输入框的弹框
confirm()       // 确认框
```
### 2. 窗口的打开和关闭
```html
window.open("URL")      // 新建窗口访问指定 的URL
window.close()          // 关闭当前窗口
```
### 3. 定时器方法
1. 间歇调用(周期性定时器)
    * 作用：每隔一段时间就执行一次代码
    * 开启定时器：
    ```html
    var timerID = setInterval(function,interval);
   /*
   参数：
   function:需要执行的代码，可以传入函数名；或匿名函数
   interval:时间间隔，迷人以毫秒为单位 1s=1000ms
   返回值：返回定时器的ID，用于关闭定时器
   */
    ```
   * 关闭定时器：
   ```html
   // 关闭定时器
   clearInterval(timerID);     
   ```
2. 超时调用(一次性定时器)
    * 作用：等待多久之后执行一次代码
    ```html
    // 开启超时时间
   var timerId = setTimeout(function,timeout)
   // 关闭超时调用：
   clearTimeout(timerId);
    ```
## window对象常用属性
window的大部分属性又是对象属性
### 1. history
作用：保存当前窗口所访问过的URL  
属性：  
length表示当前窗口访问过的URL数量  
方法：
```html
back()    对应浏览器窗口的后退按钮，访问前一个记录
forward() 对应前进按钮，访问记录中的下一个URL
go(n)     参数为number值 ，翻阅几条历史记录，正直表示前进，负值表示后退
```
### 2. location
作用：保存当前窗口的地址栏信息(URL)  
属性：  
href设置或读取当前窗口的地址栏信息  
方法：  
```html
reload(param)重载页面(刷新)
参数为布尔值，默认为false，表示从缓存中加载，设置为true，强制从服务器根目录加载
```
### 3. document
提供操作文档HTML文档的方法，参见DOM
# 二、DOM节点操作
DOM全称为"Document Object Model"，文档对象模型，提供操作HTML文档的方法。(注：每个html文件在浏览器中都视为一篇文档，操作文档实际就是操作页面元素。)


