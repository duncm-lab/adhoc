#This defines some custom styles for spreadsheets

#bold row
#bold column
#border outside of data body
#border title
#group data on a particular row
import xlwt
#sys.path.append(raw_input('Location of worksheet class: '))

top_left      = xlwt.easyxf('border: top thin, left thin') 
top_right     = xlwt.easyxf('border: top thin, right thin') 
bottom_left   = xlwt.easyxf('border: bottom thin, left thin') 
bottom_right  = xlwt.easyxf('border: bottom thin, right thin') 
left          = xlwt.easyxf('border: left thin') 
right         = xlwt.easyxf('border: right thin') 
top           = xlwt.easyxf('border: top thin') 
bottom        = xlwt.easyxf('border:bottom thin') 

class Get_outline():
    
    def __init__(self):

    #define corners
    #tuples are designed col:row
        self.top_left_corner = (min(self.act_num_cols),min(self.act_num_rows))        
        self.top_right_corner = (max(self.act_num_cols),min(self.act_num_rows))       
        self.bottom_left_corner = (min(self.act_num_cols),max(self.act_num_rows))     
        self.bottom_right_corner = (max(self.act_num_cols),max(self.act_num_rows))    
        self.top_side = []
        self.bottom_side = []
        self.left_side = []
        self.right_side = []
     
    def crTop(self):
        self.least_row = min(self.act_num_rows)      
        self.cols = range(self.act_num_cols)[1:-1]   
        for i in cols:                            
             self.top_side.append((i, least_row)) 
                                                  
    def crBottom(self):                           
       self.most_row = max(self.act_num_rows)        
       self.cols = range(self.act_num_cols)[1:-1]    
       for i in cols:                             
           self.bottom_side.append((i, most_row)) 
                                                  
    def crLeft(self):                             
        self.least_col = min(self.act_num_cols)      
        self.rows = range(self.act_num_rows)[1:-1]   
        for i in rows:                            
            self.left_side.append((least_col, i)) 
                                                  
    def crRight(self):                            
        self.most_col = max(self.act_num_cols)       
        self.rows = range(self.act_num_rows)[1:-1]   
        for i in rows:                            
            self.right_side.append((most_col, i)) 

    #top side least col +1 --> greatest col -1, least row
    #bottom side least col +1 --> greatest col -1, most row
    #left side least col, least row +1 --> most row -1
    #right side most col, least row +1 --> most row -1
