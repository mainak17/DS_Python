import psycopg2 as pg 
import pandas as pd


def get_data():
    df = pd.DataFrame()
    conn = pg.connect(host="localhost",database="cookpad",user="cookpad",password="password",port=5439)
    cur = conn.cursor()
    query = '''SELECT user_id,STRING_AGG (a.page_name,' -> ' ORDER BY a.log_time) path FROM public.pv_log a group by user_id'''
    print(query)
    cur.execute(query)
    records = cur.fetchall()

    for row in records:
        
        df2 = {'user_id': row[0], 'path': row[1]}
        df = df.append(df2, ignore_index = True)    

    # print(df)
    df.to_csv("records.csv")

    cur.close()
    conn.close()


if __name__=='__main__':
    get_data()
    

