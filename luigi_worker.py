import luigi
import pandas as pd
import sqlite3
from luigi import LocalTarget, Task, WrapperTask



class loadReviewsData(Task):
    
    def run(self):
        conn = sqlite3.connect('academi.db')
        data = pd.read_excel('raw_data/week1/reviews_q1.xlsx')
        data.to_sql(
            'reviews',
            conn,
            index=False,
            if_exists='replace'
            )
        

class loadFile1000Data(Task):
    
    def run(self):
        conn = sqlite3.connect('academi.db')
        
        data = pd.read_excel('raw_data/week1/file_1000.xls')
        data.loc[data.Gender == "Male", "Gender"] = "M"
        data.loc[data.Gender == "Female", "Gender"] = "F"
        data.drop(["First Name.1", "Unnamed: 0"],axis=1)
        
        data.to_sql(
            'file1000',
            conn,
            index=False,
            if_exists='replace'
            )
        
        
class loadDisasterData(Task): 
    
    def run(self):
        conn = sqlite3.connect('academi.db')
        
        data = pd.read_csv('raw_data/week1/disaster_data.csv')
        data.keyword = data.keyword.fillna("Null") 
        data.location = data.location.fillna("Null") 
        
        data.to_sql(
            'disaster',
            conn,
            index=False,
            if_exists='replace'
            )
        
        
class loadAlbumsData(Task): 
    
    def run(self):
        chinookDb = sqlite3.connect('raw_data/week1/chinook.db')
        academiDb = sqlite3.connect('academi.db')

        query = """SELECT * FROM albums"""
        data = pd.read_sql(sql=query, con=chinookDb)
        
        data.to_sql(
            'albums',
            academiDb,
            index=False,
            if_exists='replace'
            )
         

class loadArtistsData(Task): 
    
    def run(self):
        chinookDb = sqlite3.connect('raw_data/week1/chinook.db')
        academiDb = sqlite3.connect('academi.db')

        query = """SELECT * FROM artists"""
        data = pd.read_sql(sql=query, con=chinookDb)
        
        data.to_sql(
            'artists',
            academiDb,
            index=False,
            if_exists='replace'
            )
         
         
class loadCustomersData(Task): 
    
    def run(self):
        chinookDb = sqlite3.connect('raw_data/week1/chinook.db')
        academiDb = sqlite3.connect('academi.db')

        query = """SELECT * FROM customers"""
        data = pd.read_sql(sql=query, con=chinookDb)
        
        data.to_sql(
            'customers',
            academiDb,
            index=False,
            if_exists='replace'
            )
                 
           
class loadEmployeesData(Task): 
    
    def run(self):    
        chinookDb = sqlite3.connect('raw_data/week1/chinook.db')
        academiDb = sqlite3.connect('academi.db')

        query = """SELECT * FROM employees"""
        data = pd.read_sql(sql=query, con=chinookDb)
        data.ReportsTo = data.ReportsTo.fillna(0) 
        
        data.to_sql(
            'employees',
            academiDb,
            index=False,
            if_exists='replace'
            )
                  

class loadGenresData(Task): 
    
    def run(self):
        chinookDb = sqlite3.connect('raw_data/week1/chinook.db')
        academiDb = sqlite3.connect('academi.db')

        query = """SELECT * FROM genres"""
        data = pd.read_sql(sql=query, con=chinookDb)
        
        data.to_sql(
            'genres',
            academiDb,
            index=False,
            if_exists='replace'
            )
        
        
class loadInvoiceItemsData(Task): 
    
    def run(self):
        chinookDb = sqlite3.connect('raw_data/week1/chinook.db')
        academiDb = sqlite3.connect('academi.db')

        query = """SELECT * FROM invoice_items"""
        data = pd.read_sql(sql=query, con=chinookDb)
        
        data.to_sql(
            'invoice_items',
            academiDb,
            index=False,
            if_exists='replace'
            )
        

class loadInvoicesData(Task): 
    
    def run(self):
        chinookDb = sqlite3.connect('raw_data/week1/chinook.db')
        academiDb = sqlite3.connect('academi.db')

        query = """SELECT * FROM invoices"""
        data = pd.read_sql(sql=query, con=chinookDb)
        
        data.to_sql(
            'invoices',
            academiDb,
            index=False,
            if_exists='replace'
            )


class loadMediaTypesData(Task): 
    
    def run(self):
        chinookDb = sqlite3.connect('raw_data/week1/chinook.db')
        academiDb = sqlite3.connect('academi.db')

        query = """SELECT * FROM media_types"""
        data = pd.read_sql(sql=query, con=chinookDb)
        
        data.to_sql(
            'media_types',
            academiDb,
            index=False,
            if_exists='replace'
            )
                       

class loadPlaylistTrackData(Task): 
    
    def run(self):
        chinookDb = sqlite3.connect('raw_data/week1/chinook.db')
        academiDb = sqlite3.connect('academi.db')

        query = """SELECT * FROM playlist_track"""
        data = pd.read_sql(sql=query, con=chinookDb)
        
        data.to_sql(
            'playlist_track',
            academiDb,
            index=False,
            if_exists='replace'
            )


class loadPlaylistsData(Task): 
    
    def run(self):
        chinookDb = sqlite3.connect('raw_data/week1/chinook.db')
        academiDb = sqlite3.connect('academi.db')

        query = """SELECT * FROM playlists"""
        data = pd.read_sql(sql=query, con=chinookDb)
        
        data.to_sql(
            'playlists',
            academiDb,
            index=False,
            if_exists='replace'
            )


class loadTracksData(Task): 
    
    def run(self):
        chinookDb = sqlite3.connect('raw_data/week1/chinook.db')
        academiDb = sqlite3.connect('academi.db')

        query = """SELECT * FROM tracks"""
        data = pd.read_sql(sql=query, con=chinookDb)
        
        data.to_sql(
            'tracks',
            academiDb,
            index=False,
            if_exists='replace'
            )


class runAllTask(WrapperTask):

    def requires(self):
        yield loadReviewsData()
        yield loadFile1000Data()
        yield loadDisasterData()
        yield loadAlbumsData()
        yield loadArtistsData()
        yield loadCustomersData()
        yield loadEmployeesData()
        yield loadGenresData()
        yield loadInvoiceItemsData()
        yield loadInvoicesData()
        yield loadMediaTypesData()
        yield loadPlaylistTrackData()
        yield loadPlaylistsData()
        yield loadTracksData()
  
  
if __name__ == '__main__':
    luigi.run()