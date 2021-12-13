import pymysql

USER = 'root'
PORT = 3306
PWD = '0000'
HOST = 'localhost'


'''
입력
접속 -> 커서잡고 -> 쿼리문 작성 -> excute -> commit -> 종료
'''
def input_db(database, table, title, point, genre_code, detail, u = USER, P = PORT, p = PWD, h = HOST):
    conn = pymysql.connect(host=h, port = P, user = u, password = p, db=database, charset = 'utf8')
    curs_input = conn.cursor()
    sql_input = f'insert ignore into {table}(title, point, genre_code, detail) values(%s, %s, %s, %s)'
    curs_input.execute(sql_input, (title, point, genre_code, detail))
    conn.commit()
    conn.close()

'''
출력
커서 잡고(딕셔너리) -> 쿼리문 -> excute -> fetch -> 출력
'''
def print_db(sql_output):
    movie_list = []
    conn = pymysql.connect(host=HOST, port = PORT, user = USER, password = PWD, db='movie_list', charset = 'utf8')
    curs_output = conn.cursor(pymysql.cursors.DictCursor)
    sql_output = 'select * from ' + sql_output 
    curs_output.execute(sql_output)
    movie = curs_output.fetchall()

    for row in movie:
        movie_list.append([row['title'], row['point'], row['genre_code'], row['detail']])
    conn.close()
    
    return movie_list
    