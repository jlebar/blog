# You need to get markdown via
#   easy_install markdown2
#

all:
	weblog/weblog_run.py publish

clean:
	rm -rf output

stage: all
	rsync -a output/ jlebar_jlebar-blog@ssh.phx.nearlyfreespeech.net:staging

publish: all
	rsync -a output/ jlebar_jlebar-blog@ssh.phx.nearlyfreespeech.net:
