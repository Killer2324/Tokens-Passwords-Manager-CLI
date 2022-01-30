# Api Key Manager

Token Password Manager is a CLI Application that saves our Tokens and Passwords. For the Database I have choosen MariaDB for the Database.

## Installaling Dependencies and Config the App

### Installation

#### Install dependencies
1. First you will have to execute the **bash script**.
    This script will install all dependencies and configurate all for you
    ```
    #with virtual enviroment
    sh install_dependencies.sh

    #withouth virtual enviroment
    sh install_dependencies_withouth_venv.sh
    ```

2. Make a **database** for the storage
3. Make a file **.env** for the enviroment variables **you will have create .env in the root of the application**

### Config app
1. Create a .env in root of the application
2. Set the variables

    ```
    USER=
    PASSWORD=
    HOST=localhost
    DATABASE=
    ```
3. run the application
    
    ```
    python3 ./app/__init__.py
    ```

### Create a alias
#### Linux users
Yes, we will create an alias because without this it would be very annoying to go to the folder where the application is located.
The alias We will permitted execute the app in anywhere of system.

1. ```
   $ cd ~
   ```

2. search a file **.bashrc or .zshrc**
    
    ```
    $ ls -a
    ```

3. Edit File
    **if you use zsh terminal set nvim .zshrc**
    **if you don't have neovim, use nano or other code editor**
    
    ```
    $ nvim .bashrc
    ```

4. Go to end of the file and set. **You can change the name of the alias**

    ```
    alias token_manage="python3 /home/gonzalo/Documentos/Workspace_Dev/Proyectos/Python/CLI/Token_Password_Manager/app/__init__.py"
    ```

5. Close your terminal
6. Open your terminal and **set the alias name**

    ```
    $ token_manage
    ```