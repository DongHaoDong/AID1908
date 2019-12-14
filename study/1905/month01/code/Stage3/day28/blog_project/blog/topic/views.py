import json

from django.http import JsonResponse
from django.shortcuts import render
from tools.login_check import login_check,get_user_by_request
from .models import Topic
from user.models import UserProfile
import html
# Create your views here.


@login_check('POST','DELETE')
def topics(request,author_id):
    if request.method == 'GET':
        # 获取用户博客数据
        # http://127.0.0.1:5000/<username>/topics
        # author_id被访问的博客的博主用户民
        # visitor 访客[1. 登陆了 2. 游客(未登录)]
        # author 博主 当前被博客的博主
        authors = UserProfile.objects.filter(username=author_id)
        if not authors:
            result = {'code':308,'error':'no authhor'}
            return JsonResponse(result)
        # 取出结果中的博主
        author = authors[0]
        # visitor
        visitor = get_user_by_request(request)
        visitor_name = None
        if visitor:
            visitor_name = visitor.username
        category = request.GET.get('category')
        if category in ['tec','no-tec']:
            # /v1/topics/<author_id>?category=[tec|no-tec] 用户全量数据
            if author_id == visitor_name:
                # 博主访问自己的博客
                topics = Topic.objects.filter(author_id=author_id,category=category)
            else:
                # 访客来了
                topics = Topic.objects.filter(author_id=author_id,category=category,limit='public')
        else:
            # /v1/topics/<author_id>?category=[tec|no-tec] 用户全量数据
            if author_id == visitor_name:
                # 博主访问自己的博客 获取全部博客数据
                topics = Topic.objects.filter(author_id=author_id)

            else:
                # 方可访问博客，非博主本人
                topics = Topic.objects.filter(author_id,author_id,limit='public')
        # 返回
        res = make_topics_res(author,topics)

        return JsonResponse(res)

    elif request.method == 'POST':
        # 创建用户博客数据
        json_str = request.body
        if not json_str:
            result = {'code':301,'error':'Please give me json'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        title = json_obj.get('title')
        # xss注入
        # 进行转义
        title = html.escape(title)
        if not title:
            result = {'code': 302, 'error': 'Please give me title'}
            return JsonResponse(result)
        content = json_obj.get('content')
        if not content:
            result = {'code': 303, 'error': 'Please give me content'}
            return JsonResponse(result)
        # 获取纯文本内容 - 用于切割文章简介
        content_text = json_obj.get('content_text')
        if not content_text:
            result = {'code': 304, 'error': 'Please give me content_text'}
            return JsonResponse(result)
        # 切割文章简介
        introduce = content_text[:30]
        limit = json_obj.get('limit')
        if limit not in ['public','private']:
            result = {'code': 305, 'error': 'Your limit is wrong'}
            return JsonResponse(result)
        category = json_obj.get('category')
        # 创建数据
        Topic.objects.create(title=title,category=category,limit=limit,introduce=introduce,author=request.user)
        result = {'code':200,'username':request.user.username}
        return JsonResponse(result)

    elif request.method == 'DELETE':
        # 博主删除自己的文章
        # /v1/topics/<author_id>
        # token存储的用户
        author = request.user
        token_author_id = author.username
        # url中传过来的author_id必须与token中的用户名相等
        if author_id != token_author_id:
            result = {'code':309,'error':'You can not do it'}
            return JsonResponse(result)
        topic_id = request.GET.get('topic_id')
        try:
            topic = Topic.objects.get(id=topic_id)
        except:
            result = {'code':310,'error':'You can not do it !'}
            return JsonResponse(result)
        # 删除
        if topic.author.username != author_id:
            result = {'code':311,'error':'You can not do it !!'}
            return JsonResponse(result)
        topic.delete()
        res = {'code':200}
        return JsonResponse(res)



def make_topics_res(author,topics):
    res = {'code':200,'data':{}}
    data = {}
    data['nickname'] = author.nickname
    data['topics'] = []
    topics_list = []
    for topic in topics:
        d = {}
        d['id'] = topic.id
        d['title'] = topic.title
        d['category'] = topic.category
        d['introduce'] = topic.introduce
        d['author'] = author.nickname
        d['created_time'] = topic.create_time.strftime('%Y-%m-%d %H:%M:%S')
        topics_list.append(d)
    data['topics'] = topics_list
    res['data'] = data
    return res