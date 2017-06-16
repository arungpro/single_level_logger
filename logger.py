__author__ = 'Arun G'

import datetime

class Logger:
	def __init__(self, name = 'Error', log_file = 'error.log'):
		self.type = name
		self.file = log_file

	def log(self, log_str):
		"""
			Log method is intended to create log entries
			Input: It takes the log string as input to amend to log file
				of the type
			Output: Nothing
		"""
		date_time = '{:%d:%m:%Y::%H:%M:%S}'.format(datetime.datetime.now())
		content = '{0} {1} {2}\n'.format(date_time, self.type, log_str)

		f = open(self.file, 'w')
		f.write(content)
		f.close()

	def get(self, search_str, above = 2, below = 2):
		"""
			Get method display to stack trace of the search string from
				the log
			Input: It takes searching string and configurable upper and
				lower bound to the match line
			Output: Displays the log line with given number of line outer
				lines
		"""
		log_file = open(self.file, 'r')
		above_list = [ ]
		matched_line = ''
		below_list = [ ]

		for line in log_file:
			if not matched_line:
				if len(above_list) == above:
					if search_str in line:
						matched_line = line
						continue
					else:
						above_list.insert(0, line)
						above_list.pop()

				if len(above_list) < above:
					if search_str in line:
						matched_line = line
						continue
					else:
						above_list.insert(0, line)
			else:
				if len(below_list) == below:
					break
				else:
					below_list.insert(0, line)

		self.display(above_list, matched_line, below_list)

	def display(self, above_list, matched_line, below_list):
		for l in reversed(above_list):
			print l

		print matched_line

		for l in reversed(below_list):
			print l

if __name__ == '__main__':
	logger = Logger('Error', 'error.log')
	logger.get('offer', 1, 1)
	# logger.get('docker-compose', 1, 2)
	# logger.get('generated_recommender_SellerAnalyticsService', 1, 1)
