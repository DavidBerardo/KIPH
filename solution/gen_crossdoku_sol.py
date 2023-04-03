import numpy as np 


#sol = ['odnpastyi','pyintoads','astidynop','itdynapso','noadspity','spyoitdna','disaonypt','tapsydoin','ynotpisad']
#clues = [0,1,0,0,0,0,1,0,1,
#		 1,0,1,0,0,0,1,0,0,
#		 0,0,0,0,0,1,0,1,0,
#		 0,0,1,0,1,0,0,0,0,
#		 0,0,0,0,0,1,0,0,0,
#		 1,0,0,0,0,0,1,0,0,
#		 0,0,0,0,0,0,0,0,0,
#		 1,0,1,0,0,0,0,0,0,
#		 0,1,0,0,1,0,0,0,0]
#highlights = [5,9*2+2,9*6+3,9*7+8]
#cross_sol = [0,0,0,0,0,0,0,0,0,
#			 0,1,0,1,1,1,0,1,1,
#			 1,1,0,0,0,0,0,0,1,
#			 1,1,0,0,0,1,1,1,0,
#			 1,1,1,0,0,0,1,1,1,
#			 0,1,1,0,0,0,0,1,1,
#			 0,1,1,0,0,0,0,0,0,
#			 0,1,0,1,1,0,0,0,0,
#			 0,0,1,1,0,1,1,1,0]

sol = ['dnhocteal','eaoldnthc','ctlheadno','acenthold','todalench','hlncodate','ldteachon','ohadnlcet','nectholda']
clues = [1,0,1,0,0,1,0,0,0,
		 0,0,0,0,0,0,0,0,1,
		 0,0,0,1,0,0,1,0,0,
		 0,1,0,0,0,0,1,0,0,
		 0,0,0,1,0,0,0,0,0,
		 0,0,0,1,0,0,0,1,1,
		 1,0,0,1,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,0,
		 0,1,0,0,0,0,0,0,0]

highlights = [1*9+3,7*9+2,7*9+4,8*9+7]

cross_sol = [0,0,0,0,0,0,1,1,1,
			 1,0,1,0,0,0,0,0,0,
			 1,0,1,0,1,1,0,0,1,
			 1,0,1,1,1,0,0,1,1,
			 1,1,0,0,1,1,1,0,0,
			 1,1,0,0,1,1,1,0,0,
			 0,1,1,0,1,1,1,1,1,
			 1,0,0,0,0,0,0,1,1,
			 1,0,1,1,0,0,0,0,0]


first_cross_sol = [0,0,0,0,0,0,0,0,0,
				   0,1,0,1,1,1,0,0,1,
				   1,1,0,0,0,0,0,0,1,
				   1,1,0,0,0,1,0,1,0,
				   1,1,1,0,0,0,0,1,0,
				   0,1,1,0,0,0,0,0,0,
				   0,1,1,0,0,0,0,0,0,
				   0,1,0,1,1,0,0,0,0,
				   0,0,1,1,0,1,1,1,0]


clue_count = 1

'''
#first step version
for i in range(9):
	print('<tr>')
	for j in range(9):
		outline = '<td '
	
		letter = sol[i][j].upper()
		clue = clues[9*i+j]
		highlight = 9*i+j in highlights	

		if clue:
			outline += 'class="sol_clue" '
		elif highlight:
			outline += 'class="highlight" '
		outline += '>'

		outline += '<div class="sol"'
		if first_cross_sol[9*i+j]:
			outline += 'style="background-color: #57ebe8"'
		outline += '>'

		if first_cross_sol[9*i+j] or clue:
			outline += f'<span class="sol">{letter}</span>'

		if clue:
			outline += f''
			outline += f'<span class="clue">{clue_count}</span>'
			clue_count += 1

		outline += '</div></td>'
		print(outline)
	print('</tr>')


'''


for i in range(9):
	print('<tr>')
	for j in range(9):
		outline = '<td '

		letter = sol[i][j].upper()
		clue = clues[9*i+j]
		highlight = (9*i+j) in highlights

		if clue:
			outline += 'class="sol_clue" '
		elif highlight:
			outline += 'class="highlight" '

		style = ''
		if j in [2,5]:
			style += "border-right:5px solid black;"
		if i in [2,5]:
			style += "border-bottom:5px solid black"

		if len(style) > 0:
			outline += f'style="{style}"'
		outline += '>'

		outline += '<div class="sol"'
		if cross_sol[9*i+j]:
			outline += 'style="background-color: #57ebe8"'
		outline += '>'

		outline += f'<span class="sol">{letter}</span>'

		if clue:
			outline += f''
			outline += f'<span class="clue">{clue_count}</span>'
			clue_count += 1

		outline += '</div></td>'
		print(outline)
	print('</tr>')


