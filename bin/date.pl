use strict;
use warnings;
use 5.010;
 
use FindBin;
use File::Spec;
use lib File::Spec->catdir($FindBin::Bin, '..', 'lib');
use My::Date;
 
my $d = My::Date->new(year => 2013, month => 1, day => 27);
say $d;
say $d->year;
say $d->month;
say $d->day;
 
say '';
say $d->year(1001);
say $d->year;
 
say '';
say $d->month(12);
say $d->month;
 
say '';
say $d->day(9);
say $d->day;