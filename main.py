#

import requests
import subprocess
import time
import subprocess

# PowerShell command to execute
powershell_command = "CheckNetIsolation LoopbackExempt -a -n='Microsoft.MinecraftUWP_8wekyb3d8bbwe'"

# Run the PowerShell command
result = subprocess.run(["powershell", "-Command", f"Start-Process powershell -Verb RunAs -ArgumentList '-Command', '{powershell_command}'"], capture_output=True, text=True)

# Print the output
print(result.stdout)

def download_file(url, destination):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print(f"File '{url}' downloaded successfully.")
    else:
        print(f"Failed to download the file '{url}'.")

download_file("https://api.papermc.io/v2/projects/paper/versions/1.20.1/builds/126/downloads/paper-1.20.1-126.jar", "paper-1.20.1-126.jar")


server_jar = 'paper-1.20.1-126.jar'        # Replace with the path of the source file


#subprocess.run(['java', '-jar', server_jar, 'nogui'], check=True)

# Abrir el archivo en modo lectura y escritura
def replace(path,text,replace):
    with open(path, 'r') as file:
        file_contents = file.read()

    # Realizar el reemplazo del texto
    new_contents = file_contents.replace(text, replace)

    # Abrir el archivo en modo escritura para guardar los cambios
    with open(path, 'w') as file:
        file.write(new_contents)

    print("Reemplazo completado.")



replace('eula.txt','eula=false','eula=true')



jar_process = subprocess.Popen(['java', '-jar', server_jar, 'nogui'])
time.sleep(10)
jar_process.terminate()
jar_process.wait()


#download_file("https://download.geysermc.org/v2/projects/floodgate/versions/latest/builds/latest/downloads/spigot", "plugins/floodgate-spigot.jar")
#download_file("https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/spigot", "plugins/Geyser-Spigot.jar")


jar_process = subprocess.Popen(['java', '-jar', server_jar, 'nogui'])
time.sleep(10)
jar_process.terminate()
jar_process.wait()

replace('server.properties','enforce-secure-profile=true','enforce-secure-profile=false')
replace('plugins\Geyser-Spigot\config.yml','auth-type: online','auth-type: floodgate')
replace('plugins\Geyser-Spigot\config.yml','passthrough-motd: false','passthrough-motd: true')


print(f"fin ejecucion")

