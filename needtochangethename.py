from sys import platform
import os, wget, urllib, sys

kubectl_version = "v1.21.0"



def check_os_func():
    print("Checking your Operating System type")
    if platform == "linux" or platform == "linux2":
        return "You have Linux OS"

    elif platform == "win32":
        return "You have Windows OS"

    else:
        return "OS is neither Linux nor windows"

def check_env_vars():
    pass


def download_file_from_web():

    remote_url = "https://dl.k8s.io/release/"+kubectl_version+"/bin/windows/amd64/kubectl.exe"
    
    local_file = "kubectl.exe"
    
    try:
        wget.download(remote_url, "C:\\bin\\")
        return "Y"
    except (urllib.error.HTTPError,urllib.error.URLError) as exception:
        return exception
        
    except:
        return ("Error Occured")

l1 = sys.argv



if len(l1) == 2 :
    if l1[1] == "1":
        print(check_os_func())
    elif l1[1] == "2": 
        print(check_env_vars())
    elif l1[1] == "3":
        print(download_file_from_web())
    else:
        print("Please enter number between 1, 2 and 3")

else:
    print("Enter Only One Argument")        