# Getting Started With CGI
CGI (Common Gateway Interface) is a protocol for generating dynamic web content from executable files.
In this case, the executable files are Python scripts.

There are many ways to set up different web servers to serve CGI scripts, and that configuration process
is beyond the scope of this tutorial. Instead, examples will be served using Python 3's `http.server` library.

To begin, create a directory, and open a terminal there. We must create the following directories:

```bash
mkdir cgi-bin static static\css static\js static\img
```

The most important part of this line is `mkdir cgi-bin`. CGI servers will only treat files in a set of pre-defined
directories as executables. By convention, this is just `/cgi-bin` and its sub-directories.

Once you've created that structure, you're ready to begin. You can start the built-in CGI server from the terminal
with the following line:

```bash
python -m http.server --cgi 8080
```
To stop serving, just send a Ctrl+C to this terminal.

Some brief examples:

1. [Standard Template](cgi-bin/standard_template.py)
2. [Debugging Example](cgi-bin/how_debugging_works.py)
3. [Serving JSON](cgi-bin/serving_json.py)
4. [Handling Query Strings](cgi-bin/query_strings.py)
5. [Posting Forms](cgi-bin/handling_post.py)
6. [Serving Download Files](/cgi-bin/serving_file_downloads.py)
