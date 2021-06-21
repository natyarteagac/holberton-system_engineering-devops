# 0x01. Shell, permissions

## man or help:
- chmod
- sudo
- su
- chown
- chgrp
- id
- groups
- whoami
- adduser
- useradd
- addgroup

# Learning Objectives
## Permissions
- What do the commands chmod, sudo, su, chown, chgrp do
- Linux file permissions
- How to represent each of the three sets of permissions (owner, group, and other) as a single digit
- How to change permissions, owner and group of a file
- Why can’t a normal user chown a file
- How to run a command with root privileges
- How to change user ID or become superuser

# Tasks
- **0. My name is Betty** -
Creating a script that switches the current user to the user betty.
- **1. Who am I** -
Writing a script that prints the effective username of the current user.
- **2. Groups** -
Writing a script that prints all the groups the current user is part of.
- **3. New owner** -
Writing a script that changes the owner of the file hello to the user betty.
- **4. Empty** -
Writing a script that creates an empty file called hello.
- **5. Execute** -
Writing a script that adds execute permission to the owner of the file hello.
- **6. Multiple permissions** -
Writing a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello
- **7. Everybody!**
Writing a script that adds execution permission to the owner, the group owner and the other users, to the file hello.
- **8. James Bond** -
Writing a script that sets the permission to the file hello as follows:
  - Owner: no permission at all
  - Group: no permission at all
  - Other users: all the permissions
The file hello will be in the working directory You are not allowed to use commas for this script
- **9. John Doe** -
Writing a script that sets the mode of the file hello.
- **10. Look in the mirror** -
Writing a script that sets the mode of the file hello the same as olleh’s mode.
- **11. Directories** -
Creating a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
- **12. More directories** -
Creating a script that creates a directory called dir_holberton with permissions 751 in the working directory.
- **13. Change group** -
Write a script that changes the group owner to holberton for the file hello
- The file hello will be in the working directory
- **14. Owner and group** -
Writing a script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.
- **15. Symbolic links** -
Writing a script that changes the owner and the group owner of _hello to betty and holberton respectively.
  - The file _hello is in the working directory
  - The file _hello is a symbolic link
- **16. If only** -
Writing a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
  - The file hello will be in the working directory
- **17. Star Wars** -
Write a script that will play the StarWars IV episode in the terminal.
