use strict;
use warnings;
use Test::More qw(no_plan);
use FindBin;
use lib File::Spec->catdir($FindBin::Bin, '..', 'lib');
use My::Date;

# Test case for day
my $d = My::Date->new(year => 2013, month => 1, day => 27);
my $day=$d->day(23);
is($day,23,"Correct");
# Test case for month
my $month=$d->month(7);
is($month,7,"Correct");
# Test case for year
my $year=$d->year(2014);
is($year,2014,"Correct");
