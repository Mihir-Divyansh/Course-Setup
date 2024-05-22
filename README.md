# Course Setup for EE1101
This is intended to help you setup your devices for the course.

You will need additionally 
1. A Keyboard (Bluetooth / Wired)
2. A stand for your phone (Not compulsory, but if you have one, it will be easier for you)

## Recommended devices
1. Any android phone/tablet
2. Any windows laptop with enough storage for a dual boot.
3. If you are Rich AF (Have all Apple Devices)

## Setting up an android device 

> All instructions for android device are taken from sir's fwc-1 repo [here](https://github.com/gadepall/fwc-1)

1. Install [F-Droid](https://www.f-droid.org/).
2. Open f-droid on your device and install the following apps:
   * Termux
   * Termux:API

### Setting up Termux

1. Give termux access to your user directory in Android.

    ```bash
    termux-setup-storage
    ```

2. Upgrade packages (any _**one**_ command)

    ```bash
    pkg upg
    ```

    ```bash
    apt update && apt upgrade
    ```

3. Install mandatory packages (any _**one**_ command)

    ```bash
    apt install build-essential openssh curl git wget subversion silversearcher-ag imagemagick proot proot-distro python bsdtar mutt nmap neovim
    ```

    ```bash
    pkg in build-essential openssh curl git wget subversion silversearcher-ag imagemagick proot proot-distro python bsdtar mutt nmap neovim
    ```

### Installing and Setting up Ubuntu on Termux

1. Install ubuntu

    ```bash
    proot-distro install debian
    ```
    ```bash
    proot-distro login debian
    ```

    Inside proot-distro

    ```bash
    apt update && apt upgrade
    ```
    ```bash
    apt install apt-utils build-essential cmake neovim git wget subversion imagemagick nano ranger python3-venv
    ```

2. Installing python3

    ```bash
    apt install python3-pip python3-numpy python3-scipy python3-matplotlib python3-mpmath python3-sympy python3-cvxopt
    ```

3. Installing neovim and ranger

    ```bash
    apt install neovim ranger libxtst-dev libx11-dev python3-pynvim
    ```


4. Installing LaTeX

   ```bash
   apt install texlive-full gnumeric
   ```
## Setting up a Windows Laptop

### Dual Booting your laptop

Ubuntu is an Operating System, much like Windows is an OS. But it differs from Windows in many ways. Programming is much better in Ubuntu and all other Linux distributions, when compared to Windows. Here is a [link](https://www.onlogic.com/blog/how-to-dual-boot-windows-11-and-linux/) to help you dual boot your laptop*.

In our experience, we found Ubuntu to be the most hassle-free out of all the distros. Some others you can try before installing are
 * Parrot OS
 * Kali Linux $\color{maroon}{\text{(A pain to deal with)}}$ 
 * Pop! OS

<sup> *If you need any help, feel free to message a TA</sup>

### Setting up WSL (Windows Subsystem for Linux)
WSL lets you install a Linux operating system (like Ubuntu) directly on your Windows machine. Lets you use the Command Line Power of Linux inside of Windows. Here is a [link](https://www.geeksforgeeks.org/how-to-install-wsl2-windows-subsystem-for-linux-2-on-windows-10/) to get you started.

Both dual boot and WSL will work fine, though sir prefers dual boot. So it's your pick.

## If you have all Apple devices
Imagine having spent so much money, to spend more money.

Apple users during GVV sir's course be like 
![fig](Figures/wipe%20tears%20money.jpg)

You only really have two options.
1. Borrow someone's ANDROID phone before every class.
2. Buy a Raspberry Pi and run Lineage OS on it. (Lineage OS is like Android without officialy supported Google apps) 

Sane people generally choose the First option. The second option is all you if you decide to go for it. 