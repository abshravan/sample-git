#!/usr/bin/env python
# coding: utf-8

# In[31]:


import tkinter
import tkinter.ttk
import tkinter.messagebox

def bin2dec(value):
    return int(value, 2)

def bin2hex(value):
    return hex(int(value, 2))

def dec2bin(value):
    return bin(int(value))

def dec2hex(value):
    return hex(int(value))

def hex2bin(value):
    return bin(int(value, 16))

def hex2dec(value):
    return int(value, 16)


class MainWindow():

    C_FONT = ("Consolas", 16)
    C_TXT_MAXLEN = 32
    
    def __init__(self):
        self._window = tkinter.Tk()
        self._window.title("    Number Convertor    ")
        self._window.geometry("820x260")
        self._window.configure(background = 'light blue')
        self._window.resizable(False, False)
        
        label = tkinter.Label(self._window, text="     Number:", font=MainWindow.C_FONT)
        label.grid(row=0, column=0, padx=10, pady=5)

        self._txt_input = tkinter.Entry(self._window, width=MainWindow.C_TXT_MAXLEN, font=MainWindow.C_FONT)
        self._txt_input.grid(row=0, column=1, pady=5)
        self._txt_input.focus()

        self._bt_bin = tkinter.Button(self._window, text="Bin", font=MainWindow.C_FONT, command=self.evt_bt_bin)
        self._bt_bin.grid(row=0, column=2, padx=5, pady=5)

        self._bt_dec = tkinter.Button(self._window, text="Dec", font=MainWindow.C_FONT, command=self.evt_bt_dec)
        self._bt_dec.grid(row=0, column=4, padx=5, pady=5)

        self._bt_hex = tkinter.Button(self._window, text="Hex", font=MainWindow.C_FONT, command=self.evt_bt_hex)
        self._bt_hex.grid(row=0, column=6, padx=5, pady=5)

        separator = tkinter.ttk.Separator(self._window,orient=tkinter.HORIZONTAL)
        separator.grid(row=1, column=1, pady=10)

        label = tkinter.Label(self._window, text="     Binary:", font=MainWindow.C_FONT)
        label.grid(row=2, column=0,  padx=10, pady=5)

        self._stringvar_bin = tkinter.StringVar()
        txt_output = tkinter.Entry(self._window, textvariable=self._stringvar_bin, width=MainWindow.C_TXT_MAXLEN, state="readonly", font=MainWindow.C_FONT)
        txt_output.grid(row=2, column=1, pady=5)
    
        label = tkinter.Label(self._window, text="    Decimal:", font=MainWindow.C_FONT)
        label.grid(row=3, column=0,  padx=10, pady=5)
        
        self._stringvar_dec = tkinter.StringVar()
        txt_output = tkinter.Entry(self._window, textvariable=self._stringvar_dec, width=MainWindow.C_TXT_MAXLEN, state="readonly", font=MainWindow.C_FONT)
        txt_output.grid(row=3, column=1, pady=5)
        
        label = tkinter.Label(self._window, text="Hexadecimal:", font=MainWindow.C_FONT)
        label.grid(row=4, column=0,  padx=10, pady=5)
        
        self._stringvar_hex = tkinter.StringVar()
        txt_output = tkinter.Entry(self._window, textvariable=self._stringvar_hex, width=MainWindow.C_TXT_MAXLEN, state="readonly", font=MainWindow.C_FONT)
        txt_output.grid(row=4, column=1, pady=5)

    def evt_bt_bin(self):
        try:
            bin_value = self._txt_input.get().strip().replace(" ", "")
            dec_value = bin2dec(bin_value)
            hex_value = bin2hex(bin_value)
            self._set_values(bin_value, dec_value, hex_value)
            
        except Exception:
            tkinter.messagebox.showerror("Error", "Invalid conversion")
    def evt_bt_dec(self):
        try:
            dec_value = self._txt_input.get().strip().replace(" ", "")
            bin_value = dec2bin(dec_value)
            hex_value = dec2hex(dec_value)

            self._set_values(bin_value, dec_value, hex_value)

        except Exception as ex:
            tkinter.messagebox.showerror("Error", "Invalid conversion")
            
    def evt_bt_hex(self):
        try:
            hex_value = self._txt_input.get().strip().replace(" ", "")
            bin_value = hex2bin(hex_value)
            dec_value = hex2dec(hex_value)

            self._set_values(bin_value, dec_value, hex_value)
    
        except Exception as ex:
            tkinter.messagebox.showerror("Error", "Invalid conversion")

    def _set_values(self, bin_value, dec_value, hex_value):
        if not bin_value.startswith("0b"):
            bin_value = "0b" + bin_value
        if not hex_value.startswith("0x"):
            hex_value = "0x" + hex_value
        
        self._stringvar_bin.set(bin_value)
        self._stringvar_dec.set(dec_value)
        self._stringvar_hex.set(hex_value)

    def mainloop(self):
        self._window.mainloop()


if __name__ == "__main__":
    win = MainWindow()
    win.mainloop()


# In[ ]:





# In[ ]:




