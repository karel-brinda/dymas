#! /usr/bin/env perl -w

use strict;
use warnings;

while (<>) {
	my @t = split("\t");
	my $line=$_;

	my $coverage= int($t[3]);
	next if ($coverage==0);

	my $bases = $t[4];
	next if ($bases =~ /^(\.|,|\^.|\$)*$/);
	print $line;
}

