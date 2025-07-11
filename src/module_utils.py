from socket import create_connection



def is_url_playlist(url):
    if (len(url) > 34 and url[:34] == 'https://youtube.com/playlist?list='):
        return True
    return False


def is_internet_available():
    """
    Checks internet availability.

    Returns:
        True:   Internet is available.
        False:  Internet is not available
    """
    try:
        create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


def char_police(suspect_string):
    """
    Checks for chars that are illegal in naming a file.

    From given string, function removes \\, /, :, *, ?, ", <, >, | 
    (chars illegal in naming files) and returns it.

    Args:
        suspect_string (str): String with potenetial characters to remove.

    Returns:
        str: Argument string without signs illegal in filenaming.
    """
    charlist = [a for a in suspect_string]
    i = 0
    while i < len(charlist):
        if charlist[i] in ["\\", "/", ":", "*", "?", '"', "<", ">", "|"]:
            charlist.pop(i)
        else:
            i += 1
    
    policedstring = "".join(charlist)
    return policedstring


def illegal_to_ascii(illegal_string):
    print("Why in the world did You do it? Maybe do something better with Your life than downloading stuff containing just illegal signs?")
    return "_".join((str(ord(char)) for char in illegal_string))


def dots(integer):
    """
    Puts dots in long numbers.

    Between every 3 chars puts a dot.

    Args:
        integer (int): A number into which the function will put dots.

    Returns:
        str: Inputted integer with dots added.
    """
    integer = str(integer)
    result = ''
    while len(integer) > 3:
        result = "." + integer[-3:] + result
        integer = integer[:-3]

    result = integer + result 
    return result
