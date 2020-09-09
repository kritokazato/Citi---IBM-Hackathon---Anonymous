import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, Table , MetaData, text

metadata = MetaData()

def getCustomerDetails(id):
    DATABASE_URI = 'postgres+psycopg2://ajhcdixf:G4xwnWJNz3q1LO_D7vifi3fJLW-5Rr9H@john.db.elephantsql.com:5432/ajhcdixf'
    engine=create_engine(DATABASE_URI)
    #print(engine.table_names())
    connection=engine.connect()
    loans = Table('loans', metadata, autoload=True, autoload_with=engine)
    stmt=select([loans])
    stmt=stmt.where(loans.columns.loan_id == id)
    results = connection.execute(stmt).fetchall()
    #print(results)
    #[(1,2,3)]
    #[1,2,3]

    lst = []
    for row in results:
        for i in range(len(row)):
            # print(row[i])
            lst.append(row[i])

    personal_loan = Table('personal_loan', metadata, autoload=True, autoload_with=engine)
    stmt_pl=select([personal_loan.c.age,personal_loan.c.job , personal_loan.c.marital_status , personal_loan.c.education , personal_loan.c.credit_default , personal_loan.c.housing_loan, personal_loan.c.vehicle_loan])
    stmt_pl = stmt_pl.where(personal_loan.columns.id == id)
    results_pl = connection.execute(stmt_pl).fetchall()
    #print(results)
    lst_pl = []
    for row in results_pl:
        for i in range(len(row)):
            # print(row[i])
            lst_pl.append(row[i])

    credit_card = Table('credit_card', metadata, autoload=True, autoload_with=engine)
    stmt_cc =select([credit_card.c.age,credit_card.c.job , credit_card.c.marital_status , credit_card.c.education , credit_card.c.credit_default ])
    stmt_cc = stmt_cc.where(credit_card.columns.id == id)
    results_cc = connection.execute(stmt_cc).fetchall()
    #print(results)
    lst_cc = []
    for row in results_cc:
        for i in range(len(row)):
            # print(row[i])
            lst_cc.append(row[i])

    housing_loan = Table('housing_loan', metadata, autoload=True, autoload_with=engine)
    stmt_hl =select([housing_loan.c.age,housing_loan.c.job , housing_loan.c.marital_status , housing_loan.c.education , housing_loan.c.credit_default ])
    stmt_hl = stmt_hl.where(housing_loan.columns.id == id)
    results_hl = connection.execute(stmt_hl).fetchall()
    #print(results)
    lst_hl = []
    for row in results_hl:
        for i in range(len(row)):
            # print(row[i])
            lst_hl.append(row[i])

    lst_final =[]
    lst_final.append(lst)
    lst_final.append(lst_pl)
    lst_final.append(lst_cc)
    lst_final.append(lst_hl)

    return lst_final
    connection.close()



#print(getCustomerDetails('1'))
