use strict;
use warnings;
use Test::More qw(no_plan);
use FindBin;
use lib File::Spec->catdir($FindBin::Bin, '..', 'lib');
use My::Employee;



# Test case for empid
my $d = My::Employee->new(id => 13485, name=>"Ashish Kamat", department =>"Engineering");
my $empid=$d->id(11016);
is($empid,11016,"Correct");
# Test case for empname
my $empname=$d->name("Dipika J");
is($empname,"Dipika J","Correct");
# Test case for department
my $year=$d->department("ALM");
is($year,"ALM","Correct");
