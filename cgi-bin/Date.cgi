#!/usr/bin/perl -w
use strict;
use CGI;

my $cgi = new CGI;
print $cgi->header(-type => 'text/html');
print $cgi->start_html(-title => 'Enter Date');
print '<center>' . $cgi->h1('Enter Date') . '</center>';
# start the form
print $cgi->start_form(-method => 'POST', -action => 'Datedetails.cgi');
print "<br> Enter Day(1-30): " .
	$cgi->textfield(-name => 'DATE', -value => '', -size => 25, -maxlength => 20) . "<br>";
print "<br> Enter Month(1-12): " .
	$cgi->textfield(-name => 'MONTH', -value => '', -size => 50, -maxlength => 50) . "<br>";
print "<br> Enter Year(4 digit): " .
	$cgi->textfield(-name => 'YEAR', -value => '', -size => 8, -maxlength => 5) . "<br>";
print "<br><center>" . 
	$cgi->reset() . '  ' . $cgi->submit(-name => 'SUBMIT', -value => 'SUBMIT') . "</center><br>";
# end the form
print $cgi->end_form;
print "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
print "<a href='../index.html'>Back to Home</a>";
print $cgi->end_html;
