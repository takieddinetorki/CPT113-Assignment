import wx
import xlrd
import wx.grid
import pandas as pd
import numpy as np
from scipy import stats
from statistics import mode
import matplotlib.pyplot as plt
def Diff(li1, li2): 
    return (list(set(li1) - set(li2)))
class MainWindow(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainWindow, self).__init__(*args, **kw)
        self.InitUI()
        
    def InitUI(self):
        #-----------------------------------------------------------------------------
        # Setting up menus
        #------------------------------------------------------------------------------
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        helpMenu = wx.Menu()
        id_new = wx.NewId() 
        id_gen = wx.NewId() 
        id_clear = wx.NewId() 
        id_help = wx.NewId() 
        newfile = wx.MenuItem(fileMenu,id_new, text = "Open new file",kind = wx.ITEM_NORMAL)
        generate = wx.MenuItem(fileMenu,id_gen, text = "Generate",kind = wx.ITEM_NORMAL)
        clear = wx.MenuItem(fileMenu,id_clear, text = "Clear",kind = wx.ITEM_NORMAL)
        fileMenu.Append(newfile)
        fileMenu.Append(generate)
        fileMenu.Append(clear)
        about = wx.MenuItem(helpMenu,id_help, text = "About",kind = wx.ITEM_NORMAL)
        helpMenu.Append(about)
        menubar.Append(fileMenu, '&File')
        menubar.Append(helpMenu, '&Help')
        self.SetMenuBar(menubar)
        #-----------------------------------------------------------------------------
        # Setting up menus End
        #------------------------------------------------------------------------------
        wx.MessageBox("Dear lecturer checking this assignment,\n\n"
                        "I would like to thank you for taking the time and effort to read this","FYI", wx.OK|wx.ICON_INFORMATION)
        openFileDialog = wx.FileDialog(self, "Open file with data", "", "", 
        "", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        if openFileDialog.GetPath() == "":
            wx.MessageBox("You have not selected any files"," ", wx.OK|wx.ICON_INFORMATION)
            openFileDialog.Destroy()
        else :
            grid = wx.grid.Grid(self, wx.ID_ANY)
            
            workbook = xlrd.open_workbook(openFileDialog.GetPath())
            worksheet = workbook.sheet_by_index(0)
            num_rows = worksheet.nrows
            num_cols = worksheet.ncols
            grid.CreateGrid(num_rows, num_cols)
            for i in range(num_rows):
                for k in range(num_cols):
                    cell_value = worksheet.cell(i, k).value
                    grid.SetCellValue(i, k, str(cell_value))
            openFileDialog.Destroy()
            names = []
            self.cals = []
            days = []
            totalCals = []
            for c in range(1, num_cols - 1):
                days.append(grid.GetCellValue(0,c))
            for c in range(1, num_rows):
                names.append(grid.GetCellValue(c,0))
            for y in range(1,num_rows):
                for u in range(1,num_cols-1):
                    self.cals.append(float(grid.GetCellValue(y,u)))
            print(self.cals)



        #-------------------------------------------------------------------------------
        # Binding Events
        #-------------------------------------------------------------------------------
        self.Bind(wx.EVT_MENU, self.OnOpen, id=id_new)
        self.Bind(wx.EVT_MENU, self.OnGenerate, id=id_gen)
        self.Bind(wx.EVT_MENU, self.OnClear, id=id_clear)
        #-------------------------------------------------------------------------------
        # Binding Events End
        #-------------------------------------------------------------------------------
        self.Maximize() 
        self.SetTitle('Group 2 Assignemnt 2 - CPT113')
        self.Centre()
    
    def OnOpen(self, event):
        print("WHATEVER")

    def OnClear(self, event):
        print("WHATEVER")
        
    def OnGenerate(self, event):
            print("Maximum calorie intake:",max(self.cals))

            print("\nMinimum calorie intake:",min(self.cals))

            print("\nMode calorie intake:", mode(self.cals))

            print("\nFrequency of mode:",self.cals.count(mode(self.cals)))

            print("\nMean calorie intake:", np.mean(self.cals))

            print("\nVariance:",np.var(self.cals))

            print("\nStandard deviation:",np.std(self.cals))
            wx.MessageBox("Please check your console","FYI", wx.OK|wx.ICON_INFORMATION)
            box = plt  
            box.figure(1)
            box.title('Boxplot for calorie intake') 
            box.boxplot(self.cals)
            histogram = plt
            histogram.figure(2)
            histogram.title('Histogram for calorie intake') 
            histogram.hist(self.cals)
            histogram.show()
            box.show()

def main():
    app = wx.App()
    ex = MainWindow(None)
    ex.Show()
    app.MainLoop()
if __name__ == '__main__':
    main()
