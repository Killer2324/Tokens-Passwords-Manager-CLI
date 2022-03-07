echo "Hi, I'm the installation assistant"
echo "How do you want to name your virtual enviroment? "
read enviroment
python3 -m venv $enviroment
echo 'Ok. Making the virtual enviroment...'

echo "What is your Operating System? (linux/windows)"
read sys


if [[ sys == 'Linux' ]] || [[ sys == 'linux' ]]
then
    . venv/bin/activate
    echo 'Installing dependencies...'
    pip3 install mariadb
    pip3 install python-dotenv
else
    . venv/Scripts/activate
    echo 'Installing dependencies...'
    pip install mariadb
    pip install python-dotenv
fi

echo 'The installation finished. now You can delete this script'

exit 0
