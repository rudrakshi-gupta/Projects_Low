import mysql.connector as connector

class DBhelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',port='3306',user='root',passwd='PINK33', database='teams')
        query = 'create table if not exists teams(name Varchar(20) primary key,players Varchar(20),value int)'
        query1 = 'create table if not exists matches(players Varchar(20) primary key, scored int, faced int, F_ours int, S_ixs int, bowled int, maiden int, given int, wkts int, catches int, stumping int, ro int)'
        query2 = 'create table if not exists stats(players Varchar(20) primary key,matches int,runs int, 100s int, 50s int,value int, ctg Varchar(5))'

        cur=self.con.cursor()
        cur.execute(query)
        cur.execute(query1)
        cur.execute(query2)
        print("created")

        # query="insert into matches(players, scored, faced, F_ours,S_ixs, bowled, maiden, given, wkts, catches, stumping, ro) values (%s,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)"
        # val=[('Kohli',102,98,8,2,0,0,0,0,0,0,1),('Yuvraj',12,20,1,0,48,0,36,1,0,0,0),('Rahane',49,75,3,0,0,0,0,0,1,0,0),('Dhawan',32,35,4,0,0,0,0,0,0,0,0),('Dhoni',56,45,3,1,0,0,0,0,3,2,0),('Axar',8,4,2,0,48,2,35,1,0,0,0),('Pandya',42,36,3,3,30,0,25,0,1,0,0),('Jadeja',18,10,1,1,60,3,50,2,1,0,1),('Kedar',65,60,7,0,24,0,24,0,0,0,0),('Ashwin',23,42,3,0,20,2,45,6,0,0,0),('Umesh',0,0,0,0,54,0,50,4,1,0,0),('Bumrah',0,0,0,0,60,2,49,1,0,0,0),('Bhuwneshwar',15,12,2,0,60,1,46,2,0,0,0),('Rohit',46,65,5,1,0,0,0,0,1,0,0),('Kartik',29,42,3,0,0,0,0,0,2,0,1)]
        # cur=self.con.cursor()
        # cur.executemany(query,val)
        # self.con.commit()
        # print("Inserted Successfully!!")

    # def insert_matches(self,players,scored,faced, F_ours,S_ixs,bowled,maiden,given,wkts,catches,stumping,ro):
        
    #     # val=[('Kohli',102,98,8,2,0,0,0,0,0,0,1),('Yuvraj',12,20,1,0,48,0,36,1,0,0,0),
    #     # ('Rahane',49,75,3,0,0,0,0,0,1,0,0),('Dhawan',32,35,4,0,0,0,0,0,0,0,0),
    #     # ('Dhoni',56,45,3,1,0,0,0,0,3,2,0),('Axar',8,4,2,0,48,2,35,1,0,0,0),
    #     # ('Pandya',42,36,3,3,30,0,25,0,1,0,0),('Jadeja',18,10,1,1,60,3,50,2,1,0,1),
    #     # ('Kedar',65,60,7,0,24,0,24,0,0,0,0),('Ashwin',23,42,3,0,20,2,45,6,0,0,0),
    #     # ('Umesh',0,0,0,0,54,0,50,4,1,0,0),('Bumrah',0,0,0,0,60,2,49,1,0,0,0),
    #     # ('Bhuwneshwar',15,12,2,0,60,1,46,2,0,0,0),('Rohit',46,65,5,1,0,0,0,0,1,0,0),
    #     # ('Kartik',29,42,3,0,0,0,0,0,2,0,1)]
    #     query1="insert into matches(players,scored,faced, F_ours,S_ixs,bowled,maiden,given,wkts,catches,stumping,ro) values ('{}',{},{},{},{},{},{},{},{},{},{},{})".format(players,scored,faced, F_ours,S_ixs,bowled,maiden,given,wkts,catches,stumping,ro)
        
    #     cur=self.con.cursor()
    #     cur.execute(query1)
    #     self.con.commit()
    #     print("Inserted Successfully!!")

    # def insert_stats(self,player,matches,runs,huns,fifs,value,ctg):
    #     # val=[('Kohli', 189, 8257,28,43,120, 'BAT'),('Yuvraj',86, 3589,10,21,100,'BAT),]
    #     query="insert into matches(player,matches,huns,fifs,value,ctg) values ('{}',{},{},{},{},{},'{}')".format(player,matches,runs,huns,fifs,value,ctg)
    #     cur=self.con.cursor()
    #     cur.execute(query)
    #     self.con.commit()
    #     print("Inserted Successfully!!")

helper=DBhelper()
# helper.insert_matches('Kartik',29,42,3,0,0,0,0,0,2,0,1)