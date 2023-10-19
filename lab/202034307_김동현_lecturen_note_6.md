# Git-1 (*Week6_lab*)

# Git
A source version control system that allows you to keep track of the versions of the source code you write as you progress through development.

***Version Control*** : Version control and branching exist in git.

1.	**Version Control** : A system that records file changes over time and allows you to retrieve a version of a file at a specific point in time.

  ![Version control img](https://www.webinerds.com/hs-fs/hubfs/Imported_Blog_Media/A-Brief-Timeline-of-Version-Control-Systems-03-770.png?width=770&height=363&name=A-Brief-Timeline-of-Version-Control-Systems-03-770.png)

## *Three ways to version control*
* Local
* Centralize
* **Distributed**
2.	**Branch** : Branches are necessary when you want to work on multiple tasks independently.

![branch img]( https://woowabros.github.io/img/2017-10-30/git-flow_overall_graph.png)

***Collaboration*** : You can view other people's work and edit history. You can also set rules for collaborating with each other.

* Git configurations are stored in three levels
1. System level : --system option. Affects all uses and repositories on the system(administrative)
2. Global(user) level: --global option. Affects all repositories of a current user
3. Local level: --local option. Specific to the current repository

```sh
$ git config –list
credential.helper=osxkeychain
user.email=donghyeon350@gmail.com
```

```sh
$ git config --list --show-origin
file:/usr/local/etc/gitconfig   credential.helper=osxkeychain
file:/Users/admindonghyeon/.gitconfig   user.email=donghyeon350@gmail.com
```

* Initializing a Repository in an Exiting Directory

```sh
$ cd /Users/admindonghyeon/Documents/open_sorce_sw
$ git init
```
```sh
$ git status
현재 브랜치 master

아직 커밋이 없습니다

추적하지 않는 파일:
  (커밋할 사항에 포함하려면 "git add <파일>..."을 사용하십시오)
	.DS_Store
	OpenSorce Linux CLI.docx
	Photo/
	Week 6_Lab_Git.docx
	command_history.txt
	file_list.txt
	lab/
	myscript.sh
	pdf/
	sorted_word.txt
	word.txt
	~$ek 6_Lab_Git.docx

커밋할 사항을 추가하지 않았지만 추적하지 않는 파일이 있습니다 (추적하려면 "git
add"를 사용하십시오))
```
* git add [file_name]

```sh
$ git add file_list.txt
$ git satus
현재 브랜치 master

아직 커밋이 없습니다

커밋할 변경 사항:
  (스테이지 해제하려면 "git rm --cached <파일>..."을 사용하십시오)
	새 파일:       file_list.txt

추적하지 않는 파일:
  (커밋할 사항에 포함하려면 "git add <파일>..."을 사용하십시오)
	.DS_Store
	OpenSorce Linux CLI.docx
	Photo/
	Week 6_Lab_Git.docx
	command_history.txt
	lab/
	myscript.sh
	pdf/
	sorted_word.txt
	word.txt
	~$ek 6_Lab_Git.docx
```
---
* ***nano file_list.txt*** : You can modify the file in a terminal window.
* ***git rm ---cached[file name]*** : You can remove files to commit.
* ***Ignoring a file *** : .gitgnore file
* ***Change branch name***
 

```sh
$ git branch
* master
$ git branch -m master main
$ git branch
* main
```

* Commit
```sh
$ git commit -m "commit mesagge"
[main (최상위-커밋) 240870e] commit mesagge
 1 file changed, 6 insertions(+)
 create mode 100644 file_list.txt
```
