import sys
import urllib.request
import pandas as pd


def read_data(url):
	file_list = []
	data = urllib.request.urlopen(url)
	for line in data:
		# print(line.decode('utf-8'))
		file_list.append(line.decode('utf-8'))

	return file_list
def remove_data(file_list,user_id):

	for i in file_list:
		url = "http://localhost:8080/"+i
		url = url[:-1]
		df = pd.read_csv(url, compression='gzip', header=0)
		# print(df)

		print(df.iloc[:, lambda df: [1]])

		# if user_id == df.iloc[:, lambda df: [1]]:
		# 	print("Found User")


if __name__=='__main__':
	
	url = sys.argv[1]
	user_id = sys.argv[2]
	
	file_list = read_data(url)
	remove_data(file_list,user_id)
	