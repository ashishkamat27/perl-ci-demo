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
print $cgi->start_form(-method => 'POST', -action => 'insertstud.cgi');
print "<br> Enter your Name: " .
	$cgi->textfield(-name => 'NAME', -value => '', -size => 25, -maxlength => 20) . "<br>";
print "<br> Enter Password" .
	$cgi->textfield(-name => 'PASS', -value => '', -size => 50, -maxlength => 50) . "<br>";
print "<br> Enter Email ID: " .
	$cgi->textfield(-name => 'EMAIL', -value => '', -size => 8, -maxlength => 5) . "<br>";
print "<br> Enter Address: " .
	$cgi->textfield(-name => 'ADDRESS', -value => '', -size => 8, -maxlength => 5) . "<br>";
print "<br><center>" . 
	$cgi->reset() . '  ' . $cgi->submit(-name => 'SUBMIT', -value => 'SUBMIT') . "</center><br>";
# end the form
print $cgi->end_form;
print "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
print "<a href='../index.html'>Back to Home</a>";
print $cgi->end_html;
