import json

def apicall_personal_loan(id):
    api_key = 'teuonH42NK9fs-h2kbKROGBHhiirxc6tFhyXQ7eIOcgg'
    location = 'us-south'

    wml_credentials = {
        "apikey": api_key,
        "url": 'https://' + location + '.ml.cloud.ibm.com'
    }

    from ibm_watson_machine_learning import APIClient

    client = APIClient(wml_credentials)

    space_id = 'f6f6501f-c8e1-4c4f-9c65-59ecafdcc386'
    client.set.default_space(space_id)
    #client.deployments.get_details('85280b66-0f77-40a5-b420-a2ac53ea18d0')
    deployment_uid = '85280b66-0f77-40a5-b420-a2ac53ea18d0'
    #scoring_endpoint = 'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/d8f0e83a-0f90-4afb-9022-14b6d7922191/predictions'

    scoring_payload = {"input_data": [{"fields": ["age", "job_cat", "marital status_cat", "education_cat",
                                                  "credit default_cat", "housing loan_cat", "Vehicle loan_cat"],
                                       "values": [id]}]}

    predictions = client.deployments.score(deployment_uid, scoring_payload)

    #print(predictions)
    result = json.dumps(predictions)
    #print(type(result))
    #print(result)

    y = result.split(':')
    # print(y)
    z = y[3].split(',')
    # print(z)
    class_var = z[0][3]

    #print(class_var)
    if class_var == '0':
        Class_N = z[1][2:6]
        class_type = 'No'
        #print(Class_N)
        pri = Class_N
    else:
        Class_Y = z[2][1:5]
        #print(Class_Y)
        class_type = 'Yes'
        pri = Class_Y

    lst = []
    lst.append(class_type)
    lst.append(pri)
    return lst



#print(apicall_personal_loan([33, 9, 1, 2, 0, 3, 2]))
#['Yes', 1.0]
def apicall_vehicle_loan(id):
    api_key = 'teuonH42NK9fs-h2kbKROGBHhiirxc6tFhyXQ7eIOcgg'
    location = 'us-south'

    wml_credentials = {
        "apikey": api_key,
        "url": 'https://' + location + '.ml.cloud.ibm.com'
    }

    from ibm_watson_machine_learning import APIClient

    client = APIClient(wml_credentials)

    space_id = 'f6f6501f-c8e1-4c4f-9c65-59ecafdcc386'
    client.set.default_space(space_id)
    #client.deployments.get_details('d8f0e83a-0f90-4afb-9022-14b6d7922191')
    deployment_uid = 'b85fc3cb-4824-491b-baa3-88f981ba26ba'
    #scoring_endpoint = 'https://private.us-south.ml.cloud.ibm.com/ml/v4/deployments/4de29f68-d30f-4f01-945d-c5483e88ec8a/predictions'

    scoring_payload = { "input_data": [{"fields": ["Loan_ID","Gender","Married","Dependents", "Education","Self_Employed","ApplicantIncome","CoapplicantIncome","LoanAmount","Loan_Amount_Term","Credit_History","Property_Area"], "values": [id]}]}

    predictions = client.deployments.score(deployment_uid, scoring_payload)

    #print(predictions)
    result = json.dumps(predictions)
    #print(type(result))
    #print(result)

    y = result.split(':')
    # print(y)
    z = y[3].split(',')
    # print(z)
    class_var = z[0][4]
    #print(class_var)
    if class_var == 'N':
        Class_N = z[1][2:6]
        #print(Class_N)
        class_type = 'No'
        pri = Class_N
    else:
        Class_Y = z[2][1:5]
        #print(Class_Y)
        class_type='Yes'
        pri = Class_Y

    lst = []
    lst.append(class_type)
    lst.append(pri)
    return lst

#print(apicall_vehicle_loan([1,"Male","Yes",1,"Graduate","No",4583,1508,128,360,1,"Rural"]))

def apicall_credit_card(id):
    api_key = 'teuonH42NK9fs-h2kbKROGBHhiirxc6tFhyXQ7eIOcgg'
    location = 'us-south'

    wml_credentials = {
        "apikey": api_key,
        "url": 'https://' + location + '.ml.cloud.ibm.com'
    }

    from ibm_watson_machine_learning import APIClient

    client = APIClient(wml_credentials)

    space_id = 'f6f6501f-c8e1-4c4f-9c65-59ecafdcc386'
    client.set.default_space(space_id)
    #client.deployments.get_details('d8f0e83a-0f90-4afb-9022-14b6d7922191')
    deployment_uid = '146ca1b7-ce2f-4a5a-b146-53d1de0c92a6'
    #scoring_endpoint = 'https://private.us-south.ml.cloud.ibm.com/ml/v4/deployments/4de29f68-d30f-4f01-945d-c5483e88ec8a/predictions'

    scoring_payload = { "input_data": [{"fields": ["age", "job","marital status","education","credit default?"], "values": [id]}]}

    predictions = client.deployments.score(deployment_uid, scoring_payload)

    result = json.dumps(predictions)
    #print(type(result))
    #print(result)

    y = result.split(':')
    # print(y)
    z = y[3].split(',')
    # print(z)
    class_var = z[0][4]
    #print(class_var)
    if class_var == 'n':
        Class_N = z[1][2:6]
        #print(Class_N)
        class_type = 'No'
        pri = Class_N
    else:
        Class_Y = z[2][1:5]
        #print(Class_Y)
        class_type = 'Yes'
        pri = Class_Y

    lst = []
    lst.append(class_type)
    lst.append(pri)
    return lst

#print(apicall_credit_card([25,"services","single","secondary","no"]))

def apicall_housing_loan(id):
    api_key = 'teuonH42NK9fs-h2kbKROGBHhiirxc6tFhyXQ7eIOcgg'
    location = 'us-south'

    wml_credentials = {
        "apikey": api_key,
        "url": 'https://' + location + '.ml.cloud.ibm.com'
    }

    from ibm_watson_machine_learning import APIClient

    client = APIClient(wml_credentials)

    space_id = 'f6f6501f-c8e1-4c4f-9c65-59ecafdcc386'
    client.set.default_space(space_id)
    #client.deployments.get_details('d8f0e83a-0f90-4afb-9022-14b6d7922191')
    deployment_uid = '44695a6b-6153-454e-ae58-f26c19fb9b95'
    #scoring_endpoint = 'https://private.us-south.ml.cloud.ibm.com/ml/v4/deployments/4de29f68-d30f-4f01-945d-c5483e88ec8a/predictions'

    scoring_payload = { "input_data": [{"fields": ["age", "job","marital status","education","credit default?"], "values": [id]}]}

    predictions = client.deployments.score(deployment_uid, scoring_payload)

    result = json.dumps(predictions)
    #print(type(result))
    #print(result)

    y = result.split(':')
    # print(y)
    z = y[3].split(',')
    # print(z)
    class_var = z[0][4]
    #print(class_var)
    if class_var == 'n':
        Class_N = z[1][2:6]
        #print(Class_N)
        class_type = 'No'
        pri = Class_N
    else:
        Class_Y = z[2][1:5]
        #print(Class_Y)
        class_type = 'Yes'
        pri = Class_Y

    lst = []
    lst.append(class_type)
    lst.append(pri)

    return lst

#print(apicall_housing_loan([25,"services","single","secondary","no"]))
#print(a)
#print (int(float(a[1])*100))
