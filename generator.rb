File.open('strings.txt', 'w') do |f|
	alphabets = ('A'..'Z').to_a
	50000000.times do
		f.write "#{(0..32).map { alphabets.sample }.join}\n"
	end
end