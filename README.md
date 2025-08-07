# mellowai

## Step1 Initial Build

```
git clone https://github.com/rpmellow/mellowai.git
cd mellowai
python3 start.py
```

## Step2 Normal Build

```
cd mellowai/android/
```
```
./gradlew assembleDebug
```

## Download APK from Azure

```
scp -i key_file.pem azureuser@<IP Address>:/home/azureuser/mellowai/android/app/build/outputs/apk/debug/app-debug.apk /<your dir path>/
```
