# Route-to-Market-Simulations

## Short Description
This repository is a tool for Sales or Product managers to automate and analyze sales pipeline progression data to determine a new product's Go-to-Market model. 

## Problem Statement
A Go-to-Market model needs to be designed as an integrated system inclusive of considerations across marketing, business development, sales and business partners.  This requires a deep understanding of sales, marketing, offering and competitive issues that will impact the sales and marketing pipeline.  These insights are in the existing and historical pipeline data, but the data is often in an unstructed format (*i.e.,* Excel Spreadsheets, Weekly Reports).


## The Idea
The idea is to take the existing weekly Excel spreadsheets that Salesforce, a common platorm used to track sales pipeline metrics, generates and translate those Excel Spreadsheets into actionable insights that Sales & Product Managers can use to plan incremental sales of the new product and remediate know issues impacting the pipeline (Not enough new leads? Deals not progressing quickly enough? Don't have access to the right decision makers?). This plan can continue to be adapted to reflect changing pipeline challenges. 


## Live Demo Setup
### Clone Git Repository
```Shell
git clone https://github.com/jessicajourneycake/Route-to-Market-Simulations.git
```
### Activate Virtual Environment
```Shell
cd <Project A>

python3 -m venv <Project A>

pipenv shell
```
### Install Requirements
```Shell
pip3 install -r ./requirements.txt
```

### Run Server
```Shell
python manage.py migrate
python manage.py runserver
```

### Link to Live Demo
http://127.0.0.1:8000/home/


## Solution Components

### Component 1 - Jupyter Notebooks for Data Cleansing & Preparation 




### Component 2 - User Interface for Product & Sales Managers 
The UI for Product & Sales Managers is used to automate and analyze sales pipeline progression. It answers common questions that Product Managers face today when adapting their Go-to-Market model:
- Is this product gaining traction in the market?
- Where is the product gaining traction and in what industries?
- Are opportunities progressing?
- What hold-ups are we experiencing in the progression of an opportunity?
- Who is making the sales? 
- I've adapted my GtM model. Are these changes effective?

## Full Setup (In Progress) 

