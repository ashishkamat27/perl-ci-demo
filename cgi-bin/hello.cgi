#!/usr/bin/perl -w
use DBI;
use strict;

use CGI::Carp 'fatalsToBrowser';
print "content-type: text/html\n\n";
print '<html><head><title>Basic CGI</title><head><body>';
print '<h1> Hello World</h1>';
print "</body></html>\n";
