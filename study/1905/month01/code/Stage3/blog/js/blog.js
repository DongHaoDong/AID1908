// 针对log页定义一个对象
var log={
    startdt:"2019-11-12",
    enddt:"2019-12-12",
    updatedt:"2019-11-12",
    anthor:"donghaodong",
}
// 由对象派生业务逻辑
log.submit={
    check:function(v){
        var _v=(v=="")?true:false;
        return _v;
    },
    autohide:function(obj){
        setTimeout(function(){
            obj.hide();
        },2000)
    }
}
// 定义一个验证内容是否为空的函数
function checkvalue(){
    // 获取元素对象，保存在变量中
    var $username=$("#username");
    var $password=$("#password");
    var $err1=$("#err1");
    var $err2=$("#err2");
    // 当用户名和密码都不为空时
    if(!log.submit.check($username.val())&&!log.submit.check($password.val())){
        // 直接提交
        return true;
    }else{
        // 如果用户名为空时
        if($username.val()==""){
            // 提示用户名称不为空的错误信息显示
            $err1.show();
            // 两秒后自动隐藏
            log.submit.autohide($err1);
            // 阻止提交
            return false;
        }else{
            // 密码为空时
            // 提示密码的错误信息显示
            $err2.show();
            // 两秒后自动隐藏
            log.submit.autohide($err2);
            // 组织提交
            return false;
        }
    }
}
// 定义一个基于列表页的业务逻辑
var lst={
    template:function(t,u,p1,p2){
        var _html="";
            _html+='<div class="item">';
            _html+='<div class="title">';
            _html+='    <h3>'+t+'</h3>';
            _html+='</div>';
            _html+='<div class="con">';
            _html+='  <div class="cleft">';
            _html+='        <img src="'+u+'" alt="">';
            _html+='    </div>';  
            _html+='    <div class="cright">';
            _html+='        <tp class="ptop">';
            _html+='            '+p1;
            _html+='        </p>';
            _html+='        <p class="pbottom">';
            _html+='            '+p2;
            _html+='        </p>';
            _html+='   </div>';
            _html+='</div>';
            _html+='</div>';
            return _html;
    }
}
// 使用数组保存展示的数据
var arrData=[
    {
        t:'Python语言的优势',
        u:'image/b.jpg',
        p1='本文探讨了Python语言在AI领域的优势与运用。谁会成为AI和大数据时代的第一开发语言？这本已是一个不需要争论的问题。如果说三年前Matlab、Scala、R、Java……',
        p2='初学璐 学无止境 2018-5-13 34567阅读 999'
    },
    {
        t:'Web开发的优势',
        u:'image/b04.jpg',
        p1='本文探讨了Python语言在AI领域的优势与运用。谁会成为AI和大数据时代的第一开发语言？这本已是一个不需要争论的问题。如果说三年前Matlab、Scala、R、Java……',
        p2='初学璐 学无止境 2018-5-13 34567阅读 979'
    },
    {
        t:'JavaScript开发的优势',
        u:'image/b.jpg',
        p1='本文探讨了Python语言在AI领域的优势与运用。谁会成为AI和大数据时代的第一开发语言？这本已是一个不需要争论的问题。如果说三年前Matlab、Scala、R、Java……',
        p2='初学璐 学无止境 2018-5-13 34567阅读 979'
    }
]
// 使用流程
// 1.遍历数组，获取每一项元素的对象
// 2.将获取的元素对象填充到模板中
// 3.向页面元素追加模板内容
for(var i=0;i<arrData.length;I++){
    // 通过模板生成新的数据
    var _HTML=lst.template(arrData[i].t,arrData[i].u,arrData[i].p1,arrData[i].p2);
    // 将数据追加到列表中
    $(".lst").append(_HTML);
}

// 定义一个基于我的图片页的业务逻辑对象
var pics={
    template:function(u,n,t){
        var _html="";
        _html+='<div class="item">';
        _html+='<div class="imgs">';
        _html+='    <img src="'+u+'" alt="">';
        _html+='    <div class="tip">喜欢 | '+n+'</div>';
        _html+='</div>';
        _html+='<div class="title">';
        _html+='    <h3>'+t+'</h3>';
        _html+='</div>';
        _html+='</div>';
        return _html;
    }
}
// 定义一个包含三个对象内容的图片数组
var arrPics=[
    {
        u:'image/a.jpg',
        n:223,
        t:'python中文件txt打开报错'
    },
    {
        u:'image/b04.jpg',
        n:260,
        t:'Wieb页面开发的重要性'
    },
    {
        u:'image/banner01.jpg',
        n:200,
        t:'JavaScript开发时碰到的问题'
    }
]
// 使用流程
// 1.遍历数组，获取每一项元素的对象
// 2.将获取的元素对象填充到模板中
// 3.向页面元素追加模板内容
for(var j=0;j<arrPics.length;j++){
    // 向模板中填充内容
    var _HTML = pics.template(arrPics[j].u,arrPics[j].n,arrPics[j].t);
    // 将模板追加到页面元素中
    $("#pics").append(_HTML);
}

