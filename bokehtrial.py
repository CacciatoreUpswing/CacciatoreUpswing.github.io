#%reset
%matplotlib inline
import sqlalchemy as sa
import matplotlib.pyplot as plt  
import pandas as pd  
import numpy as np
from datetime import datetime
from io import StringIO
import seaborn
from bokeh.plotting import figure, output_file, show


### Dictionary for school names, id, colors and contract start dates ###

school_dict = {
'albemarle': ['College of the Albemarle','dJ4uO5gd/dFh389UiC1atENKjro=','#003b7a','#e1e1e1','01-01-2015'],
'andrewcollege': ['Andrew College','jpllGAtjw5fZiHFSJhE1ts+r7lU=','#005C2D', '#0A3C71','08-01-2015'],
'bladencc': ['Bladen','bPdn8ZizRNrYoNgisbD1zDFyBQs=','#154328','#e1e1e1', '08-01-2014'],
'cccc': ['Central Carolina','DjpqyMPyE8eYdqmMSM3RA6VCtbo=','#3373bd','#e36435','08-01-2014'],
'davidsonccc': ['Davidson County','dzdubSr6BjKV1n2+uvLRqXYzT4k=','#00529b','#e1e1e1', '08-01-2014'],
'durhamtech': ['Durham Tech','QMLfD3HatkC7npiI5M1D5VddUFI=','#266e45','#e47711','08-01-2014'],
'faytechcc': ['Fayetteville Tech','n2VCkk4IpfJifF6blr5X7+IKwfc=','#d3b827','#000000','8-1-2015'],
'gtcc': ['Guilford Tech','z7IU4g/CncgjID5nVxS6/NUtrHw=','#016F52','#e1e1e1','8-1-2015'],
'martincc': ['Martin', 'ssWZLBd1Fatxz0uD4UQjWbvus1U=','#B10000', '#e1e1e1','8-1-2015'],
'mitchellcc': ['Mitchell', '0B7EY/155YXykGLelOqq00dQJI8=','#8b1c40', '#e1e1e1','8-1-2015'],
'ncvps': ['NCVPS','4tBsmpzD+Z03iO0I4fepxb4pCOs=','#a8ce00','#e1e1e1','4-15-2015'],
'pittcc': ['Pitt','3fP/56TVYSPvQJiWF1grcUhjV70=','#1976d2','#4f9700','8-1-2015'],
'pqc': ['Paul Quinn','WcDLm7GWGy4kLS8wAOAV4HTyAmk=','#411158','#e1e1e1','8-1-2015'],
'rangercollege': ['Ranger','pqhXsrjAPD2Zcd3Yr3PRT6287JU=','#411158','#e1e1e1','8-1-2015'],
'richmondcc': ['Richmond', 'Y4ep63UZb/7YTF7+wasjAY89jv8=','#9F1933', '#e1e1e1','8-1-2015'],
#'smartercollege': ['Smarter College','#fdba2d','#e1e1e1'],
'southtexascollege': ['South Texas','++vBlft+L8azVp+GigumdCcNOjQ=','#411158','#e1e1e1','9-1-2015'],
'swtjc': ['SWTJC', 'r3VTTGTa0iRXDvr2ARo0RgbXoy4=','#344c9e', '#e1e1e1','8-1-2015'],
'unt': ['UNT', 'DQ5kQxwyjVMm5Bg7dttKnwTCFYI=','#00853E', '#e1e1e1','07-01-2015'],
#'upswing': ['Upswing','4oata4NHARFhu5+5u4lorOsZsqA=','#2196f3','#ff5252'],
'utpb': ['UT Permian Basin', 'bM9NJsG67yXK7Wc2BhY6lCMEbz0=','#c95100', '#000000','08-01-2015'],
'vgcc': ['Vance Granville','DhxCPIq4r39Ob7Z95EeuPi3cFk4=', '#025102', '#e1e1e1','10-01-2015'],
'westgatech': ['West Georgia Tech', 'vmXPseWiLooNKXYIfs6yb534P2E=','#e80649', '#e1e1e1','08-01-2015'],
'richlandcollege': ['Richland College', 'MCKVJ3mnV+cbF/7NMPjFBp5XPb0=','#008752', '#92278f','8-1-2015'],
'beaufortccc': ['Beaufort County','KSPBWqGbAuvCvsbliLF4ZoqBmY0=','#006dff', '#e1e1e1','08-31-2015'],
'odessa': ['Odessa', 'DBkwvCdCp3H8SptHaHDXtcX78SY=','#0067B1', '#00A2E5','9-1-2015'],
'king': ['King', '7w2W4kbi8bInL8sCjgFFO41oQdU=','#083a81', '#fbe06c','9-1-2015'],
'alameda': ['College of Alameda', 'YT4m9O+SEe3s49/wuEk5QLd0Xpw=','#024383', '#cccccc', '01-01-2016'],
'americanhighschool': ['American High School','TGSu0Rs+HrbkuEJa4ceWfrs2XuQ=', '#344c9e', '#e1e1e1', '12-01-2015'],
'uvu': ['Utah Valley', '2FaghGo/wirqvi5NxkQd8sp8NVU=','#4D7123', '#e1e1e1','01-01-2016'],
'coastalbend': ['Coastal Bend','nfS1+QJZKVYNCVTYHivBPavOxQI=', '#00ADEF', '#e1e1e1','12-01-2015'],
'nwscc': ['NWSCC', 'ISIkgjJFbxsFOjjLH8lt2eARV6M=','#ed234b', '#1c4484','1-1-2016'],
'egcc': ['Eastern Gateway','A4pbtENN7/9FsChdGVV4icJrFNM=','#00529b', '#e1e1e1','1-1-2016'],
'qannection': ['Qannection','KrDhOygsNFBCIOWdaqhqr9omPLY=' ,'#DE7410', '#e1e1e1','11-01-2015'],
'palmbeachstate': ['Palm Beach State','r/N98CMdOn4ENgnxPap2Hc8tGzA=', '#2b6859', '#e1e1e1','2-1-2016'],
#'ufv': ['UFV', '#00713D', '#e1e1e1'],
'dc3': ['Dodge City', 's54RnKO1GibYCNnbj9JLgsDlXWU=','#411158', '#e1e1e1','03-01-2016'],
'grayson': ['Grayson','E8lEHaN19JIACDP+o4OQ9kEEj2M=','#21405f', '#eaeaea','1-1-2016'],
#'kpu': ['Kwantlen Polytechnic University', '#902935', '#e1e1e1'],
#'samuelmerritt': ['Samuel Merritt University', '#31779a', '#e1e1e1']
}

#index things we want from the dictionary
school_name = [item[0] for item in school_dict.values()]
school_id = [item[1] for item in school_dict.values()]
school_color1 = [item[2] for item in school_dict.values()]
school_color2 = [item[3] for item in school_dict.values()]
contract_start = [item[4] for item in school_dict.values()]
                    

#Connect to database
#engine = sa.create_engine('postgresql+pg8000://cacciatore:Guilmant77@localhost:5555/upswing', connect_args ={'ssl':True})
engine = sa.create_engine('postgresql+pg8000://cacciatore:Guilmant77@130.211.135.204:5432/upswing', connect_args ={'ssl':True})

# First query
cnx = engine.connect()

query  = """
SELECT 
coach_sessions.coach_session_id, coach_sessions.coach_session_scheduled,student_schools.school_id,student_schools.school_name,categories.category_name,student_feedback.student_understanding_rating, transactions.transaction_minutes
FROM coach_sessions
LEFT JOIN online_coach_sessions ON (coach_sessions.coach_session_id = online_coach_sessions.coach_session_id)
INNER JOIN subjects ON (subjects.subject_id = coach_sessions.subject_id)
INNER JOIN categories ON (subjects.category_id = categories.category_id)
INNER JOIN users AS coach ON (coach.user_id = coach_sessions.coach_user_id)
LEFT JOIN transactions ON (transactions.coach_session_id = online_coach_sessions.coach_session_id)
INNER JOIN schools AS coach_schools ON (coach.school_id = coach_schools.school_id)
INNER JOIN users AS student ON (student.user_id = coach_sessions.student_user_id)
INNER JOIN schools AS student_schools ON (student.school_id = student_schools.school_id)
LEFT JOIN online_coach_session_stats AS student_stats ON (student_stats.coach_session_id = coach_sessions.coach_session_id AND coach_sessions.student_user_id = student_stats.user_id)
LEFT JOIN online_coach_session_stats AS coach_stats ON (coach_stats.coach_session_id = coach_sessions.coach_session_id AND coach_sessions.coach_user_id = coach_stats.user_id)
LEFT JOIN users AS cancelling_user ON (cancelling_user.user_id = coach_sessions.cancelled_user_id)
LEFT JOIN coach_feedback ON (coach_feedback.coach_session_id = coach_sessions.coach_session_id AND coach_feedback.coach_user_id = coach.user_id AND coach_feedback.student_user_id = student.user_id)
LEFT JOIN student_feedback ON (student_feedback.coach_session_id = coach_sessions.coach_session_id AND student_feedback.coach_user_id = coach.user_id AND student_feedback.student_user_id = student.user_id)
WHERE student_schools.school_name != 'Upswing'

--AND coach_schools.school_name = 'Upswing'
--AND student_schools.school_id = '7w2W4kbi8bInL8sCjgFFO41oQdU='

AND transaction_minutes > 0
GROUP BY coach_sessions.coach_session_id,categories.category_name, student_schools.school_id, student_schools.school_name,student_schools.school_name, student_feedback.student_understanding_rating,transactions.transaction_minutes
ORDER BY coach_sessions.coach_session_scheduled ASC; 
"""

extract = cnx.execute(query)
usage = pd.DataFrame(extract.fetchall(), columns=extract.keys())



scolors = pd.Series(school_color1)
sid = pd.Series(school_id)
color_ref = pd.DataFrame({'school_id': sid, 'school_color': scolors} )


scat_df = usage.merge(color_ref,how='left', left_on=['school_id'], right_on=['school_id'])
scat_df[['coach_session_scheduled','school_name','school_color']]

for j in range(len(scat_df.index)):
    scat_df.loc[j,'counter'] = j
    


### Try out bokeh

x = scat_df['coach_session_scheduled']
y = scat_df['counter']



output_file("/Users/chriscacciatore/Google Drive/Data/clearlytics/cum_usage.html")

# create a new plot with a datetime axis type
p = figure(width=800, height=250, x_axis_type="datetime")

p.line(x, y, color='navy', alpha=0.5)

show(p)