
# LINUX NOTES

@date : 18/6/2017

linux --- developed in 1981 --- #example -ENGINE (we can use bike engine anywhere like bullet, or yamaha but models vary same like in IT sector linux is a kernal which can be accessable in many os or @ we can develop many os by using linux kernal)

# kernal---> directly intract with -----> hardware machine

# open terminal ----> windows button ----> terminal

# user {firefox,texteditor,terminal,vlc}---- kernal {CPU/RAM}----eng hindi -----coverter[interpreter,shell]<------> kernal()

#shell lends input to the kernal

#shell is smart it checks weather the data is contain in the system or not

# shell is a interpreter b/w user and kernal

# more than one interpreter can be avaliable in linux and unix{bash,sh,tcsh,csh,zsh}

# commands and inbuild program are stored in bin or sbin which is present in root .@bin -> normal commands @sbin -> admin power programs
      '''
	CD ~
	CD sbin  
	ls
	cd bin 
	ls
      ''' 
#input ----kernal---- shell(bash)----search----{path}-----if found [convert for kernel]---- if not found [shell will rply to user]

'''
****many types of os uses linex os kernel****
example : car engine is one but varity of car is different by adding different freatures.

->> redhat {linux ----interpret----firefox,gedit}
->> RHEL {redhat enterprise linux}
->> fedora 
->> torvalds
there are around 1500 os avaliable which inherit linux os kernal
''' 

'''
***predefined system variables***
$LANG
$PATH
$BASH
$SHELL
{if we did any editing in system variable then, they can assign new value but but then command will not work properly}
example given below 
'''
# @@@ note :files are always hidden ctrl +h for hide or unhide the file

'''
***Directory***
windows :
c:\user\admin
	student---{desktop,downlords}


linux :
\home\admin
	---{desktop,downlords}
'''

There are some commands --

1. uname         -r
  (kernal name) (version)

2. uname         -p
   (bit proccessor)

3. uname         -a
  (kernal name) (version)(complete info)

4. uname         -m
  	 (machine)

5. which cat
(used to check the location of inbuild program)

6. {firefox,gedit,clock,date} 
   (all commands open)

7. >> file /etc
# File : it is used to tell what type of file it is  
   >> cd python 
   >> file ./myprac12.py
   # python script

8. cat py1.py
 # display the output

9. tac py1.py
  # show file content invert

10. rev py1.py
  # used to reverse the text

11. cat > file.txt 
# (>)greater than symbol is used to create a file {press ctrl + d} to come out from the cat command. $$$ BY USING CAT COMMAND WE CAN CREATE A FILE ALSO USE > OPERATOR AND WRITE TEXT ON A NEW FILE ALSO .

12.	>> echo "hello" double quote 
	>> echo 'hello' single quote 
  	>> echo '''
		triple line comments 	  	
	 	'''
	>> echo "hello shubham today date is `date` " # display commands in string 

13. history 
 # display whole terminal history

14. clear        
  # clean the terminal screen by complete 1 page down if we scroll up commands can be shown 

15.	>>echo SHELL 
output:	# bin/bash
	>> echo SHELL=20
	>>echo SHELL
output:	# 20
	>>date 
	# [command not found ]because in shell value is change 
	>>exit
	# once you exit everything come back to normal
   
16. '''TERMINAL VARIABLE '''
	>>PS1="root@mathurbhaiya####"


# LINUX NOTES 2 

@date : 19/6/2017

ctrl + alt + f2,3,4,5,6 [command line screen [CLI]] {if we dont want to work graphically.}

ctrl +alt +f1 {come back to graphical mode}

There are some commands --

17. pinky / w / who 
# how many user login and how many times they logged in and from where they login


'''
  
18.	>>
	>> vim filename.py
		>> [:]decision box {wq}
		>> press i for edit
		>> esc for back to the commnd mode 
# if we want to access browser and or a file then , use vim or elinks 

'''

''' ************ I/O REDIRECTION*************** '''

OUTPUT REDIRECTION : we can send output anywhere else .

19. 
	date > out.txt
	cat > out.txt
	hello friends 
	ctrl +d 

# here output data is over ride .

	date >> out.txt
	cat >> out.txt
	hello friends 
	ctrl +d
# now output of that file is date is not over ride by cat command
# [>>] append  

'''
if we write before the i/o redirection symbol then,it was created a file but showing error in terminal and the file is also empty created .
 
'''

	>>datttteeeee >> out.txt
output:	#command not found but empty file is created 
	 
	>>dateeeeee 2> out.txt
# it 2> or 2>> is used to remove the error but, if you write the right command then also the file is created empty and if you use wrong command this error messge goes in your file. 

	>>dateeeeee &> out.txt
# it 2> or 2>> is used to remove the error but, if you write the right command then the file is created with its correct output and if you use wrong command this error messge goes in your file.

'''***BLACK HOLE (BLACK BOX OF LINUX I/O redirec topic )***'''
	>>date >/dev/null
	>>date &>/dev/null
  # when we dont want to use output
 # you can find null file which is black hole file in /bin/dev/null

20.
# use to create different files

	>>touch a.html
	>>touch a.jpeg

# we can also create jpeg file or html file by touch command

21. # wc command
#use to count the words in a file

	>> wc -l data # lines 
	>> wc -w data # words
	>> wc -c data # character
	>> wc data # lines, words, character

22.
''' **** |(pipe) data directly goes to ram for proccessing ***  '''
	
	>> cal | wc -w  
	(output)--->(input , proccessing)

''' ***head and tail*** '''
#used to print ouput from starting data or ending data 

	>> cal
	>> cal | head -2 # takes starting 2 lines 
	>> cal | tail -3 # takes ending 2 lines 1 line waste 
	>> cal | head -3 | tail -1 # middile line came

23.
''' *** grep command ***  '''
# use for searching data from a file

	>>cal | grep 3 # search 3 in calender
	>> cal | cut -d " " -f1 # PRINT first line  
	>> cal | cut -d " " -f2 # print second line 
	>> cal | grep -inv sun # allot lines in calander
	>> cal | mail mathurshubham151.ss@gmail.com # we can do anything with grep command


# LINUX NOTES 3 

@date : 20/6/2017

''' *********how to check versions of OS*********** '''

24.
>> cat /etc/redhat-release
# redhat os current version

25.
>> cat /etc/issue
# Ubuntu os current version

''' *** USER MANAGEMENT AND SECURITY *** '''

''' IN REDHAT WE LOGIN DIRECTLY IN ROOT ''' 
'''# USER Creating related all information in 

 	/etc/passwd file. '''

# USER MANAGEMENT

25.

# how to create user 

root : useradd sonu
root : useradd jack 

# @@@@@@@ user account entry ----> /home
   
	>> cd /home 
	>> ls home 
output:	# all users

# switch to the another user account

root :	>> su jack # no password required 
	>> whoami
	# jack
	>> su root
password : q
	>> whoami
	# root


# as a root user we can switch anywhere but normal user can not switch anywhere

	>> su jack
	>> whoami
	# jack

	>> su sonu # password is not required
	>>pass :****
	>> whoami
	# sonu


# how to set password in users
   
root : passwd jack 
pass: ****
re-pass: ****

'''
if we are root and we want to access any account we can access easily no password is required but if we are user and we want to switch to the another user then password is needed and,

		 if any user account dont have any password 
		and any another user want to access that user account that time also it ask for the password even there is no password . thats why user --- user switch is complex password needed either that user passwd protected or not password protected.
'''

26. 
# Delete users 

>> userdel jack # delete user jack
>> userdel sonu # del user sonu
>> cd /home # go to home firectory to check users
>> ls # still deleted user shown 
>> su jack # user is no more exist only user folder is there
'''
user is deleted but data will be saved and after deleting jack , folder is exist for saving his files but user is not more 

'''

>> useradd harry
>> passwd harry
>> cd /home
>> ls # harry shown
>> userdel -r harry
>> ls # harry folder is also deleted
''' data deleted and user is also deleted by using -r flag'''

27.
# ******USER Creating related all information in********** 

>> cd /etc/passwd #file.
>> vim passwd 

shubham:x:1002:1002::/home/shubham:/bin/bash
'''
x= when ever user is login it should ask for password to user either password is enable or disable.

1002= if id have a 0 then it have a root access. if we edit 1001 to 0 in vim this file can bheave like root 

/home/shubham:/bin/bash= file location
  '''
28.
#********* compiled commands location **********

>>cat /user/bin/date

''' command if compiled then it should have execution permission. and all commands comes under in this file''' 

29.
#********* Security Terms*********

------2 types of security-------

#### DAC ----> Discritonary access control
#### MAC ----> Mandotary access control

# directory must have always execute permission

@@@@@@@---DAC -- user -- ask to file --- read/write/execute@@@@@ 

>> mkdir dir_name
>> ls -ld dir_name

# as a user what permission it have 

#drwx-wxr-x. 2 root root 6 jun 28 23:01 dir_name

(what type of file d means directory)
(first rwx for owner)
(second rwx for group)
(third rwx for other)
(first root is creater)
(second root is for group)
(then created date and time)
(directory name)

30.
# BY DEFAULT creater is owner and creater is group

 chown - change file owner and group. chown changes the user and/or group ownership of each given  file.


 chown [OPTION]... [OWNER][:[GROUP]] FILE...
       chown [OPTION]... --reference=RFILE FILE...

>> cd /home 
>> ls
# sonu shubham root users detail

>> chown sonu dir_name
#drwx-wxr-x. 2 sonu root 6 jun 28 23:01 dir_name
>> chgrp sonu dir_name
#drwx-wxr-x. 2 sonu sonu 6 jun 28 23:01 dir_name

31.
#@@@@@@ this all work is done by root 

''' ***HOW TO CREATE A GROUP*** '''

>>groupadd tech
>> >> chgrp tech dir_name
#drwx-wxr-x. 2 sonu tech 6 jun 28 23:01 dir_name

# ADD USER IN GROUP

>>useradd -G tech sonu  
# OR
>>usermod -G tech tindle

# LIST OF ALL USER IN TECH GROUP

>> grep tech /etc/group

32.
''' *******Permission Change ********** '''

#owner
#group
#others

>>ls -ld dir_name # check permissions

>>chmod u-r
>>chmod g-x
>>chmod o-w
>>chmod u+rwx,g-rwx,o+rwx
>>chmod u+rwx,g-wx,g+r,o-r,o+x fuck

33.
# ***** octal permission change ******

421 = 7 # it means all permisson granted 

'''
own	grp	oth
rwx	rwx	rwx
421	421	421 

>>> chmod ooo dir_name
=> d---------
>>> chmod 777 dir_name
=> drwxrwxrwx

'''

own	grp	oth
rwx	rwx	rwx
421=6	421=3	421=1 

>>chmod 631 dir_name
#drw--wx--x

34.
# HOW TO GIVE DEFAULT PERMISSION --- UMASK

# for directory
own	grp	oth
rwx	rwx	rwx
421=7	421=7	421=7  ----> #max permission
421=7	421=5	421=5  ----> #default permission (i can specify)
-_______________________ 

0	2	2 (minus)----> # UMASK VALUE
________________________

# ^^^^^ we can change default umask permission ^^^^^

>>cd ~
>>vim .bashrc
# edit file
|___>>>> umask 022

''' 
# for files
own	grp	oth
rw	rw	rw
42=6	42=6	42=6  ----> #max permission
42=6	42=4	42=4  ----> #default permission (i can specify)
-_______________________ 

0	2	2 (minus)----> # UMASK VALUE
________________________

# ^^^^^ we can change default umask permission ^^^^^

>>cd ~
>>vim .bashrc
# edit file
|___>>>> umask 022
'''

# LINUX NOTES 4  

@date : 21/6/2017

''' ********* NETWORKING *********** '''

1. MEDIUM ( WIRE, WIRELESS)
2. PROTOCOL ( LANGUAGE )
3. (ADDRESS)(IP OR MAC)

# What is MAC address -- media access control

* This is a fixed address 
* NIC - network interface card : where we used to insert internet cable like (LAN)in laptops called NIC card.
* MAC address depends upon NIC of any laptop and computer. 
* IF we change NIC of any Device MAC address is also changed 
* NIC can be more than one in any computer devices
* MAC address also can be more than one of any device
* MAC address  is a physical address of any device which have a 6 byte code (hexa-decimal number system) seperated by colon.
* when we connect LAN cable to laptop or PC the hardware make a copy of MAC Address. IN linux, 
ifconfig---> bro(copy of that address): 94:57:a5:04:ae:d4

# if we want to know about MAC ADDRESS of our device then, 

windows : getmac {command}
linux : ifconfig {command}----> eno1(ethernet):  94:57:a5:04:ae:d4 

# What is IP address -- internet protocol

* In market we call IP address is IP version 4
* This is 4 byte code seperated by colon. and, each byte of code contain 1 byte 
* we can open any webiste or portal by using its ip address 
* ip address is generated when device is connected to internet
* 1 byte = 8 bits --
# it can be         |__>(0000-0000) or (1111-1111)
		         |__> 2 is to power 8 => 256
			 |__> 0-255 in 1 byte number range is not more than 0-255
35.
#TO FIND OWN DEVICE IP ADDRESS -->{command}---> wlp19s0 --> my ip address 		        

>>ifconfig 
#192.168.43.238

36.
''' ***important*** '''
>> host www.google.com
#172.217.161.4
{now copy this IP address and paste it own browser search www.google.com [home page] will open, and it also show the real name of any website }

''' ***important*** '''
>> host www.facebook.com
157.240.16.35
star-z-mini.c10r.facebook.com real name of facebook

''' ******** CONNECTIVITY ******** '''

* ROUTER is used to connect 2 IP's at time 
* if the network name or subnet mask or is same then, there is no need of router
->(192.168.10)[subnet mask/network name].(182)[host] sir IP 
->192.168.10.(283)[host] my IP 
# it can be connect easily 

* if network name is not same then router is required
->(195.152.98)[subnet mask/network name].(255)[host] sir IP 
->192.168.10.(283)[host] my IP  
# it can not connect easily router is required

# HOW TO CHECK CONNECTIVITY 

37.
>>ping 192.168.10.182[host] sir IP
if connected {timings showns}

>>ping 192.168.10.182[host] sir IP
if not connected then, 
{unreachable}

then press -> ctrl + d or ping 192.168.10.182 -c 4 #{to come out from the ping command} 















 














  

