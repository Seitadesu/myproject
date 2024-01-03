import psycopg2

#データベースになります。localhostで実験する場合は、postgreSQLをご利用ください。

conn = psycopg2.connect(
    host="localhost",
    database="aisakkyoku",
    user="postgres",
    password="・・・"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE  sakkyokutable(
    id SERIAL PRIMARY KEY, 
    song VARCHAR(32) NOT NULL, 
    font VARCHAR(100), 
    color VARCHAR(32), 
    composition VARCHAR(32), 
    target VARCHAR(32), 
    how VARCHAR(32), 
    conditions VARCHAR(32), 
    language VARCHAR(32),
    keywords VARCHAR(32) NOT NULL,
    prompt VARCHAR(400) NOT NULL, 
    song_text VARCHAR(5000) NOT NULL,
    publish BOOLEAN DEFAULT FALSE,  -- Add the 'publish' column as a BOOLEAN with default value FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    url_character VARCHAR(400) NOT NULL
);
""")

conn.commit()
conn.close()
