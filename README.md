pynntp
======

Python nntp library.

This package includes advanced NNTP features, including, compressed headers.

The most important (useful) feature of this package other nntp libaries is the
ablity to use generators to produce data. This allows for streaming download
of large responses to say an XOVER command (which can produce gigabytes of data)
and allows you to process the data at the same time is is being received.
Meaning that memory use is minimal (even for the largest responses) and that
cycles aren't being wasted waiting on a blocking read (even in a single threaded
application)


Example
-------

    >>> import nntp
    >>> reader = nntp.Reader("usenet-host.com", 443, "user", "password", use_ssl=True)
    >>> reader.date()
    datetime.datetime(2013, 10, 19, 6, 11, 41, tzinfo=_tzgmt())
    >>> reader.xfeature_compress_gzip()
    True
    >>> reader.date()
    datetime.datetime(2013, 10, 19, 6, 13, 3, tzinfo=_tzgmt())


Supported Commands
------------------

NNTP commands that are currently supported include:
* CAPABILITIES
* MODE READER
* QUIT
* DATE
* HELP
* NEWGROUPS (generator)
* NEWNEWS (generator)
* LIST ACTIVE (generator)
* LIST NEWSGROUPS (generator)
* LIST OVERVIEW.FMT (generator)
* LIST EXTENSIONS (generator)
* GROUP
* NEXT
* LAST
* ARTICLE
* HEAD
* BODY
* XGTITLE
* XHDR
* XZHDR
* XOVER (generator)
* XZVER (generator)
* XPAT (generator)
* XFEATURE COMPRESS GZIP
