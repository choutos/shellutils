from ftplib import FTP

AS400HOST = 'hostname'
AS400USER = 'username'
AS400PASS = 'password'

def getfiles(filelist, as400library='FILEOUTPUT'):
    ftp = FTP(AS400HOST)
    ftp.login(user=AS400USER, passwd=AS400PASS)
    ftp.cwd('/QSYS.LIB/' + as400library + '.LIB')
    for file in filelist:
        singlename = file.split('/')[0]
        ftp.retrlines('RETR ' + file, 
        lambda s, w=open(singlename, 'w').write: w(s+"\n"))
    ftp.quit()

def getfile(filename, as400library='FILEOUTPUT'):
    ftp = FTP(AS400HOST)
    ftp.login(user=AS400USER, passwd=AS400PASS)
    ftp.cwd('/QSYS.LIB/' + as400library + '.LIB')
    ftp.retrlines('RETR ' + filename + '.FILE/' + filename + '.MBR' ,
    lambda s, w=open(filename + '.FILE', 'w').write: w(s+"\n"))

def remote_list(filename, as400library='FILEOUTPUT'):
    ftp = FTP(AS400HOST)
    ftp.login(user=AS400USER, passwd=AS400PASS)
    ftp.cwd('/QSYS.LIB/' + as400library + '.LIB')
    all_files = ftp.nlst()
    my_files = []
    for file in all_files:
        if filename in file:
            my_files.append(file)
    return my_files

