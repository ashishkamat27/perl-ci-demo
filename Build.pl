use strict;
use warnings;
use Module::Build;

my $builder = Module::Build->new(
    module_name         => 'My::Date',
    license             => 'perl',
    dist_abstract       => 'Date short description',
    dist_author         => 'Dipika Joshi <dipikaj@cybage.com>',
    build_requires => {
        'Test::More' => '0.10',
	'Devel::Cover'=> '1.09',
    },
);

$builder->create_build_script();

my $builder1 = Module::Build->new(
    module_name         => 'My::Employee',
    license             => 'perl',
    dist_abstract       => 'Employee short description',
    dist_author         => 'Dipika Joshi <dipikaj@cybage.com>',
    build_requires => {
        'Test::More' => '0.10',
	'Devel::Cover'=> '1.09',
    },
);

$builder1->create_build_script();
