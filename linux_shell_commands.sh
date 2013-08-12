netstat -tanp

#http://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard ; FHS

#Concept of hard link vs soft link : http://www.ugrad.cs.ubc.ca/~cs219/CourseNotes/Unix/commands-links.html

#bash-3.2$ ls /bin |grep vi
##rvi
##rview
##vi
##view
#bash-3.2$ ls /sbin |grep vi
##service
#bash-3.2$ ls -l /sbin/|wc -l
##261
#bash-3.2$ ls -l /bin/|wc -l
##111

#vimdiff: http://amjith.blogspot.in/2008/08/quick-and-dirty-vimdiff-tutorial.html

#/bin vs /sbin vs /usr/bin
#http://linuxtroubleshoot.blogspot.in/2011/03/difference-between-bin-vs-sbin-vs.html
#/bin usable in single user mode, /sbin is bigger set but not usable on its own, needed for system admin


#linux link troubleshoot : http://linuxtroubleshoot.blogspot.in/
# concept single user mode : http://en.wikipedia.org/wiki/Single_user_mode
