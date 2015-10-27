#!/usr/bin/perl -w
use strict;
use 5.010;
use FindBin;
use File::Spec;
use lib File::Spec->catdir($FindBin::Bin, '..', 'lib');
use My::Date;
use CGI;
 use CGI::Carp 'fatalsToBrowser';
my $cgi = new CGI;
print $cgi->header(-type => 'text/html');
print $cgi->start_html(-title => 'Date Data');
print "<center>";
print $cgi->h1('Date Data');

# get the submitted form's data
my $day = $cgi->param('DATE');
my $month = $cgi->param('MONTH');
my $year = $cgi->param('YEAR');
#print header();
#print "$day\n$month\n$year";
my $d = My::Date->new(year => $year, month => $month, day =>$day);

print "<div id='section'></div>";
print "<table border=1>";
print "<tr><th colspan=2>Date Data</th></tr>";
print "<tr><th>Day</th><td>" . $d->day . "</td></tr>";
print "<tr><th>Month</th><td>" . $d->month. "</td></tr>";
print "<tr><th>Year</th><td>" . $d->year. "</td></tr>";
print "</table></center>";
print "<a href='Date.cgi'>Back to Date</a>";
print "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
print "<a href='../index.html'>Back to Home</a>";
print $cgi->end_html;
