#!/usr/bin/python

import codecs
import re
import sys

def from_stdin():
    iterable = codecs.getreader('utf-8')(sys.stdin)
    for item in iterable:
        yield item.rstrip('\r\n').encode('utf-8')

def runShortestNoun(lemmas):
	newLemmas = []
	shortestNoun = ''
	for lemma in lemmas:
		if lemma[-1] == 'N':
			if shortestNoun == '' or len(shortestNoun) > len(lemma):
				shortestNoun = lemma
			continue
		newLemmas.append(lemma)

	if shortestNoun != '':
		newLemmas.append(shortestNoun)

	return newLemmas

def runAdjectiveKill(lemmas):
	newLemmas = []
	for lemma in lemmas:
		if lemma[-1] == 'A':
			continue
		newLemmas.append(lemma)
	return newLemmas

def run1CWins(lemmas):
	for lemma in lemmas:
		if lemma[-1] == 'V' and lemma[-4] == 'a':
			return [lemma]
		
	return lemmas

def runXClear(lemmas):
	newLemmas = []
	hasX = False
	for lemma in lemmas:
		parts = lemma.split('+')
		word = parts[0]
		if len(parts) > 2:
			newLemmas.append(word + '+' + parts[2])
		else:
			newLemmas.append(lemma)

	return newLemmas	

def runXCut(lemmas):
	newLemmas = []
	hasX = False
	for lemma in lemmas:
		parts = lemma.split('+')
		word = parts[0]
		if len(parts) > 2:
			newLemmas.append(word + '+' + parts[2])
			hasX = True

	if hasX:
		return newLemmas
	else:
		return lemmas


def analizeWordLemmas(word, lemmas):
	lemmas = runXCut(lemmas)
	# lemmas = runAdjectiveKill(lemmas)
	# lemmas = run1CWins(lemmas)
	lemmas = runShortestNoun(lemmas)
	printWordLemmas(word, lemmas)

def printWordLemmas(word, lemmas):
  flag = []
  i = 0
  N = 0
  V = 0
  A = 0
  for lemma in lemmas:
    if "+N" in lemma:
      flag.append("+N")
      N = i
    if "+V" in lemma:
      flag.append("+V")
      V = i
    if "+A" in lemma:
      flag.append("+A")
      A = i
    i += 1

  if "+V" in flag and "+N" in flag:
    lemmas = [lemmas[V]]

  elif "+N" in flag and "+A" in flag:
    lemmas = [lemmas[A]]

  print str(word) + '\t' + '\t'.join(lemmas)

firstWordMode = True
tempWord = ''
tempLemmas = []
for line in from_stdin():
	words   = line.split('\t')
	newWord = words[0]
	lemma   = words[1]

	if firstWordMode:
		tempWord = newWord
		firstWordMode = False

	if newWord == tempWord:
		tempLemmas.append(lemma)
	else:
		analizeWordLemmas(tempWord, tempLemmas)
		tempWord   = newWord
		tempLemmas = [lemma]


if tempWord != '':
	analizeWordLemmas(tempWord, tempLemmas)
