# Getting Started with Python Coding: Building Fully Featured Apps


Chang Tan
Lister Unlimited Cybersecurity Solutions, LLC.
changtan@listerunlimited.com

A lot of people underestimate the versatility of Python. First of all, Python is based on C, hence when you run a Python Script or App, there is a .pyc file that is generated in the same directory. Secondly, Python can be interpreted as both a scripting and a programming language due to the former's interactivity with C allowing you to build fully-featured apps. It depends on the scope of your goals. Third, object-oriented programming is a part of Python's design as of 2018, this subject is heavily covered in the last half of the book Learning Python the Hard Way where you are trying to construct a MUD (Multi-User Dungeon) using the features of the Class Object in Python.

With only another book to read, you can give it web-application characteristics such as Django, a web-app framework built on Python, which also has cross-compatibility with JavaScript, NodeJS, JQuery, REACT, and AngularJS, among others. You can also generate GUI's using a multitude of competing frameworks such as tkinter.

Python is a program that appeals to both Red Teamers and coders in general. In comparison to lower level programming languages, you can quickly test concepts and ideas without having to waste time building a library and allocating memory, two things that are taken care of Python's modules (mostly taken care of) and the Python Interpreter's Garbage Collector, that frees up memory in the background. There are ways to crash a Pythonic application but in general, the garbage collector is good enough to handle anything you throw at it.

When tasked with writing ONE app, I can often get a working proof-of-concept running (a 'PoC'), within 2 to 24 hours. After debugging the application and achieving the main goal, I can then branch out with additional features to better flesh out the design. At some point, I end up redesigning the entire application after learning a few ideas, such as building a toolkits.py module and having redundant and frequently used functions be imported and saved as a argument, which helps save me time.

Now how much of that can you achieve in C?

Python, is a language of productivity, it might not be making the best or most memory efficient, or fully support threading (it's a matter of debate within the community), but getting a tangible prototype running is best done in Python or any other higher level programming language like JavaScript or Ruby. What makes Python remarkable is it's capability to interact with many other interpreter shells, this includes Ruby and Java via the subprocess.call and subprocess.Popen modules. Python can also reliably generate and by-the-book adhering UNIX Daemons using subprocess forking (mainly). There are over 50 modules in the command `pip search daemon` just to generate and manage true UNIX Daemons. When I am speaking the term Daemon, I am NOT referring to system services which are managed by systemd. Those are a separate category and they run at a privilege lower than root. A true UNIX Daemon runs at a privilege higher than root and may have the option of not being able to be detected.

# Getting comfortable with whitespace indentation

A lot of people are uncomfortable with dealing with whitespaces, and the famous "indentation error", I will show you how that can be quickly remedied.

Download atom.io and run the installer

`wget https://atom.io/download/deb`

`dpkg -i atom-amd64.deb`

On the packages drop-down, click on it, hover your mouse to [whitespaces] and you'll quickly learn, by default atom.io has all of the necessary features to fix this dreaded issue, to help you save more time and continue forward with debugging.

1. You can remove trailing whitespaces on your selection.
2. You can convert spaces to tabs and back again

Often, many of us prefer organizing our whitespaces by tabs.

# Useful functions for python

# Read a text file and split into lines, then print to the screen or do something with it.
```
def txtReader(file):
  r = open(file, 'r')
  p = r.read()
  lines = p.splitlines()
  for line in lines:
    line = str(line.encode('utf-8')).strip().rstrip()
    sys.stdout.write(line)

    return line
```
To write to a text file or named pipe (foreword: I wouldn't mess with the mkfifo module in Python as Python can directly work with pipes better with the subprocess module)

# Run a process in the background (Warning, shell=True is a dangerous argument, but we are in the business of malware, just be aware of this)

For the purpose of this submodule... 'e' stands for Error Output, 'p' stands for a running process, 'o' is Standard Output, and 'l' stands for line in a list of lines.
```
import subprocess, Threading, os, sys, operator

def background_cmd(cmd):
  p = subprocess.Popen(cmd, shell=True, executable='/bin/bash', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  e = p.stderr.read()
  e = e.splitlines()
  o = p.stdout.read()
  o = o.splitlines()
  for l in o:
    l = str(l.encode('utf-8')).strip().rstrip()
    stdoutlog = '/var/log/stdoutlog.log'
    w = open(stdoutlog,'a+')
    w.write(l)
    w.close()

  for l in e:
    l = str(l.encode('utf-8')).strip().rstrip()
    stderrlog = '/var/log/stderrlog.log'
    x = open(stderrlog,'a+')
    x.write(l)
    x.close()

  return o, e, l
```

Remember that if you want to use something else than the bash shell, you can substitute `executable='/bin/bash'` for `/usr/bin/python` or `/usr/bin/ruby` for example.

To write to the screen (print) you have two choices, either as a `sys.stdout.write(line)` or `print line`. Be sure to convert it to a string, which is our next tidbit.

# Maybe you just want to run a command and have it quickly return you the results?

```
directory = "/var/log/suricata/fast.log"
check_logs_cmd = "cat {}".format(str(directory))

def check_logs_real_quick(directory, check_logs_cmd):
  p = subprocess.Popen(check_logs_cmd, shell=True, executable='/bin/bash', stderr=subprocess.PIPE, stdout=subprocess.PIPE)
  output = p.stdout.read()

  return output
```

So if you want to go through a file in the background. And have it return it to your display or perform a response because of it...

```
whats_in_my_logs = check_logs_real_quick(directory, check_logs_cmd)

```

Now you can parse the whats_in_my_logs variable for indicators or outputs.

# Perfectly format a line into a string with no whitespaces

Be sure to conform to the newest standard for Python, which dictates the conversion of 'dashes' in filenames over to the underscore or `_`. In Python, dashes with or without whitespaces dictate the subtract operator which causes compatibility problems unless escaped, quoted, or converted to a different character.
```
def lineToString(line):
  line = str(line.encode('utf-8')).rstrip().strip().replace('-','_')

  return line
```

To convert a string... in our previous example...

```
def background_cmd(cmd):
  ...
  for l in e:
    string = lineToString(line)
    ...
```

Notice how the value that is returned to the variable string is flexible, it is the same as `return line` but this time it knows, `return string`. In Python, we have a 'attribute' for each object. What we have done is change the `__name__` attribute from 'line' to 'string'.


# Enabling Automated Interaction with Foreign Shells

Many a times, I desired the ability to automate the SSH login shell, or to interact with a shell that is written in C or another language like Metasploit's Ruby on RAILS or Routersploit's encoded shell (If you look under the hood, it is encoded with it's own keys and uses weak-references, possibly as a security measure to protect the user).

Since the demand is to interact with the readable OUTPUT of another program, we can use pexpect, which scans the screen for readable output (warning: Some programs may only express it in garbled unicode, be aware of that and double check what your process outputs).

```
child = pexpect.spawn(cmd, logfile=sys.stdout, timeout=300)
fout = open(log, 'wb')
child.logfile = fout
child.logfile_read = sys.stdout
child.expect("string")
```

The line expect("string") means that pexpect will scan the screen for a string. Like I said before, it will scan it exactly as either unicode or UTF-8 (English).

To allow the session to "persist" for another command instead of crashing to a EOF Error (End-of-File Error)

```
child.expect(pexpect.EOF)
child.sendline('\n')
```

However, this takes up our only slot to expect a different outcome. It'll just keep looping and entering [return]. To add multi-choice interactivity...

```
result = child.expect([
    'string one',
    'string two',
    pexpect.EOF,
    KeyboardInterrupt
  ])

if(result==0): # if string one is seen
  do something
elif(result==1): # if string two is seen
  do something else
elif(result==2): # a EOF error is seen
  child.sendline('\n') # auto-press a newline key to keep the process running
elif(result==3): # If a KeyboardInterrupt (CTRL + C) is pressed
  exit(0) # exit
else:
  pass
```

This will keep looping through conditions 0 to condition 3 (in Python, we start a list with a index of zero or "count from zero"). Whenever a EOF condition is reached, it'll keep the process running so that it can evaluate for conditions string one, two, and KeyboardInterrupt.

This is incredibly useful, like... writing a auto-pivot module for Metasploit Framework.

```
result = child.expect([
    'Command Session',
    'Meterpreter Session',
    pexpect.EOF,
    KeyboardInterrupt
  ])

if(result==0): # Auto-Upgrade the session if possible
  child.sendline('sessions -u %s') % str(session)
elif(result==1): # if Meterpreter session is seen
  child.sendline('sessions -C "run post/manage/multi/autoroute"')
  child.expect(pexpect.EOF)
  child.sendline('sessions -C "portfwd add -l {0} -p {1} -r {2}"'.format(
      str(proxyport),
      str(remoteport),
      str(subnetrange)
    ))
elif(result==2): # a EOF error is seen
  child.sendline('\n') # auto-press a newline key to keep the process running
elif(result==3): # If a KeyboardInterrupt (CTRL + C) is pressed
  exit(0) # exit
else:
  pass
```

You can refer to a string as a argument as in `"%s" % str(arg)` or as `"{}".format(str(arg))` or as `"{0}".format(str(arg))`. The last one is the recommended method for massive multiline strings that may reuse the same variable by calling it by it's reference number.


# There are a handful of things that I wish Python could improve

1. The Python module repositories such as PyPi have become a real mess, with some modules being easily imported and others requiring obsoleted packages and/or forcing us to rely on virtualenv to enable us to use a module without being forced to break our actual Python installations (a majority of Linux Applications rely on Python, it's strongly advised to NOT dramatically modify your base Python installation)
2. As Windows does not natively support Python without running Python itself (2.7.13+), many have failed to adopt it on the Windows end. However, transpiling Linux Python code and Windows Python code is merely a handful of modules.
3. Generally, certain languages are NOT directly translatable or transpilable. Despite the abundance of JavaScript Transpilers, each one still requires direct review of the code for transpilation errors.
