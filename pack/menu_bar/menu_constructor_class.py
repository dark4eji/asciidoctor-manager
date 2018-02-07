"""
The module consists of the one MenuConstructor class and
is used for constructing the whole menu bar of the root window.

For additional information see class and methods docstrings.
"""
import os
from tkinter import Menu, Frame
from pack.menu_bar.menu_classes import OperationsMenu, OpenProject,\
    Publisher, Renamer, Creator, OpenFile, SaveAs
from pack.func_pack import config_retriever



class MenuConstructor:
    """Class that constructs menu bar"""
    def __init__(self, parent, textbox, notebook):
        self.parent = parent
        self.textbox = textbox
        self.notebook = notebook
        self.rootbar = Menu(parent, tearoff=0)  # builds the whole menu bar
        self.actionmenu = Menu(self.rootbar, tearoff=0)  # builds "Operations" menu
        self.filemenu = Menu(self.rootbar, tearoff=0)  # builds "File" menu
        self.parent.config(menu=self.rootbar)
        self.cascade_adding()
        self.constructor()
        if os.path.exists(os.path.join('C:', 'ProgramData', 'config.ini')):
            OpenProject.secured_project_path = config_retriever('project_file', 'file_path')
            self.parent.title('Asciidoctor Manager' + " [" + OpenProject.secured_project_path + "]")

    def cascade_adding(self):
        """Used for adding menus to the menu bar.
        The title for a new menu pack should be added here"""
        self.rootbar.add_cascade(label="File", menu=self.filemenu)
        self.rootbar.add_cascade(label="Operations", menu=self.actionmenu)

    def constructor(self):
        """Menus constructor"""
        self.build_pub = OperationsMenu
        self.build_ren = OperationsMenu
        self.build_cr = OperationsMenu
        self.open_project = OpenProject
        self.open_file = OpenFile
        self.save_as_file = SaveAs

        self.build_pub(self.actionmenu, Publisher, self.open_project, "Publish", self.notebook)
        self.build_cr(self.actionmenu, Creator, self.open_project, "Create Topic", self.notebook)
        self.build_ren(self.actionmenu, Renamer, self.open_project, "Rename Topics", self.notebook)

        OpenProject(self.filemenu, self.parent, "Open Project")
        OpenFile(self.filemenu, self.textbox, "Open Topic File")
        SaveAs(self.filemenu, self.textbox, "Save As")
