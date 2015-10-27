#!/usr/bin/perl -w
use DBI;
use strict;

my $driver = "mysql"; 
my $database = "perl_ci_db";
my $dsn = "DBI:$driver:database=$database";
my $userid = "root";
my $password = "";
 use CGI::Carp 'fatalsToBrowser';
# output the content-type so the web server knows

my $dbh = DBI->connect($dsn, $userid, $password ) or die $DBI::errstr;
print "content-type: text/html\n\n";
print '<html><head><title>Basic CGI</title><head><body>';

#
# you should change the connect method call to use the DBD you are
# using. The following examples all use DBD::ODBC and hence the
# first argument to the connect method is 'dbi:ODBC:DSN'.
#
my $sql = q/select empname, department from Employee/;
my $sth = $dbh->prepare($sql);
$sth->execute;
print '<table border="1">';

# table headings are SQL column names

print "<tr><th>Emp name</th><th>Department</th></tr>";
while (my @row = $sth->fetchrow_array) {
    print "<tr><td>$row[0]</td><td>$row[1]</td></tr>\n";
}
print "</table>\n";
print "<a href='employeedetails1.cgi'>Add New </a>";
print "<a href='deleteemployee.cgi'>Delete Employee</a>";

print "</body></html>\n";
