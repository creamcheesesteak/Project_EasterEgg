import sqlite3
import pandas as pd

nations = ['Australia', 'Austria', 'Belgium', 'Brazil', 'Chile', 'Croatia', 'Finland', 'France', 'Germany', 'Egypt', 'Greece',  'Hungary', 'India',
           'Indonesia', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Japan', 'Malaysia', 'Mexico',
           'Netherlands', 'Philippines', 'Poland', 'Portugal', 'Russia', 'Spain', 'Sweden', 'Switzerland', 'Taiwan', 'Thailand', 'Turkey',
           'Ukraine','Uruguay', 'Vietnam', 'Czech_Republic', 'Hong_Kong', 'New_Zealand', 'South_Korea', 'United_Kingdom']

db_nation = sqlite3.connect('../nation.db')
c = db_nation.cursor()

# c.execute("DROP TABLE "+file_name+";")

for nation in nations:
    path = 'C:/Users/LimTH/Desktop/practice/data/i_p/i_p_%s.xls' % nation
    file_name = path[path.rfind('/') + 1:-4]
    c.execute("CREATE TABLE "+file_name+" (id INTEGER PRIMARY KEY, App TEXT, App_c Text, App_cat TEXT)")
    dfs = pd.read_excel(path, header=None)
    id = 1
    for row in dfs.iterrows():
        app = row[1][0]
        app_c = row[1][1]
        app_cat = row[1][2]
        c.execute("INSERT INTO "+file_name+" (id, App, App_c, App_cat) VALUES(?,?,?,?) ", (id, app, app_c, app_cat))
        id += 1
db_nation.commit()



