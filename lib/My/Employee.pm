#!/usr/bin/perl -w
package My::Employee;
use strict;
use warnings;
 
sub new {
    my ($class, %args) = @_;
    return bless \%args, $class;
}
 
sub  id {
    my ($self, $value) = @_;
    if (@_ == 2) {
        $self->{id} = $value;
    }
    return $self->{id};
}
 
sub name {
     my ($self, $value) = @_;
    if (@_ == 2 ) {
        $self->{name} = $_[1];
    }
    return $self->{name};
}
 
sub department {
  my ($self, $value) = @_;
    if (@_ == 2 ) {
        $self->{department} = $_[1];
    }
    return $self->{department};
}

1;
