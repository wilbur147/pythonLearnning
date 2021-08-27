from flask import Flask, request

# 实例化Flask对象
app = Flask(__name__)


# 生成路由关系，并把关系保存到某个地方,app对象的 url_map字段中
@app.route('/')
def hello_world():
    return 'Hello World!'


# 测试
@app.route("/test", methods=["GET"])
def test():
    urls = request.args.get("urls")
    if urls:
        return {"code": 200, "msg": "上传成功!"}
    return {"code": 500, "msg": "上传失败，参数urls路径缺失！"}


if __name__ == '__main__':
    # 启动程序，监听用户请求
    # 一旦请求到来，执行 app.__call__方法
    # 封装用户请求
    # 进行路由匹配
    app.run(host='0.0.0.0', port=7090, debug=True)
