<h3>Project Description</h3> 
The code in newsreport.py deals with linking to a PostgreSQL database that contains news articles and 
generating a few reports on the command line, such as most popular articles and most popular authors. 

<h3>Dependencies/Prerequisites</h3>
For this project, you'll need: 
Virtualbox - https://www.virtualbox.org/wiki/Downloads
Vagrant - https://www.vagrantup.com/downloads.html
Vagrant directory from Udacity - https://github.com/udacity/fullstack-nanodegree-vm 

<h3>Installation/Requirements</h3> 
First, install Virtualbox. Then, install Vagrant. Afterwards, cd in your terminal to the Vagrant directory from Udacity and run the command vagrant up. Once vagrant finishes setting up an operating system on the VM, type vagrant ssh in the terminal. This will run the operating system from the command line. cd into /vagrant. Place the newsreport.py file from this github into that directory.  

<h3>Usage</h3> 
Type python newsreport.py in the terminal while located in the /vagrant directory. You will then see an output of info concerning popular news articles and authors. 
