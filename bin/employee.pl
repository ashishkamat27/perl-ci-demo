use strict;
use warnings;
use 5.010;
 
use FindBin;
use File::Spec;
use lib File::Spec->catdir($FindBin::Bin, '..', 'lib');
use My::Employee;
 
my $d = My::Employee->new(id => 1, name =>"Ashish Kamat", department =>"ALM");
say $d;
say $d->id;
say $d->name;
say $d->department;
 
say '';
say $d->id(13485);
say $d->id;
 
say '';
say $d->name("Ashish K");
say $d->name;
 
say '';
say $d->department("ALM");
say $d->department;