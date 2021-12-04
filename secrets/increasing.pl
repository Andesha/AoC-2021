#!/usr/bin/env perl
use strict;
use warnings;

my @array;
open(my $fh, "<", "test_input.txt")
    or die "Failed to open file: $!\n";
while(<$fh>) { 
    chomp; 
    push @array, $_;
} 
close $fh;

my $count = 0;
my $current = $array[0];
for my $i (1 .. $#array) {
    if($array[$i] > $current){
        ++$count;
    }
    $current = $array[$i];
}
print($count);
