import os
import numpy as np
from flask import Flask, render_template, request, jsonify,redirect,url_for,flash
app = Flask(__name__)

import pickle
div3_rf = pickle.load(open('div3_rf.pkl','rb'))
div3_dt = pickle.load(open('div3_dt.pkl','rb'))
div3_svm = pickle.load(open('div3_svm.pkl','rb'))
div3_nv = pickle.load(open('div3_nv.pkl','rb'))
div3_nn = pickle.load(open('div3_nn.pkl','rb'))
div2_rf = pickle.load(open('div2_rf.pkl','rb'))
div2_dt = pickle.load(open('div2_dt.pkl','rb'))
div2_svm = pickle.load(open('div2_svm.pkl','rb'))
div2_nv = pickle.load(open('div2_nv.pkl','rb'))
div2_nn = pickle.load(open('div2_nn.pkl','rb'))
div1_rf = pickle.load(open('div1_rf.pkl','rb'))
div1_dt = pickle.load(open('div1_dt.pkl','rb'))
div1_svm = pickle.load(open('div1_svm.pkl','rb'))
div1_nv = pickle.load(open('div1_nv.pkl','rb'))
div1_nn = pickle.load(open('div1_nn.pkl','rb'))

@app.route('/',methods=['GET','POST'])
def home():
    if request.method =='POST':
        # print(request.json)
        try:
            age=int(request.form['age'])
            medu=int(request.form['Medu'])
            failures=int(request.form['failures'])
            g1=int(request.form['G1'])
            g2=int(request.form['G2'])
            test=np.array([age,medu,failures,g1,g2]).reshape(1,-1)
            # print(test)
            # test = np.array([age,4,0,14,15]).reshape(1, -1)
            
            div1_dt_res = int(div1_dt.predict(test))
            div1_rf_res = int(div1_rf.predict(test))
            div1_svm_res = int(div1_svm.predict(test))
            div1_nn_res = int(div1_nn.predict(test))
            div1_nv_res = int(div1_nv.predict(test))
            div2_dt_res = int(div2_dt.predict(test))
            div2_rf_res = int(div2_rf.predict(test))
            div2_svm_res = int(div2_svm.predict(test))
            div2_nn_res = int(div2_nn.predict(test))
            div2_nv_res = int(div2_nv.predict(test))
            div3_dt_res = int(div3_dt.predict(test))
            div3_rf_res = int(div3_rf.predict(test))
            div3_svm_res = int(div3_svm.predict(test))
            div3_nn_res = int(div3_nn.predict(test))
            div3_nv_res = int(div3_nv.predict(test))
            result={'div1':[div1_nv_res,div1_nn_res,div1_svm_res,div1_dt_res,div1_rf_res],'div2':[div2_nv_res,div2_nn_res,div2_svm_res,div2_dt_res,div2_rf_res],'div3':[div3_nv_res,div3_nn_res,div3_svm_res,div3_dt_res,div3_rf_res]}
            # print(result)
            return render_template('result.html',content=result)
        except:
            flash('Enter Information correctly')
            return render_template('home.html')
    return render_template('home.html')

@app.route('/acknowledgment',methods=['GET'])
def akno():
    return render_template('akno.html')



@app.route('/via_api', methods=['GET','POST'])
def via_api():
    # print(request.json)
    if request.method =='POST':
        # print(request.json)
        age=int(request.json['age'])
        medu=int(request.json['Medu'])
        failures=int(request.json['failures'])
        g1=int(request.json['G1'])
        g2=int(request.json['G2'])
        test=np.array([age,medu,failures,g1,g2]).reshape(1,-1)
        # test = np.array([age,4,0,14,15]).reshape(1, -1)
        if len(test) == 1:
            div1_dt_res = int(div1_dt.predict(test))
            div1_rf_res = int(div1_rf.predict(test))
            div1_svm_res = int(div1_svm.predict(test))
            div1_nn_res = int(div1_nn.predict(test))
            div1_nv_res = int(div1_nv.predict(test))
            div2_dt_res = int(div2_dt.predict(test))
            div2_rf_res = int(div2_rf.predict(test))
            div2_svm_res = int(div2_svm.predict(test))
            div2_nn_res = int(div2_nn.predict(test))
            div2_nv_res = int(div2_nv.predict(test))
            div3_dt_res = int(div3_dt.predict(test))
            div3_rf_res = int(div3_rf.predict(test))
            div3_svm_res = int(div3_svm.predict(test))
            div3_nn_res = int(div3_nn.predict(test))
            div3_nv_res = int(div3_nv.predict(test))
            result={'div1':[div1_nv_res,div1_nn_res,div1_svm_res,div1_dt_res,div1_rf_res],'div2':[div2_nv_res,div2_nn_res,div2_svm_res,div2_dt_res,div2_rf_res],'div3':[div3_nv_res,div3_nn_res,div3_svm_res,div3_dt_res,div3_rf_res]}
            return jsonify(result)
        else:
            return jsonify('bad request')






if __name__ == "__main__":
    app.secret_key='thisisasecretkey'
    app.run(debug=False)