import pymysql
import subprocess

import database.con_mysql as data_con



ffmpegPath = "E:\\ffmpeg-4.0-win64-static\\bin\\ffmpeg.exe"
CurMediaPath = "E:\\voley_video\\00051.mp4"


db = data_con.connectSql()

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# SQL 查询语句
sql = "select * from analysis_event right join analysis_bitvolleyevent on analysis_event.eventID = analysis_bitvolleyevent.eventID " \
      "where analysis_event.homeFlag = 'a' order by analysis_event.time"
# try:
   # 执行SQL语句
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
print(len(results))
action_num = 0
for row in results:

  event_time = row[5]
  event_time = event_time.replace(".", ":")
  event_type = row[4]
  home_flag = row[3] # *号是我方
  event_id = row[0]
  basic_kill = row[26]
  print(row)
  print("event_time = %s, event_type = %s, home_flag = %s, event_id = %s,basic_kill=%s" % \
         (event_time , event_type , home_flag , event_id,basic_kill) )
  if basic_kill == "S":
      action_num += 1
      # 视频片段截取
      videoStartTime = event_time
      videoSaveDir = "E:\\voley_video\\save_a\\%05d.mp4" % (action_num)
      videoEndTime = "00:00:06"
      md = ffmpegPath + ' -y -i ' + CurMediaPath + ' -ss ' + videoStartTime + ' -t ' + videoEndTime + \
           ' -acodec copy -vcodec copy -async 1 ' + videoSaveDir
      subprocess.call(md)

db.close()