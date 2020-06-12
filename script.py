import wx
import main
from main import GridFrame
class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()
        
    def InitUI(self):
        wx.MessageBox("Dear lecturer checking this assignment,\n\n"
                        "I would like to thank you for taking the time and effort to read this","FYI", wx.OK|wx.ICON_INFORMATION)      
        # Will prompt the user to open a file here. Text files and MS Excel files ONLY
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.names = wx.ListBox(panel)
        self.calories = wx.ListBox(panel)
        hbox.Add(self.names, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        hbox.Add(self.calories, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        btnPanel = wx.Panel(panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        newBtn = wx.Button(btnPanel, wx.ID_ANY, 'New', size=(120, 30))
        renBtn = wx.Button(btnPanel, wx.ID_ANY, 'Rename', size=(120, 30))
        delBtn = wx.Button(btnPanel, wx.ID_ANY, 'Delete', size=(120, 30))
        clrBtn = wx.Button(btnPanel, wx.ID_ANY, 'Clear', size=(120, 30))
        fileBtn = wx.Button(btnPanel, wx.ID_ANY, 'Open new file', size=(120, 30))
        genBtn = wx.Button(btnPanel, wx.ID_ANY, 'Generate Results', size=(120, 30))
        self.Bind(wx.EVT_BUTTON, self.NewData, id=newBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnRename, id=renBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDelete, id=delBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnClear, id=clrBtn.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnOpen, id=fileBtn.GetId())
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnRename)

        vbox.Add((-1, 20))
        vbox.Add(newBtn)
        vbox.Add(renBtn, 0, wx.TOP, 5)
        vbox.Add(delBtn, 0, wx.TOP, 5)
        vbox.Add(clrBtn, 0, wx.TOP, 5)
        vbox.Add(fileBtn, 0, wx.TOP, 5)
        vbox.Add(genBtn, 0, wx.TOP, 5)
        
        btnPanel.SetSizer(vbox)
        hbox.Add(btnPanel, 0.6, wx.EXPAND | wx.RIGHT, 20)
        panel.SetSizer(hbox)

        self.SetTitle('Group 2 Assignemnt 2 - CPT113')
        self.Centre()

    def NewData(self, event):
        text = wx.GetTextFromUser('Enter a new data', 'Insert dialog')
        if text != '':
            self.listbox.Append(text)
    def OnOpen(self, event):
        # Coming soon open file functionality

    def OnRename(self, event):
        sel = self.listbox.GetSelection()
        text = self.listbox.GetString(sel)
        renamed = wx.GetTextFromUser('Rename Data', 'Rename dialog', text)
        if renamed != '':
            self.listbox.Delete(sel)
            item_id = self.listbox.Insert(renamed, sel)
            self.listbox.SetSelection(item_id)

    def OnDelete(self, event):
        sel = self.listbox.GetSelection()
        if sel != -1:
            self.listbox.Delete(sel)

    def OnClear(self, event):
        self.listbox.Clear()

def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
