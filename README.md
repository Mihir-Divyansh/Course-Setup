# Device Setup for EE1101
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



# Online Assignments : A Guide to $\text{\LaTeX{}}$

LaTeX is a tool specifically designed to create professional-looking documents, like a fancier version of Microsoft Word. Here's the key difference:

In Word, what you see is what you get. You type and format directly on the screen.

LaTeX works differently. You write your text and instructions for formatting in a plain text file. You tell LaTeX what you want (headings, bold text, equations), and it takes care of the fancy typesetting.

LaTeX is particularly powerful for technical documents like research papers or scientific reports.

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

## A few $\LaTeX{}$ commands
* $\text{\textbf{Commenting text}}$
```latex
% Adding a '%' symbol before some text "comments out" the text. 
```

Commenting text implies that you are telling the compiler to ignore that particular line.

* $\text{\textbf{Adding Figures}}$

```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.75\columnwidth]{relative_path-to-file}
    \caption{Caption}
    \label{fig:Label_name}
\end{figure}
```
