# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Practice(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists practice(
        id integer primary key autoincrement,
        jour text,
            debut text,
            fin text,
            user_id text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select *, (case when practice.jour = 1 then 'lundi' when jour = 2 then 'mardi' when jour = 3 then 'mercredi' when jour = 4 then 'jeudi' when jour = 5 then 'vendredi' when jour = 6 then 'samedi' when jour = 7 then 'dimanche' end) as monjour from practice")


        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from practice where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from practice where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into practice (jour,debut,fin,user_id) values (:jour,:debut,:fin,:user_id)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["practice_id"]=myid
        azerty["notice"]="votre practice a été ajouté"
        return azerty




