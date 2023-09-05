import email
import sys
import uuid

from .post import Post

def _set_uuid(filename):
  try:
      post_file = email.message_from_file(file(filename))
      if 'uuid' in post_file:
          logging.warning('UUID already present in %s.  '
                          'Ignoring file.' % filename)
          return
      post_file.add_header('uuid', uuid.uuid1().urn)
      file(filename, 'w').write(post_file.as_string())
  except IOError as error:
      raise SystemExit(error)

def command_uuid(args, options):
    '''
    Execute the 'uuid' command, which generates a uuid for the given file.
    '''
    if not args:
        raise SystemExit('No file specified:\n'
                         '%s uuid filename [filename...]' % sys.argv[0])

    for file in args:
        _set_uuid(file)
