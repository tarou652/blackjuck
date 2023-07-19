from flask import Flask ,render_template,request,redirect,url_for
from datetime import datetime,date
from flask.wrappers import Request
from flask_sqlalchemy import SQLAlchemy
import BLACKJACK as BJ
import pyautogui
import pandas as pd
from pandas import Series, DataFrame
def close_window():
    
    

    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db=SQLAlchemy(app)

@app.route("/")

def index():

 return render_template('home.html')


@app.route("/game")
def game():
  close_window()
  game2()

@app.route("/score")

def score():
  with  open('lastscore.txt', 'r') as f:
   data= f.read().splitlines() 
  with  open('time.txt', 'r', encoding='UTF-8') as f:
   data2= f.read().splitlines() 
  kosuu= len(data)
  data3 = pd.DataFrame({'SCORE':["0","0","0","0","0","0","0","0","0","0",],'TIME':["0","0","0","0","0","0","0","0","0","0",]},columns=['SCORE','TIME'])
  for i in range(kosuu):
    i=int(i)
    row = pd.DataFrame([[data[i],data2[i]]], columns=data3.columns)
    data3 = data3.append(row, ignore_index=True)
    data3[-2:]
  data3['SCORE']=pd.to_numeric(data3['SCORE'])
  data4=data3.sort_values(['SCORE'],ascending=False)
  
  data={"score1":"{0}".format(data4.iloc[0,0]),
        "score2":"{0}".format(data4.iloc[1,0]),
        "score3":"{0}".format(data4.iloc[2,0]),
        "score4":"{0}".format(data4.iloc[3,0]),
        "score5":"{0}".format(data4.iloc[4,0]),
        "score6":"{0}".format(data4.iloc[5,0]),
        "score7":"{0}".format(data4.iloc[6,0]),
        "score8":"{0}".format(data4.iloc[7,0]),
        "score9":"{0}".format(data4.iloc[8,0]),
        "score10":"{0}".format(data4.iloc[9,0]),
        "time1":"{0}".format(data4.iloc[0,1]),
        "time2":"{0}".format(data4.iloc[1,1]),
        "time3":"{0}".format(data4.iloc[2,1]),
        "time4":"{0}".format(data4.iloc[3,1]),
        "time5":"{0}".format(data4.iloc[4,1]),
        "time6":"{0}".format(data4.iloc[5,1]),
        "time7":"{0}".format(data4.iloc[6,1]),
        "time8":"{0}".format(data4.iloc[7,1]),
        "time9":"{0}".format(data4.iloc[8,1]),
        "time10":"{0}".format(data4.iloc[9,1]),
        }
  

  return render_template('score.html',data=data)

 
  
  
 
  

def game2():
  BJ.main()
if __name__=='__main__':
  app.run()