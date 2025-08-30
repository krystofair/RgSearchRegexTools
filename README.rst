Search tools for rg
-------------------

What it does is build regex for specific task.
Invoke the tool in rg command by ticks "`" (SHIFT+~) which will return
Regular Expression for specific tasks.

---
Why
---

  | Currently I use NeoVim without LSP.
  | I didn't find time to configure LSP in my way yet,
  | but I did find time to build ctags for project I'm working on...
  |
  | LSP in my way means that I don't like format of finding references they served.
  | I like to have small memory overhead.


Installation
------------
In my configuration I created directory `/scripts` where the tools are kept and has
execute permissions.

-------
Warning
-------
::

  This will not work Windows, because of name 'scripts' and case insensitive. So use
  another name, etc.

Then I created link in `/bin` for this tools without extension '.py'.
Mentioned directories are for *python's virtual environment.*


Usage
-----

::

  rg `reimp name-of-some-module`
  rg `reimp - name-of-function`


Current list of tools
---------------------

reimp
  For imports in python, wants two arguments: module and function names,
  but there are default values so argument can take '-' as skipping it.

inv
  For invoking a function or method. Wants single argument 'name' of the function
  or method.


