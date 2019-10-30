# 一、JavaScript概述
## 1.什么是JavaScript
### 1 JavaScript介绍 
简称JS，是一种浏览器解释型语言，嵌入在HTML文件中交给浏览器解释执行。主要用来实现网页的动态效果，用户交互及前后端的数据传输等。
### 2. JavaScript组成
1. 核心语法：ECMAScript规范了JavaScript的基本语法
2. 浏览器对象模型：MOM  
Brows00er  Object Model，提供了一系列操作浏览器的方法
3. 文档对象模型：DOM  
Document Object Model，提供了一系列操作的文档的方法
## 2.  使用方式
1. 元素绑定事件
    * 事件：指用户的行为(单击，双击等)或元素的状态(输入框的焦点状态等)
    * 事件处理：元素监听某种事件并在事件发生后自动执行事件处理函数。
    * 常用事件：onclick(单击事件)
    * 语法：将事件名称以标签属性的方式绑定到元素上，自定义事件处理。
    ```html
   <!-- 实现单击按钮在控制台输出-->
   <button onclick="console.log('Hello World');">点击</button> 
    ```
2. 文档内嵌。使用<script type="text/javascript"></script>标签书写
javaScript代码
    * 语法：
    ```html
    <script type="text/javascript">
     alert("网页警告框");
    </script>>
    ```
    * 注意：<script></script>标签可以书写在文档的任意位置，书写多次，一旦加载到script标签就会立即执行内部的javaScript代码，因此不同的位置会影响代码最终的执行效果
 3. 外部链接
    * 创建外部的javaScript文件XX.js,在HTML文档中使用<script src=""></script>引入
    ```html
    <script src="index.js"></script>
    ```
    * 注意：<script></script>既可以实现内嵌javaScript代码，也可以实现引入外部的javaScript文件，但只能二选一。
 4. javaScript输入输出语句
    * alert("");普通的网页弹框
    * prompt("");接收用户输入的弹框，返回用户输入的内容
    * console.log();控制台输出，多用于代码调试
    * document.write("\<h1>Hello World\</h1>");实现在动态的网页中写入内容。
        1. 可以识别HTML标签，脚本代码可以在文档任何地方书写，如果是普通写入(不涉及事件)，区分代码的书写位置插入
        2. 文档渲染结束后，再次执行此方法，会重写网页内容
# 二、DOM事件处理
事件:指用户的行为或元素的状态。由指定元素监听相关事件，并且绑定事件处理函数。  
事件处理函数:元素监听事件，并在事件发生时自动执行的操作。
## 事件函数分类
1. 鼠标事件
```html
onclick         // 单击
ondblclick      // 双击
on mouseover    // 鼠标移入
on mouseout     // 鼠标移出
onmousemove     // 鼠标移动
```
2. 文档或元素加载完毕
```html
onload          // 元素或文档加载完毕
```
3. 表单控件状态监听
```html
onfocus         // 文本框获取焦点
onblur          // 文本失去焦点
oninput         // 实时监听输入
onchange        // 两次输入内容发生变化时触发，或元素状态改变时触发
onsubmit        // form元素监听，点击提交按钮后触发，通过返回值控制数据是否可以发送给服务器
```
## 事件绑定方式
1. 内联样式  
    * 将事件名称作为标签属性绑定到元素上
    例子：
    ```html
    <button onclick="alert()">点击</button>
    ```
2. 动态绑定
    * 获取元素节点，动态添加事件
    例：
    ```html
      btn。onclick = function(){
   
   };
    ```
3. 事件函数的使用
    * onload  
    常用于等待文档加载完毕再执行下一步操作  
    * 鼠标事件
    * 表单事件
    * onchange：监听输入框前后内容是否发生变化，也可以监听按钮的选中状态
    * onsubmit：表单元素负责监听，允许返回布尔值，表示数据是否可以发送，返回true,发挥true,允许发送返回false,不允许提交
# 三、基础语法
## 1. 语法规范
1. javaScript是由语句组成 ，语句由关键字，变量，常量，运算符，方法组成。
2. 分号可以作为语句结束的标志，也可以省略
3. javaScript严格区分大小写
4. 注释语法
    * 单行注释使用//
    * 多行注释使用/**/
## 2. JavaScript的常量与变量
### 1.变量
1. 作用：用于存储程序运行过程中可动态修改的数据
2. 语法：使用关键字var声明，自定义变量名
    ```html
    var a;    // 变量声明
    a = 100;  // 变量赋值
    var b = 200;//声明并赋值
    var m,n,k;//同时声明多个变量
    var j = 10,c = 20;//同时声明并赋值多个变量
    ```
3. 命名规范
    * 变量名，常量名，函数名，方法名自定义，可以由数字，字母下划线，$组成，进制以数字开头
    * 禁止与关键字冲突(var,const,function,if,else,for,while,do,break,case,switch,return,class)
    * 变量名严格区分大小写
    * 变量名尽量见名知义，多个单词组成采用小驼峰，例如："userName"  

4.使用注意：
    * 变量如果省略var关键字，并且未赋值，直接访问会报错
    * 变量使用var关键字声明但未赋值，变量初始值为undefined
    * 变量省略var关键字声明，已被赋值，可以正常使用，影响变量作用域
### 2. 常量
1. 作用：存储一经定义就无法修改的数据
2. 语法：必须声明的同时赋值
```html
const PI = 3.14;
```
3. 注意：
    * 变量一经定义，不能修改，强制修改会报错
    * 命名规范同变量，为了区分变量，常量名采用全大写字母
4. 操作小数位  
toFixed(n);保留小数点后n位
使用：

    


    
           
