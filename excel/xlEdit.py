#!/usr/bin/python

import xlrd
import xlwt
import xlutils
import re

class FancySheet:

    def __init__(self):
        #declare the workbook/worksheet variable
        self.wb_var = raw_input('Enter the location of the worksheet to be formatted: ')
        self.ws_var = input('Enter the worksheet ID(0 is left-most): ')
        self.r_wbook = xlrd.open_workbook('%s' %self.wb_var)
        self.r_wsheet = self.r_wbook.sheet_by_index(self.ws_var)
        self.w_wbook = xlwt.Workbook()
        self.w_wsheet = self.w_wbook.add_sheet('formatted')
        self.col_values = []

        self.row_values = []
        self.act_num_cols = int
        self.act_num_rows = int
        self.cell_coords = []
        self.dct_cell_coords = {}

    def get_col_data(self):
        #get the column data from the worksheet to be amended
        all_cols = self.r_wsheet.col_values
        for i in range(self.r_wsheet.ncols):
            self.col_values.append(all_cols(i))
        for i in range(self.r_wsheet.ncols):
            while '' in self.col_values[i]:
                self.col_values[i].remove('')
        while [] in self.col_values:
            self.col_values.remove([])
        self.act_num_cols = len(self.col_values)

    def get_row_data(self):
        #get the row data from the worksheet to be amended
        all_rows = self.r_wsheet.row_values
        for i in range(self.r_wsheet.nrows):
            self.row_values.append(all_rows(i))
        for i in range(self.r_wsheet.nrows):
            while '' in self.row_values[i]:
                self.row_values[i].remove('')
        while [] in self.row_values:
            self.row_values.remove([])
        self.act_num_rows = len(self.row_values)

    def get_outline(self):
    #define corners
    #tuples are designed - col:row
        self.dct_top_left_corner =     {(min(range(self.act_num_cols)),min(range(self.act_num_rows))):'top, left'}
        self.dct_top_right_corner =    {(max(range(self.act_num_cols)),min(range(self.act_num_rows))):'top, right'}
        self.dct_bottom_left_corner =  {(min(range(self.act_num_cols)),max(range(self.act_num_rows))):'bottom, left'}
        self.dct_bottom_right_corner = {(max(range(self.act_num_cols)),max(range(self.act_num_rows))):'bottom, right'}
        self.dct_top_side = {}
        self.dct_bottom_side = {}
        self.dct_left_side = {}
        self.dct_right_side = {}

    def cr_top(self):
        top_side = []
        least_row = min(range(self.act_num_rows))
        cols = range(self.act_num_cols)[1:-1]
        for i in cols:
             top_side.append((i, least_row))
        for i in top_side:
            self.dct_top_side[i] = 'top'

    def cr_bottom(self):
       bottom_side = []
       most_row = max(range(self.act_num_rows))
       cols = range(self.act_num_cols)[1:-1]
       for i in cols:
           bottom_side.append((i, most_row))
       for i in bottom_side:
           self.dct_bottom_side[i] = 'bottom'

    def cr_left(self):
        left_side = []
        least_col = min(range(self.act_num_cols))
        rows = range(self.act_num_rows)[1:-1]
        for i in rows:
            left_side.append((least_col, i))
        for i in left_side:
            self.dct_left_side[i] = 'left'

    def cr_right(self):
        right_side = []
        most_col = max(range(self.act_num_cols))
        rows = range(self.act_num_rows)[1:-1]
        for i in rows:
            right_side.append((most_col, i))
        for i in right_side:
            self.dct_right_side[i] = 'right'

    def create_data(self):
        #This creates a dict with the coordinate and value
        for i in range(len(self.col_values)):
            for j in range(len(self.col_values[i])):
                self.cell_coords.append((i,j))
        for i in self.cell_coords:
            self.dct_cell_coords[i] = [self.col_values[i[0]][i[1]]]

        #logic for corners
        for i in self.dct_cell_coords:
            if i in self.dct_top_left_corner:
                self.dct_cell_coords.get(i).append(self.dct_top_left_corner.values()[0])
            elif i in self.dct_top_right_corner:
                self.dct_cell_coords.get(i).append(self.dct_top_right_corner.values()[0])
            elif i in self.dct_bottom_left_corner:
                self.dct_cell_coords.get(i).append(self.dct_bottom_left_corner.values()[0])
            elif i in self.dct_bottom_right_corner:
                self.dct_cell_coords.get(i).append(self.dct_bottom_right_corner.values()[0])
            else:
                continue

        #logic for sides
        for i in self.dct_cell_coords:
            if i in self.dct_top_side:
                self.dct_cell_coords.get(i).append(self.dct_top_side.values()[0])
            elif i in self.dct_bottom_side:
               self.dct_cell_coords.get(i).append(self.dct_bottom_side.values()[0])
            elif i in self.dct_right_side:
               self.dct_cell_coords.get(i).append(self.dct_right_side.values()[0])
            elif i in self.dct_left_side:
               self.dct_cell_coords.get(i).append(self.dct_left_side.values()[0])
            else:
                continue

        for i in self.dct_cell_coords:
            if len(self.dct_cell_coords.get(i)) > 1 and self.dct_cell_coords.get(i)[1] == 'top':
                t_style  = xlwt.XFStyle()
                t_style.borders.top = t_style.borders.THIN
                t_style.font.bold = True
                self.w_wsheet.write(i[1],i[0], self.dct_cell_coords.get(i)[0], t_style)
            elif len(self.dct_cell_coords.get(i)) > 1 and self.dct_cell_coords.get(i)[1] == 'bottom':
                b_style  =xlwt.XFStyle()
                b_style.borders.bottom = b_style.borders.THIN
                self.w_wsheet.write(i[1],i[0], self.dct_cell_coords.get(i)[0],b_style)
            elif len(self.dct_cell_coords.get(i)) > 1 and self.dct_cell_coords.get(i)[1] == 'right':
                r_style  = xlwt.XFStyle()
                r_style.borders.right = r_style.borders.THIN
                self.w_wsheet.write(i[1],i[0], self.dct_cell_coords.get(i)[0], r_style)
            elif len(self.dct_cell_coords.get(i)) > 1 and self.dct_cell_coords.get(i)[1] ==  'left':
                l_style  =xlwt.XFStyle()
                l_style.borders.left = l_style.borders.THIN
                self.w_wsheet.write(i[1],i[0], self.dct_cell_coords.get(i)[0], l_style)
            elif len(self.dct_cell_coords.get(i)) > 1 and self.dct_cell_coords.get(i)[1] == 'top, left':
                tl_style = xlwt.XFStyle()
                tl_style.borders.left = tl_style.borders.THIN
                tl_style.borders.top = tl_style.borders.THIN
                tl_style.font.bold = True
                self.w_wsheet.write(i[1],i[0], self.dct_cell_coords.get(i)[0], tl_style)
            elif len(self.dct_cell_coords.get(i)) > 1 and self.dct_cell_coords.get(i)[1] ==  'top, right':
                tr_style = xlwt.XFStyle()
                tr_style.borders.right = tr_style.borders.THIN
                tr_style.borders.top = tr_style.borders.THIN
                tr_style.font.bold = True
                self.w_wsheet.write(i[1],i[0], self.dct_cell_coords.get(i)[0], tr_style)
            elif len(self.dct_cell_coords.get(i)) > 1 and self.dct_cell_coords.get(i)[1] ==  'bottom, left':
                bl_style = xlwt.XFStyle()
                bl_style.borders.left = bl_style.borders.THIN
                bl_style.borders.bottom = bl_style.borders.THIN
                self.w_wsheet.write(i[1],i[0], self.dct_cell_coords.get(i)[0], bl_style)
            elif len(self.dct_cell_coords.get(i)) > 1 and self.dct_cell_coords.get(i)[1] ==  'bottom, right':
                br_style = xlwt.XFStyle()
                br_style.borders.right = br_style.borders.THIN
                br_style.borders.bottom = br_style.borders.THIN
                self.w_wsheet.write(i[1],i[0], self.dct_cell_coords.get(i)[0], br_style)
            else:
                self.w_wsheet.write(i[1],i[0], self.dct_cell_coords.get(i)[0])

if __name__ == '__main__':
    x = FancySheet()
    x.get_col_data()
    x.get_row_data()
    x.get_outline()
    x.cr_top()
    x.cr_bottom()
    x.cr_left()
    x.cr_right()
    x.create_data()
    x.w_wbook.save('test.xls')
