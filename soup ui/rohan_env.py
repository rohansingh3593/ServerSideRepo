
import os
import pprint
  
# Get the list of user's
# environment variables
env_var = os.environ
  
# Print the list of user's
# environment variables
print("User's Environment variable:")
pprint.pprint(dict(env_var), width = 1)

# #########################################################

# # It is send you a dictionary so 
# # Get the value of
# # 'HOME' environment variable
# home = os.environ['HOME'] # --> some time it get failed because when 'HOME' variable is not present.
  
# # Print the value of
# # 'HOME' environment variable
# print("HOME:", home)
  
# # Get the value of
# # 'JAVA_HOME' environment variable
# # using get operation of dictionary
# java_home = os.environ.get('JAVA_HOME')
  
# # Print the value of
# # 'JAVA_HOME' environment variable
# print("JAVA_HOME:", java_home)

# print(os.environ.get('HOME'))
# print(os.environ.get('VSCODE_NONCE'))
# #################################################################


# # # Print the value of
# # # 'JAVA_HOME'  environment variable 
# # print("JAVA_HOME:", os.environ['JAVA_HOME'])
  
# # # Modify the value of
# # # 'JAVA_HOME'  environment variable 
# # # os.environ['JAVA_HOME'] = '/home / ihritik / jdk-10.0.1'
  
# # # Print the modified value of
# # # 'JAVA_HOME' environment variable
# # print("Modified JAVA_HOME:", os.environ['JAVA_HOME'])

# # ######################################
# # #Adding a new environment variable
# # # Add a new environment variable 
# # os.environ['GeeksForGeeks'] = 'www.geeksforgeeks.org'
  
# # # Get the value of
# # # Added environment variable 
# # print("GeeksForGeeks:", os.environ['GeeksForGeeks'])