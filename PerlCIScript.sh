#!/bin/bash

#export PERL5LIB=/root/.cpan/build/strictures-1.005006-Jw93lo/blib/lib
#perl -v
#cd /var/lib/jenkins/jobs/Perl-CI/workspace/
#chmod +x Build.PL

perl Build.pl

perl Build manifest

./Build test
./Build testcover

cover -report clover

perlcritic -4 . > perlcritic.txt

prove -r --timer --formatter=TAP::Formatter::JUnit -l t > test_results.xml

prereq-grapher -depth 2 TAP::Formatter::JUnit
dot -Tpng dependencies.dot > dependencies1.png

prereq-grapher -depth 2 Module::Path
dot -Tpng dependencies.dot > dependencies2.png

doxygen Doxyfile
