---
layout: post
title:  "Slurm, Sciama, and VS Code"
date:   2023-01-26 14:00:00 +0000
categories: slurm sciama vscode
---

This post is a guide to getting VS Code to work with Slurm + Sciama. This is useful because then you can use VS Code to interactively develop on the HPC cluster's compute nodes, as we are not allowed to run VS Code on the login node.

## What are Slurm, Sciama, and VS Code?

Slurm is a job scheduler that allows you to submit jobs to the cluster. It's a bit like a queueing system, but it's a bit more complicated than that. You can find out more about Slurm [here](https://slurm.schedmd.com/overview.html).

Sciama is the University of Portsmouth's HPC cluster. It's a cluster of 1000s of compute cores, and multiple GPUs. You can find out more about Sciama [here]().

VS Code is a code editor that is very popular with developers. It's free, open source, and has a lot of useful features. You can find out more about VS Code [here](https://code.visualstudio.com/).

## What is the principle behind this?


*The RemoteCommand*
```
  RemoteCommand srun -n 1 -c 4 -p gpu.q -J vscode_server_${USER} --time=24:00:00 --gres=gpu:1g.5gb:1 --nodelist gpu02 -K sh -c 'module load anaconda3/2022.05 && exec /bin/bash --login'
```

The RemoteCommand is a command that will be run on the remote machine. In this case, it's a command that will run on the compute node.
These are all fairly standard srun arguments until the -K, which is [--kill-on-bad-exit](https://slurm.schedmd.com/srun.html#OPT_kill-on-bad-exit), and tells Slurm to kill the job if the connection is lost. This is important because if you close VS Code without disconnecting, the job will still be running on the cluster, and you'll have to kill it manually. Then there's some odd stuff happening affter that, and it basically just loads Anaconda and starts a bash shell.

## Instructions for Mac

Requirements: VSCode (v1.74.3 as of writing), and the Remote Development extension pack.



Next, you'll need to set up your SSH config file. This is where you'll define the hosts you want to connect to. I have a file called `~/.ssh/config` that looks like this:

``` 
Host *
    AddKeysToAgent yes
    UseKeychain yes
    IdentityFile ~/.ssh/id_rsa

Host cluster
    HostName cluster.example.com
    User username
    IdentityFile ~/.ssh/id_rsa
```

(You can find more information about the SSH config file [here](https://linuxize.com/post/using-the-ssh-config-file/).)

So we don't run vscode on the login-node, we'll have to ProxyJump to the compute node. To do this, we'll need to add the following to our SSH config file:

```
Host cluster
    HostName cluster.example.com
    User username
    IdentityFile ~/.ssh/id_rsa
    ProxyJump login-node
```

Finally, we'll need to add a RemoteCommand to run vscode on the compute node. To do this, we'll need to do two things:

1) Turn on the Enable Remote Command setting in the VSCode settings.
2) Add the following to our SSH config file:

```
Host cluster
    HostName cluster.example.com
    User username
    IdentityFile ~/.ssh/id_rsa
    ProxyJump login-node
    RemoteCommand srun -n 1 -c 4 -p gpu.q -J vscode_server_${USER} --time=24:00:00 --gres=gpu:1g.5gb:1 --nodelist gpu02 -K /bin/bash --login
```
&nbsp; 

Now, you can connect to the cluster by opening the Command Palette (⇧⌘P) and typing "Remote-SSH: Connect to Host...". Select "cluster" from the list, and you should be connected.

Once you're connected, you can open a folder on the cluster by opening the Command Palette (⇧⌘P) and typing "Remote-SSH: Open Folder...". Select the folder you want to open, and you should be good to go.

Note: If you're using a password to connect to the cluster, you'll need to add the `PasswordAuthentication yes` option to your SSH config file. You can also add the `ForwardAgent yes` option to forward your local SSH agent to the remote machine, which will allow you to use your local SSH keys to authenticate with the cluster.


## Instructions for Windows
---

Objective Reminder: To be able to connect to a *slurm allocated* compute node using VS Code by proxying through the login node, with SSH credentials passing all the way through.

Requirements: PuTTY (Pageant and PuTTYgen **from the Microsoft Store and not AppsAnywhere if using a University issued laptop!**), OpenSSH for Windows (comes with Windows 10 or 11), Latest VSCode (v1.74.3 as of writing) with the Remote Development extension pack.

Firstly, this is not as easy as it should be for a number of reasons. This process will be easier if you check that these two settings are enabled first:

1) Enable viewing hidden files and folders in File Explorer. Files or folders that start with a full stop (.) are hidden by default.  See here for instructions: https://support.microsoft.com/en-us/windows/view-hidden-files-and-folders-in-windows-10-97fbc472-c603-9d90-91d0-1166d1d9f4b5
2) Enable viewing file extensions in File Explorer. See here for instructions: https://support.microsoft.com/en-us/windows/view-file-name-extensions-12b036fd-8ae3-9aaf-8b4e-60d24b4e9efb



NOTE: I did get this to work by swapping to use the SSH version that comes with Git for Windows, but I know the University supports PuTTY everywhere so I'm going to stick with that.

### Step 1: Create a key pair
---
To use VS Code with Sciama, you'll need to either find your existing ssh key pair, or generate a key pair. If you've ever connected to the cluster before then you will have created a key already. Keys are normally kept in the `~/.ssh/` folder a.k.a `C:/Users/Username/.ssh/` on Windows. To do this, open PuTTYgen and click "Generate". Move your mouse around the window to generate some random data. Once you have enough data, click "Save private key" and save the key to `C:\Users\Username\.ssh\id_rsa`. Then, click "Save public key" and save the key to `C:\Users\Username\.ssh\id_rsa.pub`. 

### Step 2: Check the key is in the right format
---
We need this key in PuTTY format (has a file extension of ".ppk"). It's normally saved like this by default, but if it isn't, you can convert it by opening PuTTYgen and clicking "Load" and selecting the key you just saved. Then, click "Save private key" and save the key to `C:\Users\Username\.ssh\id_rsa.ppk`.

### Step 3: Configure Pageant
---
Pageant is an ssh-agent for Windows. It allows you to use your local SSH keys to authenticate with the cluster, but more importantly, remember your password so you don't have to type it in every time you connect. You will have to enter your password if you restart your computer, if Pageant crashes/is closed, or if you haven't used it for a while.

We can configure Pageant to load our private key at startup, and to create the config file that allows OpenSSH to use Pageant to authenticate with the cluster.

To do this:
1) Open the Start menu, right click "Pageant", and choose Open file location.
2) Right click "Pageant" and choose Properties.
3) Make the Target field look like this: `"C:\Program Files\PuTTY\pageant.exe" C:\Users\Username\.ssh\id_rsa.ppk --openssh-config %USERPROFILE%/.ssh/pageant.conf` where the syntax is `pageant.exe <key1> --openssh-config <config file>`.

### Step 4: Add Pageant to startup (optional)
---
For an ssh-agent to be worth using, it should be more of a background process that you don't think about, so we need Pageant to run on startup. To do this, we'll need to create a modified shortcut to Pageant and put it in the startup folder.

Press Win+R and type `shell:startup`. Copy the Pageant shortcut into this folder and it will be run on startup. However, this may get annoying so you may just want to run it manually when you need it.

### Step 5: Configure OpenSSH
---
Open the Command Palette (ctrl+shift+p) and type "Remote-SSH:Open SSH Configuration File...". Open the one located at C:\Users\Username\.ssh\config, and if it doesn't exist, create it.

Then paste this into the file: 
```
Include C:/Users/Username/.ssh/pageant.conf

Host sciama-login
  HostName login3.sciama.icg.port.ac.uk
  ForwardAgent yes
  RequestTTY yes
  User moricex

Host sciama-gpu02
  HostName gpu02
  ProxyJump sciama-login
  RequestTTY yes
  ForwardAgent yes
  RemoteCommand srun -n 1 -c 4 -p gpu.q -J vscode_server_${USER} --time=24:00:00 --gres=gpu:1g.5gb:1 --nodelist gpu02 -K sh -c 'module load anaconda3/2022.05 && exec /bin/bash --login'
  User moricex
```
You will need to change the User field to your username. The you can set the Host field to whatever name you like, but the HostName field has to be an actual hostname on sciama, like gpu02, or node147. 



NOTE: It is important that the Include statement is at the top of the file, otherwise it won't work.

### Step 6: Configure VS Code
---
Open the Command Palette (ctrl+shift+p) and type "Open Settings (JSON)". This will open the settings.json file.

Set/Add these particular settings:
```
    "remote.SSH.enableRemoteCommand": true,
    "remote.SSH.useLocalServer": true,
    "remote.SSH.maxReconnectionAttempts": 0,
```
Alternatively, you could open settings and search for "SSH" and set these settings there.

### Step 7: Connect to the cluster
---
Press the Green <> button in the bottom left corner, or open the Command Palette (ctrl+shift+p) and type "Remote-SSH: Connect to Host...". Select "sciama-gpu02" from the list, and you should connect.

---
## Instructions for Linux
---
Testing on CentOS 7 now.

---
If you have any questions or comments, feel free to reach out to me on Twitter or email.


