# Linux CLI (*Week5_lab*)

# Shell command

***I/O Redirection (Standard Output)***
```sh
$ pwd
/Users/admindonghyeon/Documents/open_sorce_sw
$ ls -lh > file_list.txt
$ cat file_list.txt
total 0
drwxr-xr-x  5 admindonghyeon  staff   160B  9 18 18:49 Photo
-rw-r--r--  1 admindonghyeon  staff     0B 10  3 18:58 file_list.txt
drwxr-xr-x  8 admindonghyeon  staff   256B  9 18 19:58 lab
drwxr-xr-x  3 admindonghyeon  staff    96B  9  5 23:19 pdf
drwxr-xr-x  2 admindonghyeon  staff    64B  9  5 23:10 test
```
Using “>>” append output to an existing file (if it already exists), or create an write to a new file if fit doesn’t exist.

***I/O Redirection (Standard Output)*** : You can redirect input from a file using “<”.

```sh
$ cat word.txt
School
Class
Home
New
Lecture
Cat
Dog
$ sort < words.txt > sorted_words.txt
$ cat sorted_words.txt
Class
Dog
Home
Lecture
New
School
```

***Pipelines***(|): Pipeline feeds output of previous command to input of next command.
* ls -lh | less : When you have a lot of directories and files, you can get a quick overview on one screen.
```sh
$ ls -sh | less
```
```sh
$ total 24
0 Photo
8 file_list.txt
0 lab
:
```
**Press “q” key to exit the screen**
* ls | wc – 1 : You can see the number of files and directroys in the current directory.

***backslash*** : Can be used to ignore line change in command (“enter”)
```sh
$ ls -l \
> --reverse \
> --human-readable
```

# Permissions
*Files and directories have a permission assigned differently to owner / group / others.
![Permissions image](https://linuxcommand.org/images/file_permissions.png)
> r (read) w (write)x (execute)
* -rwx(owner) rwx (group) rwx (others) 
* Permissions can be granted using the "chmod" command

***Shell Script*** : Week_5 PDF 

***history*** : You can see previous command history
```sh
$ history > command_history.txt
$ Cat command_history.txt
328  cat word.txt
  329  sort < words.txt > sorted_sowrds.txt
  330  sort < word.txt > sorted_word.txt
  331  cat sorted_word.txt
  332  sort < word.txt > sorted_word.txt
  333  ls -sh | less
  334  ls -sh | less
  335  ls wc -1
  336  ls | wc -1
  337  ls -l\\n
  338  nono myscript.sh
  339  nano myscript.sh
  340  ls
  341  ls -lh
  342  sh Shell scrpit
```
