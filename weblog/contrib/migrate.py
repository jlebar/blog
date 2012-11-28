import os
import sys
import ConfigParser
from optparse import OptionParser, SUPPRESS_HELP

from weblog.publish import load_post_list
from weblog.post import Post

def main():
    parser = OptionParser()
    parser.add_option("-s", "--source_dir", dest="source_dir",
                      default='.',
                      help='The source directory where the blog posts are '
                      'located. [default: \'%default\']',
                      metavar="DIR")
    parser.add_option("-o", "--output_dir", dest="output_dir",
                      default='output',
                      help='The directory where all the generated files are '
                      'written. If it does not exist it is created.'
                      '[default: \'%default\']',
                      metavar="DIR")
    parser.add_option('-e', '--encoding', dest='encoding', default='utf-8')
    parser.add_option('--redirections-only',
                      dest='redirection_only', default=False, action='store_true',
                      help='Generate only redirection files.')
    (options, args) = parser.parse_args()

    if options.redirection_only:
        print 'Creating config.py ...'
        config = ConfigParser.SafeConfigParser()
        filename = os.path.join(options.source_dir, 'weblog.ini')
        if os.path.isfile(filename):
            config.read(filename)
        else:
            raise SystemExit(filename + " doesn't exist")
        string_values = ('title', 'url', 'description', 'source_dir', 'output_dir',
                         'encoding', 'author')
        integer_values = ('post_per_page', 'feed_limit')
        obsolete_values = ('html_head', 'html_header', 'html_footer')

        output = open(os.path.join(options.output_dir, 'config.py'), 'w')

        def _config_get(key):
            try:
                return config.get('weblog', key)
            except ConfigParser.NoOptionError:
                return

        for key in string_values:
            value = _config_get(key)
            if value:
                output.write('%s = %r\n' % (key, value))

        for key in integer_values:
            value = _config_get(key)
            if value is not None:
                output.write('%s = %d\n' % (key, int(value)))

        obsoletes = list()
        for key in obsolete_values:
            if _config_get(key):
                print ('Warning: %s are now obsolete. Check documentation.' %
                       ', '.join(obsolete_values))
                break
        print 'done'

    if options.encoding:
        Post.DEFAULT_ENCODING = options.encoding

    print 'Creating redirections ...'

    _REDIRECTION_FILE = \
            ('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n'
             '<title></title>\n'
             '<meta http-equiv="REFRESH" content="0;%s">\n'
             '<a href="%s">click to get redirected</a>')
    posts = load_post_list(options.source_dir)
    for post in posts:
        dir = os.path.join(options.output_dir,
                           str(post.date.year),
                           str(post.date.month),
                           str(post.date.day))
        if not os.path.isdir(dir):
            os.makedirs(dir)
        ascii_title = post.title.encode('ascii', 'replace')
        if ascii_title != post.slug:
            new_url = post.slug + '.html'
            redirection_file = _REDIRECTION_FILE % (new_url, new_url)
            open(os.path.join(dir, ascii_title + '.html'), 'w').\
                    write(redirection_file)
    print 'Done.'

if __name__ == '__main__':
    main()
