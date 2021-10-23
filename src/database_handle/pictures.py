from database_handle import conn




with conn:
    
    def check_for_picture(picture_name):

        with conn.cursor() as cursor:
            sql = "SELECT name FROM pictures WHERE name LIKE %s"
            cursor.execute(sql, (picture_name,))
            data = cursor.fetchone()
            if not data:
                return False
            return True
        

    def add(picture_file, picture_name):
        with conn.cursor() as cursor:
            sql = """INSERT INTO pictures (name,file) VALUES (%s, %s)"""
            cursor.execute(sql,(picture_name,picture_file))
            conn.commit()
        return

    def fetch(picture_name):
        with conn.cursor() as cursor:
            sql ="Select file from pictures WHERE name LIKE %s"
            cursor.execute(sql, (picture_name,))
            data = cursor.fetchone()
        return data

    def fetch_all_names():
        with conn.cursor() as cursor:
            sql = "Select name from pictures"
            cursor.execute(sql)
            data = cursor.fetchall()
        return data
