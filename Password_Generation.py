from docx import Document #We need to import Document module for document
import random
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

          self.unique_char_block(numbers,self.str1_numbers,password,seen_char)
          self.unique_char_block(numbers+symbols, self.str2_symbols, password, seen_char)
          self.unique_char_block(numbers + symbols + lower_case, self.str3_lower_case, password, seen_char)
          self.unique_char_block(numbers + symbols + lower_case + upper_case, self.str4_upper_case, password, seen_char)
          all_chars = self.str1_numbers + self.str2_symbols + self.str3_lower_case + self.str4_upper_case
          self.unique_char_block(length,all_chars,password,seen_char)
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
  Blocked_list = obj.load_blocked_names(r"names.txt.docx")  # giving path to function call
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









#





