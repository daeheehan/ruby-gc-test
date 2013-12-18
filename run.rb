(1..15).each do |i|
	system("python useless.py #{i * 2000000}")
	system("ruby useless.rb #{i * 2000000}")
end