---
layout: post
title:  "Slurm and VS Code"
date:   2023-01-26 14:00:00 +0000
categories: slurm vscode
---

This post is a quick guide to getting VS Code to work with Slurm. I'm using VS Code on a Mac, but I think the same steps should work on Linux.

First, install the [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) extension pack. This will give you access to the Remote SSH extension, which is what we'll be using to connect to the cluster.

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

Finally, we'll need to add a RemoteCommand to run vscode on the compute node. To do this, we'll need to add the following to our SSH config file:

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

---

If you have any questions or comments, feel free to reach out to me on Twitter or email.


