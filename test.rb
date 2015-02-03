
def nTimes(athing)
  return proc {|n| puts athing * n}
end

p1 = nTimes(23)
p1.call(3)

p2 = nTimes("Hello")
p2.call(3)

50.step(80,5) {|i| print i, ''}

alias oldBackquote `
def `(cmd)
  result =  oldBackquote(cmd)
  if $? != 0
    raise "Command #{cmd} failed"
  end
  result
end

print `date`
print `data`
