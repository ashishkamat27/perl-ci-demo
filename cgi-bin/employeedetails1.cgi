#!/usr/bin/perl -w
use strict;
use CGI;

# employeedetails1.cgi
# display a page to enter employee details

my $cgi = new CGI;
print $cgi->header(-type => 'text/html');
print $cgi->start_html(-title => 'Employee Details');
print '<center>' . $cgi->h1('Employee Details') . '</center>';

# start the form
print $cgi->start_form(-method => 'POST', -action => 'insertemployee.cgi');
print "<br> Enter your Employee ID: " .
	$cgi->textfield(-name => 'EMPID', -value => '', -size => 25, -maxlength => 20) . "<br>";
print "<br> Enter your Name: " .
	$cgi->textfield(-name => 'EMPNAME', -value => '', -size => 50, -maxlength => 50) . "<br>";
print "<br> Enter your Department ID: " .
	$cgi->textfield(-name => 'DEPTID', -value => '', -size => 8, -maxlength => 5) . "<br>";
print "<br><center>" . 
	$cgi->reset() . '  ' . $cgi->submit(-name => 'SUBMIT', -value => 'SUBMIT') . "</center><br>";
# end the form
print $cgi->end_form;
print "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
print "<a href='../index.html'>Back to Home</a>";
print $cgi->end_html;
