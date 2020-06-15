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
"Create a linear function of the linear regression to return the y-axis values of the linear regression"
def linear_func(slope,intercept,x):
    return slope * x + intercept

"Create a function to plot the linear regression graph"
def linear_regression(x,y):
    #Assign values to slope and intercept accroding to the values of x and y
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    #Calculate the y-axis values of the linear regression
    regression = [linear_func(slope,intercept,x) for x in x]
    #Plot the graph of y against x
    plt.scatter(x,y)
    #Plot the graph of linear regression
    plt.plot(x, regression)
    #Displat the graphs
    plt.show()
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
        id_gen = wx.NewId() 
        id_help = wx.NewId() 
        generate = wx.MenuItem(fileMenu,id_gen, text = "Generate",kind = wx.ITEM_NORMAL)
        fileMenu.Append(generate)
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
        "Excel files (*.xlsx) | *.xlsx", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        if openFileDialog.GetPath() == "":
            wx.MessageBox("You have not selected any files"," ", wx.OK|wx.ICON_INFORMATION)
            openFileDialog.Destroy()
        else :
            self.grid = wx.grid.Grid(self, wx.ID_ANY)
            
            workbook = xlrd.open_workbook(openFileDialog.GetPath())
            worksheet = workbook.sheet_by_index(0)
            num_rows = worksheet.nrows
            num_cols = worksheet.ncols
            self.grid.CreateGrid(num_rows, num_cols)
            for i in range(num_rows):
                for k in range(num_cols):
                    cell_value = worksheet.cell(i, k).value
                    self.grid.SetCellValue(i, k, str(cell_value))
            openFileDialog.Destroy()
            names = []
            self.cals = []
            days = []
            self.weights = []
            self.heights = []
            self.phy = []
            self.totalCals = []
            for c in range(1, num_cols - 4):
                days.append(self.grid.GetCellValue(0,c))
            for c in range(1,num_rows):
                self.weights.append(float(self.grid.GetCellValue(c,8)))
            for c in range(1,num_rows):
                self.heights.append(float(self.grid.GetCellValue(c,9)))
            for c in range(1,num_rows):
                self.phy.append(float(self.grid.GetCellValue(c,9)))
            for c in range(1,num_rows):
               self.totalCals.append(float(self.grid.GetCellValue(c,11)))
            for c in range(1, num_rows):
                names.append(self.grid.GetCellValue(c,0))
            for y in range(1,num_rows):
                for u in range(1,num_cols-4):
                    self.cals.append(float(self.grid.GetCellValue(y,u)))
            print(self.weights)
            print(days)
            print(self.heights)
            print(self.totalCals)
            print(self.cals)
        #-------------------------------------------------------------------------------
        # Binding Events
        #-------------------------------------------------------------------------------
        self.Bind(wx.EVT_MENU, self.OnGenerate, id=id_gen)
        self.Bind(wx.EVT_MENU, self.OnHelp, id=id_help)
        #-------------------------------------------------------------------------------
        # Binding Events End
        #-------------------------------------------------------------------------------
        
        
        self.Maximize() 
        self.SetTitle('Group 2 Assignemnt 2 - CPT113')
        self.Centre()
    def OnHelp(self, event):
        wx.MessageBox("Having trouble? Please do not hesitate to contact us on:\n"
                        "Email: takieddine@student.usm.my\n"
                        "WhatsApp: Taki Eddine TORKI: +6011-62275435 OR Wong Chong Yang: +6011-10560813\n","FYI", wx.OK|wx.ICON_INFORMATION)
        
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
            # Correlation between the calorie intakes and the weights of students
            plt.title('Correlation between the calorie intakes and the weights of students')
            plt.xlabel('Calories intake (kcal)')
            plt.ylabel('Weight (kg)')
            linear_regression(self.totalCals, self.weights)

            # Correlation between the physical activities and the weights of students
            plt.title('Correlation between the physical activities and the weights of students')
            plt.xlabel('Physical activity (kcal)')
            plt.ylabel('Weight (kg)')
            linear_regression(self.phy, self.weights)

            # Correlation between the physical activities and the calorie intakes of students 
            plt.title('Correlation between the physical activities and the calorie intakes of students')
            plt.xlabel('Physical activity (kcal)')
            plt.ylabel('Calorie intake (kcal)')
            linear_regression(self.phy, self.totalCals)
            

def main():
    app = wx.App()
    ex = MainWindow(None)
    ex.Show()
    app.MainLoop()
if __name__ == '__main__':
    main()
