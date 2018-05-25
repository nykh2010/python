# -*- coding: utf-8 -*-
"""
Created on Sun May  6 11:24:22 2018

@author: Administrator
"""

import requests
def info(object, spacing=10, collpase=0):
    """
    Print methods and doc strings.
    """
    # 遍历一遍object对象，把里面的可以被调用的方法提取出来
    methodList = [method for method in dir(object) 
                  if callable(getattr(object, method))]
    
    # collpase = 0,保持原来doc stings的显示
    # collpase = 1,保持原来doc stings，用空格连接
    processFunc = collpase and (lambda s:" ".join(s.split())) or (lambda s:s)
    
    print('\n'.join(["%s %s"%(str(method.ljust(spacing)),
                    processFunc(str(getattr(object,method).__doc__)))
          for method in methodList]))
    
#s = 123
#info(s)
      
#info(requests)
info(requests.Response)
    
#__bool__   Returns True if :attr:`status_code` is less than 400.
#
#        This attribute checks if the status code of the response is between
#        400 and 600 to see if there was a client error or a server error. If
#        the status code, is between 200 and 400, this will return True. This
#        is **not** a check to see if the response code is ``200 OK``.
#        
#__class__  type(object_or_name, bases, dict)
#type(object) -> the object's type
#type(name, bases, dict) -> a new type
#__delattr__ Implement delattr(self, name).
#__dir__    __dir__() -> list
#default dir() implementation
#__enter__  None
#__eq__     Return self==value.
#__exit__   None
#__format__ default object formatter
#__ge__     Return self>=value.
#__getattribute__ Return getattr(self, name).
#__getstate__ None
#__gt__     Return self>value.
#__hash__   Return hash(self).
#__init__   None
#__init_subclass__ This method is called when a class is subclassed.
#
#The default implementation does nothing. It may be
#overridden to extend subclasses.
#
#__iter__   Allows you to use a response as an iterator.
#__le__     Return self<=value.
#__lt__     Return self<value.
#__ne__     Return self!=value.
#__new__    Create and return a new object.  See help(type) for accurate signature.
#__nonzero__ Returns True if :attr:`status_code` is less than 400.
#
#        This attribute checks if the status code of the response is between
#        400 and 600 to see if there was a client error or a server error. If
#        the status code, is between 200 and 400, this will return True. This
#        is **not** a check to see if the response code is ``200 OK``.
#        
#__reduce__ helper for pickle
#__reduce_ex__ helper for pickle
#__repr__   None
#__setattr__ Implement setattr(self, name, value).
#__setstate__ None
#__sizeof__ __sizeof__() -> int
#size of object in memory, in bytes
#__str__    Return str(self).
#__subclasshook__ Abstract classes can override this to customize issubclass().
#
#This is invoked early on by abc.ABCMeta.__subclasscheck__().
#It should return True, False or NotImplemented.  If it returns
#NotImplemented, the normal algorithm is used.  Otherwise, it
#overrides the normal algorithm (and the outcome is cached).
#
#close      Releases the connection back to the pool. Once this method has been
#        called the underlying ``raw`` object must not be accessed again.
#
#        *Note: Should not normally need to be called explicitly.*
#        
#iter_content Iterates over the response data.  When stream=True is set on the
#        request, this avoids reading the content at once into memory for
#        large responses.  The chunk size is the number of bytes it should
#        read into memory.  This is not necessarily the length of each item
#        returned as decoding can take place.
#
#        chunk_size must be of type int or None. A value of None will
#        function differently depending on the value of `stream`.
#        stream=True will read data as it arrives in whatever size the
#        chunks are received. If stream=False, data is returned as
#        a single chunk.
#
#        If decode_unicode is True, content will be decoded using the best
#        available encoding based on the response.
#        
#iter_lines Iterates over the response data, one line at a time.  When
#        stream=True is set on the request, this avoids reading the
#        content at once into memory for large responses.
#
#        .. note:: This method is not reentrant safe.
#        
#json       Returns the json-encoded content of a response, if any.
#
#        :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
#        :raises ValueError: If the response body does not contain valid json.
#        
#raise_for_status Raises stored :class:`HTTPError`, if one occurred.


#ConnectTimeout The request timed out while trying to connect to the remote server.
#
#    Requests that produced this error are safe to retry.
#    
#ConnectionError A Connection error occurred.
#DependencyWarning 
#    Warned when an attempt is made to import a module with missing optional
#    dependencies.
#    
#FileModeWarning A file was opened in text mode, but Requests determined its binary length.
#HTTPError  An HTTP error occurred.
#NullHandler 
#    This handler does nothing. It's intended to be used to avoid the
#    "No handlers could be found for logger XXX" one-off warning. This is
#    important for library code, which may contain code to log events. If a user
#    of the library does not configure logging, the one-off warning might be
#    produced; to avoid this, the library developer simply needs to instantiate
#    a NullHandler and add it to the top-level logger of the library module or
#    package.
#    
#PreparedRequest The fully mutable :class:`PreparedRequest <PreparedRequest>` object,
#    containing the exact bytes that will be sent to the server.
#
#    Generated from either a :class:`Request <Request>` object or manually.
#
#    Usage::
#
#import requests
#req = requests.Request('GET', 'http://httpbin.org/get')
#r = req.prepare()
#      <PreparedRequest [GET]>
#
#s = requests.Session()
#s.send(r)
#      <Response [200]>
#    
#ReadTimeout The server did not send any data in the allotted amount of time.
#Request    A user-created :class:`Request <Request>` object.
#
#    Used to prepare a :class:`PreparedRequest <PreparedRequest>`, which is sent to the server.
#
#    :param method: HTTP method to use.
#    :param url: URL to send.
#    :param headers: dictionary of headers to send.
#    :param files: dictionary of {filename: fileobject} files to multipart upload.
#    :param data: the body to attach to the request. If a dictionary is provided, form-encoding will take place.
#    :param json: json for the body to attach to the request (if files or data is not specified).
#    :param params: dictionary of URL parameters to append to the URL.
#    :param auth: Auth handler or (user, pass) tuple.
#    :param cookies: dictionary or CookieJar of cookies to attach to this request.
#    :param hooks: dictionary of callback hooks, for internal usage.
#
#    Usage::
#
#import requests
#req = requests.Request('GET', 'http://httpbin.org/get')
#req.prepare()
#      <PreparedRequest [GET]>
#    
#RequestException There was an ambiguous exception that occurred while handling your
#    request.
#    
#RequestsDependencyWarning An imported dependency doesn't match the expected version range.
#Response   The :class:`Response <Response>` object, which contains a
#    server's response to an HTTP request.
#    
#Session    A Requests session.
#
#    Provides cookie persistence, connection-pooling, and configuration.
#
#    Basic Usage::
#
#import requests
#s = requests.Session()
#s.get('http://httpbin.org/get')
#      <Response [200]>
#
#    Or as a context manager::
#
#with requests.Session() as s:
#    s.get('http://httpbin.org/get')
#      <Response [200]>
#    
#Timeout    The request timed out.
#
#    Catching this error will catch both
#    :exc:`~requests.exceptions.ConnectTimeout` and
#    :exc:`~requests.exceptions.ReadTimeout` errors.
#    
#TooManyRedirects Too many redirects.
#URLRequired A valid URL is required to make a request.
#check_compatibility None
#delete     Sends a DELETE request.
#
#    :param url: URL for the new :class:`Request` object.
#    :param \*\*kwargs: Optional arguments that ``request`` takes.
#    :return: :class:`Response <Response>` object
#    :rtype: requests.Response
#    
#get        Sends a GET request.
#
#    :param url: URL for the new :class:`Request` object.
#    :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
#    :param \*\*kwargs: Optional arguments that ``request`` takes.
#    :return: :class:`Response <Response>` object
#    :rtype: requests.Response
#    
#head       Sends a HEAD request.
#
#    :param url: URL for the new :class:`Request` object.
#    :param \*\*kwargs: Optional arguments that ``request`` takes.
#    :return: :class:`Response <Response>` object
#    :rtype: requests.Response
#    
#options    Sends an OPTIONS request.
#
#    :param url: URL for the new :class:`Request` object.
#    :param \*\*kwargs: Optional arguments that ``request`` takes.
#    :return: :class:`Response <Response>` object
#    :rtype: requests.Response
#    
#patch      Sends a PATCH request.
#
#    :param url: URL for the new :class:`Request` object.
#    :param data: (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
#    :param json: (optional) json data to send in the body of the :class:`Request`.
#    :param \*\*kwargs: Optional arguments that ``request`` takes.
#    :return: :class:`Response <Response>` object
#    :rtype: requests.Response
#    
#post       Sends a POST request.
#
#    :param url: URL for the new :class:`Request` object.
#    :param data: (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
#    :param json: (optional) json data to send in the body of the :class:`Request`.
#    :param \*\*kwargs: Optional arguments that ``request`` takes.
#    :return: :class:`Response <Response>` object
#    :rtype: requests.Response
#    
#put        Sends a PUT request.
#
#    :param url: URL for the new :class:`Request` object.
#    :param data: (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
#    :param json: (optional) json data to send in the body of the :class:`Request`.
#    :param \*\*kwargs: Optional arguments that ``request`` takes.
#    :return: :class:`Response <Response>` object
#    :rtype: requests.Response
#    
#request    Constructs and sends a :class:`Request <Request>`.
#
#    :param method: method for the new :class:`Request` object.
#    :param url: URL for the new :class:`Request` object.
#    :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
#    :param data: (optional) Dictionary or list of tuples ``[(key, value)]`` (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
#    :param json: (optional) json data to send in the body of the :class:`Request`.
#    :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
#    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
#    :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
#        ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
#        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
#        defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
#        to add for the file.
#    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
#    :param timeout: (optional) How many seconds to wait for the server to send data
#        before giving up, as a float, or a :ref:`(connect timeout, read
#        timeout) <timeouts>` tuple.
#    :type timeout: float or tuple
#    :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
#    :type allow_redirects: bool
#    :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
#    :param verify: (optional) Either a boolean, in which case it controls whether we verify
#            the server's TLS certificate, or a string, in which case it must be a path
#            to a CA bundle to use. Defaults to ``True``.
#    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
#    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
#    :return: :class:`Response <Response>` object
#    :rtype: requests.Response
#
#    Usage::
#
#import requests
#req = requests.request('GET', 'http://httpbin.org/get')
#      <Response [200]>
#    
#session    
#    Returns a :class:`Session` for context-management.
#
#    :rtype: Session





#__add__    Return self+value.
#__class__  str(object='') -> str
#str(bytes_or_buffer[, encoding[, errors]]) -> str
#
#Create a new string object from the given object. If encoding or
#errors is specified, then the object must expose a data buffer
#that will be decoded using the given encoding and error handler.
#Otherwise, returns the result of object.__str__() (if defined)
#or repr(object).
#encoding defaults to sys.getdefaultencoding().
#errors defaults to 'strict'.
#__contains__ Return key in self.
#__delattr__ Implement delattr(self, name).
#__dir__    __dir__() -> list
#default dir() implementation
#__eq__     Return self==value.
#__format__ S.__format__(format_spec) -> str
#
#Return a formatted version of S as described by format_spec.
#__ge__     Return self>=value.
#__getattribute__ Return getattr(self, name).
#__getitem__ Return self[key].
#__getnewargs__ None
#__gt__     Return self>value.
#__hash__   Return hash(self).
#__init__   Initialize self.  See help(type(self)) for accurate signature.
#__init_subclass__ This method is called when a class is subclassed.
#
#The default implementation does nothing. It may be
#overridden to extend subclasses.
#
#__iter__   Implement iter(self).
#__le__     Return self<=value.
#__len__    Return len(self).
#__lt__     Return self<value.
#__mod__    Return self%value.
#__mul__    Return self*value.n
#__ne__     Return self!=value.
#__new__    Create and return a new object.  See help(type) for accurate signature.
#__reduce__ helper for pickle
#__reduce_ex__ helper for pickle
#__repr__   Return repr(self).
#__rmod__   Return value%self.
#__rmul__   Return self*value.
#__setattr__ Implement setattr(self, name, value).
#__sizeof__ S.__sizeof__() -> size of S in memory, in bytes
#__str__    Return str(self).
#__subclasshook__ Abstract classes can override this to customize issubclass().
#
#This is invoked early on by abc.ABCMeta.__subclasscheck__().
#It should return True, False or NotImplemented.  If it returns
#NotImplemented, the normal algorithm is used.  Otherwise, it
#overrides the normal algorithm (and the outcome is cached).
#
#capitalize S.capitalize() -> str
#
#Return a capitalized version of S, i.e. make the first character
#have upper case and the rest lower case.
#casefold   S.casefold() -> str
#
#Return a version of S suitable for caseless comparisons.
#center     S.center(width[, fillchar]) -> str
#
#Return S centered in a string of length width. Padding is
#done using the specified fill character (default is a space)
#count      S.count(sub[, start[, end]]) -> int
#
#Return the number of non-overlapping occurrences of substring sub in
#string S[start:end].  Optional arguments start and end are
#interpreted as in slice notation.
#encode     S.encode(encoding='utf-8', errors='strict') -> bytes
#
#Encode S using the codec registered for encoding. Default encoding
#is 'utf-8'. errors may be given to set a different error
#handling scheme. Default is 'strict' meaning that encoding errors raise
#a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
#'xmlcharrefreplace' as well as any other name registered with
#codecs.register_error that can handle UnicodeEncodeErrors.
#endswith   S.endswith(suffix[, start[, end]]) -> bool
#
#Return True if S ends with the specified suffix, False otherwise.
#With optional start, test S beginning at that position.
#With optional end, stop comparing S at that position.
#suffix can also be a tuple of strings to try.
#expandtabs S.expandtabs(tabsize=8) -> str
#
#Return a copy of S where all tab characters are expanded using spaces.
#If tabsize is not given, a tab size of 8 characters is assumed.
#find       S.find(sub[, start[, end]]) -> int
#
#Return the lowest index in S where substring sub is found,
#such that sub is contained within S[start:end].  Optional
#arguments start and end are interpreted as in slice notation.
#
#Return -1 on failure.
#format     S.format(*args, **kwargs) -> str
#
#Return a formatted version of S, using substitutions from args and kwargs.
#The substitutions are identified by braces ('{' and '}').
#format_map S.format_map(mapping) -> str
#
#Return a formatted version of S, using substitutions from mapping.
#The substitutions are identified by braces ('{' and '}').
#index      S.index(sub[, start[, end]]) -> int
#
#Return the lowest index in S where substring sub is found, 
#such that sub is contained within S[start:end].  Optional
#arguments start and end are interpreted as in slice notation.
#
#Raises ValueError when the substring is not found.
#isalnum    S.isalnum() -> bool
#
#Return True if all characters in S are alphanumeric
#and there is at least one character in S, False otherwise.
#isalpha    S.isalpha() -> bool
#
#Return True if all characters in S are alphabetic
#and there is at least one character in S, False otherwise.
#isdecimal  S.isdecimal() -> bool
#
#Return True if there are only decimal characters in S,
#False otherwise.
#isdigit    S.isdigit() -> bool
#
#Return True if all characters in S are digits
#and there is at least one character in S, False otherwise.
#isidentifier S.isidentifier() -> bool
#
#Return True if S is a valid identifier according
#to the language definition.
#
#Use keyword.iskeyword() to test for reserved identifiers
#such as "def" and "class".
#
#islower    S.islower() -> bool
#
#Return True if all cased characters in S are lowercase and there is
#at least one cased character in S, False otherwise.
#isnumeric  S.isnumeric() -> bool
#
#Return True if there are only numeric characters in S,
#False otherwise.
#isprintable S.isprintable() -> bool
#
#Return True if all characters in S are considered
#printable in repr() or S is empty, False otherwise.
#isspace    S.isspace() -> bool
#
#Return True if all characters in S are whitespace
#and there is at least one character in S, False otherwise.
#istitle    S.istitle() -> bool
#
#Return True if S is a titlecased string and there is at least one
#character in S, i.e. upper- and titlecase characters may only
#follow uncased characters and lowercase characters only cased ones.
#Return False otherwise.
#isupper    S.isupper() -> bool
#
#Return True if all cased characters in S are uppercase and there is
#at least one cased character in S, False otherwise.
#join       S.join(iterable) -> str
#
#Return a string which is the concatenation of the strings in the
#iterable.  The separator between elements is S.
#ljust      S.ljust(width[, fillchar]) -> str
#
#Return S left-justified in a Unicode string of length width. Padding is
#done using the specified fill character (default is a space).
#lower      S.lower() -> str
#
#Return a copy of the string S converted to lowercase.
#lstrip     S.lstrip([chars]) -> str
#
#Return a copy of the string S with leading whitespace removed.
#If chars is given and not None, remove characters in chars instead.
#maketrans  Return a translation table usable for str.translate().
#
#If there is only one argument, it must be a dictionary mapping Unicode
#ordinals (integers) or characters to Unicode ordinals, strings or None.
#Character keys will be then converted to ordinals.
#If there are two arguments, they must be strings of equal length, and
#in the resulting dictionary, each character in x will be mapped to the
#character at the same position in y. If there is a third argument, it
#must be a string, whose characters will be mapped to None in the result.
#partition  S.partition(sep) -> (head, sep, tail)
#
#Search for the separator sep in S, and return the part before it,
#the separator itself, and the part after it.  If the separator is not
#found, return S and two empty strings.
#replace    S.replace(old, new[, count]) -> str
#
#Return a copy of S with all occurrences of substring
#old replaced by new.  If the optional argument count is
#given, only the first count occurrences are replaced.
#rfind      S.rfind(sub[, start[, end]]) -> int
#
#Return the highest index in S where substring sub is found,
#such that sub is contained within S[start:end].  Optional
#arguments start and end are interpreted as in slice notation.
#
#Return -1 on failure.
#rindex     S.rindex(sub[, start[, end]]) -> int
#
#Return the highest index in S where substring sub is found,
#such that sub is contained within S[start:end].  Optional
#arguments start and end are interpreted as in slice notation.
#
#Raises ValueError when the substring is not found.
#rjust      S.rjust(width[, fillchar]) -> str
#
#Return S right-justified in a string of length width. Padding is
#done using the specified fill character (default is a space).
#rpartition S.rpartition(sep) -> (head, sep, tail)
#
#Search for the separator sep in S, starting at the end of S, and return
#the part before it, the separator itself, and the part after it.  If the
#separator is not found, return two empty strings and S.
#rsplit     S.rsplit(sep=None, maxsplit=-1) -> list of strings
#
#Return a list of the words in S, using sep as the
#delimiter string, starting at the end of the string and
#working to the front.  If maxsplit is given, at most maxsplit
#splits are done. If sep is not specified, any whitespace string
#is a separator.
#rstrip     S.rstrip([chars]) -> str
#
#Return a copy of the string S with trailing whitespace removed.
#If chars is given and not None, remove characters in chars instead.
#split      S.split(sep=None, maxsplit=-1) -> list of strings
#
#Return a list of the words in S, using sep as the
#delimiter string.  If maxsplit is given, at most maxsplit
#splits are done. If sep is not specified or is None, any
#whitespace string is a separator and empty strings are
#removed from the result.
#splitlines S.splitlines([keepends]) -> list of strings
#
#Return a list of the lines in S, breaking at line boundaries.
#Line breaks are not included in the resulting list unless keepends
#is given and true.
#startswith S.startswith(prefix[, start[, end]]) -> bool
#
#Return True if S starts with the specified prefix, False otherwise.
#With optional start, test S beginning at that position.
#With optional end, stop comparing S at that position.
#prefix can also be a tuple of strings to try.
#strip      S.strip([chars]) -> str
#
#Return a copy of the string S with leading and trailing
#whitespace removed.
#If chars is given and not None, remove characters in chars instead.
#swapcase   S.swapcase() -> str
#
#Return a copy of S with uppercase characters converted to lowercase
#and vice versa.
#title      S.title() -> str
#
#Return a titlecased version of S, i.e. words start with title case
#characters, all remaining cased characters have lower case.
#translate  S.translate(table) -> str
#
#Return a copy of the string S in which each character has been mapped
#through the given translation table. The table must implement
#lookup/indexing via __getitem__, for instance a dictionary or list,
#mapping Unicode ordinals to Unicode ordinals, strings, or None. If
#this operation raises LookupError, the character is left untouched.
#Characters mapped to None are deleted.
#upper      S.upper() -> str
#
#Return a copy of S converted to uppercase.
#zfill      S.zfill(width) -> str
#
#Pad a numeric string S with zeros on the left, to fill a field
#of the specified width. The string S is never truncated.