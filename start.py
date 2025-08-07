import os
import subprocess
import zipfile
import urllib.request
import shutil

# Constants
SDK_URL = "https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip"
SDK_ZIP = "cmdline-tools.zip"
SDK_DIR = os.path.expanduser("~/Android/Sdk")
CMDLINE_DIR = os.path.join(SDK_DIR, "cmdline-tools")
LATEST_DIR = os.path.join(CMDLINE_DIR, "latest")

# Step 1: Download SDK zip
def download_sdk():
    print("📥 Downloading Android Command Line Tools...")
    urllib.request.urlretrieve(SDK_URL, SDK_ZIP)
    print("✅ Download complete.")

# Step 2: Unzip and move to correct folder
def setup_sdk_dirs():
    print("📦 Extracting SDK tools...")
    with zipfile.ZipFile(SDK_ZIP, 'r') as zip_ref:
        zip_ref.extractall("temp_cmdline_tools")
    os.makedirs(LATEST_DIR, exist_ok=True)
    for item in os.listdir("temp_cmdline_tools/cmdline-tools"):
        s = os.path.join("temp_cmdline_tools/cmdline-tools", item)
        d = os.path.join(LATEST_DIR, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    print("✅ SDK tools set up.")
    shutil.rmtree("temp_cmdline_tools")
    os.remove(SDK_ZIP)

# Step 3: Set environment variables temporarily in this script
def set_env():
    os.environ["ANDROID_SDK_ROOT"] = SDK_DIR
    os.environ["PATH"] = f"{LATEST_DIR}/bin:{SDK_DIR}/platform-tools:{os.environ['PATH']}"

def setup_sdk():
    os.system("chmod 777 /home/azureuser/Android/Sdk/cmdline-tools/latest/bin/")
    os.system("sudo apt update")
    os.system("sudo apt install openjdk-17-jdk")
    os.system("sudo apt install openjdk-17-jre")
    os.system('sh /home/azureuser/Android/Sdk/cmdline-tools/latest/bin/sdkmanager "platform-tools"')
    os.system('sh /home/azureuser/Android/Sdk/cmdline-tools/latest/bin/sdkmanager "platforms;android-33"')
    os.system('sh /home/azureuser/Android/Sdk/cmdline-tools/latest/bin/sdkmanager "build-tools;33.0.2"')
    os.system('cd /home/azureuser/')

def get_code():
    os.system("chmod 777 /home/azureuser/mellowai/android/")
    os.system("wget -P /home/azureuser/mellowai/android/gradle/wrapper/ services.gradle.org/distributions/gradle-8.2-bin.zip")


def build_gradle():
    os.chdir("/home/azureuser/mellowai/android/")  
    os.system("sh /home/azureuser/mellowai/android/gradlew assembleDebug")

def outputpath():
    print("APK Location : /home/azureuser/mellowai/android/app/build/outputs/apk/debug/")

# --- Run all steps ---
if __name__ == "__main__":
    download_sdk()
    setup_sdk_dirs()
    set_env()
    setup_sdk()
    get_code()
    build_gradle()
    outputpath()
