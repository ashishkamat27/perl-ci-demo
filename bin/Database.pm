use strict;
use CGI;

my $cgi = new CGI;
print $cgi->header(-type => 'text/html');
$host = "localhost";
$database = "demo";
$tablename = "employee";
$user = "";
$pw = "";
# PERL DBI CONNECT()
$driver = "DBI:mysql:database=$database;host=$host";
$connect_me = DBI->connect($driver, $user, $pw);
# SELECT DB
$run_query = $connect_me->prepare("SELECT * FROM $tablename");
$run_query->execute();
#looping and displaying the resulet
while($result=$run_query->fetchrow_hashref()) {
  print "<b>Value returned:</b> $result->{time}\n";
}
print "<hr>";
$run_query->execute();
while(@result = $run_query->fetchrow_array()){
print "<b>Value returned:</b> $result[1]\n";
}
