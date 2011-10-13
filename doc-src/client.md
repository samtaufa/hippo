On the client, we use Hippo to *'backup'* the client's configuration
files and get a copy of that backup onto another machine as a 
precaution (i.e. we want a current copy of the configuration on 
another machine for the event when this client dies and we want
to rebuild it.)

- [Basic Workflow](client/workflow.html)
- [Shortcuts](client/shortcuts.html)
- [Bastion](client/bastion.html)
- [Git](client/git.html)
- [Restore](client/restore.html)

Most Hippo commands are identical to their Git equivalents, and Hippo needs
root privileges to perform the majority of its functions (and is thus often
executed as root or with sudo.)