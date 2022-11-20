# focus

A command line tool to help you focus on your tasks with the help of voice sessions.


To run this:
	`python3 src/focus.py <duration in minutes> <task to finish in the duration>`

eg:
		`python3 src/focus.py 30 prepare_for_entrance`

{note that the while task will be one single arguent. So, seperate the words by underscore ('_'), not with spaces. }



the date and work you do will be written in a file called focus_logs.txt.
	Sun Nov 13 07:02:26 2022 ~ 13.1 minutes => prepared for entrance 

plus: I have attached a quote to remind myself to work if I entered 'n' at the end. This might feel little cringy but F-it.



# waste

This will help you limit the time you spend on useless things.
	`python3 src/waste.py <duration in minutes> <task to finish in the duration>`

eg:
		`python3 src/waste.py 30 watch_cat_videos`
		
// after 30 minutes, it will automatically close your browser or any currently maximized window.
