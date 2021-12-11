## Download Python
Head to the following link to download Python for the appropriate platform (macOS/Windows): https://www.python.org/downloads/

## Clone GitHub Project
Copy and paste the following commands into the Terminal. These commands download the R2M project folder onto your Desktop.
```Shell
cd Desktop
git clone git@github.ibm.com:DRT/R2M.git

```
## Install Pip
Copy and paste the following commands into the Terminal:
```Shell
cd ..
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

## Install Jupyter Notebook
Copy and paste the following command into the Terminal:
```Shell
pip install jupyterlab

```

## Run Jupyter Notebook
After you run this command, a browser will open with Jupyter Notebook.
```Shell
jupyter-lab

```

## Open R2M Jupyter Notebook
In the Jupyter Notebook directory, click on Desktop -> R2M -> R2M_Simulation_Nov2021.ipynb.
The Jupyter Notebook will open up in a new tab.

![alt text](https://github.ibm.com/DRT/R2M/blob/dev/docs/Jupyter_Notebook_Directory.png)


## Run Jupyter Notebook
Click on the "Restart" button in Jupyter Notebook.
Then, click on the "Run" button.
![alt text](https://github.ibm.com/DRT/R2M/blob/dev/docs/Jupyter_Notebook.png)

## View Results
The results are located in the R2M folder on your Desktop titled newOppCounts_clean.xlsx.

## Add New Excel Spreadsheets to R2M Simulation
### 1. Rename files to the following format: AI_Apps_Product_Pipe_MM-DD.xlsx (Ex. AI_Apps_Product_Pipe_08-04.xlsx)
![alt text](https://github.ibm.com/DRT/R2M/blob/dev/docs/Example_File.png)

### 2. Add files to "data" folder in R2M folder on Desktop
![alt text](https://github.ibm.com/DRT/R2M/blob/dev/docs/R2M_data.png)

### 3. Run Jupyter Notebook
Click on the "Restart" button in Jupyter Notebook.
Then, click on the "Run" button.
![alt text](https://github.ibm.com/DRT/R2M/blob/dev/docs/Jupyter_Notebook.png)

