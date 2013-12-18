require 'benchmark'

i = ARGV[0]

puts "Ruby, number of elements : #{i}"

elements = []
alphabets = ('A'..'Z').to_a

(i).to_i.times do
	elements << (0..32).map { alphabets.sample }.join
end

puts(Benchmark.measure { elements.sort! })
puts GC.stat
