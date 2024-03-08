<h1 align="center"> Workshop_001etl - Python-Data-Engineer </h1>
<p align="left">
   <img src="https://img.shields.io/badge/STATUS-FINISHED-green">
   </p>

### Presented by Paola Andrea Chaux Campo, students of Autonoma de Occidente University

## Table of contents
* [Description](#Description)

* [Quick](#Quick data overview)

*[Objective](#Objective)

*[Brief](#Brief description of what was done)

*[Requeriments](#Requeriments)

*[Features](#Features)

*[Installation](#Installation Steps)

*[Considerations](#Considerations)

*[Conclusión](#conclusión)

*[References](#References)


## Description

#### In this repository i worked an proyect's ETL process of posibbles candidates, with a csv file with 50.000 rows.

#### The process with the CSV file that is read by Jupyter Notebook to transfer the data to a relational database use PostgreSQL, the data is read from the database to perform the respective EDA and also the Dashboard.

## Quick data overview
#### The CSV file is data from candidates who participated in selection processes (these data were randomly generated). 
### We have 50.000 rows of data about candidates. The fields are:
*First Name
*Last Name
*Email
*Country
*Application Date
*Yoe (years of experience)
*Seniority
*Technology
*Code Challenge Score
*Technical Interview

## Objective 
#### Demonstrate my knowledge about data management and visualizations and show specific metrics in chart visualizations. Present in a report with significant conclusions.

### The visualizations that I show are:
#### Hires by technology (pie chart).
#### Hires by year (horizontal bar chart).
#### Hires by seniority (bar chart).
#### Hires by country over years (USA, Brazil, Colombia, and Ecuador only)(multiline chart) .

## Brief description of what was done
#### In this challenge,I demonstrated my skills: The given csv was used, an exploratory data analysis data to determine if it needs any imputation or some type of cleaning, it was found that it was perfect to work with, The data was uploaded to a relational database management system, which I chose Postgres, the data was called for both analysis and visualization in Power BI, conclusions were generated from the study of the graphs and the analysis and the proposed challenge was finally fulfilled.

## Requeriments
### *Jupiter Notebook.
### *Pandas.
### *Psycopg2.
### *Json.
### *Datetime.
### *Powerbiclient. 
### *Numpy.
### *Matplotlib.pyplot.
### *Python.

## 6. Features
#### The most important thing that can be highlighted is that there were several problems when using new tools but they were easily overcome. We were able to observe that although they are random data, they were quite logical when it came to drawing conclusions. I was able to find that in the last year of registration which would be 2022, there was only data until July, which had to be taken into account when making precise conclusions.

## 7. Installation Steps
### 1. Clone the repository.
### 2. Open the proyect with Visual Studio Code.
#### 3. Create a virtual environment from your terminal: "python -m venv [environment_name]"
#### 4. Activate your virtual environment: "[environment_name]/Scripts/activate"
#### 5. Install the required tools and modules in the environment.
#### 6.Set the created environment as kernel.
### 7. Run the app and enjoy it.

## Considerations
### In the visualization part in Power BI Client, what is done is a generalized report that we can edit by having an account in Power BI and logging in, this file is only shown to the user and the inclusion of this notebook is only as a guide so that they can create their own pre-made reports with this tool that facilitates interaction, after saving it we can continue editing from the picnicpal page and download it as a .pbix format or in pdf for greater flexibility to share it, it will be attached in the references of all sites to help you with this tool.

## Conclusions
####

## References
#### https://www.youtube.com/watch?v=jlvMxTn_fOU
#### https://www.youtube.com/watch?v=ag5vK3R_h7M
#### https://www.youtube.com/watch?v=pPhQfeSgO6o
#### https://www.youtube.com/redirect?
#### event=video_description&redir_token=QUFFLUhqblJHTEN4VzV6WVI0cE9Nb2liR2tkcGptWUNUQXxBQ3Jtc0tuNmV3MEF3Z3NWNDczM0Iwb3FJc3NrTE9zUGZ6ak9SUU1ueUZLZURwWWs3Q0xVc1JacEdvemZDNGhxVWhKUlN5UnhWUzdqZEliSWJ2bGtlTkNGRmNTX3JSUEFraEdhRl9oaVZ4NEVlMWRyRnFVeVYzSQ&q=https%3A%2F%2Fgithub.com%2Flearn2excel%2FPowerBI&v=pPhQfeSgO6o
#### https://powerbi.microsoft.com/es-mx/blog/create-power-bi-reports-in-jupyter-notebooks/
#### https://bertia.es/incrustar-informes-de-power-bi-en-jupyter-notebook/
#### https://pypi.org/project/powerbiclient/
#### https://www.neoguias.com/como-conectarse-postgresql-python/#Como_conectarte_a_una_base_de_datos
#### https://www.studocu.com/bo/document/universidad-mayor-de-san-andres/programacion-i/tarea-4python-ejercicios/33129056
#### https://es.stackoverflow.com/questions/185298/importar-una-funci%C3%B3n-de-otro-archivo-ipynb-en-jupyter-notebook
#### https://github.com/dventep/workshop001_etl_education/blob/main/notebooks/eda_report.ipynb
#### https://learn.microsoft.com/es-es/power-bi/consumer/end-user-change-sort
#### https://pypi.org/project/powerbiclient/
#### https://learn.microsoft.com/es-es/power-bi/create-reports/jupyter-quick-report
#### https://learn.microsoft.com/es-es/javascript/api/overview/powerbi/powerbi-jupyter
#### https://learn.microsoft.com/es-es/power-bi/connect-data/service-tutorial-connect-to-github

