# write decorator around file
# add additional operations to file -> logging

# API should allow access to underlying shape

'''
Ex if FileWithLogging is a decorator for File,
solution1: it can have all methods if File to be able to access them all 
solution2: use __getattr__ & __setattr__ & __delattr__, allow access to underlying shape
'''

class File:
    def __init__(self):
        pass

class FileWithLogging:
    def __init__(self, file):
        self.file = file
    
    def writelines(self, strings):
        # use underlying File object
        self.file.writelines(strings)
        print(f'wrote {len(strings)} lines')

    # these methods also will be sent over to underlying class -> File
    def __iter__(self):
        return self.file.__iter__()
    
    def __next__(self):
        return self.file.__next__()

    # overwrite get set and del attrs, to access underlying class File
    # redirect to the underlying base class's attributes 
    def __getattr__(self, item):
        return getattr(self.__dict__['file'], item)
    
    # change underlying file handle 
    def __setattr__(self, key, value):
        if key == 'file':
            # change file handle
            self.__dict__[key] = value
        else:
            setattr(self.__dict__['file'], key)

    def __delattr__(self, item):
        delattr(self.__dict__['file'], item)

if __name__ == "__main__":
    file = FileWithLogging(open('hello.txt', 'w'))
    file.writelines(['hello', 'world'])
    file.write('Testing') # underlying method access from File
    ## goes to __getattr__ and access underlying file from __dict__
    ## no need to add another Write method in the decorator
    file.close() ## same as ^, calls underlying class
    print(file)

