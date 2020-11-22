# Forensics Class Exercises

# Installation
```
$ ./setup
```

# Exercises


## Run Hash Cipher for Integrity's Sake
```
$ cd ./images
$ ls
$ sha256sum *
```

## Carve an Image's Memory Using foremost
```
$ foremost -i ./11-carve-fat.dd -o foremost-recovery
```

## Carve the Same Image's Memory Using scalpel
```
$ scalpel -o scalpel-recovery ./11-carve-fat.dd
```

## Run Memory Checks Using volatility
```
$ volatility -f Bob.vmem imageinfo
```

### Running Process Info
```
$ volatility -f Bob.vmem --profile=WinXPSP3x86 pslist
$ volatility -f Bob.vmem --profile=WinXPSP3x86 pstree
$ volatility -f Bob.vmem --profile=WinXPSP3x86 psscan  # show inactive/hidden processes
$ volatility -f Bob.vmem --profile=WinXPSP3x86 psxview # combination of the above
```

### Network Connections and Services
```
$ volatility -f Bob.vmem --profile=WinXPSP3x86 connections
$ volatility -f Bob.vmem --profile=WinXPSP3x86 sockets
```

### DLL Analysis
```
$ volatility -f Bob.vmem --profile=WinXPSP3x86 verinfo
$ volatility -f Bob.vmem --profile=WinXPSP3x86 dlllist
$ volatility -f Bob.vmem --profile=WinXPSP3x86 getsids
```

### Registry Analysis
```
volatility -f Bob.vmem --profile=WinXPSP3x86 hivelist
```

## Building Your Own Virtual Memory Dumps
```
$ sudo dd if=/dev/mem of=me.vmem bs=10MB count=1  # Why is this operation not permitted?
$ sudo dd if=/dev/mem of=me.vmem bs=1MB count=1
$ volatility -f me.vmem imageinfo
```

## Building Your Own Disk Storage Dumps

* Why can't you use the cp command?
* Why is dd better?
* Why can't dd copy files directly with paths?


```

$ sudo dd if=/dev/sda1 of=me.dd bs=1MB count=50
$ cat ./me.dd       # might be noisy, ctl-c if so
$ foremost -i ./me.dd -o foremost-me-recovery
$ scalpel -o scalpel-me-recovery ./me.dd
```


# Metadata Exercises

```
$ exiftool metadata.pdf
$ exiftool -all:all metadata.pdf
$ cp metadata.pdf metadata-scrubbed.pdf
$ exiftool metadata-scrubbed.pdf
$ exiftool -all:all= metadata-scrubbed.pdf
$ exiftool -Title="John L. Whiteman's Health Record" -Author="Dr. Dana Scully" -Description="SN: 123-45-6789, ID:123, Age: 45. Blood: A+" -Subject="PHI/PII Data for Mr. Whiteman"  metadata-scrubbed.pdf
$ exiftool metadata-scrubbed.pdf
```


# References


* [http://dftt.sourceforge.net](https://sourceforge.net/projects/dftt/files/Test%20Images/11_%20Basic%20Data%20Carving%20%231/11-carve-fat.zip/download?use_mirror=cfhcable&download=)

* [https://digitalcorpora.org/](http://downloads.digitalcorpora.org/corpora/scenarios/2009-m57-patents/usb/terry-work-usb-2009-12-11.E01)

* [https://github.com/volatilityfoundation/volatility/wiki/memory-samples](http://files.sempersecurus.org/dumps/cridex_memdump.zip)

* [PublicMemoryImages.wiki](https://code.google.com/archive/p/volatility/wikis)
* 
