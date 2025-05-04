from logging import exception
from docx import Document #We need to import Document module for document
import random
import tkinter as tk
from tkinter import messagebox,filedialog
class password_generation_project:
      def __init__(self):#No need to give parameter names here because we declared manually inside constructor block
          self.str1_numbers="0123456789"
          self.str2_symbols="!@#$%^&*()"
          self.str3_lower_case="abcdefghijklmnopqrstuvwxyz"
          self.str4_upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#Exceptional handling
      def get_valid_input(self,prompt):
          while True:
                 try:
                   numbers=int(input(prompt))
                   if(numbers<0):
                     print("The password should not be negative")
                   else:
                     return numbers
                 except ValueError:
                     print("Invalid input please enter")
      def unique_char_block(self,target_len, source_str, password, seen_char):
          while (len(password) < target_len):
               char = random.choice(source_str)
               if char not in seen_char:
                  password.append(char)
                  seen_char.add(char)
      def password_generation(self,numbers,symbols,lower_case,upper_case ):
          length = numbers + symbols + lower_case + upper_case
          password = []
          seen_char = set()
          print(f"Total Password length {length}")
          self.unique_char_block(numbers,self.str1_numbers,password,seen_char)
          self.unique_char_block(symbols, self.str2_symbols, password, seen_char)
          self.unique_char_block(lower_case, self.str3_lower_case, password, seen_char)
          self.unique_char_block(upper_case, self.str4_upper_case, password, seen_char)
          print(f"Password length After adding numbers len{length}")
          all_chars = self.str1_numbers + self.str2_symbols + self.str3_lower_case + self.str4_upper_case
          self.unique_char_block(length,all_chars,password,seen_char)
          print(f"Password length After adding all characters len{length}")
          random.shuffle(password)
          return ''.join(password)
      def load_blocked_names(self,docx_path):  # doc path is the input of funtion
          doc = Document(docx_path)  # Reading the document path using Document function
          names = set()  # set the name

          for para in doc.paragraphs:  # Reading each paragraph in the document
              name = para.text.strip().lower()  # each text converted to lower and removing white spaces
              if name:  # If name true
                  names.add(name)  # add the name in names
          return names  # return names
      def is_secure_password(self,name,Blocked_list):
          return name.strip().lower() not in Blocked_list  # name is not present in the blocked list returns True

obj = password_generation_project()
# Error Handling
try:  # By accessing below path if any error occurs this will report without terminating program
  Blocked_list = obj.load_blocked_names(r"C:\Lavanya Jonnadula\names.txt.docx")  # giving path to function call
except Exception as e:  # It encounter the errors and reporting error message
    print(f"Failed to load the name{e}")  # {e} captures all error message
    Blocked_list = set()

while True:
      numbers=obj.get_valid_input("How Many numbers do you want in your password?")
      symbols=obj.get_valid_input("How many symbols do you want in your password?")
      lower_case=obj.get_valid_input("How many lowercase letters do you want in your password?")
      upper_case=obj.get_valid_input("How many uppercase letters do you want in your password?")
      length = numbers + symbols + lower_case + upper_case
      if (length == 0):
          print("Password Length should not be empty")
      elif (length < 8):
          print("Your password length too short")
      else:
          print("Your password meets our requirement")
          break

password=obj.password_generation(numbers, symbols, lower_case, upper_case)
print(obj.is_secure_password("Alku",Blocked_list))  # function call with passing parameter
print(f"password {password}")
root=tk.Tk()
root.title("User Random Password Generation")
tk.Label(root, text="Numbers:").grid(row=0, column=0)
numbers_entry = tk.Entry(root)
numbers_entry.grid(row=0, column=1)
tk.Label(root,text="Symbols:").grid(row=1,column=0)
symbols_entry=tk.Entry(root)
symbols_entry.grid(row=1,column=1)
tk.Label(root,text="Lowercase:").grid(row=2,column=0)
lower_case_entry=tk.Entry(root)
lower_case_entry.grid(row=2,column=1)
tk.Label(root,text="Uppercase:").grid(row=3,column=0)
upper_case_entry=tk.Entry(root)
upper_case_entry.grid(row=3,column=1)

def load_blocked_names_gui():
    path=filedialog.askopenfilename(filetypes=[("Word documents","*.docx")])
    if path:
       try:
         global Blocked_list
         Blocked_list=obj.load_blocked_names(path)
         messagebox.showinfo("Success","Blocked Names Loaded Successfully ")
       except Exception as e:
           messagebox.showerror("error",f"Failed to load blocked names {e}")
load_button=(tk.Button(root,text="Load Blocked Names",command=load_blocked_names_gui))
load_button.grid(row=4,column=0,columnspan=2)
def password_generation_gui():
    try:
       if not numbers_entry.get().strip() or not symbols_entry.get().strip() or not upper_case_entry.get().strip() or not lower_case_entry.get().strip():
          messagebox.showwarning("Input missing","please fill in the fields")
          return
       numbers=int(numbers_entry.get())
       symbols=int(symbols_entry.get())
       uppercase=int(upper_case_entry.get())
       lowercase=int(lower_case_entry.get())
       if numbers<0 or symbols<0 or uppercase<0 or lowercase<0:
          messagebox.showerror("Negative numbers are not allowed")
          return
       length=numbers+symbols+uppercase+lowercase
       if length<8:
          messagebox.showwarning("Your password is too short")
          return
       password=obj.password_generation(numbers,symbols,lowercase,uppercase)
       print("Kinter_password",password)
       if not obj.is_secure_password(password,Blocked_list):
          messagebox.showerror("Blocked Password:generated password include blocked content")
          return
       password_display.delete(0,tk.END)
       password_display.insert(0,password)
    except ValueError:
        messagebox.showerror("Invalid Input","Please Enter valid number in all inputs")

generate_button=tk.Button(root,text="Generate Password",command=password_generation_gui)
generate_button.grid(row=5,column=0,columnspan=2)
password_display=tk.Entry(root,width=40)
password_display.grid(row=6,column=0,columnspan=2)
root.mainloop()










#





