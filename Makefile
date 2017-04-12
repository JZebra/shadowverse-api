# recursively removes all .pyc files and __pycache__ directories in the current directory

clean:
    find . | \
    grep -E "(__pycache__|\.pyc$)" | \
    xargs rm -rf
