echo "Hi, I'm the installation assistant"
echo "How do you want to name your virtual enviroment? "
read enviroment
python3 -m venv $enviroment
echo "What is your Operating System? (linux/windows)"
read sys

echo 'Ok. Making the virtual enviroment...'

if [[ sys == 'Linux' ]] || [[ sys == 'linux' ]]
    . venv/bin/activate
else
    . venv/Scripts/activate
fi

echo 'Installing dependencies...'
pip3 install mariadb
pip3 install python-dotenv

echo 'The installation finished. now You can delete this script'