#!/usr/bin/perl -w
use strict;
use CGI;

# employeedetails1.cgi
# display a page to enter employee details

my $cgi = new CGI;
print $cgi->header(-type => 'text/html');
print $cgi->start_html(-title => 'Employee Details');
print '<center>' . $cgi->h1('Student Details') . '</center>';

# start the form
print $cgi->start_form(-method => 'POST', -action => 'deleteemployee1.cgi');
print "<br> Enter  Employee ID To delete: " .
	$cgi->textfield(-name => 'EMPID', -value => '', -size => 25, -maxlength => 20) . "<br>";
	
print "<br><center>" . 
	$cgi->reset() . '  ' . $cgi->submit(-name => 'SUBMIT', -value => 'SUBMIT') . "</center><br>";
# end the form
print $cgi->end_form;
print $cgi->end_html;
