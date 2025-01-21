import snscrape.modules.twitter as sntwitter
import pandas as pd
import numpy as np
import requests
import re
import platform
import subprocess
import webbrowser
import html2text
import concurrent.futures
import redis
import json
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import END
from tkhtmlview import HTMLScrolledText
import mistune

from github import Github
from datetime import datetime, timedelta

import cv2
import datetime, time
from PIL import (
	Image,
	ImageColor,
	ImageDraw,
	ImageFilter,
	ImageFont,
	ImageSequence,
)


from schnell.app.speechutils import speak, angka, denger
from schnell.app.executor import FileExecutor
from schnell.app.envutils import env_get
from schnell.app.dirutils import isfile, filetemppath, suffix_filename, normy
from schnell.app.cryptoutils import encrypt_image, encrypt_text, encrypt_video, decrypt_image, decrypt_text, decrypt_video
# from app.mediautils import capture_gambar #, getxy
from schnell.app.screencapture import ScreenCapture
from schnell.app.autoutils import prompt
from schnell.app.imageutils import show_image_cv
from schnell.app.utils import trycopy
from schnell.app.fileutils import (
	file_append,
	file_remove,
)
from schnell.app.redisquiutils import redis_publish_image


def read_paragraph(bariskalimat):
	"""
	ctrl alt h
	"""
	speak(bariskalimat)


def execute_code(bariskalimat, language='python'):
	"""
	harus bisa: python, typescript, go
	ctrl alt p
	ctrl alt t
	ctrl alt g
	"""
	FileExecutor().execute(language=language, content=bariskalimat)


def process_twitter(bariskalimat, insert2editor_or_yellownote, num_tweets=9999):
	"""
	ctrl shift t
	ctrl alt w
	"""
	# perform the search using snscrape
	scrape_result  = sntwitter.TwitterSearchScraper(bariskalimat)
	tweets = []
	for i, tweet in enumerate(scrape_result.get_items(), 1):
		if i > num_tweets:
			break

		tweet_url = f"https://twitter.com/{tweet.user.username}/status/{tweet.id}"
		item = f'''{i}. [{tweet.user.displayname}, {tweet.user.username}, {tweet.date.strftime('%Y-%m-%d %H:%M:%S')}, {tweet_url}]\n{tweet.rawContent}'''
		# print(f"{i+1}. [{tweet.user.displayname}, {tweet.user.username}] => {tweet.content} ({tweet.date.strftime('%Y-%m-%d %H:%M:%S')}, {tweet_url})\n")
		tweets.append(item)

	# # print the tweets with counter
	# for i, tweet in enumerate(tweets, start=1):
	#     print(f"{i}. {tweet.content}")
	result = '\n\n'.join(tweets)
	insert2editor_or_yellownote(result)


def kemarin(hari):
	return datetime.now() - timedelta(days=hari)


the_g = Github(env_get("ULIBPY_GITHUB_TOKEN"))


def fetch_commit_data(commit_url):
	response = requests.get(commit_url)
	jsondata = response.json()
	print(f'fetch_commit_data {commit_url} => {jsondata}.')
	return jsondata


def fetch_file_data(file_url):
	response = requests.get(file_url)
	jsondata = response.json()
	# print(f'fetch_file_data {file_url} => {jsondata}.') # ini isi file, besar...
	kembalian = {
		'message': jsondata['commit']['message'],
		'author': jsondata['commit']['author']['name'],
		'email': jsondata['commit']['author']['email'],
		'date': jsondata['commit']['author']['date'],
		'url': jsondata['html_url'],
		'stats': f"{jsondata['stats']['total']} = +{jsondata['stats']['additions']} -{jsondata['stats']['deletions']}",
		'files': jsondata['files'],
	}
	return kembalian


def friendly_date(datestr):
	# April 10, 2023 09:50 AM
	return datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%SZ').strftime('%B %d, %Y %I:%M %p')


def get_date_range(date_string):
	# Split the date string into start and end date components
	start_date_str, end_date_str = date_string.split('|')

	# Convert the start and end date components to datetime objects
	start_date = datetime.strptime(f'{start_date_str}', '%Y,%m,%d')
	end_date = datetime.strptime(f'{end_date_str}', '%Y,%m,%d')

	# Set the start and end times to midnight UTC on January 1st and April 1st
	start_time = datetime.strptime('00:00:00Z', '%H:%M:%SZ').time()
	end_time = datetime.strptime('00:00:00Z', '%H:%M:%SZ').time()
	start_date_time = datetime.combine(start_date, start_time)
	end_date_time = datetime.combine(end_date, end_time)

	# Return a tuple containing the start and end datetime objects
	return (start_date_time, end_date_time)

# date_range = '2023,1,1|2023,4,1'
# start_date_time, end_date_time = get_date_range(date_range)
# print(start_date_time, end_date_time)

def get_commit_response(response):
	commit_data = response.json()
	if isinstance(commit_data,str) and 'API rate limit exceeded' in commit_data:
		return ''
	else:
		hasil = []
		# Create a ThreadPoolExecutor to parallelize the file fetches
		with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
			# Create a list of futures to hold the results of the file fetches
			futures = []
			for commit in commit_data:
				file_url = commit['url'] # + '/files'
				# Submit a file fetch job to the executor and add the future to the list
				futures.append(executor.submit(fetch_file_data, file_url))
			# Iterate over the futures and get the results
			for future in concurrent.futures.as_completed(futures):
				kembalian = future.result()
				files = kembalian['files']
				nama = kembalian['author']
				email = kembalian['email']
				stats = kembalian['stats']
				url = kembalian['url']
				tanggal = friendly_date(kembalian['date'])
				pesan = kembalian['message']
				filelist = [item['filename'] for item in files]
				fileliststr = ','.join(filelist)
				item = pesan + '\n' + f"{nama} | {email} | {tanggal}" + '\n' + url + '\n' + stats + f'\n[{fileliststr}]\n' + '-'*10
				hasil.append(item)
		return '\n'.join(hasil)


def get_commits_by_howmany(user_repo, how_many_commits=10):
	headers = {'Authorization': 'token put-your-token-here'}
	# Fetch the commit data from the GitHub API, including the access token in the headers
	batasi = f'?per_page={how_many_commits}'
	alamat = f'https://api.github.com/repos/{user_repo}/commits' + batasi
	response = requests.get(alamat, headers=headers)
	# response = requests.get('https://api.github.com/repos/ddiu8081/chatgpt-demo/commits')
	return get_commit_response(response)


def get_commits_by_daterange(user_repo, date_range_spec):
	headers = {'Authorization': 'token put-your-token-here'}
	start_date_time, end_date_time = get_date_range(date_range_spec)
	batasi = f'?since={start_date_time.isoformat()}&until={end_date_time.isoformat()}'
	alamat = f'https://api.github.com/repos/{user_repo}/commits' + batasi
	response = requests.get(alamat, headers=headers)
	# response = requests.get('https://api.github.com/repos/ddiu8081/chatgpt-demo/commits')
	return get_commit_response(response)


def process_github(bariskalimat, default_commit_days=7, default_jumlah_topics=100, default_jumlah_commits=10):
	"""
	default_commit_days = jumlah hari kemarin yang commitnya diambil dari hari ini
	ctrl alt g/h/b
	#topic
		#topic
		#topic|10
	user -> repos
		username
		username|10
	user/repo
		last 10 commits
			user/repo|10
		last 10 commits with commit files info
			user/repo|10f
		commit in last 10 days
			user/repo|10d
		commits between time x and y
			user/repo|x|y
			dari 1 jan 23 ke 1 april 23
				user/repo|2023,1,1|2023,4,1
		commit-specific
			show patch for file x
			user/repo|filename
			user/repo|filename1,filename2
	"""
	if bariskalimat.startswith('#'):
		print(f'[process_github] start#, topic handler -> [{bariskalimat}]')
		# #topic
		topik = bariskalimat.removeprefix('#')
		if '|' in bariskalimat:
			# specify jumlah repos yg ditampilkan
			pass
		else:
			# gunakan default jumlah utk topic
			url = 'https://api.github.com/search/repositories'
			params = {'q': topik}
			headers = {'Authorization': f'token {env_get("ULIBPY_GITHUB_TOKEN")}'}
			response = requests.get(url, params=params, headers=headers)
			data = response.json()
			result = []
			for idx,item in enumerate(data['items'], 1):
				#print(item['name'])
				name = item['name']
				url = item['html_url']
				last_update = item['updated_at']
				description = item['description'] or 'No description provided'
				# print(f"{name} | {url} | {last_update} | {description}")
				short_repo = "/".join(url.strip("/").split("/")[-2:])
				result.append(f"{idx}. {name} | {description} |{last_update}\n{short_repo}\n{url}")
			return '\n'.join(result)
	elif bariskalimat.count('/')==1:
		print(f'[process_github] count/ for commits, with | or not -> [{bariskalimat}]')
		# username/repo -> meminta commit
		if '|' in bariskalimat:
			# specify jumlah repos yg ditampilkan, bisa jumlah (jika jumlah berarti hitung dalam hari ke belakang) atau daterange
			if bariskalimat.count('|')==2: # jk minta date range, user/repo|start|end
				print(f'[process_github] count/ for commits, with |==2 or asking date range -> [{bariskalimat}]')
				# baiknya: user/repo|2023,1,1|2023,8,24
				# ddiu8081/chatgpt-demo|2023,4,1|2023,4,13 
				# yoheinakajima/babyagi|2023,4,10|2023,4,13 
				# lalu tekan ctrl+alt+g
				# bagaimana format utk startdate dan enddate...
				# kita bisanya 2023, 8, 24 utk hasilkan datetime(2023, 8, 24)
				# harus ada validasi
				# userrepo, startdate, enddate = bariskalimat.split('|')
				userrepo, date_range_spec = bariskalimat.split('|', 1)
				if ',' in date_range_spec:
					return get_commits_by_daterange(userrepo, date_range_spec)
			else: # satu | => either user/repo|10, user/repo|file, user/repo|file1,file2
				userrepo, params = bariskalimat.split('|')
				if ',' in bariskalimat: # user/repo|file1,file2
					files = params.split(',')
				elif params.isdigit(): # user/repo|10, get commits dalam hitungan hari ke belakang
					jumlah_komit = int(params)
					print(f'[process_github] count/ for commits, one | and isdigit -> jumlah komit = {jumlah_komit} -> [{bariskalimat}]')
					url = f'https://api.github.com/repos/{userrepo}'
					headers = {'Authorization': f'token {env_get("ULIBPY_GITHUB_TOKEN")}'}
					response = requests.get(url, headers=headers)
					data = response.json()
					print(f"""[process_github] {url}
					received data: {data}
					-----------------------------------
					""")
					repo_description = '(No desc)' if 'description' not in data else data['description']
					repo_url = data['html_url']
					commits_url = data['commits_url'].replace('{/sha}', '')
					commits_response = requests.get(commits_url, headers=headers)
					commits_data = commits_response.json()
					repo_num_commits = len(commits_data)

					repo_first_commit_date = data['created_at']
					repo_first_commit_timestamp = datetime.strptime(repo_first_commit_date, '%Y-%m-%dT%H:%M:%SZ')
					repo_first_commit_timestamp_str = repo_first_commit_timestamp.strftime('%A, %d %B %Y %I:%M %p')

					# Print the repository summary
					kembalian = []
					# print(f"Repository Summary")
					# print(f"===================")
					# print(f"Description: {repo_description}")
					# print(f"URL: {repo_url}")
					# print(f"Number of Commits: {repo_num_commits}")
					# print(f"Date/Time of First Commit: {repo_first_commit_timestamp_str}\n")
					kembalian.append(f"""Repository Summary"
					==================="
					Description: {repo_description}"
					URL: {repo_url}"
					Number of Commits: {repo_num_commits}"
					Date/Time of First Commit: {repo_first_commit_timestamp_str}
					""")

					url_for_commit = f'{url}/commits'
					response = requests.get(url_for_commit, headers=headers)
					data = response.json()
					counter = 1

					for commit in data[:jumlah_komit]:
						commit_hash = commit['sha']
						commit_url = commit['html_url']
						commit_message = commit['commit']['message']
						author_name = commit['commit']['author']['name']
						author_email = commit['commit']['author']['email']
						commit_date = commit['commit']['author']['date']
						commit_timestamp = datetime.strptime(commit_date, '%Y-%m-%dT%H:%M:%SZ')
						commit_timestamp_str = commit_timestamp.strftime('%A, %d %B %Y %I:%M %p')
						# utk dapatkan info files:
						# commit_files = requests.get(commit['url'] , headers=headers).json()['files']
						# list of item yg masing2 punya ['filename'] dan ['patch] (utk satu commit)
						# Print the commit details
						# print(f"{counter}. {commit_message}\n{commit_url} | {commit_timestamp_str}\n")
						kembalian.append(f"{counter}. {commit_message}\n{commit_url}\n{commit_timestamp_str}, {author_name}<{author_email}>, {commit_hash}\n")
						# Increment the counter
						counter += 1
					return '\n'.join(kembalian)
				elif re.match(r'\d+d', params): # user/repo|10d
					print(f'[process_github] count/ for commits, one 1 and format 10d => asking for jumlah days -> [{bariskalimat}]')
					jumlah_hari_kebelakang = int(params.removesuffix('d'))
					repo = the_g.get_repo(userrepo)
					commits = repo.get_commits(since=kemarin(jumlah_hari_kebelakang))
					# commits = repo.get_commits()
					result = []
					counter = 1
					for commit in commits:
						# print(f"{commit.sha} - {commit.commit.message} - {commit.commit.author.name}")
						result.append(f"{counter}. {commit.commit.author.name} <{commit.commit.author.email}> - {commit.commit.commiter.date} - {commit.commit.message} - {commit.sha}\n{commit.html_url}")
						counter += 1
					return '\n\n'.join(result)
				elif re.match(r'\d+f', params): # user/repo|10f
					# ini tampilkan file yg termodifikasi, juga link utk lihat patch (alih2 ngeprint patch di sini)
					jumlah_komit = int(params.removesuffix('f'))
					return get_commits_by_howmany(userrepo, jumlah_komit)
				else: # user/repo|filename
					filename = params
		else: # user/repo => kasihkan all commits
			print(f'[process_github] count/ for commits, with | or not => all commits -> [{bariskalimat}]')
			repo = the_g.get_repo(bariskalimat)
			# commits = repo.get_commits(since=kemarin(default_commit_days))
			commits = repo.get_commits()
			result = []
			counter = 1
			for commit in commits:
				# print(f"{commit.sha} - {commit.commit.message} - {commit.commit.author.name}")
				result.append(f"{counter}. {commit.commit.author.name} - {commit.commit.message} - {commit.commit.author.date} - {commit.sha}")
				counter += 1
			return '\n'.join(result)
	else:
		print(f'[process_github] only asking for repos -> [{bariskalimat}]')
		# username -> tampilkan semua repos
		if '|' in bariskalimat:
			# username|10 -> specify jumlah repos yg ditampilkan
			pass
		else:
			url = f'https://api.github.com/users/{bariskalimat}/repos?sort=updated'
			r = requests.get(url)
			# ['allow_forking',
			# 'archive_url',
			# 'archived',
			# 'assignees_url',
			# 'blobs_url',
			# 'branches_url',
			# 'clone_url',
			# 'collaborators_url',
			# 'comments_url',
			# 'commits_url',
			# 'compare_url',
			# 'contents_url',
			# 'contributors_url',
			# 'created_at',
			# 'default_branch',
			# 'deployments_url',
			# 'description',
			# 'disabled',
			# 'downloads_url',
			# 'events_url',
			# 'fork',
			# 'forks',
			# 'forks_count',
			# 'forks_url',
			# 'full_name',
			# 'git_commits_url',
			# 'git_refs_url',
			# 'git_tags_url',
			# 'git_url',
			# 'has_discussions',
			# 'has_downloads',
			# 'has_issues',
			# 'has_pages',
			# 'has_projects',
			# 'has_wiki',
			# 'homepage',
			# 'hooks_url',
			# 'html_url',
			# 'id',
			# 'is_template',
			# 'issue_comment_url',
			# 'issue_events_url',
			# 'issues_url',
			# 'keys_url',
			# 'labels_url',
			# 'language',
			# 'languages_url',
			# 'license',
			# 'merges_url',
			# 'milestones_url',
			# 'mirror_url',
			# 'name',
			# 'node_id',
			# 'notifications_url',
			# 'open_issues',
			# 'open_issues_count',
			# 'owner',
			# 'private',
			# 'pulls_url',
			# 'pushed_at',
			# 'releases_url',
			# 'size',
			# 'ssh_url',
			# 'stargazers_count',
			# 'stargazers_url',
			# 'statuses_url',
			# 'subscribers_url',
			# 'subscription_url',
			# 'svn_url',
			# 'tags_url',
			# 'teams_url',
			# 'topics',
			# 'trees_url',
			# 'updated_at',
			# 'url',
			# 'visibility',
			# 'watchers',
			# 'watchers_count',
			# 'web_commit_signoff_required']
			repolist = [item['html_url'] for item in r.json()]
			result = f'#Repos = {len(repolist)}\n'
			result += '\n'.join(repolist)
			return result
	return 'No.'


# Define a new class inheriting from the HTMLScrolledText
# class SelectableHTMLScrolledText(scrolledtext.ScrolledText):
# 	def __init__(self, *args, **kwargs):
# 		super().__init__(*args, **kwargs)
# 		# self.text.bind("<Control-a>", self.select_all)
# 		self.text_widget.bind("<Control-a>", self.select_all)

# 	def select_all(self, event):
# 		# self.text.tag_add(tk.SEL, "1.0", tk.END)
# 		self.text_widget.tag_add(tk.SEL, "1.0", tk.END)
# 		return "break"
# Define a new class inheriting from the HTMLScrolledText
class SelectableHTMLScrolledText(scrolledtext.ScrolledText):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.bind("<Control-a>", self.select_all)

	def select_all(self, event):
		self.tag_add(tk.SEL, "1.0", tk.END)
		return "break"
	
	# def set_markdown(self, markdown):
	# 	html = mistune.html(markdown)
	# 	self.set_html(html)
	def set_markdown(self, markdown):
		self.delete("1.0", tk.END)
		self.insert(tk.END, markdown)

	def set_html(self, html):
		self.delete("1.0", tk.END)
		self.insert(tk.END, html)

		# Add a hyperlink tag to enable clickable links
		self.tag_configure("hyperlink", foreground="blue", underline=True)
		self.tag_bind("hyperlink", "<Enter>", self._enter_hyperlink)
		self.tag_bind("hyperlink", "<Leave>", self._leave_hyperlink)
		self.tag_bind("hyperlink", "<Button-1>", self._click_hyperlink)

	def _enter_hyperlink(self, event):
		self.config(cursor="hand2")

	def _leave_hyperlink(self, event):
		self.config(cursor="")

	def _click_hyperlink(self, event):
		index = self.index(tk.CURRENT)
		tags = self.tag_names(index)
		if "hyperlink" in tags:
			url = self.get(index + " linestart", index + " lineend")
			webbrowser.open(url)

def zpt_redis_search(bariskalimat):
	"""
	"""
	# Connect to Redis
	redis_client = redis.Redis(host='localhost', port=6380, db=10)

	# Create a tkinter window
	root = tk.Tk()
	root.title("Redis Search")

	# Define a function to load and display a value from Redis in the text editor
	def load_value(key):
		# Get the value of the selected key
		value = redis_client.get(key)

		try:
			# Convert the value from JSON string to a Python dict
			value_dict = json.loads(value)
			# Set the text of the editor to the 'content' value
			#editor.delete(1.0, tk.END)
			#editor.insert(tk.END, value_dict['content'])
			markdown = value_dict['content']
			# copy juga ke clipboard
			trycopy(markdown)
			editor.set_html(mistune.html(markdown))
			# editor.set_markdown(markdown)
			# editor.set_markdown(html2text.html2text(markdown))

		except SyntaxError:
			# Handle the SyntaxError exception by printing a message and moving on to the next key
			print(f"Error parsing JSON for key {key}: unterminated string literal")
			editor.delete(1.0, tk.END)
			editor.insert(tk.END, f"Error parsing JSON for key {key}: unterminated string literal")

	# Define a function to search for keys in Redis and populate the listbox
	def search_redis(content=None):
		# Clear any existing items in the listbox
		listbox.delete(0, tk.END)

		# Get the search string from the search box
		if content:
			search_string = content
		else:
			search_string = search_box.get()

		# Iterate through all keys in the database
		for key in redis_client.scan_iter():
			# Get the value of the current key
			value = redis_client.get(key)

			try:
				# Convert the value from JSON string to a Python dict
				value_dict = json.loads(value)

				# Check if the 'content' value contains the search string
				if value_dict['content'] and search_string in value_dict['content']:
					# Add the key to the listbox
					listbox.insert(tk.END, key.decode('utf8'))

			except SyntaxError:
				# Handle the SyntaxError exception by printing a message and moving on to the next key
				print(f"Error parsing JSON for key {key}: unterminated string literal")

		# If there are no matching keys, display a message in the editor
		if listbox.size() == 0:
			editor.delete(1.0, tk.END)
			editor.insert(tk.END, "No matching keys found")

	# # Bind the listbox selection event to the load_value function
	# def on_select(event):
	# 	w = event.widget
	# 	if w.curselection():
	# 		index = int(w.curselection()[0])
	# 		key = w.get(index)
	# 		load_value(key)

	# Here, the on_select function is modified to accept an optional event argument, which is set to None by default. If the function is called without an argument (i.e., by the <<ListboxSelect>> event), it retrieves the widget from the event object. If the function is called with an argument (i.e., by the up or down arrow keys), it uses the listbox variable to retrieve the widget.

	def on_select(event=None):
		w = event.widget if event else listbox
		if w.curselection():
			index = int(w.curselection()[0])
			key = w.get(index)
			load_value(key)

	# Create a listbox on the left side of the window
	listbox_frame = ttk.Frame(root, padding=(10, 10, 10, 0))
	listbox_frame.pack(side="left", fill="y")

	listbox_label = ttk.Label(listbox_frame, text="Matching Keys")
	listbox_label.pack(side="top", fill="x")

	listbox = tk.Listbox(listbox_frame, selectmode="SINGLE")
	listbox.pack(side="left", fill="y", expand=True)

	listbox_scroll = ttk.Scrollbar(listbox_frame, orient="vertical", command=listbox.yview)
	listbox_scroll.pack(side="right", fill="y")

	listbox.configure(yscrollcommand=listbox_scroll.set)

	# Create a search box at the top of the window
	search_frame = ttk.Frame(root, padding=(10, 10, 10, 0))
	search_frame.pack(side="top", fill="x")

	search_label = ttk.Label(search_frame, text="Search:")
	search_label.pack(side="left")

	search_box = ttk.Entry(search_frame)
	search_box.pack(side="left", fill="x", expand=True)

	search_button = ttk.Button(search_frame, text="Search", command=search_redis)
	search_button.pack(side="right")

	# Bind the "<Return>" event to the search_redis function
	search_box.bind("<Return>", lambda event: search_redis())

	# Create a text editor on the right side of the window
	editor_frame = ttk.Frame(root, padding=(0, 10, 10, 10))
	editor_frame.pack(side="left", fill="both", expand=True)

	editor_label = ttk.Label(editor_frame, text="Value")
	editor_label.pack(side="top", fill="x")

	# #editor = scrolledtext.ScrolledText(editor_frame, wrap="word")
	editor = HTMLScrolledText(editor_frame, wrap="word")
	# # 10-jul-23 ubah agar bisa select, tapi masih masalah dg markdown tdk terender
	# # Create an instance of SelectableHTMLScrolledText instead of HTMLScrolledText
	# editor = SelectableHTMLScrolledText(editor_frame, wrap="word")
	editor.pack(side="left", fill="both", expand=True)

	editor_scroll = ttk.Scrollbar(editor_frame, orient="vertical", command=editor.yview)
	editor_scroll.pack(side="right", fill="y")

	editor.configure(yscrollcommand=editor_scroll.set)

	# The <<ListboxSelect>> event is still bound to the on_select function, 
	# and two additional bindings are added for the up and down arrow keys. 
	# When either of these keys is pressed, the corresponding lambda function is called with the event object, 
	# which is then passed to the on_select function.
	listbox.bind("<<ListboxSelect>>", on_select)
	# # Bind the up and down arrow keys to the on_select function
	# # listbox.bind("<Up>", on_select)
	# # listbox.bind("<Down>", on_select)
	# listbox.bind("<Up>", lambda event: on_select(event))
	# listbox.bind("<Down>", lambda event: on_select(event))


	def bind_select(event):
		if event.keysym == 'Up':
			current_selection = listbox.curselection()
			if current_selection:
				index = int(current_selection[0])
				if index > 0:
					listbox.selection_clear(0, END)
					listbox.selection_set(index - 1)
					on_select(event)
		elif event.keysym == 'Down':
			current_selection = listbox.curselection()
			if current_selection:
				index = int(current_selection[0])
				if index < listbox.size() - 1:
					listbox.selection_clear(0, END)
					listbox.selection_set(index + 1)
					on_select(event)

	listbox.bind("<Up>", bind_select)
	listbox.bind("<Down>", bind_select)

	# Start the tkinter event loop
	search_redis(bariskalimat)
	root.mainloop()


def wieke(bariskalimat, insert_to_editor, yellow_publisher):
	"""
	encryption dengan kata pengganti wieke
	# utk image
		file_output_path = encrypt_image(file_input_path)
	$ utk video
		file_output_path = encrypt_video(file_input_path)
	else utk text
		output_string = encrypt_text(input_string)
	utk # dan $, bisa terima fileinput|fileoutput
	"""
	# if bariskalimat.startswith('@'):
	#     file_input = bariskalimat.removeprefix('@')
	if bariskalimat.startswith('#'):
		file_input = bariskalimat.removeprefix('#')
		if isfile(file_input):
			try:
				output = encrypt_image(file_input)
				insert_to_editor(output)
			except Exception as err:
				yellow_publisher(f'Gagal encrypt image {file_input} => {err}')
		else:
			yellow_publisher(f'{file_input} not found')
	elif bariskalimat.startswith('$'):
		file_input = bariskalimat.removeprefix('$')
		if isfile(file_input):
			try:
				output = encrypt_video(file_input)
				insert_to_editor(output)
			except Exception as err:
				yellow_publisher(f'Gagal encrypt video {file_input} => {err}')
		else:
			yellow_publisher(f'{file_input} not found')
	else:
		insert_to_editor(encrypt_text(bariskalimat))


def gaia(bariskalimat, insert_to_editor, yellow_publisher):
	"""
	decryption dengan kata pengganti gaia
	"""
	show_file = False
	if bariskalimat.startswith('#'):
		file_input = bariskalimat.removeprefix('#')
		if '|' in file_input:
			file_input, file_output = [item.strip() for item in file_input.split('|')]
		else:
			file_output = filetemppath(suffix_filename(file_input, '_oprek', True))
			print('decrypt image to:', file_output)
			show_file = True
		if isfile(file_input):
			try:
				output = decrypt_image(file_input, file_output)
				insert_to_editor(output)
				if show_file:
					from schnell.app.mediautils import show_image
					show_image(output)
			except Exception as err:
				yellow_publisher(f'Gagal decrypt image {file_input} => {err}')
		else:
			yellow_publisher(f'{file_input} not found')
	elif bariskalimat.startswith('$'):
		file_input = bariskalimat.removeprefix('$')
		if '|' in file_input:
			file_input, file_output = [item.strip() for item in file_input.split('|')]
		else:
			file_output = filetemppath(suffix_filename(file_input, '_oprek', True))
			print('decrypt video to:', file_output)
			show_file = True
		if isfile(file_input):
			try:
				output =  decrypt_video(file_input, file_output)
				insert_to_editor(output)
				if show_file:
					from schnell.app.mediautils import play_video_loop, play_video
					play_video(output)
					print('decrypted video in:', file_output) # krn suka output rame
			except Exception as err:
				yellow_publisher(f'Gagal decrypt video {file_input} => {err}')
		else:
			yellow_publisher(f'{file_input} not found')
	else:
		print(f"decrypting [{bariskalimat}]...")
		insert_to_editor(decrypt_text(bariskalimat))


pattern = r"<(#?(\.?\d+)(?:,#?(\.?\d+))*)>?(.+)"
# <#66,.3>satu|<#30>dua|tiga|<.8>empat|<.1,#50>lima
# mg ('#66,.3', '66', '.3', 'satu')
# mg ('#30', '30', None, 'dua')
# item: tiga
# mg ('.8', '.8', None, 'empat')
# mg ('.1,#50', '.1', '50', 'lima')
def getxy(text, img, pengali=0.8, huruf='arial.ttf', ukuranhuruf=40):
	r"""
	img adlh pil_image tempat dimana text akan ditulis

	teks atas 20% -> 0.2
	teks bawah 20% -> 0.8
	bisa terima

	bahas regex
	<
	(							#1
		#?						#2
		(\.?\d+)				digit bisa diawali dg #, bisa diawali dg . -> jk diawali . jadikan bagian dari digit
		(?:,					non-capture comma
			#?					#3
			(\.?\d+)
		)*
	)
	>
	(.+)						#4
	"""
	print('/meme)getxy, text:', text)
	if text.startswith('<') and '>' in text:
		m = re.match(pattern, text)
		if m:
			print('getxy matching chevrons:', m.groups())
			# ('#66,.3', '66', '.3', 'satu')
			satu, dua, tiga, empat = m.groups()
			if '.' in dua:
				# jk float di dua, artinya pengali
				pengali = float(dua)
			else:
				# jk int di dua, artinya ukuranhuruf
				ukuranhuruf = int(dua)
			if tiga:
				if '.' in tiga:
					# jk float di dua, artinya pengali
					pengali = float(tiga)
				else:
					# jk int di dua, artinya ukuranhuruf
					ukuranhuruf = int(tiga)

			text = empat
			print('text now:', text)

	# font = ImageFont.truetype(huruf, ukuranhuruf)
	font = ImageFont.truetype(huruf, ukuranhuruf)
	text_width, text_height = font.getsize(text)
	# width, height = dummydraw_for_font.textsize(text, font=font)
	# Calculate the position for the text
	# height, width = img.shape[:2]
	width, height = img.size
	# x_pos = int((animation[0].shape[1] - text_width) / 2)
	# y_pos = int(animation[0].shape[0] * pengali - (text_height/2))
	# return x_pos, y_pos
	x = int((width - text_width) / 2)
	y = int(height * pengali - (text_height/2))
	return x, y, text, font



# DEFAULT_FONT = 'arial.ttf'
# DEFAULT_FONT = 'Impact Regular.ttf'
DEFAULT_FONT = 'impact.ttf'
# font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, thickness=2

def get_pil_image(image_path):
	try:
		image = Image.open(image_path)
		return image
	except IOError:
		print("Unable to open image file:", image_path)

def create_and_show_meme(text=None, output_file=None, DATADIR=env_get('ULIBPY_MEMO_DATADIR'), delay=1.0, huruf=DEFAULT_FONT, ukuranhuruf=40, warna=(255,255,255), font_scale=1, thickness=2, filepath=None, upper=True):
	"""
	satu|dua|tiga
	<#66>satu|<#40>dua|tiga
	kita pengen:
	bisa ganti ukuran huruf
	bisa ganti posisi y dalam persentase: misal 0.1, 0.25, 0.55 dst = pengali
	"""
	# from PyQt5.QtWidgets import QApplication
	# from PyQt5.QtGui import QClipboard, QImage

	# dummydraw_for_font = ImageDraw.Draw(Image.new(mode="RGB", size=(1,1)))
	new_output_file = None

	if not output_file:
		output_file = DATADIR + f"/ocr-fun/ocr_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
		output_file = normy(output_file)
		new_output_file = DATADIR + f"/ocr-fun/ocr_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_out.png"
		new_output_file = normy(new_output_file)
	# ternyata gambar jadi menyatu...
	# hapus dulu sblm capture
	file_remove(output_file)
	print(f'[gui.s.s.w.ef-helper.create_and_show_meme] saved screenshot:', output_file)

	# capture_gambar(output_file)
	if filepath:
		pil_image = get_pil_image(filepath)
	else:
		cap = ScreenCapture(output_file)
		cap.mainloop()
		time.sleep(delay)
		pil_image = cap.get_image()

	assert pil_image != None, 'pil_image is None, hasil cap.get_image()'
	draw = ImageDraw.Draw(pil_image)

	font = ImageFont.truetype(huruf, ukuranhuruf)
	if not text:
		text = prompt('Masukkan teks untuk meme:').strip()

	if text:
		positions = []

		if '|' in text:
			# meme hanya bisa 3 posisi satu | dua | tiga, gak spt gif.
			pecah = text.split('|')
			for i, teks in enumerate(pecah, 1):
				teks = teks.strip()
				if not teks:
					continue
				pengali = 0.8
				if len(pecah)==3: # pengali = .2, .5, .8
					# satu|dua|tiga -> 0.2=satu, 0.5dua, 0.8tiga
					if i==1:
						pengali = 0.2
					elif i==2:
						pengali = 0.5
					# else:
					# 	pengali = 0.8
				elif len(pecah)==2 and i==1: # pengali = .2, .8
					# satu|dua -> 0.2=satu, 0.8dua
					pengali = 0.2
				x,y,text,font = getxy(teks, pil_image, pengali, huruf, ukuranhuruf)
				positions.append(((x,y), text))
		else:
			x,y,text,font = getxy(text, pil_image, 0.8, huruf, ukuranhuruf)
			positions.append(((x,y), text))

		stroke_width_percent = 20 # 20% of font size
		stroke_width = int(round(ukuranhuruf * (stroke_width_percent / 100.0)))

		# cv2.putText(img, line, (x, y), font, font_scale, warna, thickness)
		for ((x,y), text) in positions:
			# cv2.putText(pil_image, text, (x, y), font, font_scale, warna, thickness)
			draw.text((x, y), text.upper() if upper else text, font=font, fill=warna, width=stroke_width)

	if platform.system() == "Windows":
		# In this code, the subprocess.call() function is used to call the Windows start command with the microsoft.photos:
		# protocol handler and the file path as an argument.
		# The // before the file path is required to properly format the argument.
		# this will only work if Microsoft Photos is installed on the computer and set as the default app for opening image files.
		# If Microsoft Photos is not installed or set as the default app,
		# you may need to modify the code to use a different application or open the file directly using a different method.
		# subprocess.call(["start", "microsoft.photos:", f"//{output_file}"])
		import os
		from schnell.app.dirutils import bongkar
		print(f'[gui.s.s.w.ef-helper.create_and_show_meme] saving {new_output_file}...')
		pil_image.save(new_output_file)
		# redis_publish_image(new_output_file)
		pyfile = bongkar('ULIBPY_ROOTDIR/schnell/app/imageutils.py')
		os.system(f'python {pyfile} {new_output_file}')
		print(f'[gui.s.s.w.ef-helper.create_and_show_meme] saving {new_output_file} done.')
	else:
		# show_image_cv(pil_image)
		# np_image = np.array(pil_image)
		np_image = np.array(pil_image, dtype=np.uint8)
		np_image = cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR) # convert from RGB to BGR
		cv2.imshow('image', np_image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	del draw
	pil_image.close()

	trycopy(new_output_file)
