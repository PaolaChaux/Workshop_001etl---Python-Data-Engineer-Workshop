#!/usr/bin/env python
# coding: utf-8

# In[21]:


import psycopg2
import pandas as pd


# In[23]:


import psycopg2
import json

def create_connection():
    try:
        with open('db_config.json') as file:
            config = json.load(file)
        connection = psycopg2.connect(
            host='localhost',
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        print('Conexión exitosa!!')
    except psycopg2.Error as e:
        connection = None
        print('No se puede conectar:', e)
    return connection


# In[27]:


def crear_tabla():
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Candidates (
                        CandidateID SERIAL PRIMARY KEY,
                        First_Name VARCHAR(255) NOT NULL,
                        Last_Name VARCHAR(255) NOT NULL,
                        Email VARCHAR(255) NOT NULL,
                        ApplicationDate DATE NOT NULL,
                        Country VARCHAR(255) NOT NULL,
                        YearsOfExperience INT NOT NULL,
                        SeniorityLevel VARCHAR(255) NOT NULL,
                        TechnologyStack VARCHAR(255) NOT NULL,
                        CodeChallengeScore SMALLINT NOT NULL,
                        TechnicalInterviewScore SMALLINT NOT NULL,
                        IsHired BOOLEAN NOT NULL
                    );
                """)
            connection.commit()
            print("Tabla creada con éxito.")
        except psycopg2.Error as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("No se pudo establecer la conexión con la base de datos.")
        
crear_tabla()


# In[28]:


df = pd.read_csv('candidates.csv', sep=';')


# In[29]:


connection = create_connection()
def insertar_datos(df):
    cursor = connection.cursor()
    query = """
    INSERT INTO Candidates (First_Name, Last_Name, Email, ApplicationDate, Country, YearsOfExperience, SeniorityLevel, TechnologyStack, CodeChallengeScore, TechnicalInterviewScore, IsHired)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        for index, row in df.iterrows():
            is_hired = row['Code Challenge Score'] >= 7 and row['Technical Interview Score'] >= 7

            data = (row["First Name"], row["Last Name"], row["Email"], row["Application Date"], row["Country"],
                    row["YOE"], row["Seniority"], row["Technology"], row["Code Challenge Score"], row["Technical Interview Score"], is_hired)
            cursor.execute(query, data)
        connection.commit()
        print("Datos insertados exitosamente")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cursor.close()
        connection.close()
        
insertar_datos(df)

