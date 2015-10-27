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
my $employeedid = $cgi->param('EMPID');
my $employeename = $cgi->param('EMPNAME');
my $departmentid = $cgi->param('DEPTID');
my $dbh = DBI->connect($dsn, $userid, $password ) or die $DBI::errstr;
my $sth = $dbh->prepare("INSERT INTO EMPLOYEE
                      (EMPID, EMPNAME, DEPARTMENT )
                      values (?,?,? )");
      $sth->execute($employeedid,$employeename,$departmentid);
$dbh->commit;
print "content-type: text/html\n\n";
#print  $departmentid, $employeedid,  $employeename;
print '<html><head><title>Basic CGI</title><head><body>';

print '<h3> 1 record inserted</h3>';


print '<a href="showemployee.cgi">Show Employees</a><br/>';
print "<a href='employeedetails1.cgi'>Add New </a><br/>";
print '</body></html>';
