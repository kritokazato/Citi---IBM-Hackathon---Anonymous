from database import getCustomerDetails
from ApiCall import apicall_vehicle_loan, apicall_personal_loan, apicall_credit_card, apicall_housing_loan
from flask import Flask, request, render_template
import json
# import things
#from flask_table import Table, Col

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('result.html')
    #return render_template('result.html', Personal_Loan_Val="80%", Personal_Loan_Sts="Yes")


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['search']
    variable=getCustomerDetails(text)
    pl=apicall_personal_loan(variable[1])
    vl=apicall_vehicle_loan(variable[0])
    cc=apicall_credit_card(variable[2])
    hl=apicall_housing_loan(variable[3])


    return render_template('result.html', Personal_Loan_Val=pl[0], Personal_Loan_Sts= str(int(float(pl[1])*100)) + '%', CC_Val= cc[0], CC_Sts = str(int(float(cc[1])*100)) + '%',HL_Val = hl[0], HL_Sts = str(int(float(hl[1])*100)) +'%' , CL_Val = vl[0], CL_Sts = str(int(float(vl[1])*100)) + '%', BL_Val = vl[0], BL_Sts = str(int(float(vl[1])*100)) + '%')



if __name__ == '__main__':
    app.run()
