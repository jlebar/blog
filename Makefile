# You need to get markdown via
#   easy_install markdown2
#

all:
	weblog/weblog_run.py publish
	find output -type d -print0 | xargs -0 chmod 755
	find output -type f -print0 | xargs -0 chmod 644

clean:
	rm -rf output

stage: all
	rsync -a output/ jlebar_jlebar-blog@ssh.nyc1.nearlyfreespeech.net:staging

publish: all
	rsync -a output/ jlebar_jlebar-blog@ssh.nyc1.nearlyfreespeech.net:
