import os
import pandas as pd
import glob
import patoolib

def extractor(FileName,InDir = 'C:\\Users\\tarun\\Downloads',OutDir = 'C:\\Users\\tarun\\Downloads\\Extracted'):
    """
    Pass file name with extension and Input Directory(InDir) along with Output Directory (OutDir)
    """
    if not os.path.exists(OutDir):
       os.makedirs(OutDir)
    os.chdir(InDir)
    os.listdir()
    Files = glob.glob(FileName)
    for file in Files:
        print('Processing {}'.format(file))
        patoolib.extract_archive(file,outdir=OutDir)
        print('{} Extracted'.format(file))
    
def concatenate(InDir = 'C:\\Users\\tarun\\Downloads\\Extracted',OutDir = 'C:\\Users\\tarun\\Downloads\\Concatenated.csv'):
    """
    If there are multiple files in a folder supposed to be Concatenated,
    Pass Input Directory(InDir) along with Output Directory (OutDir)
    """
    os.chdir(InDir)
    DfList = []
    filelist = glob.glob('*.xls')
    for filename in filelist:
        print(filename)
        df = pd.read_excel(filename,skiprows=[0,1,2])
        DfList.append(df)
    concatDf = pd.concat(DfList,axis=1)
    concatDf.to_csv(OutDir,index=None)
        
def merge(InDir = 'C:\\Users\\tarun\\Downloads', OutDir = 'C:\\Users\\tarun\\Downloads\\Merged.csv'):
    """
    If there are Duplicate Columns in a merged files,
    Pass Input Directory(InDir) along with Output Directory (OutDir)
    """
    os.chdir(InDir)
    df = pd.read_csv('Concatenated.csv')
    nodupl = df.T.drop_duplicates().T
    nodupl.to_csv(OutDir,index = None)


    
        
    