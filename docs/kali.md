# Kali 2020

## VMware
* This section describes how to install the latest VMware image for Kali 2020.

### Download Image
* Open browser
* Navigate to the Offensive Security VMware/Virtual box [download page](https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/).
* Download the *Kali Linux VMware 64-bit* image to your computer (~2.1 GB) to a directory of your choice
* Unzip the kali-linux-2020.3-vmware-amd64.7z file

### Install Image
* Start VMware Workstation 15 Player
* Select *Open a Virtual Machine*
* Open the *Kali-Linux-2020.3-vmware-amd64.vmx* file
* Once loaded rename it to *CS448-Kali-2020*
* Press *Play virtual machine*
* Press *I Copied It* if prompted (this may not happen for you)
* Select *Kali / GNU Linux*
* Enter *kali* for name and *kali* for password
* Press *Login* button

### Setup Lab Environment

* Open a new terminal (upper left-hand corner, black square icon)
* Right click, select preferences, set application transparency to 0%, close
* Press *OK* button

```
$ sudo apt-get update  # password is kali
$ git clone https://github.com/johnlwhiteman/cs448-2020-fall.git
$ cd ./cs448-2020-fall/bin
$
```








## VirtualBox
* This section describes how to install the latest Virtual Box image for Kali 2020.

### Download Image
* Open browser
* Navigate to the Offensive Security VMware/Virtual box [download page](https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/).
* Click on the Kali Linux VirtualBox Images +
* Download the *Kali Linux VirtualBox 64-bit* image to your computer (~3.2 GB)