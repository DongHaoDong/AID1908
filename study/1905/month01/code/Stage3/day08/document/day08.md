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
   
    ```