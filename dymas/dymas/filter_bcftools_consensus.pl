#! /usr/bin/env perl

use strict;
use warnings;

while (<>) {
	if (/^\#/){
		print $_;
		next;
	}

	my $line=$_;
	my @t = split("\t");
	next if ($t[4] eq ".");
	print $line;
}
