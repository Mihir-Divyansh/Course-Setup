# Device Setup for EE1101
This is intended to help you setup your devices for the course.

You will need additionally 
1. A Keyboard (Bluetooth / Wired)
2. A stand for your phone (Not compulsory, but if you have one, it will be easier for you)

### Probable Devices you may have
1. Any android phone/tablet
2. Any windows laptop with enough storage for a dual boot.
3. None of the Above (All Apple Devices) : We'll come to you later

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
    To set up neovim, follow the below

      Installing Vim Plug
      ```bash 
        curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
        curl -fLo ~/.config/nvim/init.vim --create-dirs https://raw.githubusercontent.com/gadepall/termux/main/neovim/init.vim
      ```
      To enter the plugin,
      ```bash
        nvim ~/.config/nvim/init.vim
      ```
      And inside nvim, run
      ```sh
        :PlugInstall
        :qa!
      ```
5. Installing LaTeX

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


## If you have all Apple devices
Imagine having spent so much money, to spend more money.

Apple users during GVV sir's course be like 

![fig](Figures/wipe%20tears%20money.jpg)

You only really have two options. 
1. Borrow someone's ANDROID phone / get one from home, if you have an old one lying around before every class.
2. Buy a Raspberry Pi and run Lineage OS on it. (Lineage OS is like Android without officialy supported Google apps) 

Sane people generally choose the First option. The second option is all you if you decide to go for it. 


## Setting up your Accounts: GitHub
* Click Sign Up and follow the on-screen instructions
* Create a repository with the name: EE1030, and make it public

* If this is your first time making a GitHub Repository, the website gives a list of commands you can run on command line, to set up your repository locally

### Maintaing a Local copy
* Open Termux and Login
* For good practice, create a folder for the course, and go to that folder with the following commands. 
> 'cd' stands for change directory, and goes to the folder requested

> 'mkdir' stands for make directory
```sh
    cd /sdcard
    mkdir "Your Folder Name" && cd "Your Folder Name"
```
* Clone your repo: Replace the link below with your own
```sh
    git clone https://github.com/User-Name/EE1030.git
```


# Online Assignments: A Guide to LaTeX

LaTeX is a tool specifically designed to create professional-looking documents, like a fancier version of Microsoft Word. Here's the key difference:

In Word, what you see is what you get. You type and format directly on the screen.

LaTeX works differently. You write your text and instructions for formatting in a plain text file. You tell LaTeX what you want (headings, bold text, equations), and it takes care of the fancy typesetting.

LaTeX is particularly powerful for technical documents like research papers or scientific reports, which contain tons of math typing.

It excels at handling:

* Complex mathematical equations: LaTeX can write intricate equations neatly and accurately, a challenge for regular word processors.
* Consistent formatting: Once you define a style (font, spacing), LaTeX applies it throughout the document, ensuring a polished look.
* Automatic elements: LaTeX can generate numbered references, tables of contents, and bibliographies, saving you time and effort.

Here are a few examples.
1. A document with some text on it
```latex
\documentclass{article}
\begin{document}
First document. This is a simple example, with no 
extra parameters or packages included.
\end{document}
```
![Example1](Figures/Basic%20Example.png)

2. A document with a title, author and some text

```latex
\documentclass[12pt, letterpaper]{article}
\title{First full document}
\author{Mihir Divyansh}
\date{\today}
\begin{document}
\maketitle
We have now added a title, author and date to our first \LaTeX{} document
\end{document}
```

![Example2](Figures/Example%202.png)

You are given a template by sir for your assignments. 
You can look at the files [here](LaTeX)

Your main 'tex' document should look like the example given [here](LaTeX/Example%20Assignment/main.tex)


## LaTeX Basics
To include mathematics in a document, you type the LaTeX source code for the math between dollar signs. For example, ```$ax^2+bx+c=0$``` will be typeset as $ax^2+bx+c=0$. If you enclose the code between double dollar signs, the math will be displayed on on line by itself. (This is called "displayed math.") For example, `$$ax^2+bx+c=0$$` will be typeset as $$ax^2+bx+c=0$$

In the source code, certain characters have special meaning: `$ \ { } ^ _ & ~ # %`. We have seen that $ is used to surround math code.

The backslash character, \, is used for LaTeX commands, and braces, { and }, are used to enclose the parameters to which a command applies. For example, in \sqrt{b^2-4ac}, the command is \sqrt, the parameter is b^2-4ac, and the typeset result is $\sqrt{b^2-4ac}$
. The `\frac` command is used to make a fraction, and it has two parameters, so `\frac{n!}{k!(n-k)!}` is typeset as $\frac{n!}{k!(n-k)!}$
. Some commands don't have parameters. For example, `\infty` represents the infinity ($\infty$) symbol, , and \to produces a right arrow ($\to$), . Note that you might need to leave a space after a command like \to to mark the end of the command word. For example, use `f\colon X\to Y` to get $f\colon X\to Y$. Typing `\colonX` instead of `\colon X` will just get you an error.

The special characters caret, ^, and underscore, _, are used for exponents and subscripts in math mode. If there is more than one character in the subscript or superscript, use {} to enclose the characters

Some LaTeX code uses environments. Environments are coded using \begin and \end, which take the name of the environment as parameter.
These are just a few things to get you started. Look at the example assignment, and experiment with different commands. Utilise Google and ChatGPT as much as possible to get hints .

