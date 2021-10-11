echnical Exercise
Guidance
Please fork this repository so that we can see you've successfully accessed the exercise.
Submit your solution by creating a pull request back to the source repository. You're welcome to create the PR immediately before starting the solution.
Exercise duration: 150 minutes. Commits to your fork that are made beyond this time limit will be ignored.
Challenge 1
Overview
At Cookpad 🧑👩🍳 , we keep logs of the pages that our users visit in the app. However, let's imagine that we don't have the capability of finding out the most popular path for users to reach a page.

As a Data Engineer, we would like you to create a program that given a page name, it responds with the most popular path to reach that page.

Technical Information
A "path" here means a list of consecutive pages visited by a user.

For example, if we have data as following, the path for user_id=1 is A -> B -> C.

log_time	user_id	page_name
2020-01-01 00:00:00	1	A
2020-01-01 00:00:05	1	B
2020-01-01 00:00:10	1	C
As you can see pages must be sorted by timestamp in ascending order.

The length of a path must be 4 at most. And a path should includes 4 last consecutive pages visited by a a user. For example when a user visited 6 pages, A, B, C, D, E and F in this order, the path should be C -> D -> E -> F. The minimum length of a path is 1. For example, if a user visited just one page, A, the path will be A. The last item of a path will always be the last page viewed by a user.

For example when we have data as following:

log_time	user_id	page_name
2020-01-01 00:10:00	2	B
2020-01-01 00:10:05	2	A
2020-01-01 00:10:10	2	C
2020-01-01 00:10:15	2	E
2020-01-01 00:10:20	2	A
2020-01-01 00:20:00	3	B
Paths will be:

user_id	path
2	A -> C -> E -> A
3	B
The popularity here is the number of users who have taken the path. For example, when we have paths as following the most popular path is A -> B -> C as it has 2 while others have just 1.

user_id	path
1	A -> B -> C
2	A -> B -> A -> C
3	A -> B -> C
4	C
The program must take a name of a page as argument and return the most popular path which users have taken before they reach the page.

Execution example
$ python3 find_popular_path.py Purchase
Top -> Search -> Recipe -> Purchase
Note: You can give better name to the program.

Environment
The dataset, web pv log, is as a table on the PostgreSQL DB.

Please use the docker image, public.ecr.aws/m4h2e8g9/data-engineering-technical-exercise-postgre:latest, for PostgreSQL DB.

$ docker run -p 5439:5432 public.ecr.aws/m4h2e8g9/data-engineering-technical-exercise-postgre:latest
Here is the connection information:

host: localhost
port: 5439
database: cookpad
username: cookpad
password: password
The name of web pv log table is pv_log

The pv_log table has 3 columns.

column	description
log_time	timestamp of a page view
user_id	User's ID
page_name	Name of a viewed page.
Performance matters
Please think of the PostgreSQL DB as a MPP DB like Big Query or Redshift and make your program to be able to handle much larger data like billions of rows even with your laptop.

Output
Please commit everything in exercise_1/.

Challenge 2
Overview
At Cookpad 🧑👩🍳 , we keep user activity logs to answer questions like "Which recipe was the most liked last week?". However, let's imagine that we've received data erasure request from a user but don't have capability to handle such request.

As a Data Engineer, we would like you to create a program that given a user id, remove all records related to the user from our log files.

Technical Information
Please write a program that:

Take an URL as first argument and an user id as second.
The URL returns a list of log data files.
Read log data files on the list and remove records with specified user id from them.
Save processed data as gzipped CSV files on local disk.
URL for a list of log data file
The URL returns a list of log data file in text format. It hat one file name per line as following.

% curl http://localhost:8080/index.txt
data_001.csv.gz
data_002.csv.gz
data_003.csv.gz
...
Log data files are stored in the same path as the list. So, with above example, http://localhost:8080/data_001.csv.gz returns the content of data_001.csv.gz.

Format of log data file
The format of log data file is CSV without double-quote and without header. Each field represents timestamp, user_id, content_id and client_id.

2020-03-06 17:54:16.418,3071774,8f751d5f0d4f08174faf730d1a98d575e1dc41f0ce388563cbe8508dde98b88f,931ab8407675404cfb774e697283925ab38ad80cac6db0caebaa88e0c85afd54
2020-03-06 17:54:16.461,11710937,a46f0150e28b0650daac1cb2a0fbf0c236e79718808107476474313d8bc0707e,cff16b13f46dd0b0695b02a9b4612273bea604606e1149515c16f1a5f1df1bd4
2020-03-06 17:54:16.465,11715465,1b1f54852e6d6ea02ba1c8c6f5a46001c70df7e6712524cb7c6a6d2a1cfc3254,8fc9a7b848411e247bbf76e1878799cde2f5d829d17782392987f5126631ffd5
Log data files are gzipped as you can see from the .gz extention.

Execution example
--- Check the list of log data file names
% curl http://localhost:8080/index.txt
data_001.csv.gz
data_002.csv.gz
data_003.csv.gz
...

-- Check one of the data file
% curl  http://localhost:8080/data_001.csv.gz -o data_001.csv.gz
% ls data_001.csv.gz
data_001.csv.gz

--- Run program
% java --jar erase.jar http://localhost:8080/index.txt 12345

-- Confirm that processed files are saved in the current directory
% ls
data_001.csv.gz data_002.csv.gz data_003.csv.gz ... erase.jar
Environment
The list and log data files, can be accessed via HTTP.

Please use the docker image, public.ecr.aws/m4h2e8g9/data-engineering-technical-exercise-nginx:latest, for the HTTP server.

docker run -p 8080:80 public.ecr.aws/m4h2e8g9/data-engineering-technical-exercise-nginx:latest
The docker image provides nginx server with the list and log data files.

URL of the list: http://localhost:8080/index.txt
One of the URL for data files: http://localhost:8080/data_001.csv.gz
Performance matters
Please make sure that your program can handle 1GB * 1000 data files in the following environment.

16 CPU
8GB memory
Just enough disk space for the output file(s)
Output
Please commit everything in exercise_2/.
