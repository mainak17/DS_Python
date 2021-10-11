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


def get_popular_path(path):
    df = pd.read_csv("records.csv")
    # print(df['path'])
    all_paths = []
    app_paths2 = []

    for i in df['path']:
        all_paths.append(str(i))
    # print(all_paths)

    for i in df['path']:
        print(i.count(path))
    for i in all_paths:
        app_paths2.append(i.partition(path)[0]+path)

    # for i in app_paths2:
    #     print(i)


    freq = find_frequency(app_paths2)

    # print(freq)

    keymax = max(zip(freq.values(), freq.keys()))[1]
    print(keymax)

    return keymax




def find_frequency(my_list):
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print ("% s : % d"%(key, value))

        return freq


    
  









if __name__=='__main__':
    # get_data()
    path = get_popular_path("Purchase")
    print("______________________________________________")
    print("______________________________________________")
    print("______________________________________________")
    print("Popular Path is")
    
    print(path)

