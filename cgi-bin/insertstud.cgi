#!/usr/bin/perl -w
use DBI;
use strict;
use CGI;
 use CGI::Carp 'fatalsToBrowser';
my $host='172.27.59.54';
my $driver = "mysql"; 
my $database = "ecomm";
my $dsn = "DBI:mysql:database=$database:host=$host";
my $userid = "ecomm";
my $password = 'ecomm@123';
my $cgi = new CGI;

# output the content-type so the web server knows
my $name = $cgi->param('NAME');
my $pass = $cgi->param('PASS');
my $email = $cgi->param('EMAIL');
my $address= $cgi->param('ADDRESS');
my $dbh = DBI->connect($dsn,$userid, $password ) or die $DBI::errstr;
my $sth = $dbh->prepare("INSERT INTO regiStud
                      (NAME, PASS, EMAIL,ADDRS )
                      values (?,?,?,?)");
      $sth->execute($name,$pass,$email,$address);
$dbh->commit;
print "content-type: text/html\n\n";
print  $name,$pass,$email,$address;
print '<html><head><title>Basic CGI</title><head><body>';

print '<h3> 1 record inserted</h3>';


print '<a href="showemployee.cgi">Show Employees</a>';
print '</body></html>';
