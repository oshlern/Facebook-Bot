#!/usr/bin/perl
use BdData;

my @stat;
my $result;
my $why;

"@ARGV" =~ /\bname=(\w*)\b/;
my $name = $1;

sub pick {
	my $word = shift;
	my $selected = $bdata->{$word};
	push @stat,$word if $selected;
	return $selected->[rand(@$selected)] ;

}

my @candidates = grep {$_} map {pick $_} @ARGV;

if (@candidates) {
	$why = "the greeting is based on '".join(',',@stat)."'.";
} else {
	$why = "just a random greeting.";
	@candidates = (@candidates , @$_) for values $bdata;  
}

$result = $candidates[rand @candidates];

$result = "$name, \l$result" if $name;
print qq|"result":"$result",\n"reason":$why"\n|;

#print @candidates,"\n";
#print @stat,"\n";





