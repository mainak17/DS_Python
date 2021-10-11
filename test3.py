import psycopg2 as pg 
import pandas as pd
from collections import Counter
import sys

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
    # df.to_csv("records.csv")

    cur.close()
    conn.close()

    return df





def get_popular_path(df,page):
    # df = pd.read_csv("records.csv")
    # print(df['path'])
    all_paths = []
    # print(df)
    for paths in df['path']:
        if page in paths:
            all_paths.append(str(paths.split(page)[0]+page))


    all_paths1 = []
    all_paths2 = []

    for i in all_paths:
        temp = i.split(" -> ")
        all_paths1.append(temp[-4:])


    for i in all_paths1:
        temp = " -> ".join(i)
        all_paths2.append(temp)

    
    max_key_val = find_max_frequency(all_paths2)
    return max_key_val


def find_max_frequency(my_list):
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    # for key, value in freq.items():
    #     print ("% s : % d"%(key, value))

    max_key_val = max(zip(freq.values(), freq.keys()))
    return list(max_key_val)


# Run Command : python test3.py "Purchase"

if __name__=='__main__':
    

    page = sys.argv[1]
    df = get_data()
    path = get_popular_path(df,page)
    print("Popular Page is "+path[1]+" with "+str(path[0])+" hits")