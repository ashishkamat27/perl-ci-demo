#!/usr/bin/perl -w
use DBI;
use strict;
use CGI;
 use CGI::Carp 'fatalsToBrowser';
my $driver = "mysql"; 
my $database = "perl_ci_db";
my $dsn = "DBI:$driver:database=$database";
my $userid = "root";
my $password = "";
my $cgi = new CGI;

# output the content-type so the web server knows
my $empid = $cgi->param('EMPID');
my $dbh = DBI->connect($dsn,$userid, $password ) or die $DBI::errstr;
my $sth = $dbh->prepare("DELETE  FROM Employee
                        WHERE  EMPID = ?");
$sth->execute( $empid ) or die $DBI::errstr;
print "Number of rows deleted :" + $sth->rows;
$sth->finish();
$dbh->commit or die $DBI::errstr;

$dbh->commit;
print "content-type: text/html\n\n";
print '<html><head><title>Basic CGI</title><head><body>';
 print $sth->rows;
if ($sth->rows==1)
{
print '<h3> 1 record deleted</h3>';
}
else 
{ print '<h3 color="red"> Error</h3>';}

print '<a href="showemployee.cgi">Show Employees</a>';
print '</body></html>';
