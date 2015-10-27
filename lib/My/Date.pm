#!/usr/bin/perl -w
package My::Date;
use strict;
use warnings;
 
sub new {
    my ($class, %args) = @_;
    return bless \%args, $class;
}
 
sub year {
    my ($self, $value) = @_;
    if (@_ == 2) {
        $self->{year} = $value;
    }
    return $self->{year};
}
 
sub month {
    if (@_ == 2) {
        $_[0]->{month} = $_[1];
    }
    return $_[0]->{month};
}
 
sub day {
    return $_[0]->{day} = @_ == 2 ? $_[1] : $_[0]->{day};
}

1;
