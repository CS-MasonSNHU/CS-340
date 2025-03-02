from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
     """ CRUD operations for Animal collection in MongoDB """

     def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32325
        DB = 'AAC'
        COL = 'animals'
        
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print("Connected to DB:", DB, "and collection:", COL)
    
    # Complete this create method to implement the C in CRUD.
     def create(self, data):
        # Check if the input data is not None.
        if data is not None:
            # Insert the document into the 'animals' collection.
            self.database.animals.insert_one(data)
            # Print a success message after successful insertion.
            print("Successfull creation of animal!")
            return True
        else:
            # If the provided data is None, print an error message.
            print("Failed creation of animal!")
            return False                  
        
     def read(self, query):
         print("READ CALLED")
        # If no query is provided (i.e., query is None), set it to an empty dictionary.
        # An empty query will match all documents in the collection.
         if query is None:
            print("EMPTY QUERY")
            query = {}
            
            return list(query)
    
        # Execute the query on the 'animals' collection.
        # The find() method returns a cursor, which is then converted into a list of documents.
         results = list(self.database.animals.find(query))
        
         print("RESULTS BEING PRINTED")
        # Iterate over the retrieved documents and print each one.
         for i in results:
             print(i)
         return results
    
     # update function 
     def update(self, data, newData):
        # Indicate update operation was called
        print("UPDATE CALLED")
        
        # if the update call has data that is not correct, print message and returns # of modified count
        if data is None:
            print("NO UPDATE INFO")
            return result.modified_count
        
        #Updates based on filter and outputs and returns the modified count
        result = self.database.animals.update_one(data, newData)
        print("Updated records: ", result.modified_count)
        return result.modified_count
    
    #Delete function
     def delete(self, query):
        # Indicates that delete function was called.
        print("DELETE CALLED")
        
        #if the delete call has data that is not correct, print message and returns # of deleted count
        if query is None:
            print("NO QUERY INFO")
            return result.deleted_count
        
        #Deletes based on filter and outputs and returns the deleted count
        result = self.database.animals.delete_one(query)
        print("Deleted records: ", result.deleted_count)
        return result.deleted_count
       