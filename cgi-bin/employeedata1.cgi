#!/usr/bin/perl -w
use strict;
use CGI;

# employeedata1.cgi
# display employee details by accessing each param directly

my $cgi = new CGI;
print $cgi->header(-type => 'text/html');
print $cgi->start_html(-title => 'Employee Data');
print "<center>";
print $cgi->h1('Employee Data');

# get the submitted form's data
my $employeedid = $cgi->param('EMPID');
my $employeename = $cgi->param('EMPNAME');
my $departmentid = $cgi->param('DEPTID');

# display the employee details in a table
print "<table border=1>";
print "<tr><th colspan=2>Employee Data</th></tr>";
print "<tr><th>Employee ID</th><td>" . $employeedid . "</td></tr>";
print "<tr><th>Employee Name</th><td>" . $employeename . "</td></tr>";
print "<tr><th>Department ID</th><td>" . $departmentid . "</td></tr>";
print "</table></center>";
print "<a href='employeedetails1.cgi'>Back to Employee Details</a>";
print "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
print "<a href='../index.html'>Back to Home</a>";
print $cgi->end_html;
