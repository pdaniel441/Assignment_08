#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: Patrick Danielson, 2021-Mar-07, Completed Code for Assignment
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# PDanielson, 2021-Mar-07, added code to complete Assignment_08 tasks
#------------------------------------------#
import os.path

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
lstRow = [] # empty list to store user entry

# Check for Existing Inventory File
if os.path.exists(strFileName): 
    pass
else:
    objFile = open(strFileName,'w')
    objFile.close()

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TODone Add Code to the CD class
    # -- Fields ------- #
    # -- Constructor -- #
    def __init__(self,value1,value2,value3):
        # -- Attributes --- #
        self.__cd_id = None
        self.__cd_title = None
        self.__cd_artist = None
        self.cd_id = value1
        self.cd_title = value2
        self.cd_artist = value3
        
    # -- Properties --- #
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self,value):
        if type(value) == int:
            self.__cd_id = value
        else: raise Exception('*** VALUE ERROR ***\nThe CD ID must be an integer!')
    
    
    @property
    def cd_title(self):
        return self.__cd_title
   
    @cd_title.setter
    def cd_title(self,value):
        if type(value) == str:
            self.__cd_title = value
        else: raise Exception('*** ERROR: Title Must be a String!')
    
    @property
    def cd_artist(self):
        return self.__cd_artist
        
    @cd_artist.setter
    def cd_artist(self,value):
        if type(value) == str:
            self.__cd_artist = value
        else: raise Exception('*** ERROR: Artist Must be a String!')
        
    # -- Methods ------ #


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name,lst_Inventory): -> (a list of CD objects)

    """
    # TODone Add code to process data from a file
    @staticmethod
    def load_inventory(file_name,table):
        """Function to read in data from file into a list of objects.
        
        Reads in the data from file identified by file_name into a 2D table structure
        (list of objects) containing data for CD entries stored in file.
        
        Args:
            file_name (string): name of file where data is stored
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime 
            
        Returns:
            None.
        """
        
        table.clear()  # this clears existing data and allows to load data entirely file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            data[0] = int(data[0])
            track_obj = CD(data[0],data[1],data[2])
            table.append(track_obj)
        objFile.close()
        
    # TODO Add code to process data to a file
    @staticmethod
    def save_inventory(file_name,table):
        """Function to save data table stored in runtime to a *.txt file
        
        Args:
            file_name (string): name of file to write data to
            table (list of objects): 2D data structure (list of objects) that holds data during runtime
        
        Returns:
            None.
        """
        
        objFile = open(file_name,'w')
        for obj in table:
            lst_values = [obj.cd_id,obj.cd_title,obj.cd_artist]
            lst_values[0] = str(lst_values[0])
            objFile.write(','.join(lst_values) + '\n')
        objFile.close()
            
    

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODone add docstring
    """Processes User Inputs and Output to Window
    
    properties:
        
    
    methods:
        display_menu(): -> None
        read_user_choice(): -> (string of user's choice)
        display_inventory(lst_Inventory): -> None
        get_new_entry(): -> (list of strings)
    
    """
    # TODone add code to show menu to user
    @staticmethod
    def display_menu():
        """Displays a menu with input choices to the user.
        
        Args:
            None.
            
        Returns:
            None.
        """
        print('Program Menu:\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    # TODone add code to captures user's choice
    @staticmethod
    def read_user_choce():
        """Get user input for selection from Menu Options.
        
        Args:
            None.
            
        Return:
            user_choice (string): lower case of user input when given choices of l, a, i, s, or x
        """
        choice = ''
        while choice not in['l','a','i','s','e','x']:
            choice = input('Which Operation would you like to perform? ').lower().strip()
        print()
        return choice
    
    # TODone add code to display the current data on screen
    @staticmethod
    def display_inventory(table):
        """Displays the current inventory saved in memory.
        
        Args:
            table (list of CD Objects): 2D data structure holding data during runtime
        
        Returns:
            None.
        """
        print('======= Current Inventory =======')
        print('ID\tCD Title\tArtist\n')
        for obj in lstOfCDObjects:
            print('{}, {}, {}'.format(obj.cd_id, obj.cd_title, obj.cd_artist))
        print('=================================')
        
    # TODone add code to get CD data from user
    @staticmethod
    def get_new_entry():
        """Get information from user for new CD Entry and return list of strings containing the entries.
        
        Args:
            None.
            
        Returns:
            strID (string): User input string for the entry ID
            strTitle (string): User input string for the entry CD Title
            strArtist (string): User input string for the entry CD Artist
                
        """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return [strID, strTitle, strArtist]

# -- Main Body of Script -- #
# TODone Add Code to the main body
# Load data from file into a list of CD objects on script start
FileIO.load_inventory(strFileName,lstOfCDObjects)

# Main Loop
while True:
    # 1. Display Menu to User
        # show user current inventory
        # let user add data to the inventory
        # let user save inventory to file
        # let user load inventory from file
        # let user exit program
    IO.display_menu()
    user_choice = IO.read_user_choce()
    
    # 2. Process Selection
    # 2.1 Initially Check for Exiting Program
    if user_choice == 'x':
        break
    
    # 2.2 Check other Menu Options
    # 2.2.1 Confirm and Process Selection to Load in Data from File
    if user_choice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading data from file...')
            FileIO.load_inventory(strFileName,lstOfCDObjects)
            IO.display_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue
    
    # 2.2.2 Collect Entry from User and Append Object to Table
    elif user_choice == 'a':
        lstRow = IO.get_new_entry()
        try:
            lstRow[0] = int(lstRow[0])
            lstOfCDObjects.append(CD(lstRow[0],lstRow[1],lstRow[2]))
        except ValueError as e:
            print('*** VALUE ERROR ***\nThe CD ID must be an integer!\n',e)
        continue
    
    # 2.2.3 Diplay Inventory Back to User
    elif user_choice == 'i':
        IO.display_inventory(lstOfCDObjects)
        continue
    
    # 2.2.4 Confirm and Process Selection to Save Object Attributes to Text File
    elif user_choice == 's':
        IO.display_inventory(lstOfCDObjects)
        user_choice = input('Do you wish to save this inventory to file? [y/n] ').strip().lower()
        if user_choice == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue

    # Catch All Error Message, should not be reached
    else: 
        print('General Program Error')

