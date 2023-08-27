from webbrowser import open as openurl
import tkinter.font as tkFont
from tkinter import TclError
from os import path, getcwd
import ttkbootstrap as ttk

# from threading import Thread

class App(ttk.Window):
    def __init__(self, title: str, size: tuple, version: str):
        super().__init__()

        self.title(f'{title}  {version}')
        self.geometry(f'{size[0]}x{size[1]}')
        self.resizable(False, False) #self.minsize(size[0], size[1])

        try:
            icon = path.join(getcwd(), 'assets', 'pixelamethyst-icon.ico')
            self.iconbitmap(icon)

        except TclError: # Error by getting the image
            pass

        Inter10 = tkFont.Font(family = 'Inter', weight = 'bold', size = 10)

        self.search_bar = SearchBar(self, Inter10)
        self.scroll_menu = ScrollMenu(self)
        self.bottom_bar = BottomBar(self)

        self.mainloop()

class SearchBar(ttk.Frame):
    def __init__(self, parent, custom_font):
        super().__init__(parent)

        self.place(x = 0, y = 0, relheight = 0.2, relwidth = 1)
        self.create_widgets(custom_font)

    def create_widgets(self, custom_font):

        def entry_focus_in(event):
            if search_entry.get() == 'Search mods on Modrinth...':
                search_entry.delete(0, 'end')
                search_entry.config(foreground = 'black', font = custom_font)

        def entry_focus_out(event):
            if not search_entry.get():
                search_entry.insert(0, 'Search mods on Modrinth...')
                search_entry.config(foreground = 'gray', font = custom_font)

        search_entry = ttk.Entry(self)

        search_entry.insert(0, 'Search mods on Modrinth...')
        search_entry.config(foreground = 'gray', font = custom_font)

        search_entry.bind('<FocusIn>', entry_focus_in)
        search_entry.bind('<FocusOut>', entry_focus_out)

        search_entry.pack(pady = 20, padx = 20, side = 'left', expand = True, fill = 'x')

        loaders = ['Loader', 'forge', 'fabric']
        loaders_string = ttk.StringVar(value = loaders[0])

        versions = ['Version', '1.16.5', '1.12.2', '1.7.10']
        versions_string = ttk.StringVar(value = versions[0])

        def loader_callback(selection):
            selected_loader = selection
            print(selected_loader)

        # loader_option_button.bind('<OptionmenuSelected>')

        loader_option_button = ttk.OptionMenu(self, loaders_string, *loaders,
                                              command = loader_callback)

        loader_option_button.pack(pady = 20, padx = 10, side = 'left')

        # combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(
        # text=f'version selected: {version_string.get()}'))

        version_option_button = ttk.OptionMenu(self, versions_string, *versions)
        version_option_button.pack(pady = 20, padx = 10, side = 'left')

        search_button = ttk.Button(self, text = 'Search',
                                   command = lambda: print('Search button [PRESSED]'))

        search_button.pack(pady = 20, padx = 20, side = 'left')

class ScrollMenu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(x = 0, rely = 0.2, relheight = 0.6, relwidth = 1)
        self.create_widgets()

    def create_widgets(self):
        table = ttk.Treeview(self, columns = ('name', 'slug', 'loader',
                                              'version'), show = 'headings')

        table.heading('name', text = 'Mod Name')
        table.heading('slug', text = 'Mod Slug')
        table.heading('loader', text = 'Mod Loader')
        table.heading('version', text = 'Mod Version')

        table.pack(fill = 'both', expand = True, padx = 20)

class BottomBar(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(x = 0, rely = 0.8, relheight = 0.2, relwidth = 1)
        self.create_widgets()

    def create_widgets(self, ):
        status = 'IDLE'

        download_button = ttk.Button(self, text = 'Download selected',
                                     command = lambda: print('Download selected button [PRESSED]'))

        download_button.pack(pady = 20, padx = 20, side = 'left')

        status_label = ttk.Label(self, text = 'Status :',
                                 font='Inter 10 bold')

        status_label.pack(pady = 20, padx = 5, side = 'left')

        set_status = ttk.Label(self, text = f'{status}',
                               font = 'Inter 10 bold',
                               foreground = 'green')

        set_status.pack(pady = 10, side = 'left')

        github_button = ttk.Button(self, text = 'PixelAmethyst/ModrinthDownloader',
            command = lambda: openurl('https://github.com/PixelAmethyst/ModrinthDownloader'))

        github_button.pack(pady = 20, padx = 20, side = 'right')
