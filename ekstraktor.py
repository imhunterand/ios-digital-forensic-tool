import os
import sqlite3

def ekstrak_pesan(direktori_cadangan):
    db_path = os.path.join(direktori_cadangan, 'Manifest.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT fileID FROM Files WHERE relativePath LIKE "%sms%"')
    sms_db_id = cursor.fetchone()[0]

    sms_db_path = os.path.join(direktori_cadangan, sms_db_id[:2], sms_db_id)
    conn.close()

    conn = sqlite3.connect(sms_db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT text, date, address FROM message')
    pesan = cursor.fetchall()
    
    pesan_terorganisir = []
    for p in pesan:
        pesan_terorganisir.append({
            "teks": p[0],
            "tanggal": p[1],
            "alamat": p[2]
        })

    conn.close()
    return pesan_terorganisir
