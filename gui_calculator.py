#!/usr/bin/env python3
"""
GUI Calculator Program
A graphical calculator with buttons like a phone calculator
"""

import tkinter as tk
from tkinter import font


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Variable to store the expression
        self.expression = ""
        
        # Configure style
        self.root.configure(bg="#f0f0f0")
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
    
    def create_display(self):
        """Create the display screen"""
        display_frame = tk.Frame(self.root, bg="#333333", height=100)
        display_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        
        self.display = tk.Label(
            display_frame,
            text="0",
            font=("Arial", 48, "bold"),
            bg="#333333",
            fg="#ffffff",
            anchor="e",
            padx=20,
            pady=20
        )
        self.display.pack(fill=tk.BOTH, expand=True)
    
    def create_buttons(self):
        """Create calculator buttons"""
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Button layout
        buttons = [
            ["C", "⌫", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]
        
        for row_idx, row in enumerate(buttons):
            row_frame = tk.Frame(button_frame, bg="#f0f0f0")
            row_frame.pack(fill=tk.BOTH, expand=True)
            
            for col_idx, btn_text in enumerate(row):
                self.create_button(row_frame, btn_text, row_idx, col_idx)
    
    def create_button(self, parent, text, row, col):
        """Create individual button"""
        # Button colors
        if text == "=":
            bg_color = "#4CAF50"
            fg_color = "white"
            font_size = 24
        elif text in ["C", "⌫"]:
            bg_color = "#f44336"
            fg_color = "white"
            font_size = 20
        elif text in ["÷", "×", "-", "+", "%"]:
            bg_color = "#ff9800"
            fg_color = "white"
            font_size = 24
        else:
            bg_color = "#ffffff"
            fg_color = "#333333"
            font_size = 22
        
        button = tk.Button(
            parent,
            text=text,
            font=("Arial", font_size, "bold"),
            bg=bg_color,
            fg=fg_color,
            relief=tk.RAISED,
            bd=2,
            activebackground="#ddd",
            command=lambda: self.on_button_click(text)
        )
        
        if text == "0":
            button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5, ipadx=10, ipady=20)
            tk.Button(
                parent,
                text=".",
                font=("Arial", 22, "bold"),
                bg="#ffffff",
                fg="#333333",
                relief=tk.RAISED,
                bd=2,
                activebackground="#ddd",
                command=lambda: self.on_button_click(".")
            ).pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5, ipadx=10, ipady=20)
        elif text != ".":
            button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5, ipadx=10, ipady=20)
    
    def on_button_click(self, char):
        """Handle button clicks"""
        if char == "C":
            # Clear
            self.expression = ""
            self.update_display("0")
        
        elif char == "⌫":
            # Backspace
            self.expression = self.expression[:-1]
            self.update_display(self.expression if self.expression else "0")
        
        elif char == "=":
            # Calculate
            try:
                # Replace symbols with operators
                calc_expression = self.expression.replace("÷", "/").replace("×", "*")
                result = eval(calc_expression)
                self.expression = str(result)
                self.update_display(result)
            except:
                self.update_display("Error")
                self.expression = ""
        
        elif char in ["÷", "×", "-", "+", "%"]:
            # Operators
            if self.expression and self.expression[-1] not in ["÷", "×", "-", "+", "%"]:
                self.expression += char
                self.update_display(self.expression)
        
        else:
            # Numbers and decimal
            self.expression += char
            self.update_display(self.expression)
    
    def update_display(self, value):
        """Update display"""
        if value == "":
            self.display.config(text="0")
        else:
            self.display.config(text=value)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
