# 第8 章　开发web接口


#  8.1  为何要开发web接口


#　数据是一种接口认可的资源，数据是接口的本质


# 调用一个查询发布会信息的就,首先,该接口是通过HTTP协议的GET方式发送请求的,所以可以使用浏览器调用,也可以使用接口测试工具和python所
#  提供的相关库来调用.其次,接口数据使用的是json格式.

#　从接口的调用方式和数据格式来看，显然并不是直接给普通用户来使用的，它主要为其他的开发者所调用


# 构成接口两个重要因素：协议和数据格式

#  ８．２．１　　HTTP


#  HTTP基于TCP/IP通信协议来传递数据(HTML文件，图片文件，媒体等)

#  HTTP协议工作于客户端-服务端架构上.浏览器作为HTTP客户端通过url想HTTP服务端(即web浏览器)发送请求


# 1. http协议的主要特点:无连接,媒体独立,无状态

# 2. HTTP请求方法

# 3. 响应状态码

#　当浏览器接收并显示网页前，此网页所在的服务器会返回一个包含HTTP状态码的信息头(server header)用以响应浏览器的请求

#  4. 请求头信息和响应头信息
#  请求头允许客户端向服务器端传递请求的附加信息以及客户端自身的信息
#  响应头允许服务器传递不能放在状态行中的附加影响信息，以及关于服务器的信息和对requeste-URL所标识的资源进行下一步访问的信息

#  8.2.2 json格式


#　json(即javascript对象表示法)是一种轻量级的数据交换格式，它独立于语言和平台，json解析器和json库支持不同编程语言


#  json语法是javascrpit对象表示法的子集

#  数据在名称/值对中
#  数据由逗号分隔
#  花括号保存对象


#  8.3 开发系统web接口


#  ８．３．１　　配置接口路径


#  开发web接口的访问方式与开发系统的方式相同，这里设置web接口的跟目录为"/api/",通过二级目录表示实现具体功能的接口

# 修改　urls.py
# 在sign应用下创建urls.py文件，用来配置具体接口的二级目录

# 为了避免web接口代码与views.py中的系统功能代码混在一起，重新在sign应用下创建了一个views_api.py文件，用于web接口的开发

# 其次,这里定义的接口路径暂时还未实现,当启动项目时会引起报错,所以,需要它们注释起来.开发一个接口,就去掉一个注释!


#　８．３．２　　添加发布会接口

# １．各个字段不能为空，　JsonResponse()是一个非常有用的类，它可以将字典转化为json格式返回给客户端

#　２．　对于信息重复的判断
#　3. 因为发布会状态不是必传字段，所以判断如果为空，则将状态设置为1(True),即为开启状态

# 4. 将数据插入Event表，在插入的过程中如果，日期格式错误，


#  8.3.3  查询发布会接口　　

# 8.3.4  添加嘉宾接口
# 8.3.5  添加查询嘉宾接口  (接口无非就是添加和查询)
# 8.3.6  发布会签到接口


# ８．４　编写web接口文档


#