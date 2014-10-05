#!/bin/sh

learn() {
	rm -rf temporary.*
	cp spanish.foma temporary.spanish.foma
	echo "\n\nsave stack spanish.bin\nexit" >> temporary.spanish.foma
	./foma/foma -l temporary.spanish.foma

	cat data/spanish.txt.learn | awk '{print $1}' | ./foma/flookup spanish.bin > temporary.prediction.raw.result
	cat temporary.prediction.raw.result | grep -o "\(^[^+]*\(+X\|\)+[VNA]\)\|\(^[^?]*?$\)" | uniq > temporary.prediction.result

	cat temporary.prediction.result | python py/cut_lemmas.py > temporary.final.cutted.result

	python py/evaluate.py data/spanish.txt.learn temporary.final.cutted.result
}

control() {
	rm -Rf temporary.*
	cp spanish.foma temporary.spanish.foma
	echo "\n\nsave stack spanish.bin\nexit" >> temporary.spanish.foma
	./foma/foma -l temporary.spanish.foma

	cat data/spanish.txt.test.clean | ./foma/flookup spanish.bin > temporary.prediction.raw.result
	cat temporary.prediction.raw.result | grep -o "\(^[^+]*\(+X\|\)+[VNA]\)\|\(^[^?]*?$\)" | uniq > temporary.prediction.result
		
	cat temporary.prediction.result | python py/cut_lemmas.py > temporary.final.cutted.result

	iconv -f utf-8 -t ISO8859-1 temporary.final.cutted.result > temporary.final.result.latin1
}

#control
learn 
