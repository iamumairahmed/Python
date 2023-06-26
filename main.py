from selenium import webdriver
from selenium.webdriver.common.by import By
import schedule
import time
import helper
import re
import pyodbc


def task():
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=SERVERNAME;'
                      'Database=daraz;'
                      'Trusted_Connection=yes;')
    
    cursor = conn.cursor()

    try:
        create_table_query = """
        IF NOT EXISTS (
        SELECT 1
        FROM sys.tables
        WHERE name = 'darazdata'
        )
        
        BEGIN
            EXEC('
                CREATE TABLE darazdata (
                ID INT IDENTITY(1,1) PRIMARY KEY,
                Name VARCHAR(255),
                Price FLOAT
            )
        ')
        END
        """
        
        cursor.execute(create_table_query)

        conn.commit()
    except:
        pass

    driver = webdriver.Chrome()

    url = 'https://www.daraz.pk/catalog/?q=keyboard&_keyori=ss&from=input&spm=a2a0e.home.search.go.35e34076vwahsV'
    driver.get(url)
    time.sleep(5)
    mainDiv = driver.find_elements(By.CLASS_NAME,"box--pRqdD")
    for div in mainDiv:
        name = div.find_element(By.CLASS_NAME, "title--wFj93")
        name = name.text
        print(name)

        price = div.find_element(By.CLASS_NAME, "price--NVB62")
        price = price.text
        price = price.split()
        price = price[-1]
        price = re.sub(r",", "", price)
        price = int(price)

        query = "INSERT INTO darazdata(Name, Price) VALUES (?, ?);"
        vals = (name, price)
        cursor.execute(query, vals)
        print("All Data Insert", helper.get_time())
        conn.commit()


schedule.every(60).seconds.do(task)

while True:
    schedule.run_pending()