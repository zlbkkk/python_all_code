import flask,json

server=flask.Flask(__name__)

@server.route('/index',methods=['get'])
def index():
    res={'msg':'zlb','code':0}
    return json.dumps(res,ensure_ascii=False)


server.run(port=8090,debug=True)



