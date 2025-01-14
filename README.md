# 2024 Financial Summary

## Description
This project is a endeavear to encapsulate a story of my total spending and any expenditures incurrd during 2024. To preface that I was very excited to kicked off this initiative, it provides a clear anlytic view of where, what, when and how much I spend from each transaction and reveal my spending habit that I won't otherwise take into much deep thinking

## Content

### Objective and Overview
Processes transactions data using Python scripts, stores the data in a PostgreSQL database while all the processes are running under docker's containers in a isolated environment

### Data Sources

1. **Primary Data Sources** (CSV Files):  
   - Capital One  
   - Bank of America  
   - Citi Bank  
   - PNC  
   - Herbert  

2. **Constructed Data** (Tables):  
   - Bank  
   - Payment Method  
   - Date  

### Dimensional Model

The final dimensional model consists of:  
- **Fact Table**: Transactions  
- **Dimension Tables**:  
  - Bank  
  - Payment Method  
  - Date  

*(Attach an image of the dimensional model)*  

### High-Level Process

#### Sequential Flow of Actions:
1. **Database Setup**:  
   - Docker starts a PostgreSQL server and creates the database with schemas for the required tables.  

2. **Data Extraction and Transformation**:  
   - Docker runs the `extract_and_transform.py` script, which processes source data and outputs `transaction.csv`.  

3. **Data Loading**:  
   - The processed `transaction.csv` file and dimension tables are loaded into the PostgreSQL database using the `load.py` script.  

All processes communicate with the PostgreSQL server hosted within Docker.

*(Attach an image of the high-level process)*  

### Transaction Table View

## Dashboard (Coming Soon)



