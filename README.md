<img src="https://i.imgur.com/sJzfZsL.jpg" width="150" align="right">

# InstaPy for Alda
This is a Fork of [InstaPy](https://github.com/timgrossmann/InstaPy) for usage on a **Raspberry Pi 3**.

## Install
following [Stackoverflow](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3) & [InstaPy for Raspberry Pi](https://github.com/timgrossmann/InstaPy/blob/master/docs/How_to_Raspberry.md)
1. `sudo apt-get update`
2. `sudo apt-get python3-pip` 
3. `sudo apt-get python34-setuptools (Stackoverflow)`
4. `sudo easy_install pip`
5. `sudo apt-get install libjpeg-dev zlib1g-dev (for pillow)`
6. `sudo pip install .`
7. `(maybe) echo "deb http://security.debian.org/debian-security stretch/updates main" >> /etc/apt/sources.list`
8. `(maybe) sudo apt-get update`
9. `sudo apt-get install chromium-browser`
10. `wget https://github.com/electron/electron/releases/download/v1.6.0/chromedriver-v2.21-linux-armv7l.zip [stackoverflow](https://raspberrypi.stackexchange.com/questions/67628/latest-firefox-chrome-possibilities)`
11. `unzip chromedriver_linux32.zip -d chromedriver`
12. `mv ./chromedriver/chromedriver ./assets/chromedriver (move into ./assets/ folder of InstaPy!)`
13. `sudo apt-get install tmux`

## Usage
1. ssh hduser@192.168.0.110
2. enter Password
3. tmux
4. python3 quickstart.py
5. press C-b d (press Controll & b together then press d, detaches buffer so that process is not killed while closing ssh connection)
6. exit

## Further Usage
- tmux ls (list of all detached windows)
- tmux attach -t 0 (opens detached window) 
