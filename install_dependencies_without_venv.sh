echo "Hi, I'm the installation assistant"
echo "What is your Operating System? (linux/windows)"
read sys

if [[ sys == 'Linux' ]] || [[ sys == 'linux' ]]
then
    echo 'Installing dependencies...'
    pip3 install mariadb
    pip3 install python-dotenv
else
    echo 'Installing dependencies...'
    pip install mariadb
    pip install python-dotenv
fi

echo 'The installation finished. now You can delete this script'