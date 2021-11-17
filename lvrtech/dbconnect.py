import sqlite3
import os

dbfile = os.path.abspath("TwinFit.db")
con = sqlite3.connect(dbfile, check_same_thread=False)

def create_user(userid, token, email):
    delete_table("users")
    con.execute('''CREATE TABLE IF NOT EXISTS users (token PRIMARY KEY, userid text, email text)''')
    sql = "INSERT OR REPLACE INTO users (userid, token, email) VALUES (?, ?, ?)"
    print(userid, token, email)
    con.execute(sql, [userid, token, email])
    con.commit()

def create_user_info(token, age, weight, height, gender, email):
    con.execute('''CREATE TABLE IF NOT EXISTS userinfo (token PRIMARY KEY, age INTEGER, weight INTEGER, height INTEGER, gender TEXT, email TEXT)''')
    sql = 'INSERT OR REPLACE INTO userinfo (token, age, weight, height, gender, email) values (?, ?, ?, ?, ?, ?)'
    con.execute(sql, [token, age, weight, height, gender, email])
    con.commit()

def create_activity(token, activity): 
    con.execute('''CREATE TABLE IF NOT EXISTS activity (token TEXT, summary_date TEXT, timezone INTEGER, day_start TEXT, day_end TEXT, cal_active INTEGER, cal_total INTEGER, class_5min STRING, steps INTEGER, daily_movement INTEGER, non_wear INTEGER, rest INTEGER, inactive INTEGER, low INTEGER, medium INTEGER, high INTEGER, inactivity_alerts INTEGER, average_met REAL, met_1min INTEGER, met_min_inactive INTEGER, met_min_low INTEGER, met_min_medium INTEGER, met_min_high INTEGER, target_calories INTEGER, target_km REAL, target_miles INTEGER, to_target_km REAL, to_target_miles REAL, score INTEGER, score_meet_daily_targets INTEGER, score_move_every_hour INTEGER, score_recovery_time INTEGER, score_stay_active INTEGER, score_training_frequency INTEGER, score_training_volume INTEGER, rest_mode_state INTEGER, total INTEGER, PRIMARY KEY (token, day_start))''')    
    for activity_item in activity['activity']:        
        activity_item["token"] = token
        activity_item["met_1min"] = "|".join([str(x) for x in activity_item["met_1min"]])
        columns = ', '.join(activity_item.keys())
        placeholders = ', '.join('?' * len(activity_item))
        sql = 'INSERT OR REPLACE INTO activity ({}) VALUES ({})'.format(columns, placeholders)        
        values = [int(x) if isinstance(x, bool) else x for x in activity_item.values()]        
        con.execute(sql, values)
        con.commit()

def delete_table(table):
    sql = "DROP TABLE " + table
    con.execute(sql)
    con.commit()

def get_all_users():
    result = con.execute("SELECT * FROM users").fetchall()
    return result

def get_all_userinfo():    
    result = con.execute("SELECT userinfo.*, users.userid FROM userinfo INNER JOIN users ON users.token = userinfo.token").fetchall()    
    return result

def get_all_activity():
    result = con.execute("SELECT activity.*, users.userid FROM activity INNER JOIN users ON users.token = activity.token").fetchall()
    return result